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

There are two common ways to install Conda: [**Miniconda**](https://www.anaconda.com/docs/getting-started/miniconda/main) and [**Anaconda**](https://www.anaconda.com/docs/getting-started/anaconda/main). Both use the same Conda system, but they are designed for slightly different use cases.

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

**Miniconda** is a minimal installer (~50–100 MB). It includes Conda, Python, and only a few essential packages. Everything else is installed explicitly when you need it.

**Anaconda** is a full distribution (~3–5 GB). It includes Conda, Python, and a large collection of preinstalled packages for data science and scientific computing.

```{admonition} Course recommendation
:class: tip
For SDS210, we recommend **Miniconda**. It keeps environments small, gives you more control. Miniconda encourages you to build environments intentionally instead of relying on a large predefined setup. If you have Anaconda already installed, it is also fine to stick with it.
```
In short, Anaconda optimises for convenience, while Miniconda optimises for clarity and control. For this course, learning how environments are built and managed is more important than having many packages preinstalled.

---

### Installation

To install Conda, choose either [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install) or [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install) and follow the instructions for your operating system.

In this chapter, we use the command line installation because it works consistently across systems and helps you better understand how your environment is set up. Alternatively, you can also use the appropriate [graphical installer](https://www.anaconda.com/download/success?user_state=logged_in&utm_campaign=direct_download&utm_medium=homepage_link&utm_source=platform) for your operating system.

Take your time with the installation. A clean and well understood setup will make the rest of the course much smoother.

::::::{tab-set}
:::::{tab-item} Windows
Open **Windows PowerShell as administrator** and run the following commands:

```powershell
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```

:::::
::::{tab-item} macOS (Apple Silicon)
Run the following commands in the **Terminal**:

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
