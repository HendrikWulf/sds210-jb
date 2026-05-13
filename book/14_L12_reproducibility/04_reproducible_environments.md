---
title: Reproducible environments
site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
Moving beyond "It works on my machine"
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/14_L12_reproducibility/04_reproducible_environments.ipynb)

---

```{admonition} Big idea
:class: tip

A script is not truly reproducible if it only runs on one machine by accident. To make spatial science reproducible, you must share not only your code and data, but also the exact software environment used to run it.
```

In the previous chapters, you learned how to write cleaner Python, organize larger workflows, and make code fail more clearly when assumptions break. This chapter extends that logic from the code itself to the software around it.

A notebook may be perfectly readable, well structured, and defensively coded, and still fail on another machine. A workflow that depends on `geopandas`, `rasterio`, `xarray`, `rioxarray`, or `cartopy` may work flawlessly on one computer and fail elsewhere because a package is missing, a dependency chain differs, or a newer version changed the behavior.

This is the classic **"it works on my machine"** problem.

Reproducible environments are the answer. They make the software conditions of a project explicit: the Python version, the installed libraries, and ideally the versions of those libraries as well. That way, someone else can recreate not only your code and data, but also the computational context that allowed the workflow to run.

In this chapter, you will learn what an environment actually is, why geospatial workflows are especially sensitive to dependency problems, how to record dependencies with `requirements.txt` or `environment.yml`, and what a realistic environment strategy looks like for SDS210 projects.

---

## 1. Why "it works on my machine" is not enough

A reproducibility problem often begins with invisible assumptions about software.

When you install Python and start downloading packages using `conda` or `pip`, you are building an ecosystem. Over time, as you work on different projects, you install new tools, update existing ones, and inadvertently change the software landscape of your computer's default "base" environment.

Imagine that you share a notebook with a classmate. The notebook imports:

```{code-cell} python
import geopandas as gpd
import rasterio
import xarray as xr
import rioxarray
import matplotlib.pyplot as plt
```

On your machine, everything runs. On theirs, the notebook may fail for several different reasons:
* a package is simply not installed
* the Python version is fundamentally different
* a package is much newer or older, changing how its functions behave
* an optional dependency is missing

### The geospatial fragility

In spatial data science, this problem is known. Many Python geospatial libraries are actually wrappers around complex, lower-level C++ libraries (like GDAL, PROJ, and GEOS). The code may look like ordinary Python, but under the surface, there is a massive, interconnected software stack. 

It is common for a student to write a perfectly functioning workflow that reads a GeoPackage, clips a raster, and exports a GeoTIFF. A few months later, they open the project again and discover that:
* one package import suddenly fails
* `rioxarray` no longer detects its underlying backend
* a spatial join step now raises a mysterious error

The code did not change, but the invisible global environment did.

### The solution: Virtual Environments

Relying on a single, global installation for all your classes and projects is dangerous. If the analysis only works because one particular laptop happens to have the exact right mix of packages installed by pure chance, the workflow is not reproducible.

To fix this, professional data scientists use **Virtual Environments** (managed by tools like `conda` or `venv`). Virtual environments act as isolated, soundproof rooms for your projects. Instead of installing all spatial libraries into one massive global ecosystem, you create a dedicated room containing *only* the specific tools needed for your SDS210 project.

```{admonition} Reproducibility includes software
:class: important

The code may exist, and the data may exist, but if the analysis relies on an undocumented, fragile software ecosystem, the project cannot be rerun elsewhere. True reproducibility requires sharing your environment.
```

---

## 2. What an environment actually is

Before discussing configuration files like `requirements.txt` or `environment.yml`, it helps to define what a software environment actually is.

A Python environment is an isolated software space that contains:
* A specific Python version
* A specific set of installed packages
* The exact version numbers of those packages

You can think of it as a dedicated workshop for a single project. Inside that workshop, you place only the exact tools that the project needs to run.

### The danger of the base environment

When you install Python for the first time, you get a default, global workspace (often called the "base" environment). If you install every package for every class and project into this single global workspace, your tools will inevitably start fighting with each other.

