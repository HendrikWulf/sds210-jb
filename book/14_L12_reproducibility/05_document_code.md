---
title: Documenting code

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Making spatial projects understandable, not just runnable
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/14_L12_best-practices/05_documentation_and_communication.ipynb)

---

```{admonition} Big idea
:class: tip

A {term}`reproducible project <Reproducibility>` explains itself clearly enough that someone else can follow the logic, understand the assumptions, and rerun the workflow without guesswork. Code dictates *what* happens, but documentation explains *why* it happens.
```

```{admonition} Chapter Relevance
:class: dropdown

**Project Relevance:** ★★★ (A strict bottleneck; you must supply a clear `README.md` and well-narrated notebooks to pass the "Documentation" criteria for projects 1, 2, 3, and 4.)  
**Foundation:** ★★☆ (Crucial for scientific communication and ensuring your computational workflows are genuinely interpretable.)  

**Time to Read:** 10 minutes  
**In a nutshell:** Make your spatial projects understandable to others by writing strong READMEs, descriptive docstrings, and self-explanatory scientific figures.  
**Skip this if:** You already routinely write comprehensive `README.md` files, document custom tools with type hints, and narrate your Jupyter notebooks heavily using Markdown.

```

In the previous chapters, you learned how to write cleaner Python, organize code beyond one giant notebook, make workflows more robust, and record {term}`software environments <Virtual environment>`. These are all essential technical parts of reproducibility. But a project can still fail as a scientific communication artifact even if all of those pieces are perfectly in place.

Why? Because reproducibility depends on more than just file availability. It fundamentally depends on **interpretability**.

A {term}`repository <Repository>` may contain the code, the data, and the environment file, yet still leave the reader asking basic questions:

* What does this project actually do?
* What do the input datasets represent?
* Why was this specific {term}`CRS <Coordinate Reference System>` or buffer distance chosen?
* What assumptions shaped the spatial analysis?
* What does this final map actually show?

Documentation answers those questions.

Often viewed as bureaucratic busywork left for the very end of a project, documentation is actually a core component of the scientific workflow.

In this chapter, you will learn the hierarchy of documentation in a {term}`spatial data science <Spatial data science>` project. We will move from the macro level down to the micro level, covering how to:

* write project `README.md` files that actually help
* use {term}`Jupyter notebooks <Notebook>` as narrative documents rather than raw code dumps
* document reusable spatial {term}`functions <Function>` with {term}`docstrings <Docstring>`
* write clear inline {term}`comments <Comment>` that explain the *why*, not the *what*
* improve figure titles and captions for scientific outputs

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L12_ch05_01_documentation_hierarchy/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Documentation Hierarchy.</b><br>
    Select documentation layers such as README, notebook Markdown, inline comments, docstrings, and figure captions to compare weak and strong examples and see which reader question each layer answers. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L12_ch05_01_documentation_hierarchy/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

---

## 1. README files that actually help

The {term}`README <README>` file is the front door to your project. It is the first thing anyone sees when they open your repository on {term}`GitHub`, GitLab, or a shared folder. In a well-organized project, it answers the most important questions before the reader even opens a notebook.

A weak README creates uncertainty. A strong README creates orientation.

### A weak README

A weak README assumes the reader already knows what the project is about. It forces the user to dig into the code to understand the goal.

```markdown
# SDS210 final project

This notebook analyzes spatial data. Run `workflow.ipynb`. Data is in the data folder.
```

This tells the reader almost nothing. It does not explain the scientific topic, the study area, the data sources, the outputs, or the required software environment.

### A stronger README

A strong README acts as a standalone guide. It explains the scientific objective, the required data, and the computational environment needed to run the code.

**A strong geospatial README:**

```markdown
# Urban Heat in Zurich

This project analyzes long-term urban heat patterns in Zurich using Landsat-derived land surface temperature and vegetation indicators.

## Objective
The goal of this project is to extract a 10-year time series of summer surface temperatures to identify neighborhoods with the most intense urban heat island effects.

## Data Sources
* **Landsat 8 LST:** Annual summer summaries (30m resolution).
* **City Boundaries:** Vector neighborhood layers provided by the City of Zurich.
* *Note: Due to file size constraints, raw `.tif` files are not tracked in this repository. Download them via this Earth Engine script (insert link) and place them in `data/raw/`.*

## Reproducing the Environment
This project requires a specific spatial software stack. To recreate the environment:
1. Ensure you have Conda installed.
2. Run: `conda env create -f environment.yml`
3. Activate: `conda activate zurich-heat-env`

## Usage
Execute the Jupyter Notebook `01_urban_heat_analysis.ipynb` from top to bottom. Trend maps will be exported to `outputs/maps/`.
```

