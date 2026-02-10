---
title: Programming, Python, and notebooks

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

To run a script, you typically call Python from a terminal, for example:

```text
python my_analysis.py
```

Scripts are common in software development and production systems. For learning and exploration they can feel less transparent, because the explanation, results, and code often live in separate places.

### Notebooks

Jupyter notebooks combine several elements in a single document:

* code cells
* formatted text
* figures and tables
* intermediate and final results

This makes them ideal for:

* learning new concepts step by step
* interactive data exploration
* documenting analysis decisions

You can read the explanation, run the code below it, and immediately see the output. If something is unclear, you can change one line at a time and observe what happens.

```{admonition} Important
:class: important

In this course, notebooks are the default format for exercises, examples, and most project work.
```

### Other options (for context)

You may also hear about:

* the **Python interpreter**, where you type single commands and see the result right away
* **integrated development environments (IDEs)** such as JupyterLab, PyCharm, or Visual Studio Code, which provide editors, consoles, and tools in one place

You do not need to master these now. For this course, it is enough to understand that:

* scripts are useful for standalone programs
* notebooks are our main tool for learning and data analysis
* IDEs are environments that can run both scripts and notebooks

Later sections will show you how we use JupyterLab to work with notebooks in practice.

---

## Jupyter in this course

Jupyter is the system that allows notebooks to run in a web browser.

From your perspective, you open a notebook in a tab, write code in cells, and run them. In the background, a **Jupyter server** executes the Python code and sends the results back to your browser. That server can run:

* on your own computer
* on a university server
* in the cloud

In all cases, the experience in the browser is very similar.

### JupyterLab

JupyterLab is the main interface we use in this course.

It is a browser based environment where you can:

* browse and manage files in your project
* open notebooks in tabs for code and text
* use a Python console for quick experiments
* open terminals or text editors when needed

When you start JupyterLab, it opens in a browser window and shows these components in a single workspace.

```{admonition} First impression
:class: note

When you open JupyterLab for the first time, it may look busy.  
This is normal.

At the beginning, you only need a few elements:

- the file browser on the left  
- notebook tabs in the main area  
- the run button and basic keyboard shortcuts to execute cells  

You will discover the other features gradually, when they become useful for your work.
```

In this course, JupyterLab and notebooks together form your main programming environment: you read explanations, run code, inspect results, and document your analysis in one place.

