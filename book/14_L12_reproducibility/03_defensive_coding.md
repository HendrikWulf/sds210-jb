---
title: Defensive coding

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Writing geospatial code that checks assumptions and fails clearly
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/14_L12_best-practices/03_defensive_coding.ipynb)

---

```{admonition} Big idea
:class: tip

Reliable spatial code does not only perform the intended analysis. It also anticipates mistakes, checks assumptions, and fails clearly when something is wrong.
```

In this chapter, you will learn how to write code that is safer to rerun, easier to {term}`debug <Debugging>`, and less likely to fail silently. The goal is to make your code trustworthy.

A spatial workflow may look clean and still be fragile. Python may accept the code perfectly, yet the analysis can still be wrong. A vector overlay may run even though the layers use different coordinate systems. A {term}`raster <Raster data model>` extraction may return empty values because the points do not overlap the raster extent. A column name may differ slightly from what you expected, or a filter may silently remove every row.

These are not unusual edge cases. They are normal situations in real spatial analysis.

This mindset is called {term}`defensive coding <Defensive programming>`: writing code that does not trust its inputs blindly. It checks the assumptions that matter, makes them explicit, and stops early when the workflow is no longer valid. This is especially important in geospatial work, where even a simple analysis depends on many small truths: that the file exists, that the data load correctly, that the {term}`CRS <Coordinate Reference System>` is known and compatible, that layers overlap, and that intermediate results are not empty.

Well-organized code is easier to follow, but robust code goes one step further: it verifies that the workflow still makes sense before continuing.

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★★★ (Directly helps you catch common lab errors such as missing files, wrong CRS assumptions, and empty outputs.)  
**Project Relevance:** ★★★ (Protects your final project from silent spatial mistakes and makes your code discussion easier to defend.)  
**Foundation:** ★★★ (Builds core habits for robust, trustworthy, and {term}`reproducible <Reproducibility>` spatial workflows.)  

**Time to Read:** 24 minutes  
**In a nutshell:** This chapter teaches you how to make spatial workflows stop early with clear messages instead of silently producing invalid results.  
**Skip this if:** You already validate paths, parameters, CRS compatibility, spatial overlap, raster alignment, required columns, and empty outputs in your geospatial code.
```

---

## 1. Validation of inputs and file paths

A workflow becomes fragile when it assumes that the outside world—files, folders, and user inputs—is always perfectly formatted. The most common point of failure in any {term}`script <Script>` is loading the data. If a file is missing, moved, or corrupted, the entire pipeline stops.

A defensive programmer verifies that the data and inputs actually make sense before asking the computer to do heavy processing. This is known as **failing fast**: catching the error at the very beginning of the script, rather than letting it cause an obscure crash 100 lines deeper into your {term}`notebook <Notebook>`.

### Validating file paths

Using the `pathlib` module from the previous chapter, it is straightforward to validate file paths before running data-intensive {term}`functions <Function>`.

```{code-cell} python
from pathlib import Path
import geopandas as gpd

def load_spatial_data(filepath):
    """Safely loads spatial data after verifying the file exists."""
    data_path = Path(filepath)
    
    # Defensive check: Does the file exist, and is it actually a file?
    if not data_path.is_file():
        raise FileNotFoundError(f"Missing data! Could not find: {data_path.absolute()}")
        
    return gpd.read_file(data_path)

# stations_gdf = load_spatial_data("../data/raw/stations.shp")
```

### Validating user-supplied values

Defensive coding is not just for files; it is also for {term}`variables <Variable>`. If your workflow depends on user-defined {term}`parameters <Parameter>`, validate them immediately. Python's {term}`assert statement <Assertion>` is perfect for these quick, readable checks.

If a user defines a buffer distance, ensure it is actually a positive number:

```{code-cell} python
buffer_distance_m = 500

assert buffer_distance_m > 0, "Buffer distance must be a positive number."
```

If your script filters satellite imagery by a date range, ensure the timeline flows forward:

```{code-cell} python
start_year = 2015
end_year = 2020

assert start_year <= end_year, "start_year must be smaller than or equal to end_year."
```

### Validating bounding boxes

Geospatial structures like {term}`bounding boxes <Spatial extent>` are a classic source of subtle mistakes. If you accidentally flip the minimum and maximum coordinates, the bounding box might still travel through several processing steps before it produces an obviously empty map.

Validate the geometry before using it:

```{code-cell} python
# A rough bounding box for Switzerland (WGS84 degrees)
bbox = {
    "xmin": 7.0,
    "ymin": 46.8,
    "xmax": 8.8,
    "ymax": 47.6,
}