This version removes the guesswork. It immediately gives the reader a clear mental model of the project and explicitly ties into the environment management practices you learned in the previous chapter.

### What a useful README should answer

A practical student project README should usually cover:

* **What is the project about?** The scientific question or objective.
* **What data are used?** And crucially, where to get them if they are too large to share.
* **What are the main workflow steps?** Which scripts to run, and in what order.
* **What outputs are produced?** Maps, tables, or interactive plots.
* **How can the environment be recreated?** Terminal commands.

That does not require pages of text. Clarity matters much more than length.

### Why a geospatial framing helps

Geospatial projects benefit especially from a good README because spatial workflows involve unique dependencies. Your README should explain how these pieces fit together, such as:

* specific study areas and coordinate reference systems
* source datasets from different providers and data access instructions
* intermediate spatial transformations
* multiple output types like {term}`GeoTIFFs <GeoTIFF>`, Shapefiles, or PNG maps

```{admonition} A README reduces uncertainty
:class: tip

A good README lets the reader understand the project's purpose, requirements, and logic before opening a single line of Python.
```

---

## 2. Explain inputs, outputs & assumptions

A reproducible project explains what files it includes, where they came from, and why they matter.

This is especially important in geospatial analysis, where the exact same Python script can produce different results depending on the study area, the {term}`raster resolution <Spatial resolution>`, or the coordinate reference system. You should document these details at both the project level, in your README, and the code level, in your scripts.

### Documenting inputs and outputs

A reader should not have to guess what is inside your `data/` or `outputs/` folders. You should provide a brief "data dictionary" in your README or at the top of your main notebook.

**For inputs, a reader needs to know:**

* which datasets were used and where they came from
* what spatial and temporal extent they cover
* whether they are raw or pre-processed

```text
Input data:
- `stations.gpkg`: climate monitoring stations in Switzerland (raw)
- `dem_2m.tif`: digital elevation model at 2 m resolution (swissALTI3D)
- `cantons.gpkg`: administrative boundaries used for context mapping
```

**For outputs, a reader needs to know:**

* what was generated and what it represents
* where it is stored

```text
Outputs:
- `station_elevation.csv`: extracted elevation values at station points
- `elevation_map.png`: map of station points colored by extracted elevation
- `stations_with_dem.gpkg`: station layer enriched with elevation values
```

### Documenting macro-assumptions

Some of the most important documentation is not about files at all; it is about analytical choices. If an analytical threshold or projection choice shapes the final map, it deserves explicit documentation in your {term}`Markdown` text.

These macro-assumptions often include:

* the chosen working CRS, for example EPSG:2056
* minimum area filters, for example excluding buildings smaller than 100 m²
* temporal aggregation rules, for example defining "Summer" as June 1 to August 31
* cloud cover thresholds for satellite imagery

If you document these clearly in your README or notebook introduction, collaborators immediately understand the boundaries of your science.

### Documenting micro-assumptions: inline comments

While Markdown explains the broad strokes of the workflow, inline code comments (`#`) exist to explain specific, non-obvious programmatic decisions down at the code level.

The golden rule of code comments is: **Explain *why*, not *what*.** Python syntax already tells the reader *what* is happening. Comments should be reserved for explaining the scientific assumptions or the hidden logic behind the numbers, the {term}`magic numbers <Magic number>` we discussed in the Defensive Coding chapter.

**Bad comment: explains the syntax**

```python
# Buffer the points by 500
stations_buffered = stations.buffer(500)
```

The reader already knows it is buffering by 500. What they do not know is *why* 500 was chosen instead of 100 or 1000.

**Good comment: explains the assumption**

```python
# Buffer by 500m to account for maximum GPS drift in complex alpine terrain
stations_buffered = stations.buffer(500)
```

