# Git

## 1. Introduction

At some point, this will happen:
you delete a function that *definitely* worked yesterday, a notebook experiment goes wrong, or you realise that your “final_final_v3.ipynb” is not final at all.

This is where **[Git](https://git-scm.com/)** comes in.

Git is a version control system that **tracks every change** you make to your project files. It builds a complete history of your project, step by step. You can go back in time, compare versions, undo mistakes, and understand *what changed, when, and why*. Think of Git as a **never-forget undo button** for your code and notebooks.

This is especially useful in spatial data science, where projects evolve through trial and error. With Git, you can:

* experiment freely without losing any work
* understand what changed and why
* collaborate without overwriting each other

Git works locally on your computer and integrates well with tools you will use, such as VS Code and Jupyter notebooks. Combined with platforms like **GitHub**, it also lets you back up and share your work.

## 2. Learning Objectives

After working through this section, you should be able to:

* use **Git** to track changes in code and notebooks
* save and restore project states using commits
* sync a local project with **GitHub**

These objectives focus on using Git as a **practical safety net** in your daily workflow. You will keep building on them as your projects grow and become more collaborative.

## 3. Git vs. GitHub

Before learning any commands, it’s important to get the **big picture** right. One of the most common sources of confusion is mixing up **Git** and **GitHub**. 

**Git** runs on *your computer*.
It tracks changes to your files and stores the full history of your project locally. You can use Git completely offline. A Git repository is best thought of as a **timeline** of your project.
Each point on that timeline is a **commit**, a snapshot of the entire project at a specific moment:

* all tracked files
* exactly as they looked then
* with a short message explaining what changed

Git does **not** save “versions of files”.
It saves **project states over time**. 
That’s why you can always go back, compare states, or undo mistakes without losing work.

**GitHub** lives *online*.
It hosts Git repositories on the web and acts as a **shared, central copy** of your project.
GitHub allows you to:

* back up your work safely
* collaborate with others without overwriting their changes
* share your work or make it public

GitHub does not track changes by itself, it **stores and synchronises** the history created by Git.

> **In short:** Git does the thinking. GitHub does the sharing.

---

**What happens where?**

* **Locally (Git)**

  * edit files
  * track changes
  * create commits
  * view project history

* **Online (GitHub)**

  * store a copy of the repository
  * sync work between machines
  * collaborate with others
  * share or publish code


```scss
Your computer (Git)        GitHub (online)
------------------        ----------------
edit files
↓
commit history   ───────▶ backup & sharing
```

---

**How Git thinks**

To use Git confidently, it helps to understand **how Git thinks**. Git does *not* save files one by one like `report_v1`, `report_v2`, or `final_final.ipynb`.

Instead, **Git** works with **snapshots**.

A Git repository is best thought of as a **timeline of your project**. Each point on that timeline is a **commit** — a snapshot of the entire project at a specific moment: all tracked files, exactly as they looked then, plus a short message explaining what changed.

If a file did not change, Git simply reuses it internally. That’s why Git is fast and efficient, even for large projects.

Because every commit is a snapshot, the project history is **fully recoverable**. You can go back to earlier states, compare two moments in time, or undo mistakes without panic. Nothing is overwritten — the past is still there.

> The key idea: Git does **not** store “file versions”.
> It stores **project states over time**.

Once this mental model clicks, Git commands stop feeling like magic and start feeling logical.

## 4. Git Setup

Before using Git in practice, we set it up **once**. This removes friction later and avoids confusing errors.

**Step 1: GitHub account**

Log in to your **[GitHub account](https://github.com/login)**. If you don't have one yet, [create an account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).  
Use an email address you’ll remember, as you’ll need the same one for Git.

**Step 2: Git installation**

Check in your Terminal whether **Git** is already installed:

```bash
# Check Git version
git --version

# Check installation location
which git # macOS/Linux
where git # Windows
```

If Git responds with a version number, you’re good. If not, use [this link](https://git-scm.com/install/) to install (G)it for your operating system, test it with `git --version` and come back here.

**Step 3: Identity configuration**

Git needs to know who you are. Set your name and email **once**:

```bash
# Replace with your actual name and GitHub email
git config --global user.name "Your Name"
git config --global user.email "your@email"
```

This information is attached to every commit you make.

**Step 4: Verify everything**

Check your setup:

```bash
# View all global configuration
git config --global --list

# Check specific values
git config --global user.name
git config --global user.email
```

```{admonition}
:class: warning
If Git is not installed or your name/email are wrong, **stop here and fix this first**. Otherwise, you will not be able to push your changes to GitHub.
```

---

## 5. Understanding Git

Before diving into commands, let’s understand the key concepts that make Git powerful for geospatial
programming.

### Core Git concepts

These four concepts cover almost everything you’ll need to know.

**Repository:**
A repository (short: repo) is just a **project folder** that Git watches.
It contains your files *and* the hidden information Git uses to track changes and history.

---

**Commit:**
A commit is a **snapshot of the project** at a specific moment in time.

* it has a unique ID
* it includes a short message explaining what changed
* you can always return to it

Think of a commit as a reliable **save point**.

---

**Branch:**
A branch is a **parallel timeline** of the same project.

* the `main` branch usually contains stable, working code
* other branches are used for experiments or new features

Branches let you try things out without breaking what already works.

---

**Remote**
A remote is a **linked copy of your repository stored online**, for example on GitHub.

* it acts as a backup
* it allows syncing between machines
* it enables collaboration

Git manages history locally. Remotes help you share it.

---

### The Git workflow 

Almost everything you do with **Git** follows the **same simple loop**:

```
edit → stage → commit → push
```

If you understand this loop, Git will feel more familiar.

---

**1. Working directory - *edit***

This is your normal project folder.
You edit files here: Python scripts, notebooks, text files.
At this point, Git is only *watching* and nothing is saved yet.

---

**2. Staging area - *select***

The staging area is where you **choose** what should go into the next snapshot.
You don’t have to commit everything you changed. You decide what belongs together.

> Think of staging as saying: *“These changes go together.”*

---

**3. Commit - *save a snapshot***

A commit creates a **snapshot of the staged changes** and adds it to the project history.
Each commit has:

* a unique ID
* a short message explaining what changed

Once committed, that state is safe. You can always return to it.

---

**4. Push / pull - *sync with GitHub***

* **push** → send your commits to **GitHub**
* **pull** → bring remote changes back to your computer

This is how you:

* back up your work
* sync between machines
* collaborate with others

---

***Git in VS Code*** 

VS Code includes built-in Git support. If Git is installed on your system, no additional extensions are required.

In the **Source Control** panel, you can see the same workflow you just learned:

- modified files → staging  
- staged files → commit  
- commit → push / pull  

VS Code also provides a visual diff viewer, which helps you inspect changes line by line before committing.

Extensions such as GitLens can add extra features, but they are **not required** for this course.

---

***Key takeaway***

```
Working directory → Staging area → Local history → GitHub
     (edit)            (add)         (commit)      (push)
```

> Git is not a collection of random commands.
> It’s one loop, repeated over and over — and it will be the backbone of this course.

## 6. Working with Git

In this subsection, you will learn how to use Git in practice: how to start projects, track changes, sync with GitHub, and recover from mistakes. These workflows will be reused throughout your work with Git and spatial projects.

---

### Starting a new project

There are **two common ways** to start working with Git. Which one you use depends on where the project starts.

---

***Option A: Start a project locally (empty folder → Git)***

Use this when you are starting **your own project from scratch**.

```bash
# go to your project folder
cd ~/my-geo-project

# turn the folder into a Git repository
git init

# check the repository status
git status
```

That’s it.
Your folder is now a Git repository and ready for commits. At this stage, everything still lives **only on your computer**.

---

***Option B: Clone an existing project (GitHub → local copy)***

Use this when a project already exists on **GitHub** (e.g. course material, group work, or an example repository).

1. Open the repository on GitHub
2. Click the **Code** button
3. Copy the repository URL

Then clone it:

```bash
# Download the repository from GitHub and create a local copy
# This also sets up a connection (remote) back to GitHub
git clone https://github.com/username/repository-name.git

# Change your directory to the newly created project folder
cd repository-name
```

This creates:

* a local copy of the project
* a Git repository
* a connection to GitHub

```{note}
If a repository does not belong to you (for example course material or someone else’s project), you usually cannot push changes to it. In this case, first fork the repository on GitHub to create a copy under your own account, and then clone your fork, not the original repository.
In collaborative workflows, changes are typically shared back via a **pull request**, which allows others to review your work before it is merged.
```

---

***Repository structure***

A clear repository structure makes Git more useful and your projects easier to understand for others *and* for future you.

For your project in this course, a simple and flexible structure is enough:

```text
my-project/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_processing.py
│   └── analysis.py
├── notebooks/
│   └── exploratory_analysis.ipynb
└── outputs/
    ├── figures/
    └── results/
```

You don’t need to follow this structure perfectly. The goal is **separation of concerns**:

* raw vs processed data
* code vs notebooks
* inputs vs outputs

For larger or long-term data science projects, you may want to use a standardised project structure, such as *[Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/)*.


***What to track and what to ignore***

Git works best when you track **code and documentation**, not everything your analysis produces.

**Track these files:**
- source code (`.py`, `.r`, `.sql`)
- Jupyter notebooks (`.ipynb`)
- configuration files (`requirements.txt`, `environment.yml`)
- documentation (`README.md`)
- small reference datasets

**Do NOT track these files (use `.gitignore`):**
- large data files
- temporary or cache files
- generated outputs that can be recreated
- environment files with secrets
- editor-specific files (e.g. `.vscode/`)

---

### Track changes

Once a repository is set up, the everyday workflow starts: you **edit files**, **stage changes**, and **commit snapshots**.

---

***1. Make a change***

Edit an existing file or create a new one, for example:

```text
analysis.py
```

At this point, Git notices that something changed, but nothing is saved yet.

---

***2. Check the current state***

Before doing anything else, check what Git sees:

```bash
# Show which files changed and their status
git status
```

To see *what exactly* changed inside files:

```bash
# Show line-by-line differences
git diff
```

`git status` tells you *what is different*.
`git diff` tells you *how it is different*.

---

***3. Stage changes (select what belongs together)***

Staging means choosing which changes should go into the next snapshot.

```bash
# Stage a specific file
git add analysis.py
```

Or, if all changes belong together:

```bash
# Stage all changes in the current directory
git add .
```

Think of staging as saying: *“These changes form one logical step.”*

---

***4. Commit changes (save a snapshot)***

Once changes are staged, create a commit:

```bash
# Commit staged changes with a message (-m)
git commit -m "Add rainfall analysis function"
```

This creates a snapshot that you can always return to.

You can also commit all **already tracked** files in one step:

```bash
# Stage and commit all tracked files (-a) at once
git commit -am "Update visualization parameters"
```

Use `-am` (all tracked + message) only when you know what is already tracked.
New files still need `git add` first.

---

***Writing good commit messages***

Commit messages are part of your project documentation. In geospatial and data-driven projects, they should clearly describe **what changed and why**. 
Good commit messages help you (and others) understand how an analysis evolved over time.

**Examples:**

```bash
git commit -m "Add NDVI calculation for Landsat 8 imagery"
git commit -m "Fix coordinate transformation bug in UTM conversion"
git commit -m "Update flood mapping algorithm to handle edge cases"
```

**Guidelines:**

* Start with a **verb** (Add, Fix, Update, Remove)
* Keep it **short** (ideally under 50 characters)
* Be **specific** about what changed

Clear concise messages are far more valuable than overly detailed ones.

---

### Working with GitHub

GitHub is a **remote repository** that allows you to store your project online, back it up, and collaborate with others. To exchange changes between your computer and GitHub, your local Git repository needs to be **linked** to the remote repository on GitHub.

***1. Connect your local repository to GitHub***

If your repository is not yet connected to GitHub, add the remote repository URL once:

```bash
# Add the GitHub repository as a remote called "origin"
git remote add origin https://github.com/<your-username>/<repo-name>.git
```

You only need to do this **once per repository**.

You can verify (-v) the connection with:

```bash
# Show all configured remote repositories and their URLs
git remote -v
```
This lists the remote name (usually origin) and shows where Git will push to and pull from.
If you see a GitHub URL here, the connection is set up correctly.

---

***2. Push changes to GitHub***

After committing changes locally, you still have them only on your computer.
To upload them to GitHub, you need to push.

**First push (sets the default branch):**

```bash
# Push the local 'main' branch to the remote called 'origin'
# -u sets an upstream link so Git remembers where to push/pull
git push -u origin main
```

This uploads your commits to GitHub, links your local main branch to origin/main on GitHub and makes future pushes simpler. You only need `-u origin main` once.

**All subsequent pushes:**

```bash
# Push new commits using the remembered upstream connection
git push
```
Git now knows which branch to push and where to push it. That’s why this command is short.

---

***3. Pull changes from GitHub***

To bring changes **from GitHub back to your computer** (for example when switching machines or working with others), use:

```bash
# Download changes from GitHub and merge them into your local branch
git pull
```

This step fetches new commits from GitHub and merges them into your current branch.
In most cases, this happens automatically and quietly.

> If Git reports conflicts during a pull, this simply means the same file was changed in two places. Resolve the conflict, commit the result, and continue.


---

### Basic branching

Branching lets you work on **new ideas without breaking what already works**.
Instead of changing your main project directly, you create a **separate timeline** for experiments or fixes.
For most individual lab work, staying on the `main` branch is fine. Branches become especially useful in group work and larger projects.


---

***Create a new branch***

```bash
# Create a new branch called 'satellite-analysis'
# and switch to it immediately
git checkout -b satellite-analysis
```

You are now working on a **separate version** of the project.
The `main` branch stays unchanged.

---

***Check which branch you are on***

```bash
# List all branches
# The current branch is marked with *
git branch
```

This helps you avoid committing to the wrong branch.

---

***Switch back to the main branch***

```bash
# Switch back to the main branch
git checkout main
```

Nothing is lost here. Branches remember their own history.

---

***Merge your work back into main***

Once your work on the branch is done and tested, merge it:

```bash
# Merge the branch into the current branch (main)
git merge satellite-analysis
```

This brings the changes from `satellite-analysis` into `main`.

---

***Clean up after merging***

After a successful merge, the branch is no longer needed:

```bash
# Delete the branch (only works if it was merged)
git branch -d satellite-analysis
```

This keeps your repository tidy.

> Remember, a branch is a **safe workspace** to experiment freely before merging when things work.

### Viewing project history

One of Git’s biggest strengths is that it keeps a **complete history** of your project. You can inspect that history at any time.

```bash
# Show the full commit history (newest first)
git log
```

This shows:

* commit IDs
* authors
* dates
* commit messages

If the output is long, press `q` to exit.

---

For a shorter, easier-to-read view:

```bash
# Show a compact one-line history
git log --oneline
```

This is often the most useful overview.

---

To see the history of a **single file**:

```bash
# Show commits that affected one specific file
git log -- data_processing.py
```

This helps you understand when and why a file changed.

---

***Undoing changes***

Sometimes you realise that the **last commit was a mistake** — for example, the message was wrong or the commit was too early.

To undo the last commit **without losing your work**:

```bash
# Undo the last commit but keep all changes staged
git reset --soft HEAD~1
```

What this does:

* removes the last commit from history
* keeps all changes in your working directory
* lets you recommit correctly

> This is a **safe undo**: nothing is deleted.

Only use `git reset` on commits that **have not been pushed to GitHub yet**.
If a commit is already shared, undoing it requires a different approach.

---

## 7. Exercises

hese exercises focus on using Git as a **practical safety net** for your work. You are not expected to memorise commands — use the section above as a reference.

---

***Exercise 1: Git setup check***

**Objective:**
Confirm that Git is correctly installed and configured on your system.

**Tasks:**

1. Open a terminal.
2. Check that Git is installed:

   ```bash
   git --version
   ```
3. Check your Git identity:

   ```bash
   git config --global user.name
   git config --global user.email
   ```
4. Verify that your name and email are set correctly and match your GitHub account.

**Expected outcome:**

* Git responds with a version number.
* Your name and email are correctly configured.
* You are ready to use Git with GitHub.

> If this exercise fails, **stop here and fix it** before continuing.

---

***Exercise 2: Your project repository***

**Objective:**
Create a small, clean project repository and track its first changes.

**Tasks:**

1. Create a new folder for a project (e.g. `my-first-git-project`).
2. Initialise a Git repository inside it:

   ```bash
   git init
   ```
3. Create the following structure:

   ```
   my-first-git-project/
   ├── README.md
   ├── data/
   ├── notebooks/
   └── src/
   ```
4. Write a short description of the project in `README.md`.
5. Check the repository status:

   ```bash
   git status
   ```
6. Stage and commit your changes with a meaningful message.
7. Create a new repository on GitHub and connect it as a remote.
8. Push your commit to GitHub.

**Expected outcome:**

* A GitHub repository with:

  * a clear folder structure
  * a readable README
  * at least one commit
* You understand the loop: *edit → stage → commit → push*.

---

***Exercise 3: Safe experimentation with branches and history***

**Objective:**
Practice experimenting safely and using Git history as a safety net.

**Tasks:**

1. Create a new branch called `experiment`:

   ```bash
   git checkout -b experiment
   ```
2. Make a small change (e.g. edit the README or add a comment to a file).
3. Commit the change.
4. Switch back to the `main` branch.
5. Inspect the commit history:

   ```bash
   git log --oneline
   ```
6. Merge the `experiment` branch into `main`.
7. Delete the branch after merging.

**Expected outcome:**

* You understand that branches are **safe workspaces**.
* You can inspect project history and see how changes evolve.
* You feel confident experimenting without fear of breaking things.

---

After these exercises, you should feel that:

* Git helps you **stay in control**
* mistakes are **recoverable**
* and Git is a tool that *supports* your learning, not one that gets in the way