Suppose your SDS210 project requires a newer version of `geopandas`, but a different university course requires a package that relies on an outdated version of `numpy`. If they share the same base environment, updating a package for one class might instantly break your code for the other. This creates an unstable system.

### Why isolation matters

Project-specific environments solve this by giving every project its own isolated workshop. 
* **Project A** (Spatial Analysis) has its own room with `geopandas` and `rasterio`.
* **Project B** (Machine Learning) has a separate room with `scikit-learn` and `pytorch`.
* **Project C** (Web Scraping) uses only `requests` and `beautifulsoup4`.

Because these workshops are isolated, upgrading a package in Project B will never accidentally break the code in Project A.
Therefore, the software environment is a fundamental part of the project itself, just as important as the data or the code.

---

## 3. Recording dependencies

Once you understand that environments matter, the next step is obvious: the environment needs to be recorded. If a workflow depends on a specific set of libraries, those libraries should not remain hidden assumptions. 

When sharing code, there are two different kinds of environment failures you must prevent:

1. **Missing dependencies:** The code fails immediately with a `ModuleNotFoundError` because a package is simply not installed. A reader must guess the required software by scanning the code for `import` statements.
2. **Version drift:** The package is installed, but it is a much newer (or older) version than the author used, and its behavior has fundamentally changed.

### The danger of version drift

Version drift is often harder to detect than a missing package. Geospatial libraries evolve rapidly, and if someone runs your code with a newer version of `geopandas` or `rasterio`, your functions might break entirely or silently return different spatial results.

For example, a few years ago, the underlying geometry engine for Python (`shapely`) underwent a massive upgrade to version 2.0. Operations that used to run fine suddenly threw errors. 

Another classic breakage involves Coordinate Reference Systems. In older versions of `geopandas`, it was common to define a CRS using a dictionary format:
```python
# Worked in geopandas < 0.9
my_gdf.to_crs(crs={'+init': 'epsg:2056'})
```
In modern versions, this exact line of code throws a fatal error. The library now strictly requires a string:
```python
# Required in modern geopandas
my_gdf.to_crs("EPSG:2056")
```

If your code relies on the older syntax and a collaborator runs it in a modern environment, the pipeline crashes. Conversely, if an underlying algorithm in a package like `rasterio` changes how it handles `NoData` pixels, your raster math could silently produce completely different results without ever showing an error.

```{admonition} The most dangerous failure is silent drift
:class: caution

A changed package version may not always crash the notebook. Sometimes it simply changes the mathematical behavior or the spatial output, which is much harder to notice than a clean error message.
```

### How to record and pin dependencies

To guarantee that your code behaves exactly the same way everywhere, you must create a simple text file that lists every library your project needs. More importantly, you must **pin** the versions.

This environment definition is fragile:
```text
geopandas
rasterio
xarray
```
It tells the reader *which* packages are needed, but not which versions were actually known to work. Conda or pip will just install whatever the newest version happens to be today.

Instead, you should record the exact versions you used. There are two common formats for this.

**1. The requirements.txt file (pip)**
If you use standard Python and `pip`, the standard way to record dependencies is a `requirements.txt` file using the `==` operator:
```text
geopandas==1.0.1
rasterio==1.3.10
xarray==2025.1.0
matplotlib==3.8.2
```
A collaborator can instantly install this exact list by running `pip install -r requirements.txt`.

**2. The environment.yml file (conda)**
In spatial data science, `conda` is heavily preferred because it seamlessly handles the complex, non-Python C++ system libraries (like GDAL and PROJ) that spatial packages rely on. A `conda` environment is recorded using an `environment.yml` file:
```yaml
name: sds210_project
channels:
  - conda-forge
dependencies:
  - python=3.11
  - geopandas=1.0.*
  - rasterio=1.3.*
  - xarray
  - rioxarray
```
A collaborator can recreate this isolated room on their machine by running `conda env create -f environment.yml`.

```{admonition} Flexible vs. Strict versions
:class: tip

Notice the `*` in `geopandas=1.0.*`. This allows minor bug fixes to be installed but prevents major updates (like version 2.0) that might break your code. For absolute, 100% strict reproducibility (often required for academic publication), you would lock down the exact build versions (e.g., `1.0.1`).
```

