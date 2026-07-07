---
title: Running Notebooks

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Different options for working with notebooks
</div>
<!-- markdownlint-enable MD033 -->

---

```{admonition} Big idea
:class: tip

A {term}`notebook <Notebook>` is an interactive document where **code runs in a {term}`kernel <Kernel>`** and outputs appear immediately.  
Choosing the right way to run notebooks helps you work efficiently, avoid setup frustration, and keep your work reproducible.
```

In this course, we work extensively with **Jupyter notebooks** (`.ipynb`). Before you start coding, you need to make one practical decision:

**Where will your notebook run?**

Your main options are:

* **locally** on your own computer, which is recommended for this course and for most serious programming projects
* **online** in the cloud, which is faster to start but gives you less control and flexibility

```{admonition} Recommended path
:class: tip

For this course, use **local notebooks in VS Code** whenever possible.

Use **Colab** if your local setup is not working yet or if you need a quick fallback.  
Use **Binder** or **in-page execution** only for short experiments, not for longer project work.
```

Running notebooks locally in VS Code is highly recommended because it gives you the most control over your files, your Python environment, and your workflow. However, if you need more time to set up your local system, you can use one of the online options described below to avoid falling behind.

---

## 1. Which option should I use?

Use this page as a decision guide:

* Use **local VS Code** if you want the recommended setup for the course.
* Use **JupyterLab** if you prefer a classic notebook interface in the browser.
* Use **Colab** if your local setup is not ready yet or if you need a quick online fallback.
* Use **Binder** if you only want to test a notebook temporarily.
* Use **in-page execution** if you only want to run a small example directly inside the book page.

The important distinction is that reading a Jupyter Book page and working in a notebook are not exactly the same thing. The book page helps you understand the concept. The notebook file (`.ipynb`) is where you edit code, run cells, save your work, and develop your own solutions.

---

## 2. Running notebooks locally

To get started with Python in this course and beyond, for example for your BSc or MSc thesis, running notebooks locally is the best option. A local setup gives you:

* full control over your environment
* better performance for larger datasets
* persistent files and folders on your own computer
* a workflow that transfers well to research and professional projects

