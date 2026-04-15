---
title: Repository & Code

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
How to organise, track, and share a reproducible programming project
</div>

---

Your project is assessed not only by what your code does, but also by how clearly it is organized, documented, and shared. A well-structured repository allows another student to understand your workflow, rerun your analysis, and learn from your approach.

In SDS210, reproducibility is an explicit grading requirement. Your final report must include a link to a public GitHub or GitLab repository, and this repository must contain everything necessary for someone else to reproduce your exact results on a different machine.

This section explains exactly what that means in practice.

```{admonition} Big idea
:class: tip

A good repository does not only store files. It is an active communication tool that explains your workflow.
```

---

## 1. The GitHub / GitLab Repository

For this project, you are required to maintain a **public repository** on either **GitHub** or **GitLab**. This repository serves multiple critical functions:

* It acts as a secure, cloud-based backup of your work.
* It provides a transparent history of how your project evolved over time.
* It is the primary mechanism for sharing your code and notebooks.
* It is the foundation of scientific reproducibility.

### Git vs. GitHub/GitLab

It is important to understand the distinction between these tools:

* **Git** is the software running locally on your computer that tracks changes to your files.
* **GitHub** and **GitLab** are online platforms that host your Git repositories in the cloud.

```{admonition} GitHub or GitLab
:class: note

Both platforms are excellent, free, and industry-standard. If you are unsure which to use:
* **GitHub** is the most popular platform globally. It is a great choice if you want to build a public portfolio to show future employers.
* **GitLab** is heavily used in academic and enterprise environments. If you are already using the university's GitLab instance for other courses, sticking with GitLab might be the most convenient option.

Ultimately, the underlying Git commands you type on your computer are identical for both. Choose the one you feel most comfortable with!
```