# Defensive checks to ensure the box is not inverted
assert bbox["xmin"] < bbox["xmax"], "Bounding box is invalid: xmin >= xmax."
assert bbox["ymin"] < bbox["ymax"], "Bounding box is invalid: ymin >= ymax."
```

```{admonition} Validate the outside world
:class: important

Files, paths, user inputs, and downloaded datasets are external to your code. They should be treated as highly suspicious until they pass your validation checks.
```

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L12_ch03_01_defensive_coding/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Defensive Coding Gatekeeper.</b><br>
    Select common geospatial failure modes such as missing files, CRS mismatch, no spatial overlap, or empty outputs to compare how a fragile workflow fails late while a defensive workflow stops early at the correct validation gate. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L12_ch03_01_defensive_coding/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

---

## 2. Checking assumptions early

A strong defensive habit is to check important assumptions as soon as possible, ideally right after loading the data. The longer a wrong assumption stays hidden, the more confusing the workflow becomes. By the time the final map looks strange, the real problem may have occurred 20 {term}`cells <Code cell>` earlier.

### Checking data immediately after loading

When you load a new dataset, you likely have assumptions about what it contains. You can use Python's built-in `assert` statement to declare these assumptions explicitly. If the condition is false, the notebook stops immediately and prints your custom error message.

For a vector dataset, you might expect it to have rows, a specific {term}`identifier <Identifier>`, a defined CRS, and a specific geometry type:

```{code-cell} python
stations_gdf = gpd.read_file(stations_path)

# 1. Is the dataset empty?
assert len(stations_gdf) > 0, "The stations layer is completely empty."

# 2. Does it have the columns we need?
assert "station_id" in stations_gdf.columns, "Missing required column: 'station_id'"

# 3. Is the CRS defined?
assert stations_gdf.crs is not None, "The stations layer has no CRS defined."

# 4. Are the geometries actually points?
valid_geom_types = {"Point", "MultiPoint"}
found_geom_types = set(stations_gdf.geometry.geom_type.unique())
assert found_geom_types.issubset(valid_geom_types), f"Expected points, but found: {found_geom_types}"
```

For a raster dataset, you might assume it is a single-band file with spatial reference:

```{code-cell} python
import rasterio

with rasterio.open(dem_path) as src:
    assert src.count == 1, f"Expected a single-band DEM, found {src.count} bands."
    assert src.crs is not None, "DEM raster has no CRS defined."
```

If the file accidentally contains polygons instead of points, or a 4-band aerial image instead of a 1-band DEM, the workflow will stop immediately instead of continuing under false pretenses.

### Enforcing assumptions inside functions

When you write custom, reusable functions (like the modules we built in the previous chapter), you cannot always control what data gets passed into them. You must protect these functions by validating inputs *before* doing the math.

While `assert` is great for quick checks inside your notebook script, professional Python modules usually use explicit `raise` statements (like `KeyError` or `ValueError`) to handle bad inputs inside functions.

If your code requires an `elevation_m` column to run a topographic calculation, check for it immediately:

```{code-cell} python
def calculate_lapse_rate(gdf):
    """Calculates temperature lapse rate based on elevation."""
    
    # Defensive check: Are the required columns present?
    required_cols = ["temperature_c", "elevation_m"]
    for col in required_cols:
        if col not in gdf.columns:
            raise KeyError(f"Input data is missing required column: '{col}'")
            
    # Proceed with calculation...
    return gdf["temperature_c"] / gdf["elevation_m"]
```

Another classic silent error is performing a {term}`spatial join <Spatial join>` or an intersection on datasets with mismatching projections. Protect your spatial functions by enforcing CRS alignment:

```{code-cell} python
def intersect_study_area(points_gdf, boundary_gdf):
    """Intersects points with a boundary, ensuring CRS compatibility."""
    
    # Defensive check: Do the projections match?
    if not points_gdf.crs.equals(boundary_gdf.crs):
        raise ValueError(
            f"CRS mismatch! Points: {points_gdf.crs.to_epsg()}, "
            f"Boundary: {boundary_gdf.crs.to_epsg()}"
        )
        
    return gpd.overlay(points_gdf, boundary_gdf, how="intersection")
