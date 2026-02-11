---
title: Programming & Python

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
How we express ideas as code
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/3_L1_get-started/02_programming-python-jupyter.ipynb)

```{admonition} Big idea
:class: tip
We use Python and notebooks as a practical environment to turn ideas into code, explore data, and document our work in a reproducible way.
```

In the previous section, you saw why programming matters for working with data.
In this section, we move one step closer to practice:

* what we mean by *programming* in this course
* why we use **Python** as our main language
* how we run code using **scripts** and **notebooks**
* how **JupyterLab** provides the environment in which all of this comes together

The goal is orientation. You do not need to remember every term yet.
By the end of the section, you should have a clear picture of how ideas become code and how we will work with Python throughout the course.

---

## What programming means

Programming means giving a computer precise instructions to process data and produce results.

A computer does not interpret or guess. It follows the steps you write, exactly and repeatedly. The art of programming is to decide **what steps are needed**, in **which order**, and **under which conditions**.

### Coding and programming

You will hear the words *coding* and *programming* used almost interchangeably.

* **Coding** often refers to writing the actual instructions in a programming language so that the computer can follow them.
* **Programming** is a bit broader. It includes thinking about the problem, planning the steps, and then expressing those steps as code.

In this course, we do both:

* we **design simple solutions** to data challenges
* we **express those solutions** in Python code

The focus is not on building large applications. Instead, we use code as a practical tool to:

* explore data
* automate repetitive tasks
* document analysis steps
* make results reproducible

Even short programs can already be useful. A few lines of code can load a dataset, calculate a summary, and produce a clear visualisation.

```{admonition} Reflection
:class: dropdown

Think of one task from your studies that feels repetitive or error prone.  
Could you describe the steps in enough detail that a computer could follow them?

Keep that example in mind as you work through the next sections.
```

---

## Why Python in this course

Python is the programming language we use throughout this course.

There are many languages, but Python is particularly suitable for scientific and spatial work. It combines a gentle learning curve with strong tools for serious data analysis.

:::{figure} images/03_programming-languages.png
:alt: Examples of printing “Hello, world!” in different programming languages. 
:width: 700px

