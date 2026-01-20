# Colab

## Introduction

Google [Colab](https://colab.google/) is a **cloud based Jupyter notebook** that runs entirely in your browser. Your code executes on remote machines, not on your laptop, which means you can start working **immediately** without installing anything.

In this course, Colab is a **low barrier entry point** to programming with spatial data. It allows you to focus on learning Python, understanding geospatial workflows, and experimenting with code, rather than spending time on software setup and configuration. When your local environment is not ready or something breaks, Colab is your **reliable fallback**.

Colab is also a **shared learning space**. Notebooks can be opened, run, and edited by anyone with a link. This makes it well suited for live demonstrations, guided exercises, peer collaboration, and asking for help.

Throughout this course, you can use Colab to **run all course notebooks**, modify code examples, and explore spatial data workflows in a clean, consistent, and reproducible environment.

---

## Learning objectives

After working through this section, you should be able to:

- Open and run **course notebooks** in Google Colab
- Install and use **Python packages** needed for spatial data analysis
- Manage **files and data** in Colab using Google Drive

These objectives focus on using Colab as a practical learning and experimentation environment. You will use these skills repeatedly when working through examples and practicals in the course.

---

## Getting started

Getting started with Colab is simple and only takes a few minutes.

First, open [Colab](https://colab.research.google.com/). You only need a **web browser** and a **Google account**.

Once you are signed in, create a new notebook by clicking **File -> New notebook in Drive**. This opens an empty Jupyter notebook on your Google Drive where you can start writing and running Python code immediately.

Each notebook consists of **code cells** and **text cells**. Code cells are used to run Python. Text cells are used to explain what your code does. You run a cell with **Shift Enter**.

Colab saves your notebook automatically, but the running session is temporary. This means you can always reopen the notebook later, but you may need to rerun cells when you come back to it.

For now, the key idea is simple. Open Colab, create a notebook, write code in cells, and run them from top to bottom.

---

## Understanding the notebook environment

A Colab notebook is made up of **cells** that are executed one after another. Each cell can contain either Python code or explanatory text. The order in which you run cells matters, because variables and results are stored in memory.

Colab runs your code in a **session**. This session holds all variables, imported libraries, and loaded data. If the session stops or resets, everything in memory is lost and cells need to be run again.

The **execution order** is not always the same as the visual order of cells. If you run cells out of order, results may be confusing or incorrect. When something behaves strangely, a good habit is to restart the session and run all cells from top to bottom.

The **runtime** defines where your code runs and which resources are available. Most of the time, the default runtime is sufficient (Python 3 on a CPU). In later project, you may switch runtimes for more demanding tasks (Runtime -> Change Runtime type, GPU or TPU).

Understanding these basics will help you avoid common errors and make your work in Colab more predictable and easier to debug.

---

## Managing Python packages 

Python packages define what your notebook can do. In Colab, packages are installed into the current **runtime**, not permanently. This means installs are fast, but they disappear when the session resets.

A good habit is to make all package installs **explicit** and place them near the top of the notebook. This helps others run your code and helps you recover quickly after a reset.

### Inspect installed packages

You can check which packages are already available in the current runtime.

```python
# Shows all Python packages currently installed in this Colab runtime
%pip list
```

Colab often includes common geospatial packages, but you should never rely on this without checking.

### Installing packages with pip

In Colab, pip commands usually start with a **percent sign**. This tells the notebook to run the command in a way that is safe and consistent with the current Python runtime.

```python
# Installs the required packages into the active runtime
%pip install geopandas rasterio leafmap
```

You may also see pip commands that start with an **exclamation mark**. This runs the command at the system level.

```python
# Installs the package using a system command
!pip install pygis
```

Both approaches work in Colab. In this course, prefer the **percent pip** version because it avoids confusion when working with different runtimes.

### Reducing output

Package installation can produce a lot of text. To keep notebooks readable, you can reduce the output (`-q` =) `--quiet` .

```python
# Installs the package while reducing console output
%pip install -q pygis
```

### Check package versions

When code behaves differently than expected, checking the **version** is often the first step.

```python
# Displays version number and installation path of the package
%pip show geemap
```

Different versions can lead to different results, especially in geospatial workflows.

### Uninstall packages

If a package causes conflicts or you want to start fresh, you can remove it.

```python
# Removes the package without asking for confirmation (-y = --yes)
%pip uninstall geemap -y
```

---

## Working with files and data

Understanding where your data lives is essential when working in Colab. Files stored inside the Colab **session** exist only temporarily. If the session resets, those files are lost.

To avoid losing work, important files and results should be stored in **Google Drive**. Drive provides persistent storage that stays available across sessions and devices.

### Using Google Drive for persistent storage

Before accessing Drive, you need to mount it in your notebook.

```python
# Connects your Google Drive to the Colab session
from google.colab import drive
drive.mount('/content/gdrive')
```

After mounting, your personal Drive is available under `MyDrive`. A good practice is to create a **course folder** and keep notebooks, data, and outputs organized there.

```python
# Lists the contents of your Google Drive
import os
os.listdir('/content/gdrive/MyDrive')
```

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

### Accessing data from the web and GitHub

Many datasets can be accessed directly from the web. This avoids manual downloads and keeps workflows reproducible.

```python
# Downloads a dataset from a public URL
!wget https://opengeos.org/data/world/world_cities.csv
```

Course code and example data are often stored on GitHub. You can clone a repository directly into your session.

```python
# Copies a GitHub repository into the Colab session
!git clone https://github.com/giswqs/intro-gispro.git
```

Working directly with online sources makes it easier to rerun notebooks and share them with others.

---



