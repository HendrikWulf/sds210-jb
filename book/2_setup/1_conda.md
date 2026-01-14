# Conda

*Introduction to Python Package Management*

---

## 1. Introduction

One of the biggest challenges in Python programming is not writing code, but **setting up a working environment**. This is especially true in data science and geospatial analysis, where projects often rely on many libraries that need to work together.

Different projects may require different versions of the same package. Some geospatial libraries depend on additional system software for things like coordinate transformations or reading spatial file formats. When these pieces do not match, things break quickly.

This is where **package management** becomes essential.

Package managers help you install the right software, keep projects separated, and make sure your code runs the same way on different computers. Instead of fighting with installations, you can focus on analysis and problem solving.

### Why package management matters

- Geospatial libraries rely on complex system dependencies  
- Different projects need different package versions  
- Isolated environments prevent conflicts between projects  
- Reproducible environments make results reliable  
- Shared environment files support collaboration  

In this course, you will mainly work with **Conda**, which is well suited for geospatial software because it can manage both Python packages and system libraries. You will also get to know **uv**, a very fast tool for managing Python packages when system level dependencies are not required.

The goal of this section is not to memorise commands, but to understand **how to create reliable and reproducible environments**. These skills will save you time, reduce frustration, and support professional geospatial programming workflows throughout your Spatial Data Science journey.

---

## 2. Learning Objectives

After working through this section, you should be able to:

- **Explain why package management and isolated environments matter** for geospatial programming.
- **Create and manage project specific environments** using Conda and mamba.
- **Choose appropriate tools and practices** to build reproducible and shareable Python environments, including when to use uv.

---

## 3. Installing Conda

### Miniconda or Anaconda

You can choose between:

- [**Miniconda**](https://www.anaconda.com/docs/getting-started/miniconda/main): a minimal installation that includes only Conda (~50–100 MB) 
- [**Anaconda**](https://www.anaconda.com/docs/getting-started/anaconda/main): a much larger distribution that comes with many preinstalled packages (~3–5 GB)  

For this course, **Miniconda is recommended**. It is lightweight, transparent, and encourages you to install only what you actually need.

<iframe
  width="100%"
  height="400"
  src="https://www.youtube.com/embed/3GjrIuiGxX8?start=85"
  title="Anaconda Distribution vs Miniconda"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

Both Miniconda and Anaconda can be installed either via:
- a **command line installer**, or
- a **graphical installer**

Here, we focus on the **command line installation**, as it works reliably across systems and helps you better understand how your Python environment is set up. 

Official installation guides (recommended):
- Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install  
- Anaconda: https://www.anaconda.com/docs/getting-started/anaconda/install  

Take your time with the installation. A clean and well understood setup will make the rest of the course much smoother. If you encounter any issues while installing [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/troubleshooting) or the [Anaconda Distribution](https://www.anaconda.com/docs/getting-started/anaconda/troubleshooting), please refer to their website links for troubleshooting assistance.

---

Follow the steps below to install **Miniconda** using the command line. This approach is reliable, transparent, and works consistently across systems. 
Take your time with the installation. A clean and well understood setup will make the rest of the course much smoother.

::::::{tab-set}

:::::{tab-item} Windows 

These three commands quickly and quietly download the latest 64-bit Windows installer, rename it to a shorter file name, perform a silent install, and then delete the installer:
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```
After installing, open Anaconda Prompt to use Miniconda.

:::::

:::::{tab-item} macOS

**Step 1: Download and install Miniconda**

Run the following commands **line by line** in the Terminal.

These commands will:
- create a directory called `miniconda3` in your home directory  
- download the Miniconda installer script  
- install Miniconda in silent mode  
- remove the installer script after installation  

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

**Step 2: Activate Miniconda**

After installation, **close and reopen your Terminal**, or run:
```bash
source ~/miniconda3/bin/activate
```
You should now see `(base)` at the beginning of your command prompt.


**Step 3: Initialize conda for your shell**

Initialize conda so it works automatically in new terminal sessions:
```bash
conda init --all
```

**Step 4: Verify your installation**

Run any conda command. For example: `conda list` (displays a list of packages installed in your active environment and their versions) or `conda --version` (displays conda’s version number).

:::::

:::::{tab-item} Linux


**Step 1: Download and install Miniconda**

Run the following commands **line by line**  to download and install the latest Linux installer for your chosen chip architecture.

These commands will:
- create a directory called `miniconda3` in your home directory.  
- download the Linux Miniconda installation script for a 64-bit architecture and save the script as `miniconda.sh` in the miniconda3 directory. For other chip architectures look up this link.
- run the `miniconda.sh` installation script in silent mode using bash.
- remove the `miniconda.sh` installation script file after installation is complete. 

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

**Step 2: Activate Miniconda**

After installation, **close and reopen your Terminal**, or run:
```bash
source ~/miniconda3/bin/activate
```
You should now see `(base)` at the beginning of your command prompt.


**Step 3: Initialize conda for your shell**

Initialize conda so it works automatically in new terminal sessions:
```bash
conda init --all
```

**Step 4: Verify your installation**

Run any conda command. For example: `conda list` (displays a list of packages installed in your active environment and their versions) or `conda --version` (displays conda’s version number). 

:::::

:::::

::::::

---

## 4. Understanding Conda Concepts

This section introduces the **core ideas** behind Conda that you need for the rest of the course.
The goal is not to memorise terminology, but to understand **how to think about software setups** in a clean and reproducible way.

You will revisit these ideas repeatedly in labs and projects.

---

### What is Conda?

Conda is both a **package manager** and an **environment manager**.

As a package manager, it installs software and libraries that your code depends on.
As an environment manager, it keeps different projects separated so they do not interfere with each other.

In practice, Conda helps you answer two questions for every project:

* What software does this project need
* Where should that software live on my machine

This is especially important in geospatial programming, where libraries often depend on additional system software and specific versions need to work together.

---

### What is an environment?

A Conda environment is a **self contained software setup** for a project.

Each environment includes:

* a specific Python version
* a specific set of installed packages
* the system libraries those packages rely on

Environments are isolated from each other. Installing or updating software in one environment does not affect any other environment.

This isolation allows you to:

* work on multiple projects with different requirements
* avoid breaking existing projects when installing new packages
* reproduce the same setup on another computer

Best practice is to create **one environment per project**.
If something goes wrong, you can delete the environment and recreate it without affecting your system.

---

### What is a package?

A package is a **ready to use piece of software** that adds functionality to your environment.

Packages allow you to reuse work done by others instead of writing everything from scratch. They include:

* the software itself
* information about versions and dependencies
* instructions for installation

When you install a package, Conda takes care of:

* downloading the correct files for your system
* installing required dependencies
* making sure everything works together

In geospatial programming, packages often include compiled components in addition to Python code. This is one of the reasons Conda is so useful in this field.

---

**Key takeaway**

Think of Conda as a system for **organising software**.

* Conda manages software and environments
* environments define project specific setups
* packages provide reusable functionality

If you understand these three ideas, you understand the foundation of reproducible and reliable geospatial programming.

---

## 5. Working with Conda

This short tutorial walks you through creating and using your first conda environment as part of a real Python workflow. You’ll create an environment, install packages, and use that environment to run a small Python program.

---

### Creating an environment

The conda installation process creates an environment called `base`, which is where conda itself is installed. However, when starting work on a new project, it’s best practice to create a new environment. This keeps your environments maintainable and reproducible while also keeping your base environment stable.

Let’s create a new environment called `geo-env` with Python 3.14 as the {abbr}`interpreter (The python installation that will run your code)`.

---

**1. Open a shell application**

Conda is a command line interface (CLI) tool, which means you’ll use a shell application to run conda commands. For Windows users, you’ll use an application called Anaconda Prompt, which comes installed with Anaconda Distribution and Miniconda. For macOS and Linux users, you’ll use your system’s Terminal application.

::::::{tab-set}

:::::{tab-item} Windows 
To open Anaconda Prompt, type “Anaconda Prompt” in the Windows search bar, then select Anaconda Prompt.

:::{figure} images/1_conda_win_anaconda_promt.png
:alt: Opening the Anaconda Propmt application
:width: 700px

Opening the Anaconda Propmt application.
:::


:::::

:::::{tab-item} macOS/Linux

Open Terminal:
- On macOS, open Spotlight with Cmd + Spacebar, then search for “Terminal”.
- On Linux, press Ctrl + Alt + T or search for “Terminal” in your application menu.

:::{figure} images/1_conda_mac_terminal.png
:alt: Opening the Terminal to use conda
:width: 700px

Opening the Terminal to use conda.
:::


:::::

::::::

---

**2. Create a new environment**

Use the *{abbr}`copy button (hover your mouse over the code block below)`* to copy the following command, paste it into your shell application, and press Enter (Windows) or Return (macOS/Linux) to run it.

```bash
# create env named geo-env with Python 3.14
conda create --name geo-env python=3.14   
```
The `--name` flag sets the new environment’s name.


**3. Activate your new environment**

You’ll need to activate your newly created environment before you can use it. Run the following command to activate `geo-env`:

```bash
# activate your environment geo-env
conda activate geo-env   
```
Conda displays the currently active environment in your shell application beside the input line:

::::::{tab-set}

:::::{tab-item} Windows 
```bash
(geo-env) C:\Users\username>
```
:::::

:::::{tab-item} macOS/Linux
```bash
(geo-env) ~
```
:::::

::::::

### Adding packages to your environment

Right now, your environment only has Python 3.14 and its dependencies installed. However, our project uses functionality that is not provided by the Python standard library, so we must install third-party packages to provide that functionality.

**1. Add conda packages**

We can find the additional conda packages that we need for our project on the conda-forge community channel.

``` {admonition} Channels
:class: tip
**conda-forge** is a community maintained channel that provides up to date packages, especially for geospatial and scientific software. Most geospatial libraries you will use in this course are best installed from conda-forge.
```

```bash
# installs common geospatial packages and their dependencies from conda-forge
conda install --channel conda-forge pygis
```
The `--channel` flag tells conda to give the specified channel top priority for installing packages and their dependencies. The short option `-c` can also be used instead.

**2. Add packages with pip**

Sometimes you will need a package that is not available through Conda. This is common for smaller or newer Python libraries, including some geospatial helper tools.

In these cases, you can use pip, Python’s built in package manager.

When you created your Conda environment, Python was installed automatically, and with it pip. This means you can already use pip inside your active Conda environment.

``` {admonition} When mixing Conda and pip
:class: warning
To minimize the risk of dependency conflicts, follow these simple rules:
- Install all Conda packages first
- Use pip only for packages that are not available via Conda
```
Assume your project needs a small helper library that is only published on PyPI, for example a lightweight utility for working with map tiles.

First, make sure your Conda environment is active.

Then install the package using pip:

```bash
pip install geo-tiles-helper
```