**Good comment: explains a data quirk**

```python
# Drop rows where elevation is -9999 (swisstopo's NoData value for this specific dataset)
clean_dem = raw_dem.where(raw_dem != -9999)
```

Use comments sparingly but strategically. If you find yourself writing a massive paragraph of comments to explain a complex block of code, it is often a sign that the code itself is too confusing and should be simplified or broken down into smaller, well-named functions.

```{admonition} Assumptions should be visible
:class: important

If a spatial threshold, a data quirk, or a projection choice matters for the scientific interpretation of the results, it must be documented. Hidden assumptions are the enemy of reproducibility.
```

---

## 3. Docstrings and type hints

Documentation exists at different levels of a project. As we have seen, your README explains the overall project, your notebook Markdown explains the workflow, and your inline comments explain specific line-by-line assumptions.

But what happens when you write custom, reusable functions, like the ones we built in the Defensive Coding chapter? For reusable code, Python provides two specific tools: {term}`type hints <Type hint>` and docstrings.

### Type hints add lightweight clarity

Modern Python allows you to use type hints directly in your function definitions. Type hints act as built-in, self-documenting code. Even without reading the full implementation, a collaborator instantly knows what the function expects and what it gives back.

```{code-cell} python
import geopandas as gpd

# The colon (:) defines the input type. The arrow (->) defines the output type.
def clip_to_bbox(gdf: gpd.GeoDataFrame, bbox: dict) -> gpd.GeoDataFrame:
    return gdf.cx[bbox["xmin"]:bbox["xmax"], bbox["ymin"]:bbox["ymax"]]
```

### Docstrings explain behavior

While type hints explain the {term}`data types <Data type>`, a docstring explains the *behavior*.

A docstring is a multi-line string, enclosed in `"""`, placed immediately inside the function definition. It is the standard Python way to specify what the function does, what the parameters mean, and what assumptions or errors might occur.

When you combine type hints with a clear docstring, your functions become easy for collaborators to use safely.

**A fully documented geospatial function:**

```{code-cell} python
def filter_high_elevation(gdf: gpd.GeoDataFrame, threshold_m: float) -> gpd.GeoDataFrame:
    """
    Filters a spatial dataset to retain only features above a certain elevation.
    
    Assumes the input GeoDataFrame contains a column named 'elevation_m'.
    
    Parameters
    ----------
    gdf : geopandas.GeoDataFrame
        The input spatial dataset containing point or polygon features.
    threshold_m : float
        The minimum elevation in meters. Features below this value are removed.
        
    Returns
    -------
    geopandas.GeoDataFrame
        A new GeoDataFrame containing only the high-elevation features.
        
    Raises
    ------
    KeyError
        If the required 'elevation_m' column is missing.
    """
    # Defensive check
    if "elevation_m" not in gdf.columns:
        raise KeyError("Input GeoDataFrame must contain an 'elevation_m' column.")
        
    return gdf[gdf["elevation_m"] >= threshold_m].copy()
```

### The payoff: built-in documentation

Why go through the trouble of formatting your docstring so formally? Because Python and modern code editors, like {term}`VS Code <Visual Studio Code>` or {term}`JupyterLab`, read these strings automatically.

If a collaborator imports your `filter_high_elevation` function in a different notebook, they can simply type `help(filter_high_elevation)`, or hover their mouse over the function name in their editor, and your docstring will appear. They never have to guess what data types to provide, what column names are required, or what the function will return.

```{admonition} Documentation has a hierarchy
:class: tip

* **READMEs** explain the project to a visitor.
* **Markdown** explains the workflow to a reader.
* **Comments** explain specific line logic to a reviewer.
* **Docstrings and type hints** explain reusable tools to a user.
```

#### Concept Check: Which Layer Gets the Explanation?

You are filtering buildings smaller than 100 m² because the source dataset includes many sheds and digitizing artifacts. Where should this assumption be documented?

A. Only in the README, because it is a project-level decision.

B. Near the filtering line as a why-comment, and also in the README or notebook if it shapes the final interpretation.