The setup process is explained in the [Setup](https://hendrikwulf.github.io/sds210-jb/book/setup/) section of the book. In short, you need:

* the Python environment `sds210`, created with {term}`Conda`
* an {term}`IDE`, preferably [VS Code](https://hendrikwulf.github.io/sds210-jb/book/setup/vs-code/) or [JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/)
* the SDS210 course files, including notebooks, data, and practicals

---

### Get the course files

The SDS210 course materials are provided in a course {term}`repository <Repository>`. The repository contains the lesson data, practicals, and notebooks in Jupyter Notebook format (`.ipynb`).

You have two options to get the files:

::::::{tab-set}

:::::{tab-item} Recommended: clone with Git

If you are comfortable using {term}`Git`, clone the repository. This is the best option because you can update your files later with `git pull`.

```bash
git clone https://gitlab.com/HendrikWulf/sds210.git
```

Then move into the repository folder:

```bash
cd sds210
```

To update the repository later, run:

```bash
git pull
```

:::::

:::::{tab-item} Alternative: download ZIP

If you do not want to use Git yet, download the repository as a ZIP file:

[SDS210 repository ZIP](https://gitlab.com/HendrikWulf/sds210/-/archive/main/sds210-main.zip)

Extract the ZIP file to a suitable location on your computer where you want to store your SDS210 course files.

```{admonition} Important
:class: important

If you download the ZIP file, the folder is **not** connected to Git.  
This means that `git pull` will not work.

To update your course files later, download a fresh ZIP file or switch to the Git-based workflow.
```

:::::

::::::

---

### Create the course environment `sds210`

The `environment.yml` file in the course repository contains all information needed to set up your Python environment.

If you have not yet installed Conda, download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install). Follow the default installation settings described in the [Conda setup section](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/).

After installing Conda, open **Anaconda Prompt** on Windows or your {term}`Terminal` on macOS or Linux.

Then run the following commands:

```bash
# Navigate to the extracted or cloned SDS210 folder
cd <path-to-sds210-repository-folder>

# Create the SDS210 environment
conda env create -f environment.yml

# Activate the environment
conda activate sds210
```

Once the environment is activated, you can select it as a notebook kernel in VS Code or start JupyterLab from the same terminal.

``````{admonition} Only create the course environment once
:class: important
In the [Working with Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#id-5-working-with-conda) section of the [Setup](https://hendrikwulf.github.io/sds210-jb/book/setup/) guide, we showed you how to set up the 'sds210' course environment. If you have already created the `sds210` course environment, there is no need to repeat this step, as it only needs to be done once. If you are unsure, you can quickly check which environments you have already installed.

```bash
# Check which environments you have installed
conda info --envs
```

``````

---

### IDE option 1: VS Code

VS Code is the recommended local notebook environment for this course. It combines notebooks, scripts, terminals, Git support, and extensions in one workspace.

To run a notebook in VS Code:

1. Activate your Conda environment `sds210`.
2. Open your SDS210 project folder in VS Code.
3. Open the `.ipynb` file you want to work on.
4. Select the correct Python kernel if prompted.
5. Run the notebook cells and save your work regularly.

Both installation and environment setup are explained in the [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/) and [VS Code](https://hendrikwulf.github.io/sds210-jb/book/setup/vs-code/) setup sections.

VS Code provides a notebook interface similar to JupyterLab, but it is integrated into a full code editor. This is especially useful once your projects grow beyond a single notebook.

---

### IDE option 2: JupyterLab

JupyterLab is a classic browser-based notebook environment. It is a good option if you prefer a focused notebook interface.

Once you have created and activated your `sds210` environment, start JupyterLab with:

```bash
# Activate the environment
conda activate sds210

# Move into your SDS210 project folder
cd <path-to-sds210-repository-folder>

# Start JupyterLab
jupyter lab
```

JupyterLab will start in the folder from which you launched it. You can then open any notebook (`.ipynb`) in the browser interface.

---

### Local setup checklist

Before starting a notebook locally, check:

* You are inside the correct project folder.
* The `sds210` environment is active.
* The notebook uses the `sds210` kernel.
* The required data files are in the expected folder.
* You save your notebook regularly.

---

## 3. Running notebooks online

Online options are useful if you are having trouble setting up your local environment or if you want to quickly test a notebook without installing anything.

However, online environments usually give you less control. Files may not persist automatically, startup can take time, and the available software environment may differ from your local setup.

```{admonition} Saving your work online
:class: warning

Online notebook environments do not automatically save your work to the course repository.

If you work online, always save your notebook to Google Drive, download it to your computer, or commit it to your own repository.
```

---

### Option 1: Colab

**Google Colab** is a free online service that lets you run notebooks in the cloud without installing Python locally.

For this course, Colab is the recommended online fallback if you want to get started quickly.

Many lesson pages provide an **Open in Colab** button near the top of the page. This opens a copy of the notebook in Colab, where you can run and modify the code interactively.

```{admonition} Note
:class: note

Colab does not change the original notebook in the course repository.  
If you want to keep your work, save the notebook to Google Drive or download it.
```

Colab is useful for:

* quickly trying a notebook
* working while your local setup is not ready yet
* sharing temporary notebook links
* avoiding installation problems in the short term

Colab is less suitable for:

* long-term project organisation
* complex local file structures
* workflows that rely on your own local environment
* reproducible project submissions unless you manage files carefully

---

### Option 2: Binder

Binder is another free online service that lets you run Jupyter notebooks in the cloud without local installation.

Binder launches a temporary Jupyter environment based on the course repository. Startup can take several minutes, especially when the environment has not been built recently or when many users access Binder at the same time.

The launch button (🚀) in the top-right corner can open the current notebook in Binder if this option is configured for the page.

```{admonition} Important
:class: important

Binder sessions are temporary.  
Any changes are lost when the session ends unless you download your notebook.

Despite the rocket launch symbol, Binder is usually slower to launch than Colab. It is a good practice in patience, though.
```

Binder is useful for:

* short tests
* exploring a notebook temporarily
* checking whether a notebook runs in a clean environment

Binder is less suitable for:

* long work sessions
* saving progress
* final project work
* working with large files or long-running computations

---

### Option 3: In-page execution

This Jupyter Book supports **in-page execution**, which allows you to run code cells directly on the book page without opening a separate notebook interface.

When you click the power button (⏻) at the top of the page, a temporary cloud-based Jupyter kernel is started in the background. Once the session is ready, you can execute code cells on the page and view the outputs inline.

```{admonition} Advice
:class: note

In-page execution is useful for quick experiments, demonstrations, or checking your understanding.

It is not intended for longer work sessions or saving progress. The environment is temporary, startup may take some time, and changes or outputs are lost when the page is refreshed.
```

In-page execution is useful for:

* trying a small code cell while reading
* checking how a short example behaves
* experimenting without leaving the book page

In-page execution is less suitable for:

* exercises that require saving work
* final project development
* notebooks with many files
* long-running analyses

---

## 4. Comparison of notebook options

| Option | Installation needed | Persistent work | Best for |
| --- | --- | --- | --- |
| Local VS Code / JupyterLab | Yes | Yes | Projects and long-term use |
| Colab | No | Yes, if saved | Quick start and fallback work |
| Binder | No | No | Temporary testing in Jupyter |
| In-page execution | No | No | Small experiments on the book page |

A simple rule of thumb:

* **Local VS Code** is the main workflow for this course.
* **JupyterLab** is a good local alternative if you prefer the classic notebook interface.
* **Colab** is the best online fallback.
* **Binder** and **in-page execution** are useful for temporary exploration.

---

## 5. Summary

This page introduced the different ways to run notebooks.

The recommended path is:

1. Set up the `sds210` Conda environment.
2. Work locally in VS Code whenever possible.
3. Use JupyterLab if you prefer a browser-based local notebook interface.
4. Use Colab as an online fallback.
5. Use Binder and in-page execution only for short experiments.

Learning to run notebooks reliably is part of learning to program. A notebook is not only a document with code; it is connected to a specific Python environment, a kernel, a working directory, and a set of files. Understanding this connection will help you avoid many common errors.

Next, go to the **Practical** section to actually run and edit cells, restart the kernel, and learn how to avoid hidden state.
