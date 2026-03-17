---
title: Running notebooks

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
Different options to work with notebooks
</div>

---

```{admonition} Big idea
:class: tip
A notebook is an interactive document where **code runs in a {term}`kernel`** and outputs appear immediately.  
Choosing the right way to run notebooks helps you work efficiently and keep your work reproducible.
```

In this course, we work almost entirely with **Jupyter notebooks** (`.ipynb`).
Before we start coding, you need one practical decision:

**Where will your notebook run?**

Your main options to run notebooks are:

* **online** (fastest to start, no installation)
* **locally** on your computer (best for long-term use and projects)

There is no single “best” option. Use what fits your setup and learning goals.

This page gives you a quick overview of the main options.
The hands-on practice (editing cells, running code, restart & run all, avoiding hidden state) is covered in the **Practical** section.


## 1. Running online

### Option 1: Using Colab

**Google Colab** is a free online service that lets you run notebooks in the cloud without installing anything locally.

For this course, Colab is the recommended option if you want to get started quickly and run notebooks online.

Click the **“Open in Colab”** button at the top of this page.  
This opens a copy of the notebook directly from GitHub, where you can run and modify the code interactively. 

```{admonition} Note
:class: note
Colab does not change the original notebook in the course repository.  
If you want to keep your work, save the notebook to Google Drive or download it.
```

---

### Option 2: Using Binder

Binder is another free online service that lets you run Jupyter notebooks in the cloud without local installation.

Binder launches a temporary Jupyter environment based on the course GitHub repository. Startup can take a minute or two, especially when many users access Binder at the same time.

The launch button (🚀) in the top right corner starts a temporary Binder session, when you copy https://mybinder.org` as the URL placeholder. Once launched you can run the notebook in your browser.

```{admonition} Important
:class: important

Binder sessions are temporary.  
Any changes are lost when the session ends unless you download your notebook.  
Despite the rocket launch symbol, Binder is slower to launch than Colab. It's a good practice in patience, though!
```

---

### Option 3: In-page execution

This Jupyter Book supports **in-page execution** (temporary cloud {term}`kernel`), which allows you to run code cells **directly on this page**, without opening a separate notebook interface.

When you click the power button (⏻, top of the page), a temporary cloud-based Jupyter kernel is started in the background. Once the session is ready, you can execute the code cells on this page and view the outputs inline.

```{admonition} Advice
:class: note

This option is useful for quick experiments, demonstrations, or checking understanding. 
It is not intended for longer work sessions or saving progress.

In-page execution uses a temporary Binder-backed environment. Startup may take some time, and sessions are not persistent. 
Any changes or results are lost when the page is refreshed.
```
---

## 2. Running locally

Running notebooks locally is the best option if you want to keep using Python beyond this course or work on larger projects.

To run notebooks locally, you need:

* a Python environment (Conda recommended)
* JupyterLab (or VS Code) installed

Setup instructions are in:

* [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/)
* [JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/)
* [VS Code](https://hendrikwulf.github.io/sds210-jb/book/setup/vs-code/)

---

### Option 1: JupyterLab

The GitLab repository below contains all exercises, practicals, and solutions in Jupyter Notebook format (`.ipynb`).  
Throughout the semester, new notebooks will be added weekly.  
Make sure you update your local copy regularly.

1. Download the [SDS210 repository](https://gitlab.com/HendrikWulf/sds210/-/archive/main/sds210-main.zip) and extract it to a suitable location on your computer.

2. If you have not yet installed Conda, download and install **[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)**
   Follow the default installation settings described in the Setup section on [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/).

3. Open `Anaconda Prompt` (Win) or your `Terminal` (Mac) to run the following commands:

```bash
# Update conda (recommended)
conda update -n base -c defaults conda

# Navigate to the extracted SDS210 folder
cd <path-to-sds210-repository-folder>

# Create the environment (only once)
conda env create -f environment.yml

# Activate the environment
conda activate sds210

# Start JupyterLab
jupyter lab
```

JupyterLab will start in the folder from which you launched it.
You can now open any notebook (`.ipynb`) in the interface.

```{admonition} Updating the repository
:class: important

Since new notebooks will be added weekly, you should periodically:

1. Download the latest ZIP version
2. Replace your local folder
3. Keep your own work in a separate folder to avoid overwriting

(Advanced users may prefer cloning via [Git](https://hendrikwulf.github.io/sds210-jb/book/setup/git/).)
```

---

### Option 2: VS Code

You can also use **VS Code** with the Python and Jupyter extensions.

In that case:

1. Activate your Conda environment.
2. Open your project folder in VS Code.
3. Open the `.ipynb` file.
4. Select the correct Python kernel if prompted.

Both installation and environment setup are explained in the [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/) and [VS Code](https://hendrikwulf.github.io/sds210-jb/book/setup/vs-code/) **Setup** sections.
VS Code provides a notebook interface similar to JupyterLab, but integrated into a full code editor.

---

See the **Setup** chapter for detailed instructions on:

* [installing Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#id-3-installing-conda)
* [creating environments](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#creating-an-environment)
* [installing JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/#installing-jupyterlab)
* [configuring VS Code](https://hendrikwulf.github.io/sds210-jb/book/setup/vs-code/#id-3-installing-vs-code)

Running notebooks locally gives you:

* full control over your environment
* better performance for larger datasets
* persistent files and environments

---

## 3. Summary

Here is a quick comparison of your options:

 Option                     | Installation needed | Persistent work | Best for                           |
| -------------------------- | ------------------- | --------------- | ---------------------------------- |
| Colab                      | No                  | Yes (if saved)  | Quick start, easy access           |
| Binder                     | No                  | No              | Temporary testing in Jupyter       |
| In-page ⏻                  | No                  | No              | Small experiments on the book page |
| Local (JupyterLab/VS Code) | Yes                 | Yes             | Projects, long-term use            |

This page introduced the **different ways to run notebooks**:

* **Colab** is the fastest way to start online
* **Binder** provides a temporary Jupyter environment (but can be slow)
* **In-page execution** runs cells directly in the book (temporary)
* **Local JupyterLab / VS Code** is best for serious work and long-term projects

Next, go to the **Practical** section to actually run cells, restart the kernel, and learn how to avoid hidden state.
