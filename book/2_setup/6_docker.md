---
title: Docker

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Running reproducible geospatial environments
</div>

---

## 1. Introduction

If you have ever spent hours installing geospatial Python packages only to run into errors, you are not alone. Libraries like **GDAL**, **PROJ**, and **GEOS** depend on many system components, and small differences between computers or operating systems can easily break an otherwise working script. This often leads to the classic problem: *the code works on my machine, but not on yours*.

**Docker** addresses this problem by packaging your entire working environment into a **container**. This includes the operating system, Python, all required libraries, and sometimes even the code itself. When you run a container, you are not just running Python code but a complete and self contained environment that behaves the same on every computer where Docker is installed.

You can think of a container as a lightweight virtual computer that starts in seconds and can be thrown away after use. The same container can be used by **students**, **collaborators**, or on **servers** and **cloud platforms**, without reinstalling anything. This makes Docker especially powerful for **reproducibility**, **teaching**, and **collaborative geospatial work**.

In this course, Docker is not used much, as we do not build production systems. You are not expected to become a Docker expert. However, it complements tools like **Conda** and **Colab**. While Conda helps you manage environments on your own machine, Docker helps you run the *same* environment everywhere.

---

## 2. Learning Objectives

After working through this section, you should be able to:

* Explain **when and why Docker is useful** for geospatial programming
* Run a **JupyterLab based geospatial environment** using Docker
* Use Docker to **reproduce and run course examples** reliably

These objectives focus on using Docker as a practical tool for **reproducible workflows**. You will use these skills whenever you need a stable environment that works the same on different computers, for example in project work or collaborative settings.

---

## 3. When to use Docker

Docker is a powerful tool, but it is not always the right choice. In this course, you can see Docker as **one option** among several ways to run geospatial Python code. The key question is not which tool is best, but **which tool fits your situation**.

If you work on your own laptop and mainly follow course examples, **Conda** is often sufficient. It is lightweight, fast to use, and well suited for local development. If you want to try out ideas quickly without installing anything, **Colab** is convenient, but your environment depends on the cloud setup and can change over time.

You should consider **Docker** when you need the **same environment to run everywhere**. This is especially important when you share code with others, work on different computers, or want to ensure that results can be reproduced later.

The table below summarizes the typical use cases.

| Tool   | Best for              | Limitations                        |
| ------ | --------------------- | ---------------------------------- |
| Conda  | Local development     | Depends on your operating system   |
| Colab  | Quick demos and tests | Limited reproducibility            |
| Docker | Exact replication     | Slightly higher setup effort       |

A simple rule of thumb is this. If **other people must run your code exactly as you did**, Docker is usually the right choice.

---

## 4. Installing Docker Desktop

Docker Desktop is the easiest way to get started with **Docker** on Windows and macOS. It bundles everything you need and provides a simple interface to check whether Docker is running.

::::::{tab-set}

:::::{tab-item} Windows and macOS 
1. Go to https://www.docker.com/products/docker-desktop  
2. Download Docker Desktop for your operating system  
3. Run the installer and follow the setup instructions  
4. Start Docker Desktop after the installation finishes  

When Docker is running, you will see the **Docker icon** in the system tray on Windows or in the menu bar on macOS. This indicates that Docker is active and ready to use.

During the first start, you may be asked to grant **permissions** or approve system settings. This is normal and required for Docker to run containers.

:::::

:::::{tab-item} Linux

Docker can also be used on Linux, but the installation depends on your distribution. Please follow the **official Docker documentation** for up to date instructions:

https://docs.docker.com/engine/install/

:::::

::::::

#### Verify the installation

To check whether Docker is installed correctly, open a terminal and run:

```bash
docker --version
```

If the installation was successful, you will see the **Docker version** printed in the terminal.

A common issue at this stage is that Docker is installed but **not running**. If the command does not work, make sure Docker Desktop is started and try again.

---

## 5. Core Docker Concepts

You only need a few basic concepts to work effectively with **Docker** here. The goal here is understanding, not memorizing technical details.

### Images and containers

A **Docker image** is a frozen environment. It contains the operating system, Python, and all required libraries. Images do not change when you use them.

A **Docker container** is a running instance of an image. When you start a container, Docker creates a temporary working environment from the image. You can run code, open notebooks, and interact with it like a small computer.

In short, an **image** is the recipe and a **container** is the running result.

### Key terms you will actually use

**Docker Hub**  
An online registry where Docker images are shared. You will download ready made geospatial images from there.

**Volume**  
A shared folder between your computer and the container. Volumes ensure that **your files persist** even after the container is stopped.

**Port**  
A connection between your computer and the container. This is required so you can open **JupyterLab** in your web browser.

**Container lifecycle**  
Containers are started, used, stopped, and removed. They are meant to be **temporary**, while your files live outside the container in a shared folder.

More advanced topics such as Dockerfiles or container orchestration are intentionally left out here. They are not needed to use Docker effectively in this course.

---

## 6. Running JupyterLab in Docker

This section shows the **core workflow** you will use to run geospatial notebooks in Docker. Once you understand this pattern, you can reuse it for most Docker based projects.

### Pulling a ready made image

Instead of building an environment yourself, you will use a **prebuilt Docker image** that already contains Python and the required geospatial libraries. This saves time and avoids installation problems.

For this course, we use the following image:

`giswqs/pygis:book`

