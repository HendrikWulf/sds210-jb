"""Release the sample solutions of the practicals on schedule, and take them down after the course.

Used by .github/workflows/release-solutions.yml; see .github/RELEASING-SOLUTIONS.md.
Needs only the Python standard library (3.11 or newer).

    python3 .github/scripts/release_solutions.py status
        Show the schedule and what is released, due, scheduled or taken down.
        Also checks the schedule (every notebook needs an entry in myst.yml, the takedown
        must come after the last release).

    python3 .github/scripts/release_solutions.py status --now 2027-03-16T17:05
        The same, as if it were that time (Swiss time unless an offset is given).

    python3 .github/scripts/release_solutions.py release --solutions DIR --names P02,P03
        Copy those solutions from DIR (a clone of sds210-solutions) into this repository,
        enable their entries in myst.yml and stage them for a commit (git add -f).

    python3 .github/scripts/release_solutions.py takedown --names P02,P03
        Remove those solutions from this repository and comment out their entries in myst.yml.

    python3 .github/scripts/release_solutions.py pages --set project-topics=show
        Show (or hide) a timed block of myst.yml, e.g. the project topics page.

Add --dry-run to release, takedown or pages to only print what would change.
A solution counts as released when its notebook is tracked by git in this repository.

Timed pages ([[page_release]] in the schedule) are lines of myst.yml between
"# timed: <name> (start)" and "# timed: <name> (end)". Before their date the workflow hides
them by putting "#~ " in front of each line; from their date on it shows them. The files stay
in the repository; only the book leaves them out while they are hidden.
"""

import argparse
import datetime as dt
import filecmp
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parents[2]
SCHEDULE = REPO / ".github" / "solution-releases.toml"
TOC = REPO / "myst.yml"
FMT = "%a %d %b %Y %H:%M %Z"


def as_datetime(date, time, tz, label):
    if not isinstance(date, dt.date):
        sys.exit(f"{label}: dates must be written as YYYY-MM-DD without quotes")
    return dt.datetime.combine(date, dt.time.fromisoformat(time), tzinfo=tz)


def load_schedule():
    cfg = tomllib.loads(SCHEDULE.read_text(encoding="utf-8"))
    tz = ZoneInfo(cfg["timezone"])
    releases = []
    for entry in cfg["release"]:
        notebook = entry["notebook"]
        releases.append({
            "name": entry["practical"],
            "when": as_datetime(entry["date"], entry.get("time", cfg["release_time"]), tz,
                                entry["practical"]),
            "notebook": notebook,
            "files": [notebook, str(Path(notebook).with_suffix(".md"))],
        })
    names = [r["name"] for r in releases]
    if len(names) != len(set(names)):
        sys.exit("solution-releases.toml: each practical may appear only once")
    takedown = None
    if "takedown_date" in cfg:
        takedown = as_datetime(cfg["takedown_date"], cfg.get("takedown_time", "23:59"), tz,
                               "takedown_date")
        last = max(r["when"] for r in releases)
        if takedown <= last:
            sys.exit(f"solution-releases.toml: the takedown ({takedown.strftime(FMT)}) must come "
                     f"after the last release ({last.strftime(FMT)}). Did you update all dates?")
    return tz, releases, takedown


def load_pages():
    cfg = tomllib.loads(SCHEDULE.read_text(encoding="utf-8"))
    tz = ZoneInfo(cfg["timezone"])
    pages = [{"name": p["name"],
              "when": as_datetime(p["date"], p.get("time", cfg["release_time"]), tz, p["name"])}
             for p in cfg.get("page_release", [])]
    blocks = timed_blocks(TOC.read_text(encoding="utf-8"))
    for p in pages:
        if p["name"] not in blocks:
            sys.exit(f"myst.yml has no block '# timed: {p['name']} (start)' ... '(end)'")
    unknown = set(blocks) - {p["name"] for p in pages}
    if unknown:
        sys.exit(f"myst.yml has timed blocks without a [[page_release]] entry: {', '.join(sorted(unknown))}")
    return pages


