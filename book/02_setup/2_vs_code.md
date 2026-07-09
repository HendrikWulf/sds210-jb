---
title: VS Code

site:
  outline_maxdepth: 1

#exports:
# - id: setup-vs-code-pdf
#   format: typst
#   template: https://github.com/myst-templates/plain_typst_book.git
#   articles:
#     - book/02_setup/2_vs_code.md
#   output: ../../exports/02_setup/02_setup_02_vs_code.pdf
#   show_ToC: true
#
#downloads:
# - file: 02_setup/2_vs_code.md
#   title: Markdown File
# - id: setup-vs-code-pdf
#   title: Download PDF
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Setting Up Your Code Development Environment
</div>
<!-- markdownlint-enable MD033 -->

---

## 1. Introduction

**[Visual Studio Code](https://code.visualstudio.com/) ({term}`VS Code <Visual Studio Code>`)** is a lightweight, extensible code editor. It is the main **working environment** in this course where you can write code, run it, work through {term}`debugging`, explore data, and keep your work organised.

Think of VS Code as your **digital workspace**. Instead of switching between many tools, it brings code editing, {term}`terminals <Terminal>`, notebooks, and {term}`version control <Version control>` together in one place. VS Code understands Python and helps you write cleaner code and spot problems earlier.

VS Code is especially well suited for **geospatial programming**. You can work with Python scripts and {term}`Jupyter notebooks <Notebook>` side by side, run {term}`Conda` commands in an integrated terminal, and track changes with {term}`Git` without leaving the editor. As projects grow in size and complexity, this integration becomes increasingly important.

Another reason we promote VS Code is **balance**. It is lightweight enough to start quickly, but powerful enough to support professional workflows. You can begin with a minimal setup and gradually add features as you need them.

In this chapter, you will learn how VS Code fits into the Python workflow and how to use it as a **reliable development environment** for geospatial programming.

---

## 2. Learning Objectives

After working through this chapter, you should be able to:

* Work productively in VS Code as your main workspace.
* Select and verify the correct Conda {term}`interpreter <Interpreter>` in VS Code.
* Run Python {term}`scripts <Script>` and Jupyter notebooks inside VS Code.

These objectives focus on using VS Code as part of a practical workflow. You will build on them throughout the course as your projects become more complex.

---

## 3. Installing VS Code

To install Visual Studio Code, go to the official website: [https://code.visualstudio.com](https://code.visualstudio.com)

The site automatically detects your operating system and suggests the correct installer.

---

VS Code is available for **[Windows](https://code.visualstudio.com/docs/setup/windows)**, **[macOS](https://go.microsoft.com/fwlink/?LinkID=534106)**, and **[Linux](https://code.visualstudio.com/docs/setup/linux)**, and the installation is quick on all platforms.

::::::{tab-set}

:::::{tab-item} Windows

* Download the Windows installer (`.exe`).
* Run the installer and follow the setup wizard.
* Keep the default options unless you know you want something different.

```{admonition} Tip
:class: tip

During installation, make sure the option to add VS Code to your PATH is enabled. This allows you to open VS Code from the terminal using `code .`.
```

:::::

:::::{tab-item} macOS

* Download the macOS installer (`.dmg`).
* Open the file and drag **Visual Studio Code.app** into the Applications folder.
* Start VS Code from Applications or Spotlight.
* On macOS, you may need to confirm that you trust the application the first time you open it.
* Optional but recommended: keep VS Code in your Dock for quick access.

:::::

:::::{tab-item} Linux

* Download the appropriate package for your distribution (`.deb` or `.rpm`).
* Install it using your package manager or by opening the downloaded file.
* Alternatively, follow the instructions on the [VS Code website](https://code.visualstudio.com/docs/setup/linux) for your distribution.

:::::

::::::

---

When you open VS Code for the first time, you will see a welcome screen with helpful getting-started information.

To help you navigate the different features and panels more easily, you may want to watch this beginner tutorial.

<!-- markdownlint-disable MD033-->
<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/B-s71n0dHUk"
  title="VS Code Introduction"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>
<!-- markdownlint-enable MD033 -->

At this point, VS Code is installed and ready. In the next sections, you will set it up for Python and geospatial work.

---

## 4. Essential Extensions

VS Code becomes powerful through **extensions**. Extensions add language support and tools that turn the editor into a full development environment. For this course, you only need a **small core set** to get started.

You can always add more later. Start simple.

---

### Core extensions

These two extensions are essential for this course.

**Python** by Microsoft

This is the foundation for all Python work in VS Code.

It provides:

* code completion and {term}`syntax <Syntax>` highlighting
* error detection and basic linting
* debugging support
* integration with Conda environments

Without this extension, VS Code does not really understand Python.

**Jupyter** by Microsoft

This extension adds native support for Jupyter notebooks inside VS Code.

It allows you to:

* open and run notebooks (`.ipynb`) directly in the editor
* select Conda environments as notebook {term}`kernels <Kernel>`
* mix code, text, and output in one place

This is especially useful for exploratory geospatial analysis.

```{admonition} First things first
:class: hint

Install the **Python** and **Jupyter** extensions before doing anything else. They are required for almost everything you will do in this course.
```

---

### Installing extensions

There are two common ways to install extensions.

**Using the Extensions panel**

1. Click the Extensions icon in the left sidebar.
2. Search for the extension name.
3. Click Install.

**Using the Command Palette**

1. Open the Command Palette.

   * Windows and Linux: `Ctrl + Shift + P`
   * macOS: `Cmd + Shift + P`

2. Type `Extensions: Install Extensions`.
3. Search for and install the extension.

Once installed, extensions activate automatically.

If you get stuck, you might find it helpful to watch this video on VS Code extensions.

<!-- markdownlint-disable MD033-->
<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/SKcZ3cwX8lA"
  title="Unlock the power of VS Code's Extensions"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>
<!-- markdownlint-enable MD033 -->

---

### What not to install yet

VS Code offers thousands of extensions. It is tempting to install many of them, but this often causes confusion early on.

For now:

* Do not install many formatters, linters, or AI tools.
* Do not change many settings.
* Do not try to optimise everything before you understand your workflow.

You will add more tools later, once you know what you need.

```{admonition} Keep it simple
:class: hint

Extensions should support your workflow, not distract from learning Python and geospatial concepts.
```

In the next section, you will connect VS Code to your Conda environment and run your first Python code inside the editor.

---

## 5. Connecting VS Code to Conda

VS Code may detect Python environments automatically, but you should still explicitly connect your workspace to the correct Conda environment. This ensures your code uses the correct packages. Skipping this step is one of the most common causes of setup errors.

Think of this as selecting your project's **toolbox**. It helps ensure that your scripts, notebooks, and terminal all use the same Python interpreter.

---

### Selecting a Conda environment

Before selecting an environment, first open your **project folder** in VS Code.

* Go to **File → Open Folder**.
* Select the folder of your project.
* This folder becomes your workspace.

VS Code remembers the Python environment **per workspace**, not globally.

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch02_VSCode_wiring/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: VS Code Workspace Wiring.</b><br>
    Click through the steps to open a project folder, select the <code>sds210</code> Conda environment, and run a script or notebook. Watch how the workspace, terminal, Python script, and notebook kernel become connected to the same interpreter. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch02_VSCode_wiring/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

Then select the environment:

1. Open the Command Palette.

   * Windows or Linux: `Ctrl + Shift + P`
   * macOS: `Cmd + Shift + P`

2. Type **Python: Select Interpreter**.
3. Choose your Conda environment, for example `sds210`.

Once selected, VS Code stores this choice for the current workspace.

---

### Verifying and using the environment

You can always check whether VS Code is using the correct environment.

* Look at the **Status Bar** at the bottom of VS Code. You should see the environment name and Python version.
* Or run this in a Python file:

```python
import sys
print(sys.executable)
```

The printed path should point to your Conda environment, not to a system Python.

For Jupyter notebooks:

* Open a `.ipynb` file.
* Click **Select Kernel** in the top right.
* Choose the same Conda environment you selected before.

This keeps notebooks consistent with your scripts.

```{admonition} Advice
:class: tip

If imports fail or results look strange, first check which Python environment VS Code is using.  
This solves most setup issues faster than reinstalling packages.
```

Once VS Code is connected to Conda, you are ready to work productively: writing code, running notebooks, and managing projects with confidence.

---

## 6. Working with VS Code

Now that VS Code is installed and connected to your Conda environment, this section focuses on **how you actually work in it day to day**. The goal is not to learn every feature, but to become comfortable with a small set of workflows that you will use throughout the course.

From here on, VS Code is a convenient place where you write code, run notebooks, and manage your projects.

Before diving into Python, notebooks, or geospatial libraries, it is worth getting comfortable with the basic ideas behind how VS Code works. This will save you time and reduce confusion later.

---

### The main interface

VS Code looks simple at first, but it is built around a few clearly defined areas. The labels in the figure correspond to the sections below.

:::{figure} images/2_vs-code-user-interface-labels.png
:alt: Visual Studio Code user interface with labeled interface areas.
:width: 700px

Visual Studio Code user interface.
:::

**A. Activity Bar**  
The Activity Bar runs vertically on the far left. It lets you switch between major views such as the **Explorer**, Search, Source Control (Git), Run, and Extensions. Think of it as the navigation spine of VS Code.

**B. Side Bar**  
The Side Bar shows the content of the currently selected activity. Most of the time, this is the **Explorer**, where you see your project folders and files. When you switch activities, the Side Bar adapts accordingly.

**C. Editor**  
The Editor is the main working area in the center. This is where you write Python scripts, edit notebooks, view files, and inspect results. You can open multiple files side by side and switch between them using tabs.

**D. Panel**  
The Panel appears at the bottom and hosts tools such as the **Terminal**, Output, Debug Console, and Problems view. You will frequently use the Terminal here to activate Conda environments, install packages, and run code without leaving VS Code.

**E. Status Bar**  
The Status Bar runs along the bottom edge of the window. It shows important context such as the active Python interpreter, Conda environment, file type, and cursor position. If something behaves unexpectedly, this is often the first place to check.

**F. Main Menu**  
The Main Menu at the top provides access to all VS Code functionality, including opening folders, managing settings, running code, and controlling the editor layout. Many menu actions are also available through the Command Palette.

You do not need to memorize all of this. As you work, these areas will quickly become familiar and help you stay oriented while coding and exploring data. You will likely spend most of your time in the Editor, Explorer, Terminal, and Status Bar.

---

### The workspace

VS Code works around the idea of a **workspace**, which is usually a folder on your computer.

When you open a folder in VS Code:

* all files in that folder become part of your project
* settings such as the selected Python environment are stored for that project
* the integrated terminal opens in the correct directory

See your **project folder** as a place that keeps your code, data, notebooks, and environment configuration in one place.

---

### The Command Palette

The most powerful feature in VS Code is the **Command Palette**.

Open it with:

* `Ctrl + Shift + P` on Windows and Linux
* `Cmd + Shift + P` on macOS

The Command Palette lets you:

* select Python interpreters
* install extensions
* open settings
* run VS Code features without searching through menus

If you are unsure where something is in VS Code, open the Command Palette and search for it.

---

### Integrated terminal

VS Code includes a built-in terminal that runs inside your workspace.

You can use it to:

* activate Conda environments
* install packages
* run Python scripts
* start JupyterLab

Open it via:

**View → Terminal**

The terminal usually starts in your project folder, which helps avoid many path-related mistakes.

---

### Editing and running code

VS Code is more than a text editor. It understands Python and helps you write better code.

A typical workflow is:

1. Create a new Python file.
2. Write code with syntax highlighting and auto-completion.
3. Run the file directly from VS Code.
4. Inspect output in the integrated terminal.

You can run a Python file in several ways:

* **Run → Run Without Debugging**
* right-click in the editor → **Run Python File**
* use the integrated terminal

VS Code uses the Python interpreter from your selected Conda environment.

---

### Jupyter notebooks

VS Code also supports Jupyter notebooks directly inside the editor.

This allows you to:

* explore data interactively
* mix code, output, and explanations
* use the same Conda environment as your scripts

Scripts and notebooks can live side by side in the same project and use the same environment.

```{admonition} Advice
:class: tip

Make sure scripts, notebooks, and the terminal use the same Conda environment.
```

In this course, you will mainly use the following files:

* `.ipynb` files for Jupyter notebooks
* `.py` files for Python scripts
* `.yml` files for Conda environments
* folders such as `data`, `notebooks`, and `src` (short for source)

VS Code understands all of these file types and adapts its interface automatically.

VS Code is more than a text editor. It keeps code, environments, and notebooks connected at the project level. Once you open the right folder and select the right environment, most things just work.

---

## 7. Exercises

These exercises help you practise the **basic VS Code workflows** you can use throughout SDS210. They are designed to be short, practical, and focused on habits rather than features.

Take your time. If something does not work, use it as a chance to explore the interface and ask questions.

---

### Exercise 1: Opening a project workspace

**Goal**  
Learn how VS Code works with folders and projects.

1. Create a new folder on your computer called `sds210-vscode`.
2. Open VS Code.
3. Use **File → Open Folder** and select `sds210-vscode`.
4. Inside VS Code, create the following folder structure:

   * `data`
   * `notebooks`
   * {abbr}`src (short for source)`

5. Create a file `src/DIDit.py` with:

   ```python
   print("Every machine that is clever enough to pass the Turing test could also be clever enough not to pass it.")
   ```

6. Save the file.

This folder is now your workspace. VS Code will remember settings for this project.

---

### Exercise 2: Connecting VS Code to Conda

**Goal**  
Make sure VS Code uses the correct Python environment.

1. Open the **Command Palette**.

   * Windows or Linux: `Ctrl + Shift + P`
   * macOS: `Cmd + Shift + P`

2. Select **Python: Select Interpreter**.
3. Choose your Conda environment, for example `sds210`.
4. Open `DIDit.py`.
5. Run the file using **Run → Run Without Debugging**.

Check:

* Output appears in the integrated terminal.
* The **Status Bar** shows the selected Conda environment.

Optional check:

```python
import sys
print(sys.executable)
```

The path should point to your Conda environment.

---

### Exercise 3: Working with the terminal and notebooks

**Goal**  
Use VS Code as a single place for code, commands, and notebooks.

1. Open the integrated terminal.
2. Activate your Conda environment.
3. Run:

   ```bash
   python --version
   ```

4. Create a new notebook `notebooks/DUTgemacht.ipynb`.
5. Select the same Conda environment as the kernel.
6. Run a code cell with:

   ```python
   print("Die Proletarier haben nichts zu verlieren als ihre Goldkettchen.")
   ```

Confirm that:

* The notebook runs without errors.
* Scripts and notebooks use the same environment.

---

```{admonition} Context
:class: hint

If all exercises worked, your VS Code setup is complete.

Feel free to run the course notebooks in VS Code and gradually explore its functionality over time. Think of VS Code as a central workspace for coding, working with notebooks, and managing environments. Alongside JupyterLab, it serves as a powerful IDE that integrates multiple tools into a single, efficient development environment.
```