```

```{admonition} Early checks save time
:class: tip

Do not wait until the final result looks wrong to discover that the input was already broken.
```

---

## 3. Checking spatial compatibility

Many geospatial errors are not programming errors in the ordinary sense. They are *compatibility* errors. The files load successfully, and the Python {term}`syntax <Syntax>` is perfect, but the data layers fundamentally disagree with each other.

Because Python will often try to execute the operation anyway (resulting in empty datasets or corrupted {term}`arrays <Array>`), checking spatial compatibility is the most domain-specific part of defensive coding.

### CRS compatibility

Before performing spatial joins, overlays, clipping, buffering, or raster extraction, you must verify that all layers share the same spatial reference system.

```{code-cell} python
import geopandas as gpd

stations_gdf = gpd.read_file("../data/raw/stations.gpkg")
landcover_gdf = gpd.read_file("../data/raw/landcover.gpkg")

# Ensure both layers have a defined CRS
assert stations_gdf.crs is not None, "Stations layer has no CRS."
assert landcover_gdf.crs is not None, "Land cover layer has no CRS."

# Ensure the CRSs match exactly
assert stations_gdf.crs == landcover_gdf.crs, (
    f"CRS mismatch: stations={stations_gdf.crs}, landcover={landcover_gdf.crs}"
)
```

If the CRS differs, the solution is never to continue and hope for the best. The solution is to explicitly {term}`reproject <Map reprojection>` one layer using `.to_crs()` before proceeding.

### Extent and overlap

Two layers may share the exact same CRS and still not overlap in space. This is the number one cause of mysteriously empty spatial joins or raster clips.

Instead of just printing the bounds and checking the coordinates manually, you can use `shapely` to test for overlap programmatically *before* running a computationally heavy intersection:

```{code-cell} python
from shapely.geometry import box

# total_bounds returns an array: [xmin, ymin, xmax, ymax]
# The * operator unpacks this array into the 4 separate arguments required by box()
stations_extent = box(*stations_gdf.total_bounds)
landcover_extent = box(*landcover_gdf.total_bounds)

assert stations_extent.intersects(landcover_extent), (
    "The station and land cover layers do not overlap in space!"
)
```

### Raster alignment

In raster math, two rasters that look identical on a map might still be mathematically incompatible. Before subtracting, stacking, or comparing rasters (like calculating an index or performing {term}`time-series <Time series>` change detection), you must check their structural alignment.

```{code-cell} python
import rasterio

with rasterio.open("../data/raw/band_red.tif") as red_src, rasterio.open("../data/raw/band_nir.tif") as nir_src:
    
    assert red_src.crs == nir_src.crs, "Raster CRS mismatch."
    assert red_src.shape == nir_src.shape, "Raster shape (rows/cols) mismatch."
    assert red_src.transform == nir_src.transform, "Raster transform mismatch."
```

The `transform` check is especially powerful. The transform matrix defines the exact geographic coordinates of the top-left pixel and the {term}`spatial resolution <Spatial resolution>`. If the transforms match, you are guaranteed that the pixels perfectly align in space.

```{admonition} Spatial data can be deceptively valid
:class: warning

A file can load correctly and still be entirely wrong for the analysis. The data may exist, but if the CRS, extent, or pixel alignment is incompatible, your scientific result will be invalid.
```

#### Concept Check: The Empty Overlay Mystery

You load a station point layer and a land-cover polygon layer. Both files open without errors, and both layers have a CRS. But your spatial overlay returns an empty result. What should you check first?

A. Check whether the layers have the same CRS and whether their spatial extents actually overlap.

B. Increase the buffer distance until some results appear.

C. Export both files to a new format because the file type is probably the problem.

```{admonition} Check your understanding
:class: dropdown

**Answer: A**
An empty overlay often means the layers are spatially incompatible even though they load correctly. Increasing a buffer or changing file formats can hide the real issue; first verify CRS compatibility and spatial overlap.

