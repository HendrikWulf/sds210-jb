---
title: Docker

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Running Reproducible Geospatial Environments
</div>
<!-- markdownlint-enable MD033 -->

---

## 1. Introduction

If you have struggled to install geospatial Python packages and encountered errors in the process, rest assured that you are not alone. {term}`Libraries <Library>` like **{term}`GDAL`**, **PROJ**, and **GEOS** depend on many system components, and small differences between computers or operating systems can break an otherwise working {term}`script <Script>`. This can lead to the classic problem: *the code works on my machine, but not on yours*.

**{term}`Docker`** addresses this problem by packaging your entire working environment into a **{term}`container <Container>`**. This includes the operating system, Python, all required libraries, and sometimes even the code itself. When you run a container, you are not just running Python code, but a complete and self-contained environment that behaves the same on every computer where Docker is installed.

You can think of a container as a lightweight virtual computer that starts quickly and can be thrown away after use. The same container can be used by **students**, **collaborators**, or on **servers** and **cloud platforms**, without reinstalling everything manually. This makes Docker especially powerful for **{term}`reproducibility <Reproducibility>`**, teaching, and collaborative geospatial work.

In this course, Docker is not really required, because we do not build production systems. You are not expected to become a Docker expert. However, Docker complements tools like **{term}`Conda`** and **{term}`JupyterLab`**. While Conda helps you manage environments on your own machine, Docker helps you run the *same* environment everywhere.

```{admonition} Big idea
:class: tip

Conda helps you manage Python environments locally.  
Docker packages a complete working environment so it can run consistently across different computers.
```

---

## 2. Learning Objectives

After working through this chapter, you should be able to:

* Explain **when and why Docker is useful** for geospatial programming.
* Run a **{term}`JupyterLab`-based geospatial environment** using Docker.
* Use Docker to **reproduce and run course examples** reliably.

These objectives focus on using Docker as a practical tool for reproducible workflows. You will use these skills whenever you need a stable environment that works the same on different computers, for example in project work or collaborative settings.

---

## 3. When to Use Docker

Docker is powerful, but it is not always the right choice. In this course, you can see Docker as **one option** among several ways to run geospatial Python code. The key question is not which tool is best in general, but **which tool fits your situation**.

If you work on your own laptop and mainly follow course examples, **Conda** is often sufficient. It is lightweight, fast to use, and well suited for local development. If you want to try out ideas quickly without installing anything, **Colab** is convenient, but your environment depends on the cloud setup and can change over time.

You should consider **Docker** when you need the **same environment to run everywhere**. This is especially important when you share code with others, work on different computers, or want to ensure that results can be reproduced later.

| Tool | Best for | Limitations |
| --- | --- | --- |
| Conda | Local development | Depends partly on your operating system |
| Colab | Quick demos and tests | Limited control and changing cloud environment |
| Docker | Exact replication | Slightly higher setup effort |

A simple rule of thumb:

> If **other people must run your code exactly as you did**, Docker is usually the right choice.

---

## 4. Installing Docker Desktop

Docker Desktop is the easiest way to get started with Docker on Windows and macOS. It bundles everything you need and provides a simple interface to check whether Docker is running.

::::::{tab-set}

:::::{tab-item} Windows and macOS