### The balance between strict and practical

For enterprise-level data engineering, environments are locked down to the exact hash of every tiny sub-dependency. For student projects, that level of engineering is overkill. The goal is reasonable reproducibility, not perfection. 

For your SDS210 projects, a practical balance means:
* recording all the main libraries you imported
* including their major versions
* avoiding reliance on undeclared packages installed somewhere in the background

---

## 4. Lightweight strategies for student projects

In professional data engineering, reproducible environments often involve Docker containers and automated continuous integration pipelines. For a student project or an introductory spatial analysis, that level of infrastructure is not needed. What you need is a realistic, lightweight standard that is easy to follow.

### A practical minimum for SDS210

Most student projects do not need dozens of packages. They often use a manageable combination of tools like `geopandas`, `rasterio`, `matplotlib`, `xarray`, and `rioxarray`. This means your environment can stay relatively small and understandable. 

To practice good environmental hygiene, follow this strategy for your course projects:

1. **Don't use the base environment.** Before starting a new project, create a fresh, isolated conda environment (e.g., `conda create -n sds210-project python=3.11`).
2. **Install only what you need.** Activate your environment and install the packages you need for your project.
3. **Export it.** Once your code is working, [export](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#working-with-conda-environments) your `environment.yml` or `requirements.txt` file listing the core packages and their major versions.
4. **Ship it with the code.** Place the environment file in the root folder of your project repository, right next to your notebooks.
5. **Document the setup.** Mention the environment briefly in your `README.md` file, providing the single command needed to recreate it.
6. **Verify the pipeline.** Restart your kernel and verify one last time that your notebook runs completely from top to bottom in this explicit environment.

### Why this is enough

This lightweight workflow takes only a few minutes, but it successfully moves your project towards *deliberate* reproducibility. A reproducible environment does not need to be complicated. It just needs to be explicit.

Reproducibility is a spectrum. By writing readable code (Chapter 1), organizing your files logically (Chapter 2), coding defensively against spatial errors (Chapter 3), and documenting your environment (Chapter 4), you transition from writing temporary scripts to producing robust scientific projects.

---

## 5. Exercise (check)

Below is a short import block from a hypothetical geospatial notebook. 

### Task

Use the import block to think about the environment the project depends on.

1. Identify the main Python dependencies. *(Hint: Is every imported module an external package?)*
2. Decide whether `requirements.txt` (pip) or `environment.yml` (conda) would be a safer choice for this specific stack.
3. Write the terminal command you would use to automatically export this environment to a file, assuming your active environment is named `sds210-project`. 
4. Draft two short README lines explaining how a collaborator can recreate the environment from your exported file.

### Import block

```{code-cell} python
import geopandas as gpd
import rasterio
import xarray as xr
import rioxarray
import matplotlib.pyplot as plt
from pathlib import Path

```

### Your workspace

Create your response here:

```bash
# Your export command here...

```

```text
# Your README snippet here:
This project was developed with ...
To recreate the environment, run ...

```

````{admonition} Sample solution
:class: dropdown

**1 & 2. Dependencies and format**
Because this project relies heavily on `geopandas` and `rasterio` (which require complex C++ libraries like GDAL and PROJ), an `environment.yml` file using Conda is the much safer choice. Notice that `pathlib` is **not** an external dependency; it is built into Python!

**3. The export command**
Instead of writing the file from scratch, you should export your active, working environment using the terminal:
```bash
conda env export --name sds210-project > environment.yml
```
*(Pro-tip: A raw export often includes highly specific operating system build hashes. It is a good best practice to open the resulting `environment.yml` file and clean it up to look like the minimal, cross-platform examples shown earlier in this chapter!)*

**4. README.md snippet**
```text
This project was developed with Python 3.11. 
To instantly recreate the exact software environment, run the following command in your terminal:

conda env create --name sds210-project-copy --file environment.yml
```

```{admonition} Reflection
:class: note

Look back at the import block. Which package would you trust *least* to "just work" on another machine a year from now if it were not explicitly recorded with a version number? Why?

```

````

---

## 6. Summary



