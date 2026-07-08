---
title: Colab

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Running Jupyter Notebooks in the Cloud
</div>
<!-- markdownlint-enable MD033 -->

---

## 1. Introduction

{term}`Google Colab` ([Colab](https://colab.google/)) is a **cloud-based {term}`Jupyter notebook <Notebook>` environment** that runs entirely in your browser. Your code executes on remote machines, not on your laptop, which means you can start working **immediately** without installing anything locally.

In this course, Colab provides a **low-barrier entry point** to {term}`programming <Computer programming>` with spatial data. It enables you to start coding immediately, without spending time on software setup and configuration. If your local environment is not ready or something breaks, Colab is your reliable fallback.

Colab is also a **shared learning space**. Notebooks can be opened, run, and edited by anyone with a link. This makes it well suited for live demonstrations, guided exercises, peer collaboration, and asking for help.

Throughout this course, you can use Colab to run course notebooks, modify code examples, and explore spatial data workflows in a clean and accessible environment.

```{admonition} Recommended use
:class: tip

Use Colab as a quick start and fallback option.

For longer work sessions, larger projects, and the final project, a local setup with VS Code or JupyterLab is still recommended because it gives you more control over files, environments, and reproducibility.
```

---

## 2. Learning Objectives

After working through this chapter, you should be able to:

* Open and run **course notebooks** in Colab.
* Install and use required **Python packages**.
* Manage **files and data** in Colab using Google Drive.

These objectives focus on using Colab as a practical learning and experimentation environment. You will use these skills repeatedly when working through examples and practicals in the course.

---

## 3. Getting Started

Getting started with Colab is simple and only takes a few minutes.

First, open [Colab](https://colab.research.google.com/). You only need a **web browser** and a **Google account**.

Once you are signed in, create a new notebook by clicking **File → New notebook in Drive**. This opens an empty Jupyter notebook on your Google Drive where you can start writing and running Python code immediately.

Each notebook consists of **{term}`code cells <Code cell>`** and **{term}`Markdown cells <Markdown cell>`**. Code cells are used to run Python. Markdown cells are used to explain what your code does. You run a cell with **Shift + Enter**.

Colab saves your notebook file automatically, but the running session is temporary. This means you can reopen the notebook later, but you may need to rerun cells when you come back to it.

For now, the key idea is simple: open Colab, create a notebook, write code in cells, and run the notebook from top to bottom.

---

## 4. The Notebook Environment

A Colab notebook is made up of cells that are executed one after another. Each cell can contain either Python code or explanatory text. The order in which you run cells matters, because {term}`variables <Variable>` and results are stored in memory.

Colab runs your code in a **session**. This session holds all variables, imported {term}`libraries <Library>`, and loaded data. If the session stops or resets, everything in memory is lost and cells need to be run again.

The {term}`execution order <Execution order>` is not always the same as the visual order of cells. If you run cells out of order, results may be confusing or incorrect. When something behaves strangely, a good habit is to restart the session and run all cells from top to bottom. This helps avoid {term}`hidden state <Hidden state>`.

The **runtime** defines where your code runs and which resources are available. Most of the time, the default runtime is sufficient: Python 3 on a {abbr}`CPU (Central Processing Unit)`. In later projects, you may switch runtimes for more demanding tasks using **Runtime → Change runtime type**, for example to use a {abbr}`GPU (Graphics Processing Unit)` or {abbr}`TPU (Tensor Processing Unit)`.

<!-- markdownlint-disable MD033-->
<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch04_Colab_GoogleDrive/" 
    width="100%" 
    height="600px" 
    frameborder="0" 
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Colab Session vs Google Drive.</b><br>
    Click the buttons to create variables, install packages, upload files, save results to Google Drive, and reset the runtime. The animation shows which parts live only in the temporary Colab session and which parts persist in Drive after the session disappears. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch04_Colab_GoogleDrive/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

Colab also makes it easy to work together on the same notebook. Sharing works much like sharing a Google Doc. Each notebook has **sharing settings** that control who can view or edit it. You can choose to share with specific people or allow access to anyone with the link.

```{admonition} Key idea
:class: tip

The notebook file can be saved in Google Drive, but the active runtime is temporary.

If the runtime resets, variables, installed packages, and files stored only in the session disappear. Important notebooks, data, and results should be saved to Google Drive.
```

---

## 5. Managing Python Packages

Python packages define what your notebook can do. In Colab, {term}`third-party packages <Third-party package>` are installed into the current **runtime**, not permanently. This means installs are fast, but they disappear when the session resets.

A good habit is to make all package installs **explicit** and place them near the top of the notebook. This helps others run your code and helps you recover quickly after a reset.

---

### Inspect installed packages

You can check which packages are already available in the current runtime.

```python
# Shows all Python packages currently installed in this Colab runtime
%pip list
```

A Colab runtime may already include some common geospatial packages, but you should never rely on this without checking.

---

### Installing packages with pip

In Colab, {term}`pip` commands usually start with a **percent sign**. This tells the notebook to run the command in a way that is safe and consistent with the current Python runtime.

```python
# Installs the required packages into the active runtime
%pip install geopandas rasterio leafmap
```

You may also see pip commands that start with an **exclamation mark**. This runs the command as a shell command.

```python
# Installs the package using a system command
!pip install pygis
```

Both approaches can work in Colab. In this course, prefer the **percent pip** version because it avoids confusion when working with notebook runtimes. Do not use {term}`Conda` in Colab. Use pip instead.

```{admonition} Package installs belong near the top
:class: tip

Place all `%pip install ...` commands near the beginning of the notebook.

This makes the notebook easier to rerun after a runtime reset and easier for others to understand.
```

---

### Reducing output

Package installation can produce a lot of text. To keep notebooks readable, you can reduce the output with `-q`, which stands for `--quiet`.

```python
# Installs the package while reducing console output
%pip install -q pygis
```

---

### Check package versions

When code behaves differently than expected, checking the package {term}`version <Version>` is often the first step.

```python
# Displays version number and installation path of the package
%pip show geemap
```

Different versions can lead to different results, especially in geospatial workflows.

---

### Uninstall packages

If a package causes conflicts or you want to start fresh, you can remove it.

```python
# Removes the package without asking for confirmation (-y = --yes)
%pip uninstall geemap -y
```

---

## 6. Working with Files and Data

Understanding where your data lives is essential when working in Colab. Files stored inside the Colab **session** exist only temporarily. If the session resets, those files are lost.

To avoid losing work, important files and results should be stored in **Google Drive**. Drive provides persistent storage that stays available across sessions and devices.

---

### Using Google Drive for storage

Before accessing Drive, you need to mount it in your notebook.

```python
# Connects your Google Drive to the Colab session
from google.colab import drive
drive.mount('/content/gdrive')
```

After mounting, your personal Drive is available under `MyDrive`. A good practice is to create a **course folder** and keep notebooks, data, and outputs organised there.

```python
# Lists the contents of your Google Drive
import os
os.listdir('/content/gdrive/MyDrive')
```

```{admonition} Session storage vs Drive storage
:class: warning

Files in `/content/` belong to the temporary Colab session.  
Files in `/content/gdrive/MyDrive/` are stored in Google Drive and persist after the session ends.
```

---

### Uploading and downloading data

You can upload files from your local computer directly into the current session. This is useful for small datasets or quick tests.

```python
# Opens a file picker to upload files from your computer
from google.colab import files
uploaded = files.upload()
```

To download results back to your computer, use the following command.

```python
# Downloads a file from the session to your local machine
from google.colab import files
files.download('results.csv')
```

Remember that uploaded files stored only in the session should be moved to Drive if you want to keep them.

---

### Accessing data from the web

Many datasets can be accessed directly from the web. This avoids manual downloads and supports {term}`reproducibility`.

```python
# Downloads a dataset from a public URL
!wget https://opengeos.org/data/world/world_cities.csv
```

Course code and example data are often stored in a {term}`GitHub` {term}`repository <Repository>`. You can {term}`clone <Git clone>` a repository directly into your session.

```python
# Copies a GitLab repository into the Colab session
!git clone https://gitlab.com/HendrikWulf/sds210.git
```

Working directly with online sources makes it easier to rerun notebooks and share them with others.

---

## 7. Running Course Notebooks

Many notebooks in this course can be run directly in Google Colab. This allows you to start working immediately without setting up a local environment.

When a page in this Jupyter Book provides an **Open in Colab** link, you can use it to open the notebook directly in Colab. While this approach gets you started online, it should not replace your local Conda and VS Code setup in the long term.

You can also open notebooks directly from a GitHub repository if a GitHub version of the notebook is available. Colab can load notebooks from GitHub without downloading them manually.

A GitHub-based Colab URL usually follows this pattern:

```text
https://colab.research.google.com/github/<owner>/<repository>/blob/<branch>/<path-to-notebook>.ipynb
```

Once the notebook is open, run the cells from top to bottom. This ensures that all package installs, imports, and data-loading steps are executed in the correct order.

If the notebook modifies files or produces results, save a copy to **Google Drive**. This ensures your work persists even if the session resets.

Running notebooks in Colab is meant to support learning and experimentation. Feel free to change code, add cells, and explore, knowing that you can always reopen a clean version from the book or repository.

```{admonition} Safe Colab workflow
:class: tip

1. Open the notebook from the book or repository.
2. Save your own copy to Google Drive.
3. Run all cells from top to bottom.
4. Save important outputs to Drive.
5. Share a link only after checking permissions.
```

---

## 8. Exercises

The following exercises help you practise the learning objectives of this chapter. They focus on running notebooks in Colab, managing packages, and working with data in a session-based environment.

---

#### Exercise 1: Colab setup

**Objective**  
Get comfortable with Colab as a working environment for this course.

**Tasks**

1. Open Google Colab and create a new notebook.
2. Check which runtime is active and confirm that it uses Python.
3. Mount your **Google Drive**.
4. Install the required Python packages for this course.
5. Create a folder in your Drive for course notebooks and data.
6. Add a short Markdown cell that explains what this notebook is for.
7. Save the notebook with a clear and descriptive name.

This exercise focuses on opening notebooks, installing packages, and using Drive for persistent storage.

---

#### Exercise 2: Working with files and data

**Objective**  
Practise moving data between the Colab session, Google Drive, and the web.

**Tasks**

1. Download a small dataset from the web using `wget`.
2. Upload a second file from your local computer to Colab.
3. Move both datasets into your course folder in **Google Drive**.
4. Load one dataset into a Pandas {term}`DataFrame` or a GeoPandas {term}`GeoDataFrame`.
5. Inspect the data and print the first few rows.
6. Save a processed result to Drive.
7. Download the result back to your local computer.

This exercise reinforces how data lives in Colab sessions and how to make results persistent.

---

#### Exercise 3: Running and sharing a course notebook

**Objective**  
Run a complete notebook and prepare it for collaboration.

**Tasks**

1. Open one course notebook in Colab using the provided link.
2. Save your own copy to **Google Drive**.
3. Run all cells from top to bottom without errors.
4. Modify one code cell in a meaningful way.
5. Add a Markdown cell explaining what you changed and why.
6. Change the sharing settings so others can view the notebook.
7. Share the link with a peer and ask them to run it.

This exercise focuses on reproducible execution, documentation, and sharing notebooks with others.

---

After these exercises, you should understand that Colab is more than a place to run code quickly. It is a temporary cloud runtime connected to a persistent notebook file and, when needed, to Google Drive. Once you understand what is temporary and what is persistent, Colab becomes a useful and reliable tool for learning, experimentation, and collaboration.