HIDDEN = "#~ "
MARKER = re.compile(r"^[ \t]*# timed: (?P<name>[\w-]+) \((?P<kind>start|end)\)")


def timed_blocks(toc):
    """Map each timed block name to its line ranges and its state (shown or hidden)."""
    lines, blocks, open_name = toc.splitlines(), {}, None
    for i, line in enumerate(lines):
        m = MARKER.match(line)
        if not m:
            continue
        if m["kind"] == "start":
            if open_name:
                sys.exit(f"myst.yml: timed block '{open_name}' is not closed before line {i + 1}")
            open_name, start = m["name"], i
        else:
            if m["name"] != open_name:
                sys.exit(f"myst.yml: '# timed: {m['name']} (end)' in line {i + 1} has no matching start")
            blocks.setdefault(open_name, []).append((start + 1, i))
            open_name = None
    if open_name:
        sys.exit(f"myst.yml: timed block '{open_name}' is not closed")
    states = {}
    for name, ranges in blocks.items():
        body = [lines[j] for a, b in ranges for j in range(a, b) if lines[j].strip()]
        hidden = {line.startswith(HIDDEN) for line in body}
        if len(hidden) != 1:
            sys.exit(f"myst.yml: timed block '{name}' is partly hidden; put '{HIDDEN}' in front of "
                     "all of its lines or none")
        states[name] = {"ranges": ranges, "shown": not hidden.pop()}
    return states


def set_block(toc, name, show):
    lines = toc.splitlines(keepends=True)
    for a, b in timed_blocks(toc)[name]["ranges"]:
        for j in range(a, b):
            if not lines[j].strip():
                continue
            if show and lines[j].startswith(HIDDEN):
                lines[j] = lines[j][len(HIDDEN):]
            elif not show and not lines[j].startswith(HIDDEN):
                lines[j] = HIDDEN + lines[j]
    return "".join(lines)


def is_tracked(path):
    result = subprocess.run(["git", "ls-files", "--error-unmatch", path], cwd=REPO,
                            capture_output=True)
    return result.returncode == 0


def toc_pattern(notebook):
    # Matches "- file: <notebook>" with or without a leading "# " (commented out).
    return re.compile(rf"^(?P<indent>[ \t]*)(?P<comment>#[ \t]*)?- file: {re.escape(notebook)}[ \t]*$",
                      re.MULTILINE)


def check_toc(releases):
    toc = TOC.read_text(encoding="utf-8")
    missing = [r["notebook"] for r in releases if not toc_pattern(r["notebook"]).search(toc)]
    if missing:
        sys.exit("myst.yml has no entry (commented or not) for:\n  " + "\n  ".join(missing))


def in_book(release, toc):
    return not toc_pattern(release["notebook"]).search(toc).group("comment")


def write_output(**values):
    """Pass values to later workflow steps (only inside GitHub Actions)."""
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            for key, value in values.items():
                f.write(f"{key}={value}\n")


def write_summary(text):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(text + "\n")


def parse_now(text, tz):
    if not text:
        return dt.datetime.now(tz)
    now = dt.datetime.fromisoformat(text)
    return now if now.tzinfo else now.replace(tzinfo=tz)


def parse_names(text, releases):
    names = [n.strip() for n in text.split(",") if n.strip()]
    unknown = [n for n in names if n not in {r["name"] for r in releases}]
    if unknown:
        sys.exit(f"unknown practical(s): {', '.join(unknown)}")
    return names