> If you need a refresher on configuring your [Git Setup](https://hendrikwulf.github.io/sds210-jb/book/setup/git/#id-4-git-setup) or [Starting Your Own Project](https://hendrikwulf.github.io/sds210-jb/book/setup/git/#workflow-b-starting-your-own-project), please review the [Git setup chapter](https://hendrikwulf.github.io/sds210-jb/book/setup/git/ .

### Use Git from Day One

Git should be integrated into your workflow from the very beginning. Instead of saving multiple messy files like `project_final_v2.ipynb` or `really_final_map.py`, you will use Git to save ("commit") meaningful snapshots of your project over time.

Using Git throughout the project allows you to safely experiment with new code, easily recover from mistakes by rolling back to previous versions, and continuously back up your progress online. A project that is tracked with Git from day one is vastly easier to manage than one that is hastily uploaded the night before the deadline.

### Ignoring Large Files (`.gitignore`)

While Git is excellent for tracking your scripts and notebooks, it is not designed to store massive datasets. It is recommended that you do not commit large files to your repository. Before making your first commit, ensure you have a `.gitignore` file in your root directory and explicitly list your `data/` folder (along with any large or temporary output files) to prevent them from being tracked and uploaded to the cloud.

### Getting Started: A Step-by-Step Guide

If you are setting up a project repository for the first time, the order of operations can be confusing. The easiest and safest way to start your project is to create the repository online *first*, and then bring it down to your computer. Follow these steps:

1.  **Create the Remote Repository:** Go to GitHub or GitLab and create a new repository. During the setup screen, be sure to check the boxes to automatically initialize the repository with a **`README.md`** file and a **`.gitignore`** file (choose the *Python* template if asked).
2.  **Clone it to Your Computer:** Copy the URL of your new repository and use `git clone <URL>` in your terminal to link the cloud repository to your local machine. This downloads the initialized folder to your computer.
3.  **Build the File Structure:** Open the newly cloned folder on your computer and create your empty subfolders (e.g., create a `data/` folder and a `notebooks/` folder).
4.  **Configure your `.gitignore`:** Open the `.gitignore` file in a text editor and add the line `data/` at the bottom. This explicitly tells Git to ignore any raw data or shapefiles you place in that folder, preventing massive files from being tracked and crashing your cloud upload.
5.  **Start Coding and Committing:** Create your first Jupyter Notebook inside the `notebooks/` folder. Now, you can safely experiment with your code, using `git commit` to save meaningful snapshots of your progress, and `git push` to back everything up online.

<!-- end list -->

```{admonition} Minimum expectation
:class: important

Create your remote repository immediately and commit your work regularly. **Do not** wait until the final week to upload your files. A project that is tracked with Git from day one is vastly easier to manage than one that is hastily uploaded the night before the deadline.
```

---

## 2. Recommended Repository Structure

A clean folder structure makes your project immediately easier to understand and rerun. While there is no single "perfect" layout, your repository must be logical, tidy, and easy to navigate.

Do not treat your repository like a dump for everything on your computer. Massive raw data files (unless strictly necessary), temporary `.csv` outputs, and unrelated coursework do not belong in your main project repository.

### A Standard Project Structure

A professional, easy-to-follow starting point looks like this:

```text
my-project/
├── README.md               # The manual for your project
├── .gitignore              # List of (large) files that shouldn't sync
├── environment.yml         # The list of required Python packages
├── data/                   # The raw and processed datasets
│   ├── raw/
│   └── processed/
├── notebooks/              # Your Jupyter Notebooks
└── outputs/                # Your final exported maps and charts
```

By explicitly separating your data, code, and outputs, you make it incredibly easy for a reviewer to understand the purpose of every file. If your project grows complex and you begin writing custom Python functions to keep your notebook clean, you might also add a `src/` or `scripts/` folder to hold those `.py` files.

```{admonition} The Structure Test
:class: note

Could a fellow student open your repository for the first time and instantly know where to find your data, your code, and your final maps?
```

---

## 3. The README and Setup Instructions

The **`README.md`** is the most important text file in your repository. It is the very first thing anyone sees when they visit your GitHub/GitLab page, and it serves as the instruction manual for your project. A strong README drastically reduces confusion and ensures your project is truly reproducible.

You do not need to write a massive essay. A concise, clearly formatted README is much better than a long, rambling one.

### What to Include in your README

A robust README should contain the following sections:

1.  **Project Title & Description:** A one or two-sentence summary of the spatial question you are answering.
2.  **Data Sources:** Explicit links to where the raw open data was obtained.
3.  **Setup Instructions:** Exactly what software and libraries are required to run the code (e.g., pointing to an `environment.yml` or `requirements.txt` file).
4.  **Execution Order:** Clear instructions on how to run the project (e.g., *"Run the `data_cleaning.ipynb` notebook first, followed by `spatial_analysis.ipynb`"*).

If your project relies on special local settings or manual data downloads that you fail to explain in the README, your project is not reproducible.

```{admonition} Big mistake to avoid
:class: caution

Never assume the reviewer knows where your data is stored, which specific packages you used, or the order in which to run your files. State everything explicitly in the README.
```

---

## 4. Reproducible Notebooks

Your Jupyter Notebook is the beating heart of your project. It weaves together your Python code, your spatial visualizations, and your markdown explanations. However, a notebook is only valuable if it can be executed reliably by someone else. Therefore, your notebook must be capable of running from top to bottom on a different computer without crashing.

### The Golden Rule: Relative Paths

The most common reason student projects fail to reproduce is the use of absolute file paths.

**Bad (Absolute Path):** This will immediately crash on any computer that is not yours.

```python
gdf = gpd.read_file("/Users/yourname/Desktop/sds210_project/data/Zurich.gpkg")
```

**Good (Relative Path):** This will work flawlessly on any computer, as long as the repository structure is maintained.

```python
gdf = gpd.read_file("data/Zurich.gpkg")
```

### Keeping the Notebook Readable

A good notebook is a document meant for human eyes, not just a script for the Python interpreter. To keep it readable:

  * Use short markdown cells to introduce new sections of analysis.
  * Group your code logically (e.g., all imports in the very first cell).
  * Avoid leaving large blocks of broken, commented-out, or unnecessary "test" code in your final submission.
  * Ensure your printed outputs and maps actually help the reader interpret the analysis.

<!-- end list -->

```{admonition} The Ultimate Check
:class: tip

Before you submit your project, click **"Kernel -> Restart & Run All"** in Jupyter. If the notebook runs from the very top to the very bottom without throwing a single error, you have achieved basic reproducibility.
```

---

## 5. Code Quality Expectations

We do not expect you to write professional, commercial-grade software. However, your code must be structured, readable, and thoughtful. Code quality is a formal part of the project assessment because it directly impacts both the explanation and the reproducibility of your work.

### What Good Code Looks Like

Strong project code generally exhibits the following traits:

  * It uses highly descriptive, meaningful variable names (e.g., `zurich_neighborhoods_gdf` instead of just `data2`).
  * It avoids unnecessary repetition. If you copy and paste the same block of plotting code four times, you should wrap it into a single, reusable function.
  * It includes concise `# comments` to explain *why* a complex operation is happening, not just *what* it is doing. (Remember: clarity is the goal, not clutter. Do not comment every single line).

### Git as a Code Quality Tool

Git is not just a backup tool; it is a mechanism for maintaining code quality. By forcing you to work in small, intentional steps, Git keeps your project organized.

A sensible routine looks like this:

1.  Make a small, meaningful improvement to your code.
2.  Test that the improvement actually works.
3.  **Commit** the change with a clear, descriptive message (e.g., `"Filter wildfire dataset to remove NaN coordinates"` or `"Add Equal Earth projection to final map"`).
4.  **Push** the commit to GitHub/GitLab.

These commit messages create a transparent history of your project, making it easy to track your development process and pinpoint exactly when a bug was introduced.

---

```{admonition} In Summary
:class: note

A strong project repository is clean, well-structured, and effortless to rerun. Use Git from the very beginning, organize your folders logically, write a README that explicitly explains the setup process, ensure your notebook uses relative paths to run from top to bottom, and treat code quality as a core component of your scientific communication.
```