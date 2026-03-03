---
title: Git

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Keeping track of change
</div>

---

## 1. Introduction

At some point, this might happen: you delete a function that *definitely* worked yesterday, a notebook experiment goes wrong, or you realise that your `final_final_v3.ipynb` is not final at all.

This is where **[Git](https://git-scm.com/)** comes in.

Git is a version control system that **tracks every change** you make to your project files. It builds a complete history of your project, step by step. You can go back in time, compare versions, undo mistakes, and understand *what changed, when, and why*. Think of Git as a **never-forget undo button** for your code and notebooks.

This is especially useful in spatial data science, where projects evolve through trial and error. With Git, you can:
* experiment freely without losing any work
* understand what changed and why
* collaborate without overwriting each other

Git works locally on your computer and integrates well with tools you will use, such as VS Code and Jupyter notebooks. Combined with platforms like **GitHub**, it also lets you back up and share your work.

<iframe
  width="100%"
  height="450"
  src="https://player.vimeo.com/video/41027679"
  title="What is Version Control"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

## 2. Learning Objectives

After working through this section, you should be able to:
* use **Git** to track changes in code and notebooks
* save and restore project states using commits
* sync a local project with **GitHub**

These objectives focus on using Git as a **practical safety net** in your daily workflow. You will keep building on them as your projects grow and become more collaborative.

---

## 3. Git vs. GitHub

Before learning any commands, it’s important to get the **big picture** right. One of the most common sources of confusion is mixing up **Git** and **GitHub**.

:::{figure} images/3_1_git_vs_github.png
:alt: Diagram comparing Git on a local laptop to GitHub in the cloud.
:width: 500px
:align: center

Git is the software running on your computer. GitHub is the online platform where you store and share your Git repositories.
:::

**Git** runs on *your computer*.
It tracks changes to your files and stores the full history of your project locally. You can use Git completely offline. A Git repository is best thought of as a **timeline** of your project. Each point on that timeline is a **commit**, a snapshot of the entire project at a specific moment. Every commit includes all tracked files exactly as they looked then, plus a **short message** explaining what changed.

**How Git thinks:** Git does **not** save “versions of files” (like `script_v1`, `script_v2`). It saves **project states over time**. If a file did not change, Git simply reuses it internally. Because every commit is a snapshot, nothing is ever overwritten. The past is still there, so you can always go back or undo mistakes without panic.

**GitHub** lives *online*.
It hosts Git repositories on the web and acts as a **shared, central copy** of your project. GitHub allows you to back up your work safely, collaborate with others without overwriting their changes, and share your work publicly. GitHub does not track changes by itself; it **stores and synchronises** the history created by Git.

**What happens where?**

* **Locally (Git):** Edit files, track changes, create commits, view history.
* **Online (GitHub):** Store a backup, sync between machines, collaborate, share code.

```{admonition} The Big Picture
:class: tip
**Git** does the thinking (tracking changes locally).  
**GitHub** does the sharing (hosting backups online).

```

<iframe
  width="100%"
  height="450"
  src="https://player.vimeo.com/video/41381741"
  title="What is Git?"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

## 4. Git Setup

Before using Git in practice, we set it up **once**. This removes friction later and avoids confusing errors.

**Step 1: GitHub account** Log in to your **[GitHub account](https://github.com/login)**. If you don't have one yet, [create an account](https://github.com/signup). Use an email address you’ll remember, as you’ll need the same one for Git.

**Step 2: Git installation** Check in your Terminal whether **Git** is already installed:

```bash
# Check Git version
git --version

# Check installation location
which git   # macOS/Linux
where git   # Windows

```

If Git responds with a version number, you’re good. If not, use [this link](https://git-scm.com/install/) to install Git for your operating system, test it with `git --version`, and come back here.

**Step 3: Identity configuration** Git needs to know who you are. Set your name and email **once**:

```bash
# Replace with your actual name and GitHub email
git config --global user.name "Your Name"
git config --global user.email "your@email"

```

This information is attached to every commit you make.

**Step 4: Verify everything** Check your setup:

```bash
# View all global configuration
git config --global --list

```

```{admonition} Caution
:class: caution
If Git is not installed or your name/email are wrong, **stop here and fix this first**. Otherwise, you will not be able to push your changes to GitHub later.

```

<iframe
width="100%"
height="450"
src="https://player.vimeo.com/video/41493906"
title="Get Going with Git"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen>
</iframe>

---

## 5. Understanding Git

Before diving into commands, let’s understand the key concepts that make Git powerful for geospatial programming.

### Core Git Concepts

* **Repository (Repo):** A project folder that Git watches. It contains your files *and* the hidden information Git uses to track changes and history.
* **Commit:** A snapshot of the project at a specific moment in time. Think of it as a reliable **save point**. Each commit has a unique ID, includes a short message explaining what changed, and once created, it is a state you can always return to.
* **Branch:** A parallel timeline of the same project. The `main` branch contains stable, working code, while other branches are used for experiments. They let you try things out without breaking what already works.
* **Remote:** A linked copy of your repository stored online (e.g., on GitHub). While Git manages history locally, remotes allow you to back up your work, sync between machines, and collaborate.

### The Git Workflow

Almost everything you do with **Git** follows the **same simple loop**:

`Edit → Stage → Commit → Push`

If you understand this loop, Git will feel familiar.

1. **Working Directory (*edit*):** This is your normal project folder. You edit files here (scripts, notebooks). At this point, Git is only *watching*, and nothing is saved yet.
2. **Staging Area (*select*):** This is where you **choose** which changes should go into the next snapshot. You decided what changes form a logical step together; you don't have to commit everything you edited at once.
> Think of staging as saying: *“These specific changes are ready to be saved.”*


3. **Commit (*save a snapshot*):** This creates a permanent **snapshot of the staged changes** and adds it to the project history. Once committed, that state is safe.
4. **Push / Pull (*sync with GitHub*):** These commands align the histories of your computer and your linked GitHub remote.
* **push** → send your local commits to **GitHub** (to back up or share).
* **pull** → bring remote changes from GitHub back to your computer.

---

### Git in VS Code

VS Code includes built-in Git support. If Git is installed on your system, no additional extensions are required.

In the **Source Control** panel (the branch icon on the left), you can see the same workflow you just learned visualized: modified files move to staging (+), staged files move to commit, and committed changes move to push. VS Code also provides a visual diff viewer, which helps you inspect changes line by line before staging them.

---

### Key Takeaway

```text
Working directory → Staging area → Local history → GitHub
     (edit)            (add)         (commit)      (push)

```

:::{figure} images/3_2_git_staging_workflow.png
:alt: The Git workflow moving from Working Directory to Staging Area to Local Repository to GitHub.
:width: 700px
:align: center

The core Git loop: editing files, staging the specific changes you want to save, committing them to history, and pushing the backup online.
:::

> Git is not a collection of random commands.
> It’s one loop, repeated over and over — and it will be the backbone of this course.
---

## 6. Working with Git

In this section, you will learn how to use Git in practice. We will cover two distinct workflows you will use in this course: syncing the official course material, and managing your own personal projects.

### Workflow A: Syncing the SDS210 Course Material

Throughout this course, new practical notebooks are released weekly on GitLab. Instead of downloading ZIP files every week, you can use Git to download the repository **once** and update it with a single command.

**1. Navigate to your desired location** Open your terminal (*Terminal* on macOS/Linux, *Git Bash* or *Anaconda Prompt* on Windows). Decide where you want to store the course folder and use `cd` (change directory) to go there.

```bash
# Example (macOS/Linux):
cd ~/Documents

# Example (Windows, Git Bash):
cd /c/Users/<username>/Documents

```

*(Tip: Type `ls` to list the files in your current folder to ensure you are in the right place.)*

**2. Clone the repository (Do this ONCE)** Download the repository to your computer. This creates a new folder called `sds210/` in your current directory.

```bash
git clone https://gitlab.com/HendrikWulf/sds210.git

```

**3. Enter the repository folder** This is the step that is most frequently forgotten! To run Git commands on the course material, you must be **inside** the folder that contains the hidden `.git` directory.

```bash
cd sds210

```

If you list (`ls`) all files (`-a`) you should see the course files and folders, including the hidden `.git` folder:

```bash
ls -a

```

**4. Update the repository (Do this WEEKLY)** Whenever new notebooks are added to the course, open your terminal, navigate inside your `sds210` folder, and pull the updates:

```bash
git pull

```

:::{figure} images/3_3_sds210_safe_workflow.png
:alt: Diagram showing the sds210 folder syncing from GitLab and notebooks being copied to an sds210-work folder.
:width: 500px
:align: center

Always copy notebooks out of the main course repository into your personal work folder before editing them to prevent merge conflicts.
:::

```{admonition} Crucial: Don't lose your own work!
:class: caution

If you edit the course notebooks directly inside the `sds210` folder and save them with their original name, pulling weekly updates may result in **merge conflicts** or overwrite your answers. 

**The Safe Workflow:**
1. Treat the `sds210/` repository as the **clean, read-only course source**.
2. Create a separate folder next to it for your own work (e.g., `sds210-work/`).
3. Copy the notebooks you want to solve or modify from the course folder into your work folder. 

```

#### Troubleshooting Course Updates

* **“fatal: not a git repository”** You are trying to pull, but you are not inside the cloned folder.
*Fix:* Run `cd path/to/sds210` first.
* **“Updates were rejected” / Merge conflicts** This happens if you accidentally modified files directly inside the repo instead of your work folder.
*Fix:* Move your modified notebook to a safe location outside the folder or rename them. Then, you can force the repo to match the online version using `git restore .` followed by `git pull`.

---

### Workflow B: Starting Your Own Project

When you are starting **your own personal project** from scratch (like your final assignment), you won't clone an existing repository. Instead, you will create an empty folder and turn it into a Git repository.

```bash
cd ~/Documents/my-geo-project
git init       # Turn the empty folder into a Git repository
git status     # Check the repository status

```

Everything now lives **only on your computer** until you link it to GitHub.

#### Repository Structure & Ignoring Files

A clear repository structure makes Git more useful. For your personal projects, a simple structure is enough:

```text
my-project/
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
└── outputs/

```

```{admonition} The .gitignore file
:class: important
Git works best when tracking **code and documentation**, not heavy data. 
**Do NOT track:** large datasets (`.csv`, `.tif`), temporary files, or environment files with passwords. Create a text file named `.gitignore` and type folder names (like `data/`) inside it to force Git to ignore them.

```

#### Tracking Your Changes

Once your personal repository is set up, the everyday workflow starts: **edit, stage, commit**.

```bash
# 1. Check the current state
git status   # Tells you WHAT is different
git diff     # Tells you exactly HOW files changed line-by-line

# 2. Stage changes (Select what belongs in this snapshot)
git add analysis.py
git add .               # Alternatively, stage ALL changes in the folder

# 3. Commit changes (Save the snapshot)
git commit -m "Add NDVI calculation for Landsat 8 imagery"

# Shortcut: Stage and commit all already-tracked files at once
git commit -am "Update visualization parameters"

```

*Note: Commit messages should be short (under 50 chars), start with a verb (Add, Fix, Update), and clearly describe **what changed and why**.*

#### Backing Up to GitHub

To safely back up your personal project and share it, you need to link your local repository to GitHub.

```bash
# Connect local repo to GitHub (Run ONCE per project)
git remote add origin [https://github.com/](https://github.com/)<your-username>/<repo-name>.git

# Verify the connection worked
git remote -v

# Push changes to GitHub for the FIRST time (sets default branch)
git push -u origin main

# All subsequent pushes
git push

# If collaborating, download others' updates to your computer
git pull

```

---

### Basic Branching

Branching lets you work on **new ideas without breaking what already works**. Instead of changing your main project directly, you create a **separate timeline** for experiments or fixes.

:::{figure} images/3_4_git_branching_merging.png
:alt: Diagram showing a main Git branch and a parallel experiment branch that merges back.
:width: 600px
:align: center

Branching allows you to safely experiment on a parallel timeline without affecting the stable `main` branch until you are ready to merge.
:::


```bash
# Create a new branch called 'experiment' and switch to it immediately
git checkout -b experiment

# Check which branch you are currently on
git branch

# ... edit files, add, and commit your experimental work ...

# Switch back to the stable main branch
git checkout main

# Merge your successful experiment into the main branch
git merge experiment

# Delete the branch after a successful merge to keep things tidy
git branch -d experiment

```

### Viewing History and Undoing

One of Git’s biggest strengths is that it keeps a complete history of your project.

```bash
# Show the full commit history (press 'q' to exit)
git log

# Show a compact one-line history (often the most useful)
git log --oneline

# Show commits that affected one specific file
git log -- data_processing.py

```

Sometimes you realise that the **last commit was a mistake** (e.g., the message was wrong or it was too early). To undo the last commit **without losing your work**:

```bash
# Undo the last commit BUT keep your file changes safe in the staging area
git reset --soft HEAD~1

```

*(Note: Only use `git reset` on commits that **have not been pushed to GitHub yet**.)*

---

## 7. Exercises

These exercises focus on using Git as a **practical safety net**. Use the section above as a reference.

#### Exercise 1: Git setup check

**Objective:** Confirm that Git is correctly installed and configured.

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

#### Exercise 2: Your project repository

**Objective:** Create a clean project repository and track its first changes.

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

#### Exercise 3: Safe experimentation with branches

**Objective:** Practice experimenting safely using Git history.

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

After these exercises, you should feel that Git helps you **stay in control**, mistakes are **recoverable**, and Git is a tool that *supports* your learning rather than getting in the way.