C. Only inside a docstring, because every explanation belongs in reusable functions.

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
The local filtering decision should be visible near the code line that applies it, especially because the number would otherwise be a magic number. If the threshold changes the scientific interpretation of the outputs, it should also be summarized at the project or notebook level; the docstring alone is too hidden and too function-specific.
```

---

## 4. Captions, figure titles, & provenance

Documentation is not only about code. It also applies to your scientific outputs.

The final step of most spatial workflows is communication via maps or plots. However, a map can be visually impressive and still communicate very little if the title is vague, the units are unclear, the data source is hidden, or the processing steps are never mentioned. In reproducible science, visual outputs must be self-explanatory.

### Weak and strong figure titles

A strong title tells the reader exactly what variable is shown, where it is shown, and over what time period it was summarized.

**Weak title:**

```text
Map
```

**Strong title:**

```text
Mean annual snow cover fraction in Switzerland, 2001–2024
```

### Captions should add meaning

A caption should not simply restate the title. It should explain what the figure shows, how to interpret it, and what macro-assumptions were made to produce it.

**Weak caption:**

```text
This figure shows the results.
```

**Strong caption:**

```text
Stations are colored by elevation values extracted from the DEM after reprojection to EPSG:2056. Higher elevation stations cluster in the Alpine regions.
```

Now the caption adds both provenance, such as reprojection and extraction, and interpretation, such as clustering.

### Provenance notes in code

For scientific outputs, it is crucial to note the source dataset and important parameters. If you add these details directly into your plotting code, every generated image carries its own context. If the map is saved as a `.png` and embedded in a report or a presentation, the scientific context travels with it.

When plotting in a notebook, ensure your figures contain descriptive titles, axis labels with units, and a small text addition noting where the data originated. For example, are the coordinates in degrees or meters?

```{code-cell} python
import matplotlib.pyplot as plt
import geopandas as gpd

# fig, ax = plt.subplots(figsize=(8, 6))
# rhone_rivers_gdf.plot(ax=ax)

# 1. Add a descriptive title
# ax.set_title("Major River Networks in the Rhone Catchment", fontsize=14)

# 2. Add axis labels with clear units/CRS
# ax.set_xlabel("Easting (CH1903+ / LV95)")
# ax.set_ylabel("Northing (CH1903+ / LV95)")

# 3. Add a provenance note to the bottom of the figure
# fig.text(0.15, 0.02, "Data: swisstopo TLM3D (2023)", fontsize=9, style='italic')

# plt.show()
```

```{admonition} Figures are part of the documentation
:class: note

A figure should explain not only what it looks like, but also what it represents and where it came from. A map without context is just a picture.
```

---

## 5. Telling the workflow story in notebooks

Jupyter Notebooks are powerful because they allow you to interleave code with text. However, a common mistake is treating a notebook like a pure Python script, using only code cells and ignoring Markdown.

A notebook is not just a place where code runs; it is a narrative document. The reader should be able to follow the scientific question, the data origins, the analysis steps, and the interpretation of the outputs just by scrolling. A notebook that begins immediately with imports and data loading forces the reader to reverse-engineer the purpose of the analysis.

### Start with context

Before the first code block, use Markdown to establish the geographical context and overall objective. Explain what the notebook does, why the analysis matters, what data are used, and what the reader should expect by the end.

```md
# Extracting Station Elevations

This notebook extracts elevation values from a 2m DEM at climate monitoring station locations in Switzerland. The goal is to compare station elevation patterns across regions and produce a cleaned, enriched output layer for the final temperature trend analysis.
```

That single paragraph makes the notebook much more approachable.

### Use Markdown to frame steps

Before executing a code block, use Markdown to outline the methodology and introduce the analytical role of the step.

**Poor narrative: pure Python script style**

```python
# Loading data and clipping it
import geopandas as gpd
study_area = gpd.read_file("catchment.gpkg")
rivers = gpd.read_file("rivers.shp")
clipped_rivers = rivers.clip(study_area)
```

**Strong narrative: notebook style**

*(In a Markdown cell)*

### Isolating the River Network

To analyze hydrological connectivity, we first need to restrict the national river network to our specific study area, the Rhone catchment. We will load both vector layers and perform a spatial clip.

*(In a Code cell)*

```{code-cell} python
import geopandas as gpd