```

---

## 4. Avoiding hard-coded magic numbers

A {term}`magic number <Magic number>` is a direct, hard-coded value scattered arbitrarily throughout your code without any explanation of what it means. Magic numbers make workflows fragile, difficult to update, and scientifically ambiguous.

### The problem with hidden logic

**Bad: Magic numbers hidden in logic**

```{code-cell} python
# Why 10000? Why 20? Why 0.3? The reader has no idea.
buildings_filtered = buildings[buildings.geometry.area > 10000]
roads_buffered = roads.geometry.buffer(20)
vegetation_mask = ndvi_array > 0.3
```

Each of these numbers might be scientifically reasonable, but the code does not explain them. If you decide to change your buffer distance to 50 meters, you have to hunt through your entire notebook to find every instance of `20` and hope you do not accidentally replace a `20` that belonged to a completely different calculation.

### A stronger, explicit version

By defining these values as descriptive variables at the top of your script or notebook, you make your code much safer to modify. In Python, it is a standard convention to write these constants in all uppercase. *(Note: You can also use underscores to make large numbers easier to read, such as `10_000`.)*

**Good: Named constants**

```{code-cell} python
MIN_BUILDING_AREA_M2 = 10_000
ROAD_BUFFER_M = 20
VEGETATION_THRESHOLD = 0.3

buildings_filtered = buildings[buildings.geometry.area > MIN_BUILDING_AREA_M2]
roads_buffered = roads.geometry.buffer(ROAD_BUFFER_M)
vegetation_mask = ndvi_array > VEGETATION_THRESHOLD
```

Now, the assumptions are entirely visible. If you need to tweak a parameter to test its effect on your model, you change it in exactly one place at the top of your file.

### Common geospatial constants

This practice is especially critical in spatial workflows where numerical thresholds define the analytical outcome. You should always use named constants for:

* buffer distances
* EPSG / CRS codes
* cloud cover percentages
* spectral index thresholds, like NDVI or {term}`NDSI <Normalized Difference Snow Index>`
* minimum area or elevation thresholds
* resampling resolutions

```{admonition} If a number matters scientifically, give it a name
:class: note

A named constant turns a hidden, arbitrary assumption into an explicit analytical decision.
```

---

## 5. Clear error messages and failing loudly

Defensive coding is not only about checking conditions; it is also about how the workflow reacts when something goes wrong. A robust workflow should fail **clearly and loudly**.

### Protecting against empty results

A very common spatial bug occurs when an intersection or spatial join results in an empty dataset, often because the datasets do not actually overlap in space. If you feed an empty {term}`GeoDataFrame` into a plotting function or a statistical model, it will not crash immediately. Instead, it will cause confusing downstream errors or generate a blank map.

Use an `assert` statement to force your code to fail loudly the moment an assumption is broken:

```{code-cell} python
# Perform the spatial overlay
clipped_stations = gpd.overlay(stations_gdf, study_area_gdf, how="intersection")

# Defensive check: Did the overlay actually capture any points?
assert len(clipped_stations) > 0, "The spatial intersection resulted in an empty dataset! Check your extents."
```

### Choosing the right exception

While `assert` is perfect for quick notebook checks, professional Python modules use explicit `raise` statements to handle bad inputs. Python has dozens of built-in exceptions, but in spatial data science, you will mostly rely on these three:

* **{term}`ValueError`**: The user passed a variable with the right *type*, such as a number, but an inappropriate *value*. Use this for invalid thresholds, distances, or bounding box coordinates.

  ```python
  if buffer_distance_m < 0:
      raise ValueError(f"Buffer distance cannot be negative. You provided: {buffer_distance_m}")
  ```

* **{term}`TypeError`**: The user passed a variable of the completely wrong {term}`data type <Data type>`. Use this when your function expects a specific spatial object but receives something else.

  ```python
  import geopandas as gpd
  
  if not isinstance(gdf, gpd.GeoDataFrame):
      raise TypeError("Input must be a GeoDataFrame, not a standard pandas DataFrame.")
  ```

* **`KeyError`**: You are trying to access a {term}`dictionary <Dictionary>` key or a {term}`DataFrame` column that does not exist. Use this when verifying that your spatial data contains the specific attributes your model needs.

  ```python
  if "elevation_m" not in stations_gdf.columns:
      raise KeyError("The required column 'elevation_m' is missing from the dataset.")
  ```

### What makes a good error message

When a script fails, the error message is the only clue you (or your collaborator) have to fix it. Writing a custom error message is an act of empathy for the person debugging the code.

A useful error message should always include three things:

1. **What failed** (the action)
2. **The object or variable involved** (the specific data)
3. **The violated assumption** (why it failed)

**Weak:**

```python
raise ValueError("Invalid input")
```

If you see this error 6 months from now, you will have no idea what "input" was invalid or why.

**Better:**

```python
raise ValueError(f"Bounding box is invalid: xmin ({bbox['xmin']}) must be smaller than xmax ({bbox['xmax']}).")
```

### Example: Confirming raster and vector alignment

Applying this philosophy to our custom spatial functions makes them robust. Before extracting raster values to point geometries, you can explicitly check that the points fall within the raster's bounding box and provide a highly descriptive error if they do not.

```{code-cell} python
def verify_raster_coverage(points_gdf, raster_bounds):
    """Ensures points fall entirely within the raster extent."""
    
    xmin, ymin, xmax, ymax = points_gdf.total_bounds
    r_xmin, r_ymin, r_xmax, r_ymax = raster_bounds
    
    # Defensive checks with clear, descriptive error messages
    assert xmin >= r_xmin, f"Points xmin ({xmin}) extends beyond raster western edge ({r_xmin})."
    assert xmax <= r_xmax, f"Points xmax ({xmax}) extends beyond raster eastern edge ({r_xmax})."
    assert ymin >= r_ymin, f"Points ymin ({ymin}) extends beyond raster southern edge ({r_ymin})."
    assert ymax <= r_ymax, f"Points ymax ({ymax}) extends beyond raster northern edge ({r_ymax})."