def cmd_status(args):
    tz, releases, takedown = load_schedule()
    check_toc(releases)
    toc = TOC.read_text(encoding="utf-8")
    now = parse_now(args.now, tz)
    window = now + dt.timedelta(minutes=args.lookahead)
    only = set(parse_names(args.only, releases)) if args.only else None
    online = {r["name"] for r in releases if is_tracked(r["notebook"]) or in_book(r, toc)}

    # What to do: release (due solutions), takedown (after the course) or nothing.
    if args.take_down or (only is None and takedown and takedown <= window and online):
        action, chosen = "takedown", [r for r in releases if r["name"] in online]
        start = now if args.take_down else takedown
    elif only is not None:
        action, chosen, start = "release", [r for r in releases if r["name"] in only], now
    else:
        # After the takedown, nothing is released on schedule any more (until the dates of the
        # next year are entered).
        course_running = takedown is None or now < takedown
        chosen = [r for r in releases if course_running and r["name"] not in online
                  and r["when"] <= window]
        action = "release" if chosen else ""
        start = max((r["when"] for r in chosen), default=now)
    chosen_names = {r["name"] for r in chosen}

    # Timed pages: shown from their date on, hidden before it.
    pages, page_plan, page_rows = load_pages(), [], []
    blocks = timed_blocks(toc)
    for p in pages:
        shown = blocks[p["name"]]["shown"]
        if not shown and p["when"] <= window:
            page_plan.append(f"{p['name']}=show")
            start = max(start, p["when"])
            state = "show now" if p["when"] <= now else "show soon"
        elif shown and p["when"] > window:
            page_plan.append(f"{p['name']}=hide")
            state = "hide now"
        else:
            state = "shown" if shown else "hidden"
        page_rows.append((p["name"], p["when"].strftime(FMT), state))

    rows = []
    after_takedown = takedown is not None and takedown <= now
    for r in releases:
        if r["name"] in chosen_names:
            state = "take down" if action == "takedown" else ("due" if r["when"] <= now or only else "due soon")
        elif r["name"] in online:
            state = "released"
        elif after_takedown and r["when"] < takedown:
            state = "taken down"
        else:
            state = "scheduled"
        rows.append((r["name"], r["when"].strftime(FMT), state, r["notebook"]))

    print(f"Now: {now.strftime(FMT)}")
    for row in rows:
        print("  {:<4} {:<26} {:<10} {}".format(*row))
    if takedown:
        print(f"  Takedown of all solutions: {takedown.strftime(FMT)}")
    for name, when, state in page_rows:
        print(f"  Page '{name}': from {when}: {state}")
    names = ",".join(r["name"] for r in chosen)
    page_changes = ",".join(page_plan)
    wait = max(0, int((start - now).total_seconds()))
    verb = {"release": "To release now", "takedown": "To take down now"}.get(action, "To do now")
    todo = ", ".join(x for x in (names, page_changes and f"pages {page_changes}") if x)
    print(f"\n{verb}: {todo or 'nothing'}" + (f" (after waiting {wait} s)" if todo and wait else ""))

    write_output(action=action, names=names, pages=page_changes, wait_seconds=wait)
    table = ["| Practical | Release (Swiss time) | Status |", "|---|---|---|"]
    table += [f"| {n} | {w} | {s} |" for n, w, s, _ in rows]
    if takedown:
        table.append(f"| all | {takedown.strftime(FMT)} | takedown |")
    table += [f"| page '{n}' | {w} | {st} |" for n, w, st in page_rows]
    write_summary(f"Checked at {now.strftime(FMT)}. Planned: {todo or 'nothing'}\n\n"
                  + "\n".join(table))


def cmd_release(args):
    _, releases, _ = load_schedule()
    check_toc(releases)
    names = parse_names(args.names, releases)
    by_name = {r["name"]: r for r in releases}
    solutions = Path(args.solutions).resolve()

    toc = TOC.read_text(encoding="utf-8")
    to_stage = []
    for name in names:
        r = by_name[name]
        for rel in r["files"]:
            src, dst = solutions / rel, REPO / rel
            if not src.exists():
                sys.exit(f"{name}: {rel} not found in the solutions repository")
            if dst.exists() and filecmp.cmp(src, dst, shallow=False):
                print(f"{name}: {rel} unchanged")
            else:
                print(f"{name}: {'update' if dst.exists() else 'add'} {rel}")
                if not args.dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
            to_stage.append(rel)
        if in_book(r, toc):
            print(f"{name}: already in myst.yml")
        else:
            print(f"{name}: enable {r['notebook']} in myst.yml")
            toc = toc_pattern(r["notebook"]).sub(lambda m: f"{m.group('indent')}- file: {r['notebook']}",
                                                 toc, count=1)

    if args.dry_run:
        print("\nDry run: nothing changed.")
        return
    TOC.write_text(toc, encoding="utf-8")
    # -f because .gitignore keeps solution files out of the repository until they are released.
    subprocess.run(["git", "add", "-f", "--", *to_stage, "myst.yml"], cwd=REPO, check=True)
    write_summary(f"\nReleased: {', '.join(names)}")


