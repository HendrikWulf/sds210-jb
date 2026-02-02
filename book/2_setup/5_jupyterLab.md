---
title: JupyterLab
---

<div class="page-subtitle">
An interactive workspace for exploratory data analysis
</div>

---

## 1. Introduction

[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) is the main **working environment** in this course. It is not just a place to run code, but a space where **thinking**, **coding**, and **documentation** come together.

In spatial data science, work is rarely linear. You load data, inspect it, try something, visualize the result, adjust your approach, and document what you learned. JupyterLab is designed for exactly this kind of **exploratory** and **iterative** work.

A Jupyter notebook combines **executable code**, **text explanations**, **figures**, and **maps** in one place. This makes it easier to:
- understand what your code does
- explain why you made certain choices
- revisit and reproduce your analysis later

This is especially important when working with spatial data, where data sources, projections, and processing steps can strongly influence results. By keeping code and explanation together, notebooks support **reproducibility**, **transparency**, and a clear **analysis narrative**.

In this section, you will learn how to use JupyterLab as a structured workspace for spatial data science. The focus is not on learning every feature, but on developing good **working habits** that you will use throughout the course and beyond.

> This section focuses on **how we work**, not just **what we run**.

---

## 2. Learning Objectives

After working through this section, you should be able to:

- **explain** how JupyterLab fits into a spatial data science workflow  
- **navigate** the JupyterLab interface and manage notebooks and files  
- **create and run** notebooks that combine code, text, and visual output in a **reproducible** way  

These objectives focus on using JupyterLab as a practical **working environment** for exploration, documentation, and analysis. You will use these skills throughout the course when developing and refining your own spatial data workflows.

---

## 3. Getting Started

Before using JupyterLab, it is important to think about **where** it is installed and **which environment** it belongs to. Most problems with JupyterLab do not come from the tool itself, but from using the **wrong Python environment**.

In this course, JupyterLab is always part of a **project specific environment**. This keeps your setup clean, avoids version conflicts, and makes your work easier to reproduce.

### Recommended setup strategy

JupyterLab should **not** be installed system wide. Instead, you install it inside a dedicated **conda environment**.

The basic idea is simple:
- one **environment** per project
- the environment must be **activated** before starting JupyterLab
- all packages used in a notebook come from the active environment

If this is new to you, revisit the **[Conda](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/)** section before continuing. Environment activation is a required habit for this course.

### Installing JupyterLab

The recommended way to install JupyterLab for spatial data science is with **conda**, as it handles geospatial dependencies reliably. Install JupyterLab into the currently active conda environment (-c = --channel).

```bash
conda install -c conda-forge jupyterlab
```

If you are working in a pip based environment, you can install JupyterLab with:

```bash
pip install jupyterlab
```

Only use one package manager per environment. Mixing conda and pip without care is a common source of errors.

### Verifying the installation

After installation, always check that JupyterLab is available in the **active environment**.

Run the following command in your terminal:

```bash
jupyter lab --version
```

You should see a version number printed in the terminal. If you get an error, check the following first:

* is the **correct environment** activated
* was JupyterLab installed into that environment
* are you accidentally using a different Python installation

Taking a minute to verify your setup now will save you a lot of time later.

---

## 4. Launching JupyterLab

Before working with notebooks, it helps to understand what actually happens when you start JupyterLab. This section focuses on building a **mental model** of how JupyterLab works, rather than on clicking through menus.

### Run `jupyter lab`

When you run `jupyter lab`, you are not opening a normal desktop application. Instead, JupyterLab starts a **local server** on your computer.

Here is what is happening in the background:

- a **local server** starts and runs in your terminal  
- your **web browser** acts as the user interface  
- the address usually points to **localhost**, which means your own machine  
- the terminal must stay open because it is running the server  

If you close the terminal, the server stops and JupyterLab shuts down. Understanding this connection between **terminal**, **server**, and **browser** helps explain many common issues students run into later.

### The JupyterLab interface

The JupyterLab interface is designed as a flexible workspace. A useful way to remember its structure is the following mental model:

> **Command – Canvas – Context – Status**

:::{figure} images/5_JupyterLab_interface_components.png
:alt: The main interface components of JupyterLab IDE.
:width: 700px