```

```{admonition} Fail loudly, not silently
:class: important

A silent failure is dangerous because it lets the workflow continue with broken assumptions, ultimately producing fake science. A clear, loud failure is easier to fix and much safer scientifically.
```

---

## 6. Testing parts before chaining them

Many defensive coding problems are not solved by syntax alone; they are solved by workflow habits. A common, frustrating habit is writing ten processing steps in a row and then only inspecting the final map. If the map is blank, the debugging problem is now spread across the entire workflow.

Small checks localize problems. If a workflow breaks after step 2, that is much easier to fix than discovering at step 10 that the problem actually began at step 1.

### The danger of long method chains

Modern {term}`libraries <Library>` like `pandas` and `geopandas` allow you to chain many {term}`methods <Method>` together in a single, elegant block. While method chaining reads beautifully, it is the enemy of defensive coding during the development phase.

**The danger of long chains:**

```python
final_gdf = (
    gpd.read_file("stations.shp")
    .to_crs("EPSG:2056")
    .dropna(subset=["temperature"])
    .clip(study_area_gdf)
    .reset_index(drop=True)
)
```

If `final_gdf` ends up completely empty, which step caused the problem? Was it a CRS mismatch during the clip? Did `dropna` remove all your rows?

When building and testing your workflows, break these chains apart. Assign intermediate variables and check your assumptions along the way.

**Defensive development:**

```{code-cell} python
# Step 1: Read and project
stations = gpd.read_file("stations.shp").to_crs("EPSG:2056")
assert len(stations) > 0, "Failed to load geometries."

# Step 2: Clean missing data
clean_stations = stations.dropna(subset=["temperature"])
assert len(clean_stations) > 0, "All stations dropped due to missing temperature data!"

# Step 3: Spatial operation
final_gdf = clean_stations.clip(study_area_gdf).reset_index(drop=True)
assert len(final_gdf) > 0, "No stations intersect the study area boundary."
```

Once you are certain the logic holds, you can confidently rewrite the code into a cleaner, chained format, or wrap it safely into a custom {term}`module <Module>`.

### Building the habit: Inspect and visualize

Beyond `assert` statements, you should actively inspect intermediate products while the workflow is still small enough to reason about.

**Inspect a layer right after loading:**

Do not assume you know what the shapefile looks like. Check the first few rows, the CRS, and the bounding box immediately.

```{code-cell} python
# print(stations.head())
# print(stations.crs)
# print(stations.total_bounds)
```

**Inspect raster metadata before doing math:**

Before applying an equation to a 5-gigabyte DEM, verify its fundamental properties.

```{code-cell} python
import rasterio

# with rasterio.open("../data/raw/dem.tif") as src:
#     print(src.crs)
#     print(src.bounds)
#     print(src.shape)
#     print(src.res)
```

**Test one step before looping:**

A classic mistake is writing a {term}`for loop <Loop>` to clip 50 datasets before checking if the clipping logic actually works. Always test your spatial operation on a single file, and visually verify it with `.plot()`, before scaling it up to a loop.

```{admonition} Verify as you go
:class: tip