Examples of printing “Hello, world!” in different programming languages. Credit: [GeoPython](https://python-gis-book.readthedocs.io/en/latest/part1/chapter-01/nb/01-computers-and-programs.html#what-is-a-programming-language)
:::

### Why Python fits our goals

Python works well for this course because it:

* is **readable** and close to everyday language, which makes code easier to understand and discuss
* is a **general purpose language** that supports several styles of programming (for example procedural and object oriented), so you can start simple and grow into more advanced patterns later
* is **interpreted and interactive**, which means you can try out ideas in small steps, see results immediately, and learn by experimentation rather than long compile cycles
* is **dynamically typed**, so you can write code quickly without declaring data types up front, while still working with clear and predictable values
* has a rich ecosystem of **scientific and geospatial libraries** for working with tables, arrays, rasters, time series, and vector data
* integrates well with **GIS and remote sensing tools**, including QGIS and other spatial software that provide a Python console
* is **free and open source**, with a large community, extensive documentation, and many examples you can reuse and adapt

In practice this means you can focus on **questions and workflows**, not on low level technical details.

:::{figure} images/04_programming_languages_carto.png
:alt: Popular programming languages. 
:width: 700px

Figure showing the most popular programming languages from the survey on *The State of Spatial Data Science - 2024*. Credit: [Carto](https://carto.com/blog/the-state-of-spatial-data-science-2024-report)
:::

### What this means for you

You do not need to know any of these technical terms now. What matters is:

* Python is widely used in science and industry
* it runs on all major operating systems
* it is a good long term investment for your studies and beyond

```{admonition} Course focus
:class: note

The goal is not to learn all of Python.  
The goal is to use Python as a practical tool for working with spatial data.
```

---

## Ways to run Python code

There is more than one way to write and run Python code.
Each option has its strengths, and you will encounter several during your studies.

In this course we mainly use **notebooks**, but it helps to know what else exists.

### Scripts

Python scripts are plain text files with the file extension `.py`.

They are well suited for:

* programs that run for a long time
* tasks you want to repeat in the same way
* automation on servers or as scheduled jobs

To run a script, you typically call Python from your {term}`Integrated Development Environment`, a terminal or from a Python {term}`interpreter`.

:::{figure} images/05_python-script-example2.png
:alt: Example of a Python script file.
:width: 700px

Example of a Python script file.
:::

Scripts are common in software development and production systems. For learning and exploration they can feel less transparent, because the explanation, results, and code often live in separate places.

### Notebooks

Jupyter notebooks combine several elements in a single interactive document:

* code cells
* formatted text & equations
* figures and tables
* intermediate and final results

Notebook files have the extension `.ipynb`. They are divided into **cells**. Each cell has a specific purpose:

* **Code cells** contain executable Python code.
* **Markdown cells** contain formatted text written in [Markdown](https://en.wikipedia.org/wiki/Markdown).

You run the notebook in a web browser, while a Jupyter server executes the code in the background. The server can run on your computer or on a remote machine.

:::{figure} images/06_jupyter_notebook.png
:alt: Elements of a Jupyter Notebook.
:width: 700px

Elements of a Jupyter Notebook. Credit: [GeoPython](https://python-gis-book.readthedocs.io/en/latest/part1/chapter-01/nb/03-writing-and-running-python-code.html#jupyter-notebooks-code-and-documentation-combined)
:::

---

This capability of combining code and documentation makes them ideal for:

* learning new concepts step by step
* interactive data exploration
* documenting analysis decisions

You can read the explanation, run the code below it, and immediately see the output. If something is unclear, you can change one line at a time and observe what happens.

:::{figure} images/07_jupyter-notebook-window.png
:alt: An example Jupyter Notebook.
:width: 700px

An example Jupyter Notebook. Credit: [GeoPython](https://python-gis-book.readthedocs.io/en/latest/part1/chapter-01/nb/03-writing-and-running-python-code.html#jupyter-notebooks-code-and-documentation-combined)
:::

In summary, notebooks enable you to document your process, display your code and results, and interpret your output, all within **a single document**.
This makes them especially powerful for data science. A notebook can describe a **complete workflow**, from the initial data to the final findings.
Because all steps are visible and executable, others can **reproduce your work**. This transparency is an important part of modern scientific practice.

```{admonition} Important
:class: important

In this course, notebooks are the default format for examples, exercises, and most project work.
```

### Integrated Development Environments (IDEs)

An **Integrated Development Environment (IDE)** is a software application designed to help you write and manage code more efficiently.

Compared to the simple Python interpreter, IDEs provide many tools in one place, such as:

* a code editor
* a file browser
* debugging tools
* error highlighting
* version control integration

IDEs can look complex at first, but they can also be very helpful. Many IDEs highlight syntax errors immediately and suggest fixes, which makes it easier to learn and debug your code.

Several popular IDEs are used for Python:

* **JupyterLab**
  A browser-based environment designed for working with notebooks. It combines a file browser, notebook interface, Python console, and terminal in one workspace. This is the environment we use in this course.

* **Visual Studio Code (VS Code)**
  A flexible code editor that becomes a full IDE through extensions. It supports many programming languages, including Python.

* **PyCharm**
  A powerful IDE designed specifically for Python. It provides advanced tools for larger software projects and professional development.

You do not need to master an IDE right away. In this course, we focus on JupyterLab as a baseline. In addition, we encourage you to explore Visual Studio Code for its advanced tools when you start with your projects.  
At this stage, the focus now is learning how to think in code, not mastering development tools.

---

## Jupyter in this course

Jupyter is the system that allows notebooks to run in a web browser.

From your perspective, you open a notebook in a tab, write code in cells, and run them. In the background, a **Jupyter server** executes the Python code and sends the results back to your browser. That server can run:

* **on your own computer**, for example when you start JupyterLab locally
* **on a university or research server**, which you access remotely
* **in a cloud service**, such as Google Colab, which provides a managed notebook environment

In all cases, the experience in the browser is very similar.

### JupyterLab

[JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/) is the main interface we use in this course.

It is a browser based environment where you can:

* browse and manage files in your project
* open notebooks in tabs for code and text
* use a Python console for quick experiments
* open terminals or text editors when needed

When you start JupyterLab, it opens in a browser window and shows these components in a single workspace.

---

#### How to start JupyterLab 

If you installed [Miniconda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#id-3-installing-conda), the typical workflow looks like this:

1. **Open a terminal**
2. **Navigate to your working directory**, for example:

   ```bash
   cd path/to/your/project-folder
   ```

3. **Create and activate your environment** (once you installed [Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/))

   ```bash
   conda create -n sds-env python=3.14
   conda activate sds-env
   ```

4. **Install and start JupyterLab**

   ```bash
   conda install jupyterlab
   jupyter lab
   ```

Your browser will open automatically.
JupyterLab will show the contents of the folder from which you started it.

```{admonition} Why start in the project folder?
:class: note
JupyterLab always starts in the current directory.  
Starting it inside your project folder keeps your files organised.
```

---

#### How to stop JupyterLab

When you are finished:

1. Go back to the terminal where JupyterLab is running.

2. Press:

   ```
   Control + C
   ```

3. Confirm with `y` if prompted.

Then optionally deactivate the environment:

```bash
conda deactivate
```

The Jupyter server will stop, and the browser tab can be closed.

---

````{admonition} Jupyter Notebook vs JupyterLab
:class: dropdown

Both **Jupyter Notebook** and **JupyterLab** are tools from Project Jupyter.
Both allow you to create and run notebook files (`.ipynb`).
The difference lies in the interface and capabilities.

---

#### Jupyter Notebook (classic interface)

The classic Jupyter Notebook provides:

* one notebook per browser tab
* a simple, linear interface
* basic menu and toolbar
* limited layout flexibility

It is:

* easy to understand
* minimal and lightweight
* suitable for small projects or beginners

You mainly work inside a single notebook at a time.

---

#### JupyterLab (modern interface)

JupyterLab is the more advanced and flexible environment.

It provides:

* multiple notebooks in tabs
* a file browser
* terminals
* text editors
* a Python console
* drag-and-drop layout

It feels more like a full development environment inside the browser.

You can:

* open several notebooks side by side
* inspect data in a console
* edit scripts and notebooks in the same workspace
* manage files without leaving the interface

---

#### Key differences at a glance

| Feature            | Jupyter Notebook | JupyterLab                    |
| ------------------ | ---------------- | ----------------------------- |
| Interface style    | Single document  | Multi-tab workspace           |
| File browser       | Separate page    | Built-in panel                |
| Terminal access    | No               | Yes                           |
| Layout flexibility | Limited          | Flexible                      |
| Best for           | Simple workflows | Larger or structured projects |
````

---

:::{figure} images/08_jupyter-lab-window.png
:alt: The starting window of JupyterLab
:width: 700px

The JupyterLab starting window
:::


```{admonition} First impression
:class: note

When you open JupyterLab for the first time, it may look busy.  
This is normal.

At the beginning, you only need:

- the file browser on the left  
- notebook tabs in the main area  
- the run button or Shift + Enter to execute cells  

You will discover the other features gradually as they become useful.
```

In this course, JupyterLab and notebooks together form your main programming environment: you read explanations, run code, inspect results, and document your analysis in one place.

```