def cmd_takedown(args):
    _, releases, _ = load_schedule()
    check_toc(releases)
    names = parse_names(args.names, releases)
    by_name = {r["name"]: r for r in releases}

    toc = TOC.read_text(encoding="utf-8")
    to_remove = []
    for name in names:
        r = by_name[name]
        for rel in r["files"]:
            if is_tracked(rel):
                print(f"{name}: remove {rel}")
                to_remove.append(rel)
        if in_book(r, toc):
            print(f"{name}: comment out {r['notebook']} in myst.yml")
            toc = toc_pattern(r["notebook"]).sub(lambda m: f"{m.group('indent')}# - file: {r['notebook']}",
                                                 toc, count=1)

    if args.dry_run:
        print("\nDry run: nothing changed.")
        return
    # Remove the files first, so a failure leaves myst.yml untouched.
    if to_remove:
        subprocess.run(["git", "rm", "-q", "-f", "--", *to_remove], cwd=REPO, check=True)
    TOC.write_text(toc, encoding="utf-8")
    subprocess.run(["git", "add", "--", "myst.yml"], cwd=REPO, check=True)
    write_summary(f"\nTaken down: {', '.join(names)}")


def cmd_pages(args):
    pages = {p["name"] for p in load_pages()}
    toc = TOC.read_text(encoding="utf-8")
    for item in [x.strip() for x in args.set.split(",") if x.strip()]:
        name, _, what = item.partition("=")
        if name not in pages or what not in ("show", "hide"):
            sys.exit(f"--set expects name=show or name=hide with a known page, got {item!r}")
        print(f"page '{name}': {what}")
        toc = set_block(toc, name, show=(what == "show"))
    if args.dry_run:
        print("\nDry run: nothing changed.")
        return
    TOC.write_text(toc, encoding="utf-8")
    timed_blocks(toc)  # check the result is consistent
    subprocess.run(["git", "add", "--", "myst.yml"], cwd=REPO, check=True)
    write_summary(f"\nPages: {args.set}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    status = sub.add_parser("status", help="show the schedule and what is due")
    status.add_argument("--now", default="", help="pretend it is this time, e.g. 2027-03-16T17:05")
    status.add_argument("--lookahead", type=int, default=0,
                        help="also count releases or the takedown due within this many minutes")
    status.add_argument("--only", default="", help="release these practicals now, ignoring dates")
    status.add_argument("--take-down", action="store_true", help="take all released solutions down now")
    release = sub.add_parser("release", help="copy solutions in and enable them in myst.yml")
    release.add_argument("--solutions", required=True, help="clone of the private solutions repository")
    release.add_argument("--names", required=True, help="comma-separated practicals, e.g. P02,P03")
    release.add_argument("--dry-run", action="store_true")
    takedown = sub.add_parser("takedown", help="remove solutions and comment them out in myst.yml")
    takedown.add_argument("--names", required=True, help="comma-separated practicals, e.g. P02,P03")
    takedown.add_argument("--dry-run", action="store_true")
    pages = sub.add_parser("pages", help="show or hide timed blocks of myst.yml")
    pages.add_argument("--set", required=True, help="e.g. project-topics=show or project-topics=hide")
    pages.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    {"status": cmd_status, "release": cmd_release, "takedown": cmd_takedown,
     "pages": cmd_pages}[args.command](args)


if __name__ == "__main__":
    main()
