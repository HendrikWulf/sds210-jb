# Releasing the sample solutions of the practicals

Students clone this repository, so it must not contain a practical's sample solution before the
submission deadline. The solutions therefore live in the **private** repository
[`HendrikWulf/sds210-solutions`](https://github.com/HendrikWulf/sds210-solutions), with the same
file paths as here (`book/<lesson>/...`). After each deadline, a GitHub Action copies the solution
into this repository and publishes it in the book.

Only the sample solutions of the practicals are handled this way. The "Sample solution"
drop-downs inside the lesson pages are part of the lessons and always public.

## The pieces

| File | Role |
|---|---|
| `.github/solution-releases.toml` | The schedule: one entry per practical with its date, the time zone and the release time |
| `.github/workflows/release-solutions.yml` | The GitHub Action that runs the release |
| `.github/scripts/release_solutions.py` | Does the work: reads the schedule, copies files, edits `myst.yml` |
| `.gitignore` | Keeps solution files out of this repository until they are released |
| `myst.yml` | Table of contents: each solution has a commented entry (`# - file: ...`) that the release enables |
| Secret `SOLUTIONS_DEPLOY_KEY` | Lets the Action read the private repository (see below) |

## What happens on a release day

1. **Hourly check.** From February to June, GitHub starts the workflow every hour at minute 40
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

Each run writes a table of the whole schedule (released, due, scheduled) to its summary page:
**Actions → Release practical solutions → a run**.

If GitHub starts a scheduled run late (common in busy hours, usually a few minutes), the release
simply happens a little after 17:00. If a run is missed completely, the next hourly run releases
the solution. Releases that are overdue are always caught up.

## Common tasks

### Change a date or the time

Edit `.github/solution-releases.toml` and push to `main` (directly or with a pull request; the
pull request check validates the file). Dates are written `2027-03-16` without quotes. The
release time for all practicals is `release_time`; one practical can get its own time with a
line such as `time = "12:00"`. Times are Swiss local time; summer time is handled automatically.

Check the result locally:

```bash
python3 .github/scripts/release_solutions.py status
python3 .github/scripts/release_solutions.py status --now 2027-03-16T17:05   # as if it were then
```

### Release a solution early, or now

**Actions → Release practical solutions → Run workflow**, enter the practical (for example
`P03`) in *practical*, and run. This ignores the date.

### Fix a solution after it was released

Edit and push it in `sds210-solutions` (see that repository's README), then run the workflow by
hand as above with that practical. It copies the new version and publishes the book. If nothing
changed, the run says so and does nothing.

### Test without changing anything

Run the workflow by hand with **Dry run** ticked. Fill in *now* (for example `2027-03-16T17:05`)
to see what would be released at that moment. A dry run also checks that the deploy key still
works, because it clones the private repository.

### Next year

Change the dates in `solution-releases.toml`. To start again with all solutions hidden, remove
the released files from this repository and comment out their entries in `myst.yml` again:

```bash
git rm --cached book/*/*_practical*solution*.ipynb book/*/*_practical*solution*.md
# then put "# " in front of the solution entries in myst.yml, commit and push
```

Keep in mind that solutions released in earlier years remain in the history of this repository
and in students' clones.

### Add a new practical

Put the solution in `sds210-solutions` under the same path it will have here, add a commented
entry `# - file: book/...ipynb` at the right place in `myst.yml`, and add a `[[release]]` entry
to `solution-releases.toml`. File names must contain `_practical` and `solution` (as the current
ones do), so that `.gitignore` keeps them out of this repository.

## Things to know

- **Scheduled workflows are switched off after 60 days without commits.** GitHub disables
  scheduled workflows in public repositories when nothing was pushed for 60 days, for example
  over the summer or winter break. Before the semester, open **Actions → Release practical
  solutions**; if a banner says the workflow is disabled, click **Enable workflow** (or run
  `gh workflow enable release-solutions.yml`). A dry run then confirms everything works.
- **The deploy key.** `SOLUTIONS_DEPLOY_KEY` (Settings → Secrets and variables → Actions of this
  repository) holds the private half of an SSH key; the public half is a read-only deploy key of
  `sds210-solutions` (its Settings → Deploy keys). It does not expire. If it is removed or
  replaced, the "Get the solutions" step fails; create a new pair with
  `ssh-keygen -t ed25519 -N "" -f key`, add `key.pub` as a deploy key (read-only) and the
  contents of `key` as the secret, then delete both files.
- **Do not add solutions here by hand before their date.** `.gitignore` protects against
  `git add .`, but `git add -f` would still add them. Everything ever pushed to this public
  repository stays visible in its history.
- **Changing the hours the workflow runs.** The `cron` line in the workflow is in UTC:
  `"40 * * 2-6 *"` means minute 40 of every hour, every day, February to June. Releases at other
  times of day need no change, because the workflow runs every hour.