catchment_gdf = gpd.read_file("../data/raw/rhone_catchment.gpkg")
national_rivers_gdf = gpd.read_file("../data/raw/swiss_rivers.shp")

rhone_rivers_gdf = national_rivers_gdf.clip(catchment_gdf)
```

This helps the notebook read like a guided scientific workflow rather than a raw execution log.

### Explain results after they appear

Documentation does not stop when the code finishes running. After you generate a figure, map, or summary table, add a brief Markdown cell to interpret the result.

```md
**Interpretation:** As shown in the map above, the highest elevation stations are densely concentrated in southern and eastern Switzerland. This matches the expected topographic pattern of the Alps and confirms that the raster point-extraction worked correctly.
```

That small paragraph turns the notebook from a technical transcript into a communicative, scientific document.

```{admonition} A good notebook has a reader in mind
:class: important

If someone unfamiliar with the project opens your notebook, they should be able to understand the purpose, follow the workflow, and interpret the outputs without constant guesswork.
```

---

## 6. Weak vs. strong documentation

It is useful to see the difference between weak and strong documentation side by side. The difference is not about making things look pretty; it is about making them scientifically interpretable.

### 1. The project entry: README

**Weak project entry:**

```text
# DEM analysis

This notebook uses some spatial data and creates outputs.
```

This tells the reader nothing about the science, the data, or the requirements.

**Strong project entry:**

```text
# Station Elevation Analysis in Switzerland

This project extracts elevation values from a 2m DEM at station locations across Switzerland. The workflow loads point and raster data, aligns them in a common CRS, performs raster extraction, and exports a cleaned point layer with elevation attributes.

## Input data
- `stations.gpkg`: point layer of monitoring stations
- `dem_2m.tif`: digital elevation model (swissALTI3D)

## Outputs
- `stations_with_elevation.gpkg`
- `station_elevation_map.png`

## Key assumptions
- Raster extraction is performed after reprojection to EPSG:2056
- Output values are reported in meters above sea level
```

### 2. Reusable functions: docstrings and type hints

**Weak function documentation:**

```{code-cell} python
def extract_values(points, raster):
    # Does some extraction
    return points
```

This may run, but the user has to guess the expected data types and what the function actually modifies.

**Strong function documentation:**

```{code-cell} python
import geopandas as gpd
from pathlib import Path

def extract_raster_values(points_gdf: gpd.GeoDataFrame, raster_path: Path) -> gpd.GeoDataFrame:
    """
    Extract raster values at point locations.

    Parameters
    ----------
    points_gdf : geopandas.GeoDataFrame
        Point layer in the exact same CRS as the raster.
    raster_path : pathlib.Path
        Path to the raster file.

    Returns
    -------
    geopandas.GeoDataFrame
        A copy of the input point layer with a new column containing extracted raster values.
    """
    # Extraction logic here...
    return points_gdf
```

### 3. Scientific outputs: figures and maps

**Weak figure communication:**

```text
Title: Results
Caption: This shows the final map.
```

**Strong figure communication:**

```text
Title: Elevation of monitoring stations in Switzerland (2024)
Caption: Station points are colored by DEM-derived elevation in meters after raster extraction in EPSG:2056. Higher values correctly cluster in the Alpine south and east.
Data Source: swisstopo (2024).
```

### The takeaway

In all three cases, the code underneath might be identical. But the **strong** examples treat the reader as a collaborator, while the **weak** examples treat the reader as a mind-reader. Good documentation is the bridge between code that merely runs and science that can be trusted.

---

## 7. Exercise

Below are poorly documented components from a hypothetical spatial analysis project. They technically work, but they force the reader to guess their purpose, inputs, and assumptions.

### Task

Improve the project's documentation at both the macro and micro levels.

**Part 1: The macro level: README and outputs**

1. Rewrite the weak README text so that it clearly explains the objective, data, and outputs.
2. Suggest a strong figure title and caption to replace the weak ones.

**Part 2: The micro level: functions and comments**

1. Add **type hints** to the parameters and the return value of the `clean_and_mask` function.
2. Write a standard **docstring** explaining what the function does, its parameters, and its return value.
3. Replace the weak code comments, which only explain the *what*, with strong comments that explain the *why*: the spatial assumptions.

### The weak documentation

**Weak README:**

```text
# SDS210 project

