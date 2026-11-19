# Yearly checklist for SDS210

What to do each year around the spring semester, in order. Tick the boxes in a copy, or work
through the list with Claude ("go through ANNUAL-CHECKLIST.md with me").

Related guides: [solution releases](.github/RELEASING-SOLUTIONS.md) ·
[course data on Source Cooperative](source-coop/UPLOAD.md)

## After the course (July – August)

- [ ] **2 July: check the takedown.** Actions → *Release practical solutions*: the run of
      1 July shows "Take down sample solutions after the course". The solution pages are gone
      from the book's table of contents.
- [ ] **Decide whether the practicals will be reused.** If yes, remove the released solutions
      from the repository's history before the next semester:
      `bash .github/scripts/purge_solution_history.sh` (needs `pip install git-filter-repo`).
      Then reset the clones on your other computers, as the script explains.
- [ ] **Note improvements while they are fresh**: problems students had, unclear tasks, errors
      in solutions. Solutions are edited in `sds210-solutions`, practicals and lessons here.

## Preparing the semester (January – mid-February)

### Dates and course pages

- [ ] **Schedule page** `book/01_about/4_schedule.md`: both tables (weeks, dates, holidays),
      lab times and room.
- [ ] **Project pages**: dates in `book/15_projects.md`, `book/15_projects/04_assessment.md`,
      `book/15_projects/05_reports.md`; the booking link (SharePoint sheet of the semester's
      Teams site) in `book/15_projects/06_presentation.md`.
- [ ] **Search for last year**: `grep -rn "2027" book --include=*.md` (with last year's number)
      finds remaining dates.

### Solution releases

- [ ] **New dates** in `.github/solution-releases.toml`: one `date` per practical, the
      `takedown_date`, and the date of the project topics page (`[[page_release]]` at the end).
      Pushing the file hides the topics page until its new date. Check with `python3 .github/scripts/release_solutions.py status`.
      The pull request check fails if the takedown is not after the last release.
- [ ] **Practicals changed?** Update the exercise notebooks here and the solutions in
      `sds210-solutions` (regenerate the `.md` with `jupytext --to myst <notebook>`, push).
      A renamed or new practical also needs its entry in `solution-releases.toml` and a
      commented line in `myst.yml` (see the solution release guide).

### Software environment

- [ ] **Package versions**: review `source-coop/environment.yml` (students) and
      `requirements.txt` (book build); test with
      `conda env create --file source-coop/environment.yml -n sds210-test`.
- [ ] **Upload the environment** to Source Cooperative: `stage_data.py`, `aws s3 sync`,
      `stage_data.py --verify-remote` (all in `source-coop/UPLOAD.md`).
- [ ] **Notebook outputs**: if packages changed, rerun the notebooks so the stored outputs
      (which the book shows) match; the pre-commit hook regenerates the paired `.md` files.
- [ ] **Jupyter Book version**: if you upgrade it, change it in all three places:
      `requirements.txt`, `.github/workflows/build.yml`, `.github/workflows/deploy.yml`.
- [ ] **Docker image** on the GitLab registry (`registry.gitlab.com/hendrikwulf/sds210`):
      rebuild if the environment changed.
- [ ] **Dependabot**: merge open pull requests that update the GitHub Actions.

### Course data

- [ ] **New or changed data files**: update `source-coop/manifest.csv`, stage, upload and verify
      (`source-coop/UPLOAD.md`), then point the notebooks to the new URLs.
- [ ] **Check that all data URLs work**:
      `conda run -n sds210 python source-coop/stage_data.py --out ~/sds210-source-coop --verify-remote`.

### GitHub, two weeks before the first release

- [ ] **Enable the release workflow.** Actions → *Release practical solutions*: if a banner says
      the workflow is disabled (GitHub does this after 60 days without commits), click
      **Enable workflow**.
- [ ] **Dry run**: *Run workflow* with **Dry run** ticked and *now* set to the first release
      time plus a few minutes (e.g. `2028-03-14T17:05`). The log must show the first practical
      as due and "Dry run: nothing changed". This also tests the deploy key.
- [ ] **Book online**: the last *Deploy book to GitHub Pages* run succeeded and the site loads.
- [ ] **Other computers**: `git pull` in your clones of `sds210-jb` and `sds210-solutions`.

## During the semester

- [ ] **Release days** (Tuesdays, 17:00): nothing to do. GitHub emails you if a run fails.
      A quick look at the book after the first release is reassuring.
- [ ] **Late June**: check that the release workflow is still enabled, so the takedown on
      1 July runs (see the 60-day rule above).
