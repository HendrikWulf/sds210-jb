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


Both Miniconda and Anaconda can be installed either via:
- a **command line installer**, or
- a **graphical installer**

Here, we focus on the **command line installation**, as it works reliably across systems and helps you better understand how your Python environment is set up.

Official installation guides (recommended):
- Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install  
- Anaconda: https://www.anaconda.com/docs/getting-started/anaconda/install  

Take your time with the installation. A clean and well understood setup will make the rest of the course much smoother.

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
- download the Linux Miniconda installation script for your chosen chip architecture and save the script as `miniconda.sh` in the miniconda3 directory.
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

