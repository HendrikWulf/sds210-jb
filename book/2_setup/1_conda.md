---
title: Conda 

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Introduction to Python Package Management
</div>

---

## 1. Introduction

One of the biggest challenges in Python programming is not writing code, but **setting up a working environment**. This is especially true in data science and geospatial analysis, where projects often rely on many libraries that need to work together.

Different projects may require different versions of the same package. Some geospatial libraries depend on additional system software for things like coordinate transformations or reading spatial file formats. When these pieces do not match, things break quickly.

This is where **package management** becomes essential.

Package managers help you install the right software, keep projects separated, and make sure your code runs the same way on different computers. Instead of fighting with installations, you can focus on analysis and problem solving.

### Why package management matters

* Geospatial libraries rely on complex system dependencies
* Different projects need different package versions
* Isolated environments prevent conflicts between projects
* Reproducible environments make results reliable
* Shared environment files support collaboration 

In this course, we introduce **Conda**, which is well suited for geospatial software because it can manage both Python packages and system libraries. You will also get to know **uv**, a very fast tool for managing Python packages when system level dependencies are not required.

The goal of this section is not to memorise commands, but to understand **how to create reliable and reproducible environments**. These skills will save you time, reduce frustration, and support professional geospatial programming workflows throughout your Spatial Data Science journey.

---

## 2. Learning Objectives

After working through this section, you should be able to:

* **Explain why package management and isolated environments matter** for geospatial programming.
* **Create and manage project specific environments** using Conda.
* **Choose appropriate tools and practices** to build reproducible and shareable Python environments, including when to use uv.

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
If you feel uncertain about using the shell, you may want to briefly review the [basic commands](https://www.w3schools.com/bash/bash_commands.php) and [networking](https://www.w3schools.com/bash/bash_curl.php) section in this [Bash Tutorial](https://www.w3schools.com/bash/index.php) by W3Schools before continuing.

Official installation guides (recommended):
* Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install  
* Anaconda: https://www.anaconda.com/docs/getting-started/anaconda/install  

Take your time with the installation. A clean and well understood setup will make the rest of the course much smoother. If you encounter any issues while installing [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/troubleshooting) or the [Anaconda Distribution](https://www.anaconda.com/docs/getting-started/anaconda/troubleshooting), please refer to their website links for troubleshooting assistance.

---

Follow the steps below to install **Miniconda** using the command line. This approach is reliable, transparent, and works consistently across systems. 

::::::{tab-set}

:::::{tab-item} Windows 

Open **Windows PowerShell** (not the regular Command Prompt) and paste the three commands below there.

To open PowerShell, press `Windows key` and type **PowerShell**

These three commands quickly and quietly download the latest 64-bit Windows installer, rename it to a shorter file name, perform a silent install, and then delete the installer:
```powershell
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```

After installing, close the PowerShell and open Anaconda Prompt to use Miniconda.

:::::

:::::{tab-item} macOS (Apple Silicon)

**Step 1: Download and install Miniconda**

Run the following commands **line by line** in the Terminal.

These commands will:
* create a directory called `miniconda3` in your home directory (`-p` flag stands for parents) 
* download the Miniconda installer script to your new miniconda3 directory
* install Miniconda in silent mode (`-b`), taking care of updates (`-u`), in the given  path (`-p`)
* remove the installer script after installation  

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

Initialize conda for all currently available shells so it works automatically in new terminal sessions:
```bash
conda init --all
```

**Step 4: Verify your installation**

Run any conda command. For example: `conda list` (displays a list of packages installed in your active environment and their versions) or `conda --version` (displays conda’s version number).

```bash
(base) name@computer ~ % conda --version
 conda 25.11.1
```

````{admonition} Do not auto-activate (base)
:class: dropdown

If you prefer a clean shell without automatically activating the base environment:

```bash
~/miniconda3/bin/conda config --set auto_activate_base false
```

After this, `conda` will be available, but no environment will be active by default.

````

:::::


:::::{tab-item} macOS (Intel)

As of August 15, 2025, Anaconda has stopped building packages for Intel Mac computers (osx-64). Existing Intel (MacOSX-x86_64) installers are still available at https://repo.anaconda.com/miniconda/ and the last Miniconda installer release for Intel Mac computers will be 25.7.x.

**Step 1: Download and install Miniconda**

Run the following commands **line by line** in the Terminal.

These commands will:

* create a directory called `miniconda3` in your home directory (`-p` flag stands for parents)
* download the Miniconda installer script for Intel-based Macs
* install Miniconda in silent mode (`-b`), allow updates (`-u`), in the given path (`-p`)
* remove the installer script after installation

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

---

**Step 2: Activate Miniconda**

After installation, **close and reopen your Terminal**, or run:

```bash
source ~/miniconda3/bin/activate
```

You should now see `(base)` at the beginning of your command prompt.

---

**Step 3: Initialize conda for your shell**

Initialize conda so it works automatically in new terminal sessions:

```bash
conda init
```

Restart your Terminal afterwards if prompted.

---

**Step 4: Verify your installation**

Run any conda command. For example: `conda list` (displays a list of packages installed in your active environment and their versions) or `conda --version` (displays conda’s version number).

```bash
(base) name@computer ~ % conda --version
 conda 25.7.0
```

---

:::::


:::::{tab-item} Linux


**Step 1: Download and install Miniconda**

Run the following commands **line by line**  to download and install the latest Linux installer for your chosen chip architecture.

These commands will:
* create a directory called `miniconda3` in your home directory.  
* download the Linux Miniconda installation script for a 64-bit architecture and save the script as `miniconda.sh` in the miniconda3 directory. For other chip architectures look up [this link](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-terminal-installer).
* run the `miniconda.sh` installation script in silent mode using bash.
* remove the `miniconda.sh` installation script file after installation is complete.

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
conda init
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

A package (aka. {term}`library`) is a **ready to use piece of software** that adds functionality to your environment.

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

Let’s create a new environment called `sds-env` with Python 3.12 as the {abbr}`interpreter (The python installation that will run your code)`.

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
* On macOS, open Spotlight with Cmd + Spacebar, then search for “Terminal”.
* On Linux, press Ctrl + Alt + T or search for “Terminal” in your application menu.

:::{figure} images/1_conda_mac_terminal.png
:alt: Opening the Terminal to use conda
:width: 700px

Opening the Terminal to use conda.
:::


:::::

::::::

---

**2. Create a new environment**

Use the **{abbr}`copy button (hover over the code block)`** 📄 to copy the command below.
Paste it into your shell (Anaconda Prompt, Terminal, or PowerShell) and press Enter (Windows) or Return (macOS/Linux) to run it.

```bash
conda create --name sds-env python=3.12
```
This command tells Conda to:

* create a **new isolated environment**
* name it `sds-env`
* install **Python 3.12** inside that environment

The `--name` flag assigns a human-readable name, which makes the environment easy to activate and manage later.

---

When you create a **named** Conda environment, Conda stores it automatically in its default `envs` directory.

::::::{tab-set}

:::::{tab-item} Windows 

`C:\Users\<username>\miniconda3\envs\sds-env`

:::::

:::::{tab-item} macOS/Linux

`/Users/<username>/miniconda3/envs/sds-env`

:::::

::::::

You usually do **not** need to interact with this folder directly.
Conda takes care of activating, updating, and removing environments for you.

```{admonition} Tip
:class: tip

Create environments in Conda’s `envs` directory  
and keep your **project files** in a separate project folder.

This separation keeps setups clean, reproducible, and easy to debug.
```

---

**3. Activate your new environment**

You’ll need to activate your newly created environment before you can use it. Run the following command to activate `sds-env`:

```bash
conda activate sds-env   
```
Conda displays the currently active environment in your shell application beside the input line:

::::::{tab-set}

:::::{tab-item} Windows 
```powershell
(sds-env) C:\Users\username>
```
:::::

:::::{tab-item} macOS/Linux
```bash
(sds-env) ~
```
:::::

::::::

From now on, every Python and conda command you run applies to this environment.

``` {admonition} Attention
:class: attention
Most setup issues come from one of these mistakes.

* Installing packages into the `base` environment by accident
* Forgetting to **activate** the correct environment before installing or running code
* Mixing conda and pip without thinking (install conda packages first, pip only if needed)
* Copying the wrong operating system commands during installation

If something breaks, stop and check your active environment first.
``` 

**Deactivate your environment when you are done**

When you finish working in an environment, you can deactivate it using:

```bash
conda deactivate
```

After deactivation, you return to the base environment and the environment name disappears from the prompt.

``` {admonition} Tip
:class: tip
Activating and deactivating environments is cheap and safe. Switch environments whenever you change projects.
```

---

### Adding packages to your environment

Right now, your environment only has Python 3.12 and its dependencies installed. However, our project uses functionality that is not provided by the Python standard library, so we must install third-party packages to provide that functionality.

---

**1. Add conda packages**

We can find the additional conda packages that we need for our project on the conda-forge community channel.

``` {admonition} Channels
:class: tip
**conda-forge** is a community maintained channel that provides up to date packages, especially for geospatial and scientific software. Most geospatial libraries you will use in this course are best installed from conda-forge.
```

The input below installs common geospatial packages and their dependencies from the conda-forge channel.

```bash
conda install --channel conda-forge pygis
```
The `--channel` flag tells conda to give the specified channel top priority for installing packages and their dependencies. The short option `-c` can also be used instead.

---

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
Assume your project needs a small helper library that is only published on [{abbr}`PyPI (Python Package Index)`](https://pypi.org/), for example a lightweight utility for working with map tiles. First, make sure your Conda environment is active. Then install the package using pip:

```bash
pip install geospatial
```

``` {admonition} Fun Fact
:class: note
Many Python tools are named after reptiles. The Python package manager pip references the process of hatching eggs. Interestingly, the naming of the Python language itself had nothing to do with reptiles as it was inspired by the comedy series [Monty Python's Flying Circus](https://youtu.be/5ptUMe9eqYE?si=OzfQ_zW7W55Fwq9i). 
```

---

### Working with Conda environments

At this point, you have created an environment and installed packages into it. Now let’s look at how to **inspect, update, and manage environments** during day to day work.

Think of this section as learning how to *stay in control* once your environment exists.

**1. Checking your environments**

It is good practice to start a session by checking which environments exist and which one is currently active.

```bash
conda info --envs
```

Conda lists all environments on your system.
The environment marked with an asterisk is the active one.

``` {admonition} Hint
:class: hint
If something behaves unexpectedly, the first thing to check is whether the correct environment is active.
```
---

**2. Inspecting what is installed**

To see which packages are installed in an environment, including where they came from, use:

```bash
conda list --name sds-env --show-channel-urls
```

This helps you understand:

* which packages are installed
* which versions are used
* whether they came from conda-forge or another channel

This is especially useful when debugging or documenting your setup.

---

**3. Installing and removing packages safely**

If you need to modify an environment without activating it, you can always target it explicitly.

**Install** packages into a specific environment:

```bash
conda install --name sds-env geopandas rasterio
```

**Remove** a package you no longer need from the environment:

```bash
conda remove --name sds-env rasterio
```

---

If a package was installed using `pip`, it should also be removed using `pip`.

First, make sure you are targeting the **correct environment** (either by activating it or by using the full path to `pip`).

**Remove** a package with pip:

```bash
pip uninstall geospatial
```

---

``` {admonition} Tip
:class: tip
Always remove packages using the same tool you used to install them.  
Specifying the environment name makes your commands explicit and reduces the risk of installing packages into the wrong environment.
```

---

**4. Updating packages**

Over time, packages receive updates. To update all packages in an environment:

```bash
conda update --all --name sds-env
```

Use this with care in active projects, as updates may change behaviour.
For long term or shared projects, updating should be done intentionally and documented.

---

**5. Copying and cleaning up environments**

Sometimes you want to experiment without breaking a working setup.

Clone an existing environment:

```bash
conda create --clone sds-env --name sds-env-test
```

This creates a full copy that you can safely modify.

When an environment is no longer needed, remove it completely:

```bash
conda remove --name sds-env-test --all
```

Removing unused environments helps keep your system clean and avoids confusion later.

---

**6. Exporting environments for reproducibility**

One of the most important steps in professional workflows is **documenting your environment**.

Export an environment to a file (to your current working directory):

```bash
conda env export --name sds-env > sds-env.yml
```

This file records package names and versions so others can recreate the same setup.

Recreate an environment from such a file:

```bash
conda env create --name sds-env-copy --file sds-env.yml
```

``` {admonition} Tip
:class: tip
Always export your environment when submitting assignments, sharing code, or finishing a project.
```

---

### A typical Conda workflow

By now, you have seen the full lifecycle of working with Conda for a project. The exact package names will change, but the workflow stays the same.

```bash
# create a new environment for the project
conda create -n sds-env python=3.12

# activate the environment
conda activate sds-env

# install required geospatial packages
conda install -c conda-forge geopandas rasterio

# check what is installed
conda list

# work on your project
python analysis.py

# export the environment for reproducibility
conda env export > environment.yml

# deactivate when you are done
conda deactivate

```

What matters is not the exact commands, but the pattern:

* one environment per project
* activate before you work
* prefer conda-forge for geospatial packages
* use pip only when Conda is not an option
* document environments for reproducibility

You will repeat this workflow throughout your geospatial projects. Over time, it becomes second nature.

``` {admonition} Tip
:class: tip
Think in environments, not installations. A clean environment is the foundation of reliable and reproducible geospatial programming.
```

---

## 6. Working with uv

So far, we introduced **Conda**, which is the main tool used in this course for managing geospatial environments. Conda is reliable and well suited for packages with complex system dependencies.

Sometimes, however, you may want a **lighter and faster tool** for Python only workflows. This is where **uv** comes in.

---

### What is uv and when to use it?

**[uv](https://docs.astral.sh/uv/)** is a modern Python package manager written in [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)). It is designed to be *{abbr}`extremely fast (10-100x faster than pip)`* while remaining compatible with Python’s existing ecosystem.

Use **Conda** when:

* working with geospatial libraries that depend on system software
* installing packages like GDAL, GEOS, PROJ, geopandas, or rasterio
* reproducibility across operating systems matters

Use **uv** when:

* working with pure Python packages from [{abbr}`PyPI (Python Package Index)`](https://pypi.org/)
* setting up small or temporary environments
* prototyping quickly or running experiments

In this course, **Conda remains the default**, but uv is a useful complement to know.

``` {admonition} Note
:class: note
Conda manages full software stacks. uv focuses on Python only and prioritizes speed.
```
---

### Installing and creating an environment

You only need to install uv once to your `base` environment.

::::::{tab-set}

:::::{tab-item} Windows 
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

:::::

:::::{tab-item} macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

:::::

::::::

Navigate to your project directory and create a virtual environment:

```bash
cd path/to/your/project
uv venv --python 3.12
```

Activate the environment:

::::::{tab-set}

:::::{tab-item} Windows 
```powershell
.venv\Scripts\activate
```

:::::

:::::{tab-item} macOS/Linux
```bash
source .venv/bin/activate
```

:::::

::::::

---

### Installing and running packages

Install packages at high speed:

```bash
uv pip install jupyterlab leafmap
```

Install from a requirements file:

```bash
uv pip install -r requirements.txt
```

Run Python or tools directly inside the environment:

```bash
uv run python script.py
```

```bash
uv run jupyter lab
```

``` {admonition} Note
:class: note
Use uv for Python only workflows. For geospatial packages with system dependencies, always prefer Conda.
```

---

### A typical `uv` workflow

With `uv`, environments usually live **inside the project folder**.
This makes each lab self-contained and easy to reset.

Assume you are working in your **SDS-labs directory**:

```text
SDS-labs/
└── lab-03/
```
---

#### 1. Go to your lab directory

```bash
cd SDS-labs/lab-03
```

This is where the environment will live.

---

#### 2. Create a virtual environment

```bash
uv venv
```

This creates a local environment:

```text
lab-03/
├── .venv/        ← virtual environment
└── notebooks/
```

You usually do **not** touch `.venv` directly.

---

#### 3. Activate the environment

```bash
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

Your shell now uses the Python from `.venv`.

---

#### 4. Install packages for the lab

```bash
uv pip install geopandas rasterio jupyterlab
```

Packages are installed **only for this lab**, not globally.

To check what is installed:

```bash
uv pip list
```

---

#### 5. Start JupyterLab

```bash
jupyter lab
```

* Jupyter opens **in your browser**
* The notebook kernel uses the `.venv` environment
* You work entirely in the browser

---

#### 6. Finish your work

1. **Stop JupyterLab**
   In the terminal:

   ```
   Ctrl + C
   ```

2. **Deactivate the environment**

   ```bash
   deactivate
   ```

Your system is now clean again.

---

#### 7. (Optional) Record dependencies

To keep track of what was installed:

```bash
uv pip freeze > requirements.txt
```

This file allows you (or someone else) to recreate the environment later.

---

### Conda vs `uv` at a glance

Both workflows follow the same logic:

```text
create → activate → install → work → stop → deactivate
```

```{admonition} When to use which?
:class: tip

Use **Conda** when:
- you want one environment for an entire course/project
- you rely heavily on compiled geospatial libraries

Use **uv** when:
- each lab should be isolated
- you want fast setup and easy reset
- you prefer project-local environments
```

### Key takeways

* Conda is your main tool for geospatial environments
* uv is a fast option for Python only tasks
* Knowing both helps you choose the right tool for the job

This is not about using more tools, but about **using the right tool in the right context**.

---

## 7. Best practices

As your projects grow, good habits around environments will save you a lot of time and frustration. The goal is not perfection, but **clarity and control**.

**1. Keep environments simple and focused**

Each project should have its **own environment**.

Good practice:

* use descriptive but short names such as `sds-env`, `sds210-lab1`, or `thesis-env`
* install only what the project actually needs
* remove environments you no longer use

Avoid putting everything into one large environment. Large environments are harder to debug, slower to solve, and difficult to reproduce.

``` {admonition} Tip
:class: tip
If you hesitate before installing a package, that is often a sign it belongs in a different environment.
```

---

**2.  Document environments early**

An environment is part of your project, just like your code.

* export environments to a file
* keep the file with your project
* update it when dependencies change

This makes your work reproducible for:

* yourself in the future
* your lab partner
* your supervisor
* automated systems

You do not need to export after every small change, but do it whenever the environment becomes important.

---

**3. Prefer reliable packages sources**

Installing packages is easy. Installing them **well** takes a bit of discipline. For geospatial work:

* prefer `conda-forge`
* specify the channel explicitly
* install Conda packages before using pip

This reduces conflicts and improves reproducibility.

---

**4. Update and troubleshoot intentionally**

When things go wrong:

* check which environment is active
* read error messages carefully
* update conda or mamba before trying random fixes

If installations behave strangely, clearing cached packages can help:

```bash
conda clean --all
```

``` {admonition} Caution
:class: caution
Most environment problems come from installing packages into the wrong environment or mixing tools carelessly.
```

---

**Big picture**

You do not need to [memorise commands](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#), but you should internalise these ideas:

* environments isolate projects and prevent conflicts
* conda-forge is essential for geospatial work
* environments are part of your project documentation
* clean setups lead to reliable results

Avoid installing packages into:

* the system Python
* the Conda base environment

Instead, create a new environment for each project. This habit alone will prevent many hard-to-debug problems later on.

By following these practices, you are not just learning tools. You are learning **professional workflows** that scale from coursework to research and real-world projects.

---

## 8. Exercises

These exercises help you practice the core skills needed to work confidently with Conda in real projects.

---

### Exercise 1: Creating and Using a Project Environment

**Goal:** Create a clean Conda environment and use it for geospatial work.

1. Create a new Conda environment called `sds-env` with Python 3.12
2. Activate the environment
3. Install the `pygis` package from the `conda-forge` channel
4. List all installed packages in the environment
5. Start Python and verify that the environment is working
6. Install `geopandas` and `rasterio` explicitly into `sds-env`
7. Check which channel each package was installed from
8. Deactivate the environment and confirm that it is no longer active
9. Create a second environment called `sds-env-alt` with Python 3.12
10. Compare the installed packages between the two environments


``` {admonition} Sample Solution - Exercise 1
:class: dropdown

```bash
# ============================================================
# Exercise 1 solution: Setting up your first geospatial environment
# Goal: Create a conda environment, install core geospatial packages,
#       verify installation, and export the environment for reproducibility.
# Notes:
#   - Replace environment names if you chose different ones.
# ============================================================

# 1) Create a new Conda environment called "sds-env" with Python 3.12
# This creates an isolated environment with its own Python interpreter.
conda create --name sds-env python=3.12

# 2) Activate the new environment
# From now on, all Python and conda commands apply to sds-env.
conda activate sds-env

# 3) Install the pygis meta-package from the conda-forge channel
# pygis pulls in a common set of geospatial libraries and dependencies.
conda install --channel conda-forge pygis

# 4) List all installed packages in the active environment
# This shows package names, versions, and build information.
conda list

# 5) Start Python to verify the environment is working
# You should see the Python prompt without errors.
python

# Inside the Python prompt, try a simple check (then exit Python):
# >>> import sys
# >>> print(sys.version)
# >>> exit()

# 6) Install additional geospatial packages explicitly
# Even though pygis may already include some of them,
# installing explicitly makes dependencies visible.
conda install --channel conda-forge geopandas rasterio

# 7) Check which channel each package was installed from
# This is useful for debugging and documentation.
conda list --show-channel-urls

# 8) Deactivate the environment
# This returns you to the base environment.
conda deactivate

# Confirm that sds-env is no longer active
# The active environment is marked with an asterisk (*).
conda info --envs

# 9) Create a second environment with a different Python version
# This is useful for testing compatibility across Python versions.
conda create --name sds-env-alt python=3.12

# Activate the second environment
conda activate sds-env-alt

# List installed packages in sds-env-alt
# At this point, it should contain only Python and core dependencies.
conda list

# 10) Compare environments by listing both explicitly
# You can visually compare package names and versions.
conda list --name sds-env
conda list --name sds-env-alt

# Deactivate when finished
conda deactivate
```

---

### Exercise 2: Inspecting and Managing Environments

**Goal:** Learn how to stay in control once environments exist.

1. List all Conda environments on your system
2. Identify which environment is currently active
3. Inspect the installed packages in `sds-env`, including their source channels
4. Install an additional package into `sds-env` without activating it
5. Remove that package again
6. Update all packages in `sds-env`
7. Clone `sds-env` into a new environment called `sds-env-test`
8. Remove `sds-env-test` once you are done

``` {admonition} Sample Solution - Exercise 2
:class: dropdown

```bash
# ============================================================
# Exercise 2 solution: Inspecting and managing environments
# Goal: Learn how to inspect, modify, and clean up Conda
#       environments once they exist.
# Notes:
#   - This solution assumes that "sds-env" already exists
#     from Exercise 1.
#   - Commands are written to be run step by step in a shell.
# ============================================================

# 1) List all Conda environments on your system
# The active environment is marked with an asterisk (*).
conda info --envs

# Alternative command (does the same thing):
# conda env list

# 2) Identify which environment is currently active
# Look for the asterisk (*) in the output above.
# If sds-env is active, it will be marked with *.

# 3) Inspect installed packages in sds-env, including source channels
# This shows package names, versions, and where they came from.
conda list --name sds-env --show-channel-urls

# 4) Install an additional package into sds-env without activating it
# This is useful when managing environments programmatically or remotely.
conda install --name sds-env --channel conda-forge maplibre

# 5) Remove the package again
# This cleanly uninstalls the package and updates dependencies if needed.
conda remove --name sds-env maplibre

# 6) Update all packages in sds-env
# Use this carefully in real projects, as updates may change behavior.
conda update --all --name sds-env

# 7) Clone sds-env into a new environment called sds-env-test
# This creates a full copy with the same Python version and packages.
conda create --clone sds-env --name sds-env-test

# Verify that the new environment exists
conda info --envs

# 8) Remove sds-env-test once you are done
# Make sure it is not active before removing it.
conda remove --name sds-env-test --all

# Final check to confirm cleanup
conda info --envs

```

---

### Exercise 3: Reproducibility with Environment Files

**Goal:** Practice exporting and recreating environments.

1. Export the `sds-env` environment to a file called `sds-env.yml`
2. Create a new environment called `sds-env-copy` from that file
3. Activate `sds-env-copy` and verify that it works
4. Compare the package lists of `sds-env` and `sds-env-copy`
5. Add one additional package to `sds-env-copy`
6. Export the updated environment to a new file
7. Remove the original `sds-env`
8. Recreate it only from the exported file


``` {admonition} Sample Solution - Exercise 3
:class: dropdown

```bash
# ============================================================
# Exercise 3 solution: Reproducibility with environment files
# Goal: Practice exporting, recreating, and validating Conda
#       environments using environment files.
# Notes:
#   - This exercise assumes that "sds-env" already exists
#     and contains geospatial packages from previous exercises.
#   - Commands are meant to be run step by step.
# ============================================================

# 1) Export the existing sds-env environment to a YAML file
# This file captures package names and versions for reproducibility.
conda env export --name sds-env > sds-env.yml

# Optional sanity check: view the file contents
# cat sds-env.yml

# 2) Create a new environment called sds-env-copy from the file
conda env create --name sds-env-copy --file sds-env.yml

# 3) Activate sds-env-copy
conda activate sds-env-copy

# Verify that Python starts correctly
python --version

# Optional quick import test to confirm the environment works
python
python -c "import geopandas, rasterio; print('OK')"

# Deactivate again before continuing
conda deactivate

# 4) Compare package lists between sds-env and sds-env-copy
# This helps confirm that the environments are equivalent.
conda list --name sds-env
conda list --name sds-env-copy

# 5) Add one additional package to sds-env-copy
# Activate the copy first
conda activate sds-env-copy

# Install an additional geospatial helper package
conda install --channel conda-forge maplibre

# 6) Export the updated environment to a new file
conda env export --name sds-env-copy > sds-env-copy.yml

# Deactivate after finishing changes
conda deactivate

# 7) Remove the original sds-env
# Make sure it is not active before removing it.
conda remove --name sds-env --all

# Confirm that sds-env is gone
conda info --envs

# 8) Recreate sds-env only from the exported file
conda env create --name sds-env --file sds-env.yml

# Activate and verify the recreated environment
conda activate sds-env
python --version

# Optional import check
python -c "import geopandas, rasterio; print('OK')"

# Final cleanup
conda deactivate

```

---

**Reflection**

After completing the exercises, take a moment to reflect:

* Which step felt most confusing
* Which command felt most useful
* What would you do differently next time

Being comfortable with environments is less about memorising commands and more about **knowing what to check when something breaks**.

If you can create, inspect, export, and recreate environments confidently, you have mastered one of the most important foundations of professional geospatial programming.