You can download it from **Docker Hub** by running:

```bash
docker pull giswqs/pygis:book
```

This command downloads the image to your computer. You only need to do this once.

### Running the container

To start a container and launch **JupyterLab**, run the following command in your terminal:

```bash
docker run -it -p 8888:8888 -v $(pwd):/app/workspace giswqs/pygis:book
```

What this command does:

* `docker run` starts a new container
* `-it` makes the container interactive
* `-p 8888:8888` connects JupyterLab inside the container to your browser
* `-v $(pwd):/app/workspace` shares your current folder with the container
* `giswqs/pygis:book` selects the image to use

After running the command, Docker starts the container and launches JupyterLab inside it.

### Accessing JupyterLab

In the terminal output, look for a URL that starts with:

`http://127.0.0.1:8888/lab?token=...`

Copy this URL into your web browser or use Ctrl and click to open it. This will open **JupyterLab**.

Inside JupyterLab, you are working in the `/app/workspace` folder. This folder is linked to your current directory on your computer. This means you are **inside a container**, but your **files are stored on your own machine**.

---

## 7. Working with files and persistence

One common concern when using Docker is whether your work will be lost when a container stops. The key concept that prevents this is the **volume**.

### How volumes work

A **volume** connects a folder on your computer to a folder inside the container. Here, your local working directory is linked to the container folder `/app/workspace`.

This has important consequences:

* Files you create or edit in the container are **saved on your computer**
* Files that exist on your computer appear automatically inside the container
* Only files stored outside the shared folder disappear when the container stops

As long as you work inside the shared folder, your notebooks and data are safe.

### A safe workflow pattern

A simple and reliable workflow looks like this:

1. Start the container  
2. Work only inside the **mounted folder**  
3. Stop the container when you are done  
4. Your files remain on your computer  

If something goes wrong, you can always start a new container and continue working with the same files. This is a normal and expected way of using Docker.

---

## 8. Essential Docker commands

You only need a small set of **Docker commands** to work comfortably. The goal is to recognize what each command does, not to memorize everything.

### Everyday commands

`docker pull`  
Downloads a Docker image from **Docker Hub** to your computer.

`docker run`  
Starts a new **container** from an image and runs it.

`docker ps`  
Shows all **currently running containers**.

`docker stop`  
Stops a running container in a clean way.

These commands cover most daily tasks when running JupyterLab in Docker.

### Troubleshooting commands

`docker ps -a`  
Shows all containers, including those that are stopped.

`docker images`  
Lists all Docker images that are stored on your computer.

`docker logs`  
Displays output from a container, which can help when something does not work as expected.

`docker help`  
Shows help for Docker commands and options.

Focus on understanding **when to use a command** rather than remembering the exact syntax. With practice, these commands will become familiar.

---

## 9. Common pitfalls 

This section highlights a few **common mistakes** when starting with Docker and shows how to avoid them. Reading this carefully can save you a lot of frustration.

**Forgetting volume mounting**  
If you start a container without a **volume**, files created inside the container will disappear when it stops. Always make sure you mount a local folder so your work is **saved on your computer**.

**Port already in use**  
If JupyterLab does not open, the selected **port** may already be used by another service. In this case, choose a different port and try again.

**Multiple containers running**  
It is easy to forget that a container is still running in the background. Use `docker ps` to check active containers and stop those you no longer need.

**Assuming Docker replaces Conda everywhere**  
Docker is not a replacement for **Conda** in all situations. Conda is often better for everyday local work. Docker is most useful when **reproducibility** and sharing environments matter.

Being aware of these issues early will help you use Docker more confidently and efficiently.

---

## 10. Exercises

These exercises focus on **running Docker**, **verifying the environment**, and **handling common issues**. Together, these exercises cover all learning objectives. You do not need to memorize commands. The goal is to gain confidence using Docker as a practical tool.

#### Exercise 1: First Docker run

This exercise helps you get Docker running and access **JupyterLab**.

1. Install **Docker Desktop** following the instructions in this chapter  
2. Create a new folder called `docker_test`  
3. Open a terminal and navigate into this folder  
4. Run the following command:

```bash
docker run -it -p 8888:8888 -v $(pwd):/home/jovyan/work ghcr.io/opengeos/leafmap:latest
```

5. Open the JupyterLab URL shown in the terminal
6. In JupyterLab, navigate to `leafmap/docs/maplibre` and run any notebook

You should now be working in a fully configured **geospatial environment**.

---

#### Exercise 2: Inspecting the environment

This exercise builds a **verification mindset**.

1. In the running container, create a new notebook
2. Check that key libraries are available:

```python
import geopandas as gpd
import rasterio
import leafmap
print("All libraries imported successfully")
```

3. Create a simple interactive map:

```python
import leafmap.maplibregl as leafmap
m = leafmap.Map(projection="globe")
m
```

4. Save the notebook as `leafmap_test.ipynb` in the shared folder

If this works, your **Docker environment** is ready for course work.

---

#### Exercise 3: Ports and conflicts

This exercise helps you handle **port issues**, which are common in practice.

1. Stop the running container using `Ctrl C`
2. Start the container again, but use port `8889` instead of `8888`
3. Open JupyterLab in your browser using the new port
4. Verify that `leafmap_test.ipynb` is still available

This confirms that your files are **persistent** and that you can adapt when ports are already in use.