This project analyzes station data and raster data.
```

**Weak Figure Communication:**

```text
Title: Results
Caption: This shows the final map.
```

**Weak Helper Function:**

```{code-cell} python
import xarray as xr

# function to fix raster
def clean_and_mask(raster_data, mask_layer, threshold):
    # check threshold
    if threshold < 0:
        raise ValueError("Invalid threshold")
        
    # mask it
    cleaned = raster_data.where(mask_layer > 0)
    
    # apply threshold
    final = cleaned.where(cleaned > threshold)
    
    return final
```

### Your workspace

Draft your improved README, figure caption, and rewritten function below.

```{code-cell} python
import xarray as xr

# Rewrite the clean_and_mask function here
```

````{admonition} Sample solution
:class: dropdown

**1. Stronger README**

```text
# Station Elevation Analysis

This project extracts elevation values from a digital elevation model at climate station locations in Switzerland. The workflow aligns point and raster data, performs spatial extraction, and exports a cleaned station layer enriched with elevation attributes.

## Data & Outputs
- **Inputs:** `stations.gpkg` (points) and `dem_2m.tif` (swissALTI3D raster)
- **Outputs:** `stations_with_elevation.gpkg` and `station_elevation_map.png`
```

**2. Stronger Figure Communication**

```text
Title: Elevation of monitoring stations in Switzerland
Caption: Stations are colored by elevation values extracted from the DEM after reprojection to EPSG:2056. The spatial pattern highlights the dense concentration of high-elevation sites in the Alpine regions.
```

**3, 4, & 5. Stronger Function Documentation**

```{code-cell} python
import xarray as xr

def clean_and_mask(raster_data: xr.DataArray, mask_layer: xr.DataArray, threshold: float) -> xr.DataArray:
    """
    Applies a spatial mask and a minimum value threshold to a raster array.
    
    Parameters
    ----------
    raster_data : xarray.DataArray
        The continuous raster data to be processed (e.g., a DEM or NDVI array).
    mask_layer : xarray.DataArray
        A binary raster mask. Areas where mask_layer <= 0 will be dropped.
    threshold : float
        The minimum valid value for the raster_data. 
        
    Returns
    -------
    xarray.DataArray
        The cleaned and masked raster array.
    """
    if threshold < 0:
        raise ValueError("Threshold must be positive to ensure physically valid limits.")
        
    # Exclude areas outside the study region defined by the binary mask
    cleaned = raster_data.where(mask_layer > 0)
    
    # Remove physically impossible values (e.g., negative elevations or reflectances)
    final = cleaned.where(cleaned > threshold)
    
    return final
```
````

```{admonition} Reflection
:class: note

Which missing piece of documentation would have been the most frustrating for you as a new reader: the vague README, the missing docstring, the empty figure description, or the unhelpful code comments?
```

---

## 8. Summary

Documentation is not an optional extra added after the real analysis is done; it is a core component of the scientific workflow. A reproducible project must be not only runnable but also understandable.

**Key Takeaways:**

* **Start at the front door:** A strong `README.md` acts as a standalone guide, explaining the objectives, data sources, outputs, and environment setup before the reader even opens the code.
* **Explain the *why*, not the *what*:** Use inline comments to explain the spatial assumptions and underlying logic behind your code, not the Python syntax itself.
* **Document reusable tools:** Use type hints and docstrings so collaborators can easily understand the inputs, outputs, and behavior of your custom functions without having to read the implementation.
* **Make figures self-explanatory:** Scientific outputs need descriptive titles, clear units, meaningful captions, and provenance notes to ensure they can be trusted and interpreted correctly.
* **Narrate your notebooks:** Use {term}`Markdown cells <Markdown cell>` to guide the reader through the analytical story, providing geographical context before code and scientific interpretation after results.

Reproducibility depends on more than just code availability and environment files. It fundamentally depends on **interpretability**.

```{admonition} Outlook
:class: tip

At this point, you have seen the main pillars of good computational practice: readable code, organized workflows, robust defensive checks, reproducible environments, and clear documentation. The next step is to bring these ideas together into a complete, professional view of reproducible spatial data science projects.
```