1. Go to the [Docker Desktop download page](https://www.docker.com/products/docker-desktop).
2. Download Docker Desktop for your operating system.
3. Run the installer and follow the setup instructions.
4. Start Docker Desktop after the installation finishes.

When Docker is running, you will see the **Docker icon** in the system tray on Windows or in the menu bar on macOS. This indicates that Docker is active and ready to use.

During the first start, you may be asked to grant **permissions** or approve system settings. This is normal and required for Docker to run containers.

:::::

:::::{tab-item} Linux

Docker can also be used on Linux, but the installation depends on your distribution. Please follow the [official Docker Engine installation instructions](https://docs.docker.com/engine/install/) for up-to-date guidance.

:::::

::::::

### Verify the installation

To check whether Docker is installed correctly, open a {term}`Terminal` and run:

```bash
docker --version
```

If the installation was successful, you will see the Docker {term}`version <Version>` printed in the terminal.

A common issue at this stage is that Docker is installed but **not running**. If the command does not work, make sure Docker Desktop is started and try again.

```{admonition} First check
:class: tip

Before running any Docker command, check that Docker Desktop is open and running. Installing Docker and starting Docker are two different things.
```

---

## 5. Core Docker Concepts

You only need a few basic concepts to work effectively with Docker in this course. The goal is understanding, not memorising technical details.

### Images and containers

A **Docker image** is a frozen environment. It contains the operating system, Python, and all required libraries. Images do not change when you use them.

A **Docker container** is a running instance of an image. When you start a container, Docker creates a temporary working environment from the image. You can run code, open notebooks, and interact with it like a small computer.

In short:

> An **image** is the recipe.  
> A **container** is the running result.

### Other key terms

**Docker Hub**  
An online registry where Docker images are shared. You can download ready-made geospatial images from there.

**Volume**  
A shared folder between your computer and the container. Volumes ensure that **your files persist** even after the container is stopped.

**Port**  
A connection between your computer and the container. This is required so you can open JupyterLab in your web browser.

**Container lifecycle**  
Containers are started, used, stopped, and removed. They are meant to be **temporary**, while your files should live outside the container in a shared folder.

More advanced topics such as Dockerfiles or container orchestration are intentionally left out here. They are not needed to use Docker effectively in this course.

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch06_docker_launch_pad/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Docker Container Launch Pad.</b><br>
    Click the launch steps to pull an image, start a container, mount your project folder, map the JupyterLab port, and stop the container again. Watch how the container can disappear while the mounted project files stay safely on your own computer. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L00_setup_ch06_docker_launch_pad/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

```{admonition} Key idea
:class: tip

The container is temporary.  
Your mounted project folder is persistent.

This distinction is the most important Docker concept for beginners.
```

---

## 6. Running JupyterLab in Docker

This section shows the core SDS210 Docker workflow. The important idea is:

* the **Docker image** provides the reproducible software environment
* the **GitLab course repository** provides the notebooks, data, and practicals
* the **mounted folder** keeps your work safely on your own computer

The SDS210 Docker image does not contain the course data or your personal work. This keeps the image smaller and avoids duplicating large files. Your course files remain in the cloned GitLab repository on your own computer.

---

### Pulling the SDS210 image

For this course, we use the following Docker image:

```text
registry.gitlab.com/hendrikwulf/sds210:latest
```

Open your **Terminal** or **shell application** first. For this step, it does **not matter which directory your terminal is currently in**, because the image is downloaded into Docker itself, not into your project folder. You can download it by running:

```bash
docker pull registry.gitlab.com/hendrikwulf/sds210:latest
```

This command downloads the SDS210 image to your computer. You only need to do this once, unless the image is updated later.

After the download has finished, you should see a message similar to:

```text
Status: Downloaded newer image for registry.gitlab.com/hendrikwulf/sds210:latest
```

```{admonition} What is inside the image?
:class: note

The SDS210 Docker image contains JupyterLab and the Python packages used in this course, including the geospatial libraries needed for the practical notebooks.

It does **not** contain the full course data folder. The data and practical notebooks come from the SDS210 GitLab repository and are mounted into the container from your computer.
```

---

### Getting the course files

The Docker image provides the software environment. The course notebooks, data, and practicals come from the SDS210 GitLab repository. Now make sure your terminal is in the folder where you want to keep your course files.

Clone the course repository once:

```bash
git clone https://gitlab.com/HendrikWulf/sds210.git
```

Then move into the course folder:

```bash
cd sds210
```

This folder will be mounted into the Docker container. Any notebooks or outputs you create there will remain on your computer after the container stops.

```{admonition} Image versus repository
:class: tip

The Docker image gives you the software environment.

The GitLab repository gives you the course files.

You need both: pull the image, clone the repository, and then mount the repository folder into the container.
```

---

### Running the container

To start a container and launch JupyterLab, run the command below from inside the cloned `sds210` folder.

::::::{tab-set}

:::::{tab-item} macOS, Linux, or Git Bash

```bash
docker run --rm -it -p 8888:8888 -v "$(pwd)":/home/jovyan/work registry.gitlab.com/hendrikwulf/sds210:latest
```

:::::

:::::{tab-item} Windows PowerShell

```powershell
docker run --rm -it -p 8888:8888 -v "${PWD}:/home/jovyan/work" registry.gitlab.com/hendrikwulf/sds210:latest
```

:::::

::::::

What this command does:

* `docker run` starts a new container.
* `--rm` removes the container automatically when it stops.
* `-it` keeps the container interactive in the terminal.
* `-p 8888:8888` connects JupyterLab inside the container to your browser.
* `-v "$(pwd)":/home/jovyan/work` shares your current course folder with the container.
* `registry.gitlab.com/hendrikwulf/sds210:latest` selects the SDS210 image.

After running the command, Docker starts the container and launches JupyterLab inside it.

---

### Accessing JupyterLab

In the terminal output, look for a URL that starts with:

```text
http://127.0.0.1:8888/lab?token=...
```

Copy this URL into your web browser, or use Ctrl and click to open it. This will open JupyterLab.

Inside JupyterLab, you are working in:

```text
/home/jovyan/work
```

This folder is linked to the `sds210` folder on your own computer. This means you are **inside a container**, but your **files are stored on your own machine**.

```{admonition} Kernel choice
:class: tip

If JupyterLab asks you to select a kernel, choose:

**Python (SDS210)**

This kernel uses the Python environment prepared inside the SDS210 Docker image.
```

---

## 7. Working with Files and Persistence

One common concern when using Docker is whether your work will be lost when a container stops. The key concept that prevents this is the **mounted folder**.

### How the mounted folder works

The command above connects your local `sds210` folder to the container folder:

```text
/home/jovyan/work
```

This has important consequences:

* Files you create or edit in JupyterLab are **saved on your computer**.
* Files that exist in your local `sds210` folder appear automatically inside the container.
* Files stored outside `/home/jovyan/work` may disappear when the container stops.

As long as you work inside `/home/jovyan/work`, your notebooks and data are safe.

```{admonition} Important
:class: warning

Do not store important work only inside the container's internal file system.

Work inside `/home/jovyan/work` so your files remain available after the container stops.
```

---

### A safe SDS210 Docker workflow

A simple and reliable workflow looks like this:

1. Clone or update the SDS210 GitLab repository.
2. Pull the current SDS210 Docker image.
3. Start the Docker container from inside the `sds210` folder.
4. Work only inside `/home/jovyan/work`.
5. Save notebooks, scripts, data, and outputs there.
6. Stop the container when you are done.
7. Your files remain on your computer.

If something goes wrong, you can stop the container and start a new one. The software environment comes from the image, while your work remains in the mounted folder.

---

### Updating the image and the course files

There are two separate updates.

To update the software environment:

```bash
docker pull registry.gitlab.com/hendrikwulf/sds210:latest
```

To update the course files:

```bash
git pull
```

Run `git pull` from inside the cloned `sds210` folder.

```{admonition} Image versus course files
:class: note

Updating the Docker image updates the software environment.

Updating the GitLab repository updates the notebooks, practicals, and data.

These are related, but they are not the same thing.
```

---

## 8. Essential Docker Commands

You only need a small set of Docker commands to work comfortably. The goal is to recognise what each command does, not to memorise everything.

### Everyday commands

`docker pull registry.gitlab.com/hendrikwulf/sds210:latest`  
Downloads or updates the SDS210 Docker image.

`docker run`  
Starts a new container from an image and runs it.

`docker ps`  
Shows all currently running containers.

`docker stop`  
Stops a running container in a clean way.

These commands cover most daily tasks when running JupyterLab in Docker.

---

### Troubleshooting commands

`docker ps -a`  
Shows all containers, including those that are stopped.

`docker images`  
Lists all Docker images stored on your computer.

`docker logs`  
Displays output from a container, which can help when something does not work as expected.

`docker help`  
Shows help for Docker commands and options.

Focus on understanding **when to use a command** rather than remembering the exact syntax. With practice, these commands will become familiar.

---

## 9. Exercises

These exercises focus on **running Docker**, **verifying the SDS210 environment**, and **handling common issues**. You do not need to memorise commands. The goal is to gain confidence using Docker as a practical reproducibility tool.

---

### Exercise 1: First SDS210 Docker Run

**Objective**  
Start the SDS210 Docker-based JupyterLab environment and open it in your browser.

**Tasks**

1. Install **Docker Desktop** following the instructions in this chapter.
2. Clone the SDS210 course repository:

   ```bash
   git clone https://gitlab.com/HendrikWulf/sds210.git
   ```

3. Move into the repository:

   ```bash
   cd sds210
   ```

4. Pull the SDS210 Docker image:

   ```bash
   docker pull registry.gitlab.com/hendrikwulf/sds210:latest
   ```

5. Start the container.

   macOS, Linux, or Git Bash:

   ```bash
   docker run --rm -it -p 8888:8888 -v "$(pwd)":/home/jovyan/work registry.gitlab.com/hendrikwulf/sds210:latest
   ```

   Windows PowerShell:

   ```powershell
   docker run --rm -it -p 8888:8888 -v "${PWD}:/home/jovyan/work" registry.gitlab.com/hendrikwulf/sds210:latest
   ```

6. Open the JupyterLab URL shown in the terminal.
7. Create a new notebook inside `/home/jovyan/work`.

**What to verify**

* Docker starts without errors.
* JupyterLab opens in your browser.
* The `/home/jovyan/work` folder is visible.
* A notebook created there appears in your local `sds210` folder.

---

### Exercise 2: Inspecting the SDS210 Environment

**Objective**  
Build a verification mindset by checking what is available inside the container.

**Tasks**

1. In the running container, create a new notebook.
2. Select the **Python (SDS210)** kernel if prompted.
3. Check that key libraries are available:

   ```python
   import geopandas as gpd
   import rasterio
   import xarray as xr
   import rioxarray
   import folium
   import cartopy
   import contextily
   print("SDS210 Docker environment ready")
   ```

4. Save the notebook as `sds210_docker_test.ipynb` inside `/home/jovyan/work`.

**What to verify**

* The imports run successfully.
* The notebook file appears in your local `sds210` folder.
* The notebook still exists after stopping and restarting the container.

---

After these exercises, you should understand Docker as a practical reproducibility tool: it runs the SDS210 software environment, connects it to your local course files through a mounted folder, and exposes browser-based tools such as JupyterLab through a port.
