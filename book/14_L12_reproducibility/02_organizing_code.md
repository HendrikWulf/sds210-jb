---
title: Organizing code
site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Moving from one giant notebook to structured spatial workflows
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/14_L12_reproducibility/02_organizing_code.ipynb)

---

```{admonition} Big idea
:class: tip

As spatial analysis grows, structure matters as much as {term}`syntax <Syntax>`. Well-organized code is easier to understand, easier to {term}`debug <Debugging>`, and much easier to rerun on another machine or with another dataset.
```

```{admonition} Chapter Relevance
:class: dropdown

**Project Relevance:** ★★★ (Essential for fulfilling the "Repository Organization" assessment criteria in projects 1, 2, 3, and 4.)  
**Foundation:** ★★★ (The critical shift from prototyping in a single giant notebook to building structured, professional data science pipelines.)  

**Time to Read:** 15 minutes  
**In a nutshell:** Transition from messy notebooks to structured spatial workflows by using robust relative paths, modular logic, and standardized project directories.  
**Skip this if:** You already rigidly separate your raw data, processed data, and notebooks, and strictly use `pathlib` for all file I/O operations.

```

In the previous chapter, you focused on readable code at the scale of the line and the {term}`cell <Code cell>`. This chapter moves one level up: **workflow structure**.

{term}`Jupyter Notebooks <Notebook>` are excellent for exploration, visualization, and early spatial analysis. But as projects grow, one notebook can become difficult to manage. Imports, file paths, cleaning steps, {term}`reprojections <Map reprojection>`, plots, and exports accumulate until the workflow becomes hard to follow and even harder to rerun reliably.

This chapter shows how to move beyond the giant notebook. You will learn how to split repeated logic into {term}`functions <Function>`, move reusable code into {term}`modules <Module>`, organize files more clearly, and build spatial workflows that are easier to understand, reuse, and {term}`reproduce <Reproducibility>`.

```{admonition} A note on your course project
:class: note

While this chapter teaches you how to break a massive workflow into separate scripts and folders, **it is perfectly fine to use a single Jupyter Notebook from start to finish for your SDS210 course project.** The modular techniques introduced here (like `pathlib`, custom functions, and `.py` modules) are essential for large-scale, professional {term}`spatial data science <Spatial data science>`. We want you to understand how to build these pipelines, but you are not required to build complex multi-file code for your course submission. Apply these principles where they help clarify your work, but focus on writing clean, readable code first.
```

---

## 1. When a notebook becomes too long

Jupyter Notebooks are incredible tools for exploration, but a notebook has become too long when the scientific narrative is drowned out by the code. If your reader (or your future self) has to scroll past 500 lines of complex spatial data cleaning just to see a single map, the structure is actively hindering communication.

In spatial data science, workflows naturally expand. A seemingly simple task often follows a familiar pattern:

1. load multiple vector and {term}`raster <Raster data model>` files
2. project them into a common {term}`CRS <Coordinate Reference System>`
3. clip, mask, or clean the data
4. compute spatial summaries (like extracting elevation values)
5. plot the result
6. export the final table or figure

None of these tasks are wrong. The problem appears when they are all mixed together without clear structure. A small error in an early preprocessing step—such as a wrong CRS assumption—can silently propagate through the rest of the analysis.

### The trap of hidden states and manual fixes

Long, disorganized notebooks encourage bad habits, such as relying on {term}`hidden states <Hidden state>` ({term}`variables <Variable>` stored in memory from a cell you ran, then deleted 20 minutes ago) and manual interventions.

A common symptom of a disorganized workflow is the temptation to "fix" raw data outside of Python. Imagine you download a {term}`CSV <Comma-separated values>` of Swiss weather stations and notice some coordinates are missing. It is very tempting to open the file in Excel, manually delete the bad rows, save it, and then load it into your notebook.

**Avoid manual data edits** Manually editing raw data likely breaks your workflow. When a colleague tries to run your notebook on the original dataset, it might crash. When the agency publishes an updated dataset next month, you will have to remember exactly which rows you manually deleted.

Each step, from filtering out missing coordinates to renaming columns, should be performed programmatically in your code. Raw data should best be treated as read-only.

```{admonition} Structure is part of correctness
:class: important

Well-organized code is not only nicer to read; it makes mistakes easier to detect. In spatial analysis, a clear structure prevents subtle errors such as broken file paths, mixed coordinate systems, or the use of stale intermediate outputs.
```

