---
title: Running notebooks

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
A first interactive notebook session
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/3_python/03_notebooks.ipynb)

```{admonition} Big idea
:class: tip
A notebook is an interactive workspace where code, explanation, and results live together. Understanding how notebooks execute code is essential for reproducible and reliable scientific analysis.
```

In this course, we work almost entirely with **Jupyter notebooks**.  

This page shows you how to run them and lets you try things out right away.

There is no single “best” option. Choose what fits your setup and learning style.

---

## 1. Setup options

There are multiple ways to run Jupyter notebooks.  
You can run them locally on your machine or use an online service like Colab or Binder.

### Using Colab

**Google Colab** (recommended) is a free online service that lets you run notebooks in the cloud without installing anything locally.

For this course, Colab is the recommended option if you want to run notebooks online.

Click the **“Open in Colab”** button at the top of this page.  
This opens a copy of the notebook directly from GitHub, where you can run and modify the code interactively. 
Feel free to change the notebook as you wish and save a local version for your personal use. 
The original version of the notebook on GitHub remains unchanged.

---

### Using Binder 

Binder (slower alternative) is another free online service that lets you run Jupyter notebooks in the cloud without local installation.

Binder launches a temporary Jupyter environment based on the course GitHub repository. Startup can take a minute or two, especially when many users access Binder at the same time.

The launch button (🚀) in the top right corner starts a temporary Binder session, when you copy https://mybinder.org` as the URL placeholder. Once launched you can run the notebook in your browser.

```{admonition} Important
:class: important

Binder sessions are temporary.  
Any changes are lost when the session ends unless you download your notebook.  
Despite the rocket launch symbol, Binder is slower to launch than Colab. It's a good practice in patience, though!
```
---

### In-page execution

This Jupyter Book supports **in-page execution** (temporary cloud {term}`kernel`), which allows you to run code cells **directly on this page**, without opening a separate notebook interface.

When you click the power button (⏻, top of the page), a temporary cloud-based Jupyter [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)) is started in the background. Once the session is ready, you can execute the code cells on this page and view the outputs inline.

```{admonition} Advice
:class: note

This option is useful for quick experiments, demonstrations, or checking understanding. 
It is not intended for longer work sessions or saving progress.

In-page execution uses a temporary Binder-backed environment. Startup may take some time, and sessions are not persistent. 
Any changes or results are lost when the page is refreshed.
```
---

### Running locally

To continue working with python beyond this course you need to run notebooks on your own computer.

To do this, you need:

- a Python environment (Conda recommended)  
- JupyterLab installed  

Both installation and environment setup are explained in detail in the [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/) and [JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/) **Setup** sections.

---

#### Option 1: JupyterLab

Activate your environment and start Jupyter:

```bash
conda activate sds-env
jupyter lab
```

Your browser will open automatically.
You can then navigate to your notebook file and open it.

---

#### Option 2: VS Code

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

| Option | Installation needed | Persistent     | Best for          |
| ------ | ------------------- | -------------- | ----------------- |
| Colab  | No                  | Yes (if saved) | Quick start       |
| Binder | No                  | No             | Temporary testing |
| Local  | Yes                 | Yes            | Serious work / Projects     |

## 2. Summary

You have learned to:

- distinguish Markdown and Code cells  
- execute cells interactively  
- understand why execution order matters  
- store and reuse values  

These mechanics may seem simple, but they are foundational.
Reliable execution is the basis for trustworthy analysis.