The main interface components of JupyterLab {abbr}`IDE (Integrated Development Environment)` (source: [python-gis-book](https://python-gis-book.readthedocs.io/en/latest/part1/chapter-01/nb/04-using-jupyterlab.html)).
:::


Each part has a clear role:

- **Left Sidebar**  
  This is your **project and control** area. You browse files, manage running notebooks, and access additional tools.

- **Main Area**  
  This is the **work canvas**. Notebooks, terminals, and files open here and can be arranged side by side.

- **Menu Bar**  
  This contains **global actions** such as saving files, running cells, changing kernels, and adjusting the layout.

- **Status Bar**  
  This provides **feedback and state** information, such as whether the kernel is busy or idle.

Keeping this structure in mind makes it easier to navigate JupyterLab and transfer these skills to other development environments later in the course.

---

## 5. Notebooks as Scientific Documents

In this course, notebooks are not temporary scratchpads. They are **scientific documents** that combine code, explanation, and results. A good notebook tells the story of your analysis in a way that others and your future self can understand.

### Creating a notebook

When JupyterLab starts, you will see the **Launcher**. This is the entry point for creating new files.

:::{figure} images/5_JupyterLab_Notebook_instructions.png
:alt: The basic components of a Jupyter Notebook opened in JupyterLab.
:width: 700px

The basic components of a Jupyter Notebook opened in JupyterLab (source: [python-gis-book](https://python-gis-book.readthedocs.io/en/latest/part1/chapter-01/nb/04-using-jupyterlab.html)).
:::

To create a notebook:
- choose a **Python kernel** that belongs to your active environment
- create the notebook from the Launcher
- give the file a **clear and meaningful name**

Good naming matters. A notebook called `analysis.ipynb` tells you very little. A name like `snow_cover_exploration_v1.ipynb` makes the purpose clear even months later.

### Cells, execution, and state

Notebooks run code in **cells**, and these cells are executed **sequentially**. This means the order in which you run cells matters.

A common source of confusion is **hidden state**. Variables can exist in memory even if the cell that created them is no longer visible or was changed later.

To avoid problems:
- run cells from top to bottom
- use **Restart Kernel and Run All** regularly
- check that your notebook works from a clean start

This habit is essential for **reproducibility** and for submitting reliable work.

### The geospatial output

To see how notebooks behave, start with a minimal geospatial example. The goal here is not to understand the mapping library, but to observe the notebook workflow.

You typically go through three steps:
- **import** a library
- **create** an object
- display the **rendered output**

When you run a cell that produces visual output, JupyterLab automatically renders it below the cell. This tight link between code and output is what makes notebooks so powerful for **exploration** and **communication** in spatial data science.

---

## 6. Productivity Fundamentals

Working efficiently in JupyterLab is less about speed and more about **reducing cognitive load**. Using the keyboard helps you stay focused on your analysis instead of constantly switching between mouse and menus.

This section introduces only the **essential concepts and shortcuts** you need to work fluently. You do not need to memorize everything at once.

### Notebook modes

Jupyter notebooks operate in two distinct modes. Many beginner mistakes happen because these modes are confused.

**Edit mode**
- used to *write and modify code or text*
- a cursor is visible inside the cell
- the cell border indicates active editing

**Command mode**
- used to *navigate and manage cells*
- no text cursor is visible
- the whole cell is selected as an object

Always be aware of which mode you are in. If something does not behave as expected, mode confusion is often the reason.

### Core shortcuts

You only need a small set of shortcuts to work productively. These are the ones you will use constantly:

- **Shift Enter** to run a cell and move to the next one  
- **Ctrl Enter** to run a cell and stay in place  
- **Alt (⌥) Enter** to run a cell and create a new one below  
- **Esc** to switch to command mode  
- **Enter** to switch to edit mode  
- **A** to insert a cell above  
- **B** to insert a cell below  
- **M** to change a cell to markdown  
- **Y** to change a cell to code  
- **DD** to delete a cell  
- **Z** to undo a cell deletion  

Most keyboard shortcuts depend on the **current notebook mode**.
Shortcuts that act on the **structure of the notebook**, such as creating, deleting, or moving cells, only work in **command mode**. If they do nothing, you are usually still in edit mode.
Shortcuts that **run cells**, such as Shift Enter or Ctrl Enter, work in both modes. Shortcuts that **edit text** only work in edit mode.
Mastering these shortcuts already gives you most of the productivity benefits.

### Editing vs Structuring

A useful way to think about notebook work is to separate two activities:

- **editing** content inside a cell which happens in edit mode  
- **structuring** the analysis by adding moving or reorganizing cells which happens in command mode  

Being aware of this distinction helps you work more deliberately. You edit when you think about code and text. You structure when you think about the **story** your analysis is telling.

---

## 7. Working Without a Local Setup

Not everyone can or wants to install software locally right away. For this reason, most parts of the course material can also be run using **Binder** and **Colab**.

Both services allow you to work with notebooks directly in your **browser**, without setting up a local Python environment.

### What Binder and Colab are

**Binder** starts a temporary **JupyterLab** environment that is linked to a course repository.  
**Colab** provides hosted **Jupyter notebooks** that run on Google infrastructure.

Both options:
- run in the **browser**
- require no local installation
- are suitable for **learning and experimentation**

### When to use them

Binder and Colab are useful when:
- you want to **quickly explore** course notebooks
- you are working on a **shared or restricted computer**
- your local setup is not ready yet

They help lower entry barriers and ensure everyone can participate.

### Limitations to keep in mind

Both Binder and Colab have **limitations**:
- startup can take time
- environments are **temporary**
- file persistence is limited or requires extra steps

Because of this, they are best used for short tasks and exploration.

> Binder and Colab are for **learning**, not for **long term projects**.

---

## 8. Exercises

These exercises help you practice using JupyterLab as a **working environment** for spatial data science. The goal is not to learn every feature, but to build confidence with the core workflows you will use throughout the course.

Work through the exercises at your own pace. If something breaks, that is part of the learning process.

---

#### Exercise 1: Setting Up Your JupyterLab Environment

**Objective**  
Set up and verify a working JupyterLab environment for spatial data analysis.

**What you practice**  
- working with **conda environments**  
- installing packages  
- launching and testing JupyterLab  

**Tasks**

1. Create and activate a dedicated environment:
```bash
conda create -n geolab python=3.12
conda activate geolab
````

2. Install JupyterLab and basic geospatial packages:

```bash
conda install -c conda-forge jupyterlab geopandas matplotlib ipyleaflet
```

3. Launch JupyterLab:

```bash
jupyter lab
```

4. Explore the interface:

* locate the **file browser**, **main area**, **menu bar**, and **status bar**
* open multiple tabs and arrange them side by side

5. Verify your setup:

* create a new notebook
* run the following imports in a code cell:

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import ipyleaflet
print("Geospatial environment ready")
```

**What to verify**

* JupyterLab starts without errors
* the notebook runs from top to bottom
* all imports work successfully

---

#### Exercise 2: Keyboard Shortcuts and Efficient Workflow

**Objective**
Develop fluency with keyboard driven notebook work.

**What you practice**

* switching between **edit** and **command** mode
* running and structuring cells
* reducing reliance on the mouse

**Tasks**

1. Practice essential shortcuts:

* run cells with **Shift Enter**, **Ctrl Enter**, and **Alt Enter**
* switch modes using **Esc** and **Enter**
* create cells using **A** and **B**
* delete and recover cells using **DD** and **Z**

2. Create a practice notebook using only the keyboard:

* create at least **eight cells**
* mix **code** and **markdown**
* change cell types using **M** and **Y**
* navigate using arrow keys in command mode

3. Practice editing and restructuring:

* copy and paste cells
* rearrange the order of cells
* merge or split cells if needed

4. Check notebook state:

* restart the kernel
* run all cells from top to bottom
* confirm that the notebook still works

**What to verify**

* you can build and restructure a notebook without using the mouse
* the notebook runs cleanly after a kernel restart

---

#### Optional Challenge: Workflow Efficiency

**Objective**
Improve speed and confidence when working in notebooks.

**What you practice**

* combining shortcuts into a smooth workflow
* separating editing from structuring

**Tasks**

* create a new notebook
* add ten cells with alternating code and markdown
* use only the keyboard
* restart the kernel and run all cells

**What to verify**

* the notebook structure is clear
* all cells run without errors
* you feel more comfortable navigating and controlling JupyterLab

These exercises prepare you to use JupyterLab naturally in later labs and projects, where the focus will be on **spatial data analysis**, not on tool mechanics.

