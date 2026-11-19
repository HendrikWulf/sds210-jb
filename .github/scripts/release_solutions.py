"""Release the sample solutions of the practicals on schedule.

Used by .github/workflows/release-solutions.yml; see .github/RELEASING-SOLUTIONS.md.
Needs only the Python standard library (3.11 or newer).

    python3 .github/scripts/release_solutions.py status
        Show the schedule and which solutions are released, due or still scheduled.
        Also checks the schedule: every notebook needs an entry in myst.yml.

    python3 .github/scripts/release_solutions.py status --now 2027-03-16T17:05
        The same, as if it were that time (Europe/Zurich unless an offset is given).

    python3 .github/scripts/release_solutions.py release --solutions DIR --names P02,P03
        Copy those solutions from DIR (a clone of sds210-solutions) into this repository,
        enable their entries in myst.yml and stage them for a commit (git add -f).
        Add --dry-run to only print what would change.

A solution counts as released when its notebook is tracked by git in this repository.
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


def load_schedule():
    cfg = tomllib.loads(SCHEDULE.read_text(encoding="utf-8"))
    tz = ZoneInfo(cfg["timezone"])
    releases = []
    for entry in cfg["release"]:
        if not isinstance(entry["date"], dt.date):
            sys.exit(f"{entry['practical']}: date must be written as YYYY-MM-DD without quotes")
        time = dt.time.fromisoformat(entry.get("time", cfg["release_time"]))
        notebook = entry["notebook"]
        releases.append({
            "name": entry["practical"],
            "when": dt.datetime.combine(entry["date"], time, tzinfo=tz),
            "notebook": notebook,
            "files": [notebook, str(Path(notebook).with_suffix(".md"))],
        })
    names = [r["name"] for r in releases]
    if len(names) != len(set(names)):
        sys.exit("solution-releases.toml: each practical may appear only once")
    return tz, releases


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


def cmd_status(args):
    tz, releases = load_schedule()
    check_toc(releases)
    now = parse_now(args.now, tz)
    window = now + dt.timedelta(minutes=args.lookahead)
    only = {n.strip() for n in args.only.split(",")} if args.only else None
    if only and not only <= {r["name"] for r in releases}:
        sys.exit(f"unknown practical(s): {', '.join(sorted(only - {r['name'] for r in releases}))}")

    due, rows = [], []
    for r in releases:
        released = is_tracked(r["notebook"])
        if only is not None:
            state = "selected" if r["name"] in only else ("released" if released else "scheduled")
        elif released:
            state = "released"
        elif r["when"] <= now:
            state = "due"
        elif r["when"] <= window:
            state = "due soon"
        else:
            state = "scheduled"
        if state in ("due", "due soon", "selected"):
            due.append(r)
        rows.append((r["name"], r["when"].strftime("%a %d %b %Y %H:%M %Z"), state, r["notebook"]))

    print(f"Now: {now.strftime('%a %d %b %Y %H:%M %Z')}")
    for row in rows:
        print("  {:<4} {:<26} {:<10} {}".format(*row))
    names = ",".join(r["name"] for r in due)
    latest = max((r["when"] for r in due if only is None), default=now)
    wait = max(0, int((latest - now).total_seconds()))
    print(f"\nTo release now: {names or 'nothing'}" + (f" (after waiting {wait} s)" if names and wait else ""))

    write_output(due=names, wait_seconds=wait)
    table = ["| Practical | Release (Swiss time) | Status |", "|---|---|---|"]
    table += [f"| {n} | {w} | {s} |" for n, w, s, _ in rows]
    write_summary(f"Checked at {now.strftime('%d %b %Y %H:%M %Z')}\n\n" + "\n".join(table))


def cmd_release(args):
    _, releases = load_schedule()
    check_toc(releases)
    names = [n.strip() for n in args.names.split(",") if n.strip()]
    by_name = {r["name"]: r for r in releases}
    unknown = [n for n in names if n not in by_name]
    if unknown:
        sys.exit(f"unknown practical(s): {', '.join(unknown)}")
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
        pattern = toc_pattern(r["notebook"])
        match = pattern.search(toc)
        if match.group("comment"):
            print(f"{name}: enable {r['notebook']} in myst.yml")
            toc = pattern.sub(lambda m: f"{m.group('indent')}- file: {r['notebook']}", toc, count=1)
        else:
            print(f"{name}: already in myst.yml")

    if args.dry_run:
        print("\nDry run: nothing changed.")
        return
    TOC.write_text(toc, encoding="utf-8")
    # -f because .gitignore keeps solution files out of the repository until they are released.
    subprocess.run(["git", "add", "-f", "--", *to_stage, "myst.yml"], cwd=REPO, check=True)
    write_summary(f"\nReleased: {', '.join(names)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    status = sub.add_parser("status", help="show the schedule and what is due")
    status.add_argument("--now", default="", help="pretend it is this time, e.g. 2027-03-16T17:05")
    status.add_argument("--lookahead", type=int, default=0,
                        help="also count releases due within this many minutes as due")
    status.add_argument("--only", default="", help="treat these practicals as due, ignoring dates")
    release = sub.add_parser("release", help="copy solutions in and enable them in myst.yml")
    release.add_argument("--solutions", required=True, help="clone of the private solutions repository")
    release.add_argument("--names", required=True, help="comma-separated practicals, e.g. P02,P03")
    release.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    {"status": cmd_status, "release": cmd_release}[args.command](args)


if __name__ == "__main__":
    main()
