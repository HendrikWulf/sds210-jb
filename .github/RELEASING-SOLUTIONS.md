# Releasing the sample solutions of the practicals

Students clone this repository, so it must not contain a practical's sample solution before the
submission deadline. The solutions therefore live in the **private** repository
[`HendrikWulf/sds210-solutions`](https://github.com/HendrikWulf/sds210-solutions), with the same
file paths as here (`book/<lesson>/...`). After each deadline, a GitHub Action copies the solution
into this repository and publishes it in the book. After the course, the same Action takes all
solutions down again.

Only the sample solutions of the practicals are handled this way. The "Sample solution"
drop-downs inside the lesson pages are part of the lessons and always public.

For the yearly preparation of the course, see [`ANNUAL-CHECKLIST.md`](../ANNUAL-CHECKLIST.md).

## The pieces

| File | Role |
|---|---|
| `.github/solution-releases.toml` | The schedule: one entry per practical with its date, the release time, the takedown date, the time zone |
| `.github/workflows/release-solutions.yml` | The GitHub Action that runs releases and the takedown |
| `.github/scripts/release_solutions.py` | Does the work: reads the schedule, copies or removes files, edits `myst.yml` |
| `.github/scripts/purge_solution_history.sh` | Run by you once a year after the takedown: removes the solutions from the repository's history |
| `.gitignore` | Keeps solution files out of this repository until they are released |
| `myst.yml` | Table of contents: each solution has a commented entry (`# - file: ...`) that the release enables |
| Secret `SOLUTIONS_DEPLOY_KEY` | Lets the Action read the private repository (see below) |

(`.github` is a hidden folder. In Finder, press Cmd + Shift + . to show it.)

## The year of a solution

```text
scheduled ──(release date, 17:00)──▶ released ──(takedown, 1 July 23:59)──▶ taken down
  only in sds210-solutions          in the book and          gone from the book and the
                                    in this repository       current files; still in the
                                                             history until you purge it
```

## What happens on a release day

1. **Hourly check.** From February to July, GitHub starts the workflow every hour at minute 40
   (UTC). The first step reads the schedule and compares it with the clock. A solution is
   *released* once its notebook is tracked in this repository; otherwise it is *due* when its
   release time has passed. A solution due within the next 30 minutes also counts. If nothing
   is due, the run ends after a few seconds, which is what almost every run does.
2. **Waiting.** If a solution is due within the next 30 minutes, the job sleeps until the exact
   release time, for example the 16:40 run waits 20 minutes until 17:00.
3. **Getting the solution.** The job clones the private repository into a folder `_solutions`,
   using the deploy key stored in the secret `SOLUTIONS_DEPLOY_KEY`.
4. **Copying.** The script copies the notebook and its paired `.md` file into `book/...`, and in
   `myst.yml` turns `# - file: book/.../xx_practical-...-solution.ipynb` into
   `- file: ...`, so the page appears in the book.
5. **Committing.** The job commits these files to `main` as `github-actions[bot]`, with the
   message "Release sample solution P03". From now on the solution is in the repository:
   students get it with their next `git pull`, and its Colab badge works.
6. **Publishing.** The job starts the workflow *Deploy book to GitHub Pages*, which rebuilds the
   book. About two minutes later the solution is online.

Each run writes a table of the whole schedule (released, due, scheduled, taken down) to its
summary page: **Actions → Release practical solutions → a run**.

If GitHub starts a scheduled run late (common in busy hours, usually a few minutes), the release
simply happens a little after 17:00. If a run is missed completely, the next hourly run releases
the solution. Releases that are overdue are always caught up.

## What happens at the takedown

At `takedown_date` / `takedown_time` (1 July 2027, 23:59), the hourly run at 23:40 waits until
23:59, then removes all released solution files from this repository (`git rm`), comments their
entries in `myst.yml` out again, commits ("Take down sample solutions after the course") and
redeploys the book. After that, scheduled releases stop: the dates have passed, but nothing is
released again until you enter the dates of the next year.

What the takedown cannot do: the solutions stay in the **history** of this repository (old
commits) and in every clone students made during the semester. If the practicals will be used
again, remove them from the history before the next semester:

```bash
pip install git-filter-repo        # once
bash .github/scripts/purge_solution_history.sh
```

The script works on a fresh copy from GitHub (your working folder is not touched), saves a
backup of the full history to `~/sds210-jb-history-backup-<date-time>.bundle`, rewrites the
history without the solution files, checks that the current files are unchanged, and asks before
it force-pushes. It refuses to run while solutions are released. Afterwards, every existing
clone has to be reset (the script prints how), so run it in summer, not during the semester.

## Timed pages (project topics)

The same workflow shows single pages of the book from a given date on. The page with the
project topics (`book/15_projects/01_topics.md`) appears on **12 April 2027 at 09:00** and stays
afterwards. The rest of the Projects section is always visible.

- **Schedule:** a `[[page_release]]` entry at the end of `.github/solution-releases.toml`
  (`name = "project-topics"`, `date`, `time`).
- **What is hidden:** the lines of `myst.yml` between `# timed: project-topics (start)` and
  `# timed: project-topics (end)`, i.e. the table-of-contents entry of the topics page. While
  hidden, each line starts with `#~ `; the workflow adds or removes that prefix.
- **Before the date** the workflow hides the block, **from the date on** it shows it. The hourly
  run at 08:40 waits until 09:00, then shows the page, commits ("Update timed pages") and
  redeploys the book. Pushing a changed schedule also starts the workflow, so a new date takes
  effect immediately (for example, next year's date hides the page again).
- **Not secret:** the page file stays in this repository and is visible on GitHub; only the
  book leaves it out.
- **Links into the hidden page**, such as the "topics" link on the Projects overview page
  (`book/15_projects.md`), lead nowhere while it is hidden and work from the date on.
- **Show or hide by hand:** `python3 .github/scripts/release_solutions.py pages --set project-topics=show`
  (or `=hide`), then commit `myst.yml`. The next scheduled run puts the block back to what the
  date says, so to change it for good, change the date.
- **Another timed page:** wrap its lines in `myst.yml` in `# timed: <name> (start)` /
  `# timed: <name> (end)` and add a `[[page_release]]` entry with that name.

## Common tasks

### Change a date or the time

Edit `.github/solution-releases.toml` and push to `main` (directly or with a pull request; the
pull request check validates the file). Dates are written `2027-03-16` without quotes. The
release time for all practicals is `release_time`; one practical can get its own time with a
line such as `time = "12:00"`. Times are Swiss local time; summer time is handled automatically.
The takedown must come after the last release, otherwise the check fails, which catches a
forgotten year.

Check the result locally:

```bash
python3 .github/scripts/release_solutions.py status
python3 .github/scripts/release_solutions.py status --now 2027-03-16T17:05   # as if it were then
```

### Release a solution early, or now

**Actions → Release practical solutions → Run workflow**, enter the practical (for example
`P03`) in *practical*, and run. This ignores the date (also after the takedown).

### Fix a solution after it was released

Edit and push it in `sds210-solutions` (see that repository's README), then run the workflow by
hand as above with that practical. It copies the new version and publishes the book. If nothing
changed, the run says so and does nothing.

### Take the solutions down early

**Run workflow** with **Take down** ticked. All released solutions are removed at once.

### Test without changing anything

Run the workflow by hand with **Dry run** ticked. Fill in *now* (for example `2027-03-16T17:05`
or `2027-07-01T23:59`) to see what would happen at that moment. A dry run of a release also
checks that the deploy key still works, because it clones the private repository.

### Next year

Follow [`ANNUAL-CHECKLIST.md`](../ANNUAL-CHECKLIST.md): new dates and takedown date in
`solution-releases.toml`, purge the history if practicals are reused, enable the workflow, dry
run.

### Add a new practical

Put the solution in `sds210-solutions` under the same path it will have here, add a commented
entry `# - file: book/...ipynb` at the right place in `myst.yml`, and add a `[[release]]` entry
to `solution-releases.toml`. File names must look like the current ones
(`<nr>_practical_L<nr>_solution.ipynb`, with `-` or `_`, `solution` or `solutions`), so that
`.gitignore` and the purge script recognise them.

## Things to know

- **Scheduled workflows are switched off after 60 days without commits.** GitHub disables
  scheduled workflows in public repositories when nothing was pushed for 60 days, for example
  over the summer or winter break. Before the semester, open **Actions → Release practical
  solutions**; if a banner says the workflow is disabled, click **Enable workflow** (or run
  `gh workflow enable release-solutions.yml`). A dry run then confirms everything works.
  The release commits count as activity: with the last release on 11 May, the takedown on
  1 July is within the 60 days. If you move the last release much earlier, check that the
  workflow is still enabled in late June.
- **The deploy key.** `SOLUTIONS_DEPLOY_KEY` (Settings → Secrets and variables → Actions of this
  repository) holds the private half of an SSH key; the public half is a read-only deploy key of
  `sds210-solutions` (its Settings → Deploy keys). It does not expire. If it is removed or
  replaced, the "Get the solutions" step fails; create a new pair with
  `ssh-keygen -t ed25519 -N "" -f key`, add `key.pub` as a deploy key (read-only) and the
  contents of `key` as the secret, then delete both files.
- **Do not add solutions here by hand before their date.** `.gitignore` protects against
  `git add .`, but `git add -f` would still add them. Everything ever pushed to this public
  repository stays visible in its history until it is purged.
- **When the workflow runs.** The `cron` line in the workflow is in UTC: `"40 * * 2-7 *"` means
  minute 40 of every hour, every day, February to July. Releases at other times of day need no
  change, because the workflow runs every hour. If the takedown moves to August or later, change
  `2-7` to include that month.
- **Copies outside this repository.** Forks of this repository and GitHub's snapshots of old
  pull requests keep their own copies; the purge script cannot reach them. GitHub Support can
  remove cached views and pull-request snapshots (docs: "Removing sensitive data from a
  repository").