Do not build a long spatial pipeline and inspect only the final output. Check intermediate results, visualize your steps, and assert your assumptions while the workflow is still small enough to understand.
```

---

## 7. Exercise

Below is a deliberately fragile geospatial workflow. It runs, but it hides assumptions and is highly vulnerable to silent failures. Your task is to apply the defensive coding habits you learned in this chapter to make it more robust.

### Task

Improve the fragile workflow by:

1. checking that the input file actually exists before loading it
2. checking that the dataset has a CRS defined
3. checking that the required attribute column exists
4. replacing all magic numbers and hard-coded {term}`strings <String>` with named constants at the top of the script
5. adding an `assert` statement to ensure the final filtered dataset is not empty

### The fragile workflow

```{code-cell} python
from pathlib import Path
import geopandas as gpd

stations_path = Path("../data/raw/stations.gpkg")

# Deliberately fragile: No checks, magic numbers hidden in the logic
stations = gpd.read_file(stations_path)
stations = stations.to_crs("EPSG:2056")
stations["geometry"] = stations.geometry.buffer(500)
selected = stations[stations["station_type"] == "climate"]
# selected.plot()
```

### Your workspace

```{code-cell} python
from pathlib import Path
import geopandas as gpd

# Rewrite the defensive workflow here
```

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
from pathlib import Path
import geopandas as gpd

# 1. Replace magic numbers with named constants
STATIONS_PATH = Path("../data/raw/stations.gpkg")
TARGET_CRS = "EPSG:2056"
BUFFER_DISTANCE_M = 500
REQUIRED_COLUMN = "station_type"
TARGET_STATION = "climate"

# 2. Check input path
if not STATIONS_PATH.is_file():
    raise FileNotFoundError(f"Missing input file: {STATIONS_PATH.absolute()}")

stations_gdf = gpd.read_file(STATIONS_PATH)

# 3. Check assumptions early
assert stations_gdf.crs is not None, "Stations layer has no CRS defined."
assert REQUIRED_COLUMN in stations_gdf.columns, f"Missing required column: '{REQUIRED_COLUMN}'"

# 4. Execute spatial operations
stations_gdf = stations_gdf.to_crs(TARGET_CRS)
stations_gdf["geometry"] = stations_gdf.geometry.buffer(BUFFER_DISTANCE_M)

# 5. Filter and add a final assertion
selected_gdf = stations_gdf[stations_gdf[REQUIRED_COLUMN] == TARGET_STATION]
assert len(selected_gdf) > 0, f"No '{TARGET_STATION}' stations remain after filtering."

# selected_gdf.plot()
```
````

```{admonition} Reflection
:class: note

Look at the sample solution. Which potential failure does the improved version now catch earlier? Which scientific assumptions are now explicit that were previously hidden in the logic?
```

---

## 8. Summary

Defensive coding is the habit of writing workflows that do not trust their inputs blindly. By checking assumptions, validating data, and failing loudly when something is wrong, you protect your workflow from silently producing invalid spatial results.

**Key Takeaways:**

* **Validate the outside world:** Always verify that files exist and user inputs are valid before running heavy processing steps.
* **Check assumptions early:** Ensure your datasets are not empty, have the correct geometry types, and contain the required columns right after loading.
* **Verify spatial compatibility:** Never assume layers align. Explicitly check that CRSs match, spatial extents overlap, and raster transforms align.
* **Banish magic numbers:** Replace unexplained, hard-coded numbers with named, uppercase constants at the top of your script.
* **Choose the right exception:** Use `assert` for quick notebook checks, but use explicit exceptions (`ValueError`, `TypeError`, `KeyError`) with highly descriptive error messages for custom functions.
* **Verify as you go:** Test and visualize small intermediate steps rather than blindly chaining long sequences of methods together and hoping the final map is correct.

These habits make spatial code more robust, easier to debug, and much safer to rerun. That matters not only for programming convenience but for scientific trustworthiness.

### What comes next

Robust, defensive code is a massive step toward full reproducibility. In the next chapter, we will broaden the perspective from safe code to completely reproducible research workflows: managing environments, {term}`version control <Version control>`, and {term}`virtual environments <Virtual environment>`.