---

## 2. Robust file paths with `pathlib`

Before you can break up a giant notebook and organize your code into separate files, you should ensure your {term}`script <Script>` knows how to find your data. One of the most common causes of fragile code is poor path handling. How you write file paths determines whether your code is portable or entirely brittle.

### The problem with absolute paths

An {term}`absolute path <Absolute path>` points to a specific location on a specific hard drive. It might look like this:

```{code-cell} python
# This will crash on any computer except yours
stations_gdf = gpd.read_file("C:/Users/name/Documents/SDS210/data/raw/stations_epsg2056.shp")
```

This path is not portable. It will break as soon as:

* you share the code with a project partner
* you move the project folder to a new location
* the operating system changes

### Use relative paths instead

{term}`Relative paths <Relative path>` are much safer because they are anchored to the project folder itself, rather than your personal machine.

While you could write a relative path as a simple {term}`string <String>` (e.g., `"../data/raw/stations.shp"`), modern Python provides a much better tool: the `pathlib` module. `pathlib` is the best practice because it automatically handles the different slash directions (`\` vs `/`) required by Windows, macOS, and Linux.

### A geospatial example

Here is how you use `pathlib` to safely navigate a standard project structure, assuming your current notebook is inside a `notebooks/` folder:

```{code-cell} python
from pathlib import Path
import geopandas as gpd

# 1. Define the root data directory relative to this notebook (go up one level)
data_dir = Path("../data")

# 2. Build explicit paths to your raw and processed folders using the / operator
raw_dir = data_dir / "raw"
processed_dir = data_dir / "processed"

# 3. Create the path to the specific file
vector_path = raw_dir / "buildings_epsg2056.gpkg"

# 4. Load the data safely
buildings_gdf = gpd.read_file(vector_path)
```

By using `Path` and the `/` {term}`operator <Operator>`, your code becomes easy to read and adapt. If you need to save an output later, you can simply write `buildings_gdf.to_file(processed_dir / "clean_buildings.gpkg")`.

```{admonition} Portability starts with paths
:class: important

If your code only works on your own laptop because every file path points to your personal Desktop or Downloads folder, the workflow is not reproducible.
```

---

## 3. Splitting logic into functions

Once your paths are robust, the next major step toward better organization is moving repeated or conceptually distinct logic into **functions**.

Functions help clean up giant notebooks because they:

* reduce repetitive typing
* make analytical steps easier to name (clarifying your intent)
* isolate complex logic for easier debugging
* allow you to reuse the exact same task elsewhere safely

### A repeated spatial task: The copy-paste trap

Imagine you need to buffer three different {term}`GeoDataFrames <GeoDataFrame>` (stations, rivers, and roads) to perform an intersection. Without a function, you might just copy and paste the same logic:

**The messy approach (copy-pasting):**

```{code-cell} python
# Buffer stations by 500m
stations_gdf["geometry"] = stations_gdf.geometry.buffer(500)
stations_gdf = stations_gdf.to_crs("EPSG:2056")

# Buffer rivers by 50m
rivers_gdf["geometry"] = rivers_gdf.geometry.buffer(50)
rivers_gdf = rivers_gdf.to_crs("EPSG:2056")

# Buffer roads by 10m
roads_gdf["geometry"] = roads_gdf.geometry.buffer(10)
roads_gdf = roads_gdf.to_crs("EPSG:2056")
```

Did you spot the spatial bug? In the code above, we accidentally applied a metric buffer (e.g., 500 m) *before* projecting the data into a metric coordinate system (EPSG:2056). To fix this error, you now have to rewrite the logic in three different places.

### The modular approach

By turning this task into a function, we fix the bug in a single place and give the operation a clear, descriptive name:

```{code-cell} python
def project_and_buffer(gdf, buffer_distance_m, target_crs="EPSG:2056"):
    """Reprojects a GeoDataFrame to a metric CRS and applies a buffer."""
    # Fix: Reproject FIRST, then buffer!
    projected_gdf = gdf.to_crs(target_crs).copy()
    projected_gdf["geometry"] = projected_gdf.geometry.buffer(buffer_distance_m)
    return projected_gdf

# Applying the safe, reusable function
stations_buffered = project_and_buffer(stations_gdf, 500)
rivers_buffered = project_and_buffer(rivers_gdf, 50)
roads_buffered = project_and_buffer(roads_gdf, 10)
```

Now, your notebook cells become much shorter, your analytical steps read like a clear recipe, and your spatial logic is protected from copy-paste errors.

```{admonition} A practical rule
:class: tip

If you find yourself copying and pasting the exact same code block more than once, it is usually time to turn it into a function.
```

#### Concept Check: Where Should the Buffer Happen?

You have three point layers in WGS84 coordinates (`EPSG:4326`) and you need a 500 m buffer around each point. Which workflow is safest?

A. Buffer first, then reproject, because the buffer distance will be converted later.

B. Reproject first to a metric CRS, then buffer using meters.

C. Keep the repeated buffer code in three separate cells so each layer can be inspected independently.

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
A 500 m buffer only makes sense after the data are in a metric coordinate system, so reprojection must happen before buffering. A applies metric logic to degree-based coordinates, while C repeats the same risk in multiple places instead of fixing the logic once in a reusable function.

```

---

## 4. A standard project layout

A good project layout makes your code easier to navigate and your workflows easier to rerun. It reduces cognitive load; when a reader sees a folder named `data/raw/`, they instantly know what kind of files belong there before reading a single line of code.

As established in the [project guidelines](https://hendrikwulf.github.io/sds210-jb/book/projects/repository/#id-2-recommended-repository-structure), a professional, easy-to-follow {term}`repository <Repository>` explicitly separates your data, notebooks, and scripts:

```text
my-spatial-project/
├── README.md               # The manual for your project
├── .gitignore              # List of files that shouldn't sync
├── environment.yml         # Required Python packages
├── data/                   # Raw and processed datasets
│   ├── raw/
│   └── processed/
├── notebooks/              # Narrative Jupyter Notebooks
│   ├── 01_exploration.ipynb
│   └── 02_analysis.ipynb
├── outputs/                # Exported maps, figures, and charts
└── src/                    # Custom Python modules (.py scripts)
    └── spatial_utils.py
```

<!-- markdownlint-disable MD033-->
<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L12_ch02_01_workflow_organizer/"
    width="100%" 
    height="600px" 
    frameborder="0" 
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Spatial Workflow Organizer.</b><br>
    Toggle between a giant notebook and a structured project, then click stages such as raw data, notebooks, modules, processed outputs, and orchestration to see where each part belongs in a reproducible spatial workflow. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L12_ch02_01_workflow_organizer/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

### Keeping raw data raw

Notice that the `data/` directory is split into `raw/` and `processed/`. This enforces one of the strongest organizational habits in scientific coding: **treating raw data as untouched input.**

A dangerous (but common) pattern is to download a spatial dataset, open it manually in QGIS or Excel, delete some invalid rows by hand, save over the original file, and *then* load it into Python. This creates invisible, undocumented preprocessing. Another person cannot rerun your workflow, and you will likely forget what you changed two weeks later.

Instead, your workflow should look like this:

* Keep the original, untouched data in `data/raw/`.
* Do all renaming, projecting, and filtering programmatically in Python.
* Save the cleaned outputs to `data/processed/`.

```{code-cell} python
import geopandas as gpd
from pathlib import Path

# 1. Read from raw
raw_path = Path("../data/raw/stations.gpkg")
stations_gdf = gpd.read_file(raw_path)

# 2. Transform programmatically
stations_gdf = stations_gdf.rename(columns={"StationID": "station_id"})
stations_gdf = stations_gdf.to_crs("EPSG:2056")

# 3. Write to processed
processed_path = Path("../data/processed/stations_cleaned.gpkg")
# stations_gdf.to_file(processed_path)
```

Now the transformation is visible, repeatable, and easily modifiable.

```{admonition} Reproducibility starts before the analysis
:class: warning

If your preprocessing happens manually outside the code (like clicking around in a GUI), your workflow is already less reproducible, even if the later analysis is beautifully written.
```

---

## 5. Moving reusable code into modules

With a clean folder structure in place, we can finally solve the "scrolling problem."

Functions improve organization inside a single notebook, but if you have 15 different helper functions taking up the first 300 lines of your file, your notebook is still cluttered. A notebook is strongest when it focuses on the scientific narrative; it is weaker when it acts as a giant container for utility code.

The solution is to move these complex, reusable functions into an external Python module (a `.py` script) inside your `src/` folder. This separates the "heavy lifting" from the storytelling.

### Creating and importing your module

Create a plain text file named `spatial_utils.py` inside your `src/` folder and move your custom function definitions into it:

**Inside `src/spatial_utils.py`:**

```{code-cell} python
import geopandas as gpd

def prepare_buffers(gdf, buffer_distance_m, target_crs="EPSG:2056"):
    """Reprojects a GeoDataFrame and applies a metric buffer."""
    projected_gdf = gdf.to_crs(target_crs).copy()
    projected_gdf["geometry"] = projected_gdf.geometry.buffer(buffer_distance_m)
    return projected_gdf
```

Now, inside your Jupyter Notebook, you can import your custom tool exactly like you import {term}`standard libraries <Standard library>`. *(Note: Because your notebook is inside the `notebooks/` folder, you must temporarily append the parent directory to your system path so Python can "see" the `src/` folder.)*

**Inside `notebooks/01_exploration.ipynb`:**

```{code-cell} python
import sys
sys.path.append("..")  # Point Python to the main project folder

import geopandas as gpd
from src.spatial_utils import prepare_buffers

# Load data safely using relative paths
stations_gdf = gpd.read_file("../data/raw/stations.shp")

# Use your custom tool
stations_buffered = prepare_buffers(stations_gdf, 500)
```

### Sharing code across multiple notebooks

Modules become powerful when your analysis spans multiple notebooks.

Imagine a Landsat workflow spread across an entire project:

* `01_cloud_masking.ipynb`
* `02_ndsi_calculation.ipynb`
* `03_summary_plots.ipynb`

If all three notebooks need the exact same helper function to normalize raster bands or clip arrays to a bounding box, you should never copy and paste that function into each notebook. Place it in `src/raster_utils.py`. If you ever need to fix a bug in the clipping math, you update the `.py` script once, and all three notebooks instantly benefit from the fix.

```{admonition} Rule of thumb
:class: important

If a function is useful in more than one notebook, it is a strong candidate for a standalone Python module.
```

---

## 6. Focus on the narrative

This chapter is not an argument against Jupyter Notebooks. It is an argument for using notebooks for what they do best.

**Notebooks are excellent for:**

* exploration and visual inspection
* combining text, code, maps, and scientific interpretation
* teaching and guided analysis

**Notebooks are less good as:**

* giant containers for all reusable logic
* environments with hidden dependency chains based on execution order
* places where long utility code competes with the analytical story

By moving data cleaning logic and complex spatial functions into external `.py` modules, your Jupyter Notebook is freed up to act as a **narrative layer**. A mature spatial data science notebook should read like a scientific paper.

* **{term}`Markdown cells <Markdown cell>`** should explain the *why*: the research question, the assumptions, and the interpretation of the results.
* **Code cells** should be short and focused on the *what*: loading data, applying high-level functions, and generating visualizations.

---

### Separating workflow stages

A common source of confusion in student projects is that loading, cleaning, analysis, and plotting are constantly mixed together in giant, monolithic cells. If a single cell loads a shapefile, drops missing values, reprojects it, intersects it with a bounding box, and plots a map all at once, you have mixed your concerns.

A stronger workflow separates these stages clearly into short, sequential steps:

1. **Input and loading**
2. **Preparation and cleaning**
3. **Analysis**
4. **Visualization**
5. **Export**

---

### A clean geospatial example

Suppose we want to attach elevation values from a raster DEM to a set of station points. Instead of one massive cell, a narrative-driven notebook breaks this into logical chapters.

#### 1. Input and loading

Use robust relative paths to bring the data into the environment.

```{code-cell} python
from pathlib import Path
import geopandas as gpd

data_dir = Path("../data")

stations_path = data_dir / "raw" / "stations.shp"
dem_path = data_dir / "raw" / "swiss_dem_10m.tif"

stations_gdf = gpd.read_file(stations_path)
```

#### 2. Preparation and cleaning

Apply basic standardizations, like ensuring coordinate systems match.

```{code-cell} python
TARGET_CRS = "EPSG:2056"
stations_gdf = stations_gdf.to_crs(TARGET_CRS)
```

#### 3. Analysis

This is where you leverage the custom modules you built in Section 4. The notebook stays clean because the complex array math is hidden inside the imported function.

```{code-cell} python
from src.raster_utils import sample_raster_at_points

# The heavy lifting is abstracted away
stations_gdf["elevation_m"] = sample_raster_at_points(stations_gdf, dem_path)
```

#### 4. Visualization

Generate maps and charts to visually verify the results and communicate findings.

```{code-cell} python
import matplotlib.pyplot as plt

stations_gdf.plot(
    column="elevation_m", 
    cmap="viridis", 
    legend=True,
    markersize=50
)
plt.title("Station Elevations (m)")
```

#### 5. Export

Save the finalized, clean dataset to the `processed/` folder so it can be used in other notebooks or shared with colleagues.

```{code-cell} python
output_path = data_dir / "processed" / "stations_with_elevation.gpkg"
stations_gdf.to_file(output_path, driver="GPKG")
```

Even when these individual steps are short, explicitly separating them clarifies exactly what the notebook is doing at any given moment.

```{admonition} Think of the notebook as a narrative layer
:class: note

A strong spatial notebook emphasizes exploration, interpretation, and communication. It should make it easy for a reader to answer five questions:  
1. What data came in?  
2. What changed?  
3. What was analyzed?  
4. What was visualized?  
5. What was written out?
```

---

## 7. Advanced: Orchestrating the workflow

Once you have separated your code into modules and organized your folders, you might wonder: *How do I run the whole project from start to finish?*

In a fully modular setup, you do not want to open five different notebooks and click "Run All" in a specific order. Instead, advanced spatial workflows use a central "main" script to orchestrate the execution.

Because separate notebooks do not naturally share memory (RAM), the main function manages the flow of data by reading and writing intermediate files.

**The Data Flow:**

1. `01_ingest.ipynb` runs ➔ Writes `stations_cleaned.gpkg` to `data/processed/`
2. `02_analysis.ipynb` runs ➔ Reads the GeoPackage, attaches DEM data, and writes a new output.

### Execution with Papermill

In professional data science, tools like `papermill` are used to execute notebooks programmatically. Papermill allows your main script to treat Jupyter Notebooks as if they were functions, passing {term}`parameters <Parameter>` (like dates or file paths) into them and saving the executed output.

A simple orchestrator script (`main.py`) sitting in your root directory might look like this:

```{code-cell} python
import papermill as pm
from pathlib import Path

def run_spatial_pipeline(study_area_name):
    print(f"Starting pipeline for {study_area_name}...")
    
    # Step 1: Clean the raw data
    pm.execute_notebook(
        input_path='notebooks/01_preparation.ipynb',
        output_path='outputs/01_preparation_executed.ipynb',
        parameters={'study_area': study_area_name}
    )
    
    # Step 2: Run the DEM analysis
    pm.execute_notebook(
        input_path='notebooks/02_dem_analysis.ipynb',
        output_path='outputs/02_dem_analysis_executed.ipynb',
        parameters={'study_area': study_area_name}
    )
    
    print("Pipeline complete!")

# This standard Python idiom ensures the pipeline only runs if you execute 
# this specific file directly (e.g., by running `python main.py` in the terminal). 
# It prevents the code from running automatically if you simply import a 
# function from this file into another script or notebook.
if __name__ == "__main__":
    run_spatial_pipeline('swiss_alps')
```

### Why orchestrate?

Orchestration ensures that your entire workflow—from raw data to final map—can be reproduced with a single command. It eliminates the risk of human error, such as forgetting to run step 2 before running step 3.

While you may not need `papermill` for your first course project, understanding this architecture prepares you for building automated spatial pipelines in the real world.

---

## 8. Summary

Organizing your code is an act of empathy for your collaborators and your future self. A well-structured project guarantees that your analysis can be understood, debugged, and rerun months later on a completely different computer without crashing.

**Key Takeaways:**

* **Never edit raw data manually:** Treat raw data as read-only. All spatial filtering and cleaning must happen programmatically in Python.
* **Use robust relative paths:** Always use `pathlib` instead of absolute paths to ensure your scripts can locate data regardless of the operating system.
* **Stop copy-pasting:** Move repetitive logic into functions to clarify your intent and prevent subtle spatial bugs, such as buffering before reprojecting.
* **Adopt a standard project layout:** Explicitly separate your raw data, processed data, notebooks, and scripts into distinct, predictable folders.
* **Extract utility code into modules:** Store complex, reusable spatial functions in external `.py` scripts (like `spatial_utils.py`) to reduce notebook clutter.
* **Let notebooks tell the story:** Keep your notebook cells short and explicitly separate your workflow stages (Input ➔ Prep ➔ Analysis ➔ Viz ➔ Export).

In the next chapter, we will tie all of these best practices together by exploring full project reproducibility, {term}`version control <Version control>`, and {term}`virtual environment <Virtual environment>` management.
