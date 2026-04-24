---
title: Exploring Data Cubes
site: 
  outline_maxdepth: 1
---

<div class="page-subtitle">
Reading, inspecting, and visualizing multidimensional datasets
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/12_L10_time-series/02_exploring_data_cubes.ipynb)

---

```{admonition} Big idea
:class: tip

Before you analyze a data cube, you must learn to read its structure: dimensions, coordinates, variables, and metadata.
```

In the previous chapter, you learned that a data cube is a multidimensional matrix paired with explicit spatial and temporal labels. Understanding this structure conceptually is the first step. The next crucial skill is learning how to practically interact with these objects in Python.

Before you begin applying map algebra or calculating time series trends, you must know exactly what your data contains. This chapter provides a standard, reliable workflow for ingesting, inspecting, formatting, and visually verifying any new multidimensional dataset using `xarray`.

---

## 1. Opening the cube

The function you use to open a data cube depends entirely on the storage format of the file on your hard drive or in the cloud. `xarray` acts as a universal reader, but you must choose the right tool for your specific file.

* **`xr.open_dataset()`**: This is the standard function for reading native multidimensional formats like NetCDF (`.nc`) or HDF5 (`.h5`). It reads the file and returns a `Dataset` container, which can hold multiple aligned variables (like temperature and precipitation).
  ```python
  ds = xr.open_dataset("climate_data.nc")
  ```
* **`xr.open_dataarray()`**: Use this when you are reading a NetCDF file that you know contains only one single variable. It skips the `Dataset` container and directly returns the `DataArray`.
  ```python
  da = xr.open_dataarray("single_variable.nc")
  ```
* **`xr.open_zarr()`**: This is the dedicated function for reading cloud optimized Zarr stores (`.zarr`), allowing you to stream chunked data directly into memory.
  ```python
  ds_zarr = xr.open_zarr("cloud_data.zarr")
  ```
* **The GeoTIFF bridge**: If you are reading a standard GIS raster (`.tif`), standard `xarray` will struggle to understand its spatial projection. By installing the `rioxarray` extension, you unlock a new reading engine. You can then load GeoTIFFs while perfectly preserving their Coordinate Reference System (CRS).
  ```python
  import rioxarray
  
  # Method 1: Using the xarray engine
  da_tif = xr.open_dataarray("satellite_image.tif", engine="rasterio")
  
  # Method 2: Using the rioxarray wrapper
  da_tif = rioxarray.open_rasterio("satellite_image.tif")
  ```

```{admonition} Do I need to import rioxarray?
:class: note

Notice that Method 1 (`engine="rasterio"`) will actually work even if you delete the `import rioxarray` line. This is because `xarray` automatically finds the installed engine in the background to read the file. 

However, if you want to use any specific GIS tools later—like checking the projection (`.rio.crs`) or saving a new map (`.rio.to_raster()`)—you **must** explicitly import `rioxarray` in your script to unlock those capabilities.
```

For this chapter, we will use a built-in tutorial dataset to practice reading and inspecting these structures.

```{code-cell} python
import xarray as xr

# Load a standard NetCDF tutorial dataset
ds = xr.tutorial.open_dataset("air_temperature")
```

---

## 2. Reading the xarray display

When you evaluate an `xarray` object in a Jupyter Notebook, you are presented with an interactive HTML summary. Learning to read this summary is an important debugging skill you can develop for multidimensional analysis.

```{code-cell} python
ds
```

If you run the cell above, you will see a structured output. Notice the interactive icons: you can click the arrows (▶) to expand sections, and the document icons (📄 or ≡) to peek at the actual data values and metadata without printing massive arrays to your screen. 

From top to bottom, the output is divided into five key components:

* **Dimensions:** This shows the shape of your cube. You will see `lat: 25`, `lon: 53`, and `time: 2920`. This instantly tells you the matrix has 25 rows, 53 columns, and 2920 time steps. Because dimensions are named, their physical order in the array does not matter.
* **Coordinates:** These are the labels for the dimensions. Notice that the names are printed in **bold font**. This indicates they are "dimension coordinates" backed by an index, allowing for lightning fast data selection. 
* **Data variables:** This lists the actual physical measurements stored inside the container. Here, there is only one variable called `air`. It also shows the specific dimensions that variable relies on `(time, lat, lon)` and its data type (e.g., `float64`).
* **Indexes:** This section confirms which coordinates have an underlying search index built in. In most cases, these are backed by a standard Pandas index.
* **Attributes:** This section holds the global metadata. Expanding this reveals the dataset history, conventions, and units, providing the necessary context to trust the data you are analyzing.

### Extracting a single variable

The display above shows the entire `Dataset` container. To actually analyze the temperature data, you need to extract the specific `DataArray`. `xarray` allows you to do this using standard dictionary syntax or a convenient dot notation shortcut.

```{code-cell} python
# Extracting using dictionary syntax (safest)
da = ds["air"]

# Extracting using dot notation (fastest for typing)
da = ds.air
da
```

If you print this new `da` object, you will see a very similar HTML display, but it now represents just the single variable rather than the whole container.

```{admonition} Text vs HTML displays
:class: note

The interactive HTML display is only available inside Jupyter Notebooks. If you run your code in a standard Python console or terminal, `xarray` will automatically fall back to a plain text representation. In the text version, dimension coordinates are marked with an asterisk (`*`) instead of bold text.
```

---

## 3. Renaming and formatting

Scientific datasets can come with obscure variable names, missing metadata, or poorly formatted coordinates. Before you start writing complex analysis code, it is highly recommended to clean your dataset. This makes your code self documenting and prevents errors later on.

**Renaming variables and dimensions**
If a temperature variable is awkwardly named `t2m` or simply `air`, you can rename it to something descriptive. You use the `.rename()` method, passing a dictionary where the key is the old name and the value is the new name. This exact same approach works for renaming dimensions.

```{code-cell} python
# Rename the variable 'air' to 'temperature'
ds_clean = ds.rename({"air": "temperature"})

# Verify the change
print(list(ds_clean.data_vars))
```

**Modifying and assigning coordinates**
Sometimes, a dataset will load with plain integer indices instead of real world coordinates, or the coordinates might be in the wrong format (like strings instead of proper datetime objects). You can overwrite or assign entirely new coordinate arrays using dictionary syntax.

```{code-cell} python
import pandas as pd

# Example: Overwriting the time coordinate with a newly generated Pandas date range
ds_clean.coords["time"] = pd.date_range("2013-01-01", "2014-12-31 18:00", freq="6h")
```

**Updating attributes and metadata**
Attributes are dictionaries that hold arbitrary metadata. You might want to add missing information, like the physical units of your new `temperature` variable, or add a descriptive note to the entire dataset container. 

```{code-cell} python
# Add metadata to a specific variable
ds_clean["temperature"].attrs["units"] = "Kelvin"

# Add global metadata to the entire dataset container
ds_clean.attrs["project_author"] = "Spatial Data Science Lab"

# Check the new variable attributes
print(ds_clean["temperature"].attrs)
```

By taking a few lines of code to rename variables, fix coordinates, and assign units, you transform a confusing raw file into a clean, professional data structure ready for analysis.

---

## 4. First checks for a cube

While the interactive HTML display is fantastic for visual inspection, you will often need to write automated scripts. Every time you load a new dataset, you should run a mental checklist of its properties using the following programmatic commands.

**Standard array properties:**
```{code-cell} python
# Check the dimensions and their specific lengths
print(ds_clean.sizes)

# Check the available variables
print(list(ds_clean.data_vars))

# Check the global dataset attributes (e.g., to find the author or conventions)
print(ds_clean.attrs)
```

**Memory and safety checks:**
Data cubes can easily consume all your computer's RAM. Before running heavy calculations, you should always check the size of your object.
```{code-cell} python
# Calculate total memory size in Megabytes
memory_mb = ds_clean.nbytes / (1024 ** 2)
print(f"Total size: {memory_mb:.2f} MB")
```

**Spatial properties (via rioxarray):**
If you loaded a GeoTIFF using `rioxarray`, or if you explicitly assigned a CRS to a NetCDF file, you unlock a powerful suite of GIS metadata checks using the `.rio` accessor.

```python
# Import the rioxarray extension to activate the .rio accessor
import rioxarray

# Check the Coordinate Reference System (CRS)
print(ds_clean.rio.crs)

# Check the spatial resolution (pixel width and height)
print(ds_clean.rio.resolution())

# Check the geographic bounding box (xmin, ymin, xmax, ymax)
print(ds_clean.rio.bounds())

# Check the designated 'nodata' value used for missing pixels
print(ds_clean["temperature"].rio.nodata)
```

``` {admonition} Hierarchical Data (Groups)
:class: tip

Some complex formats like HDF5 and NetCDF4 act like full file systems containing nested folders (called groups). If you encounter a dataset like this, standard `xr.open_dataset()` will only load the root level. 

Instead, you can use `xr.open_datatree("file.nc")`. This returns a `DataTree` object, allowing you to inspect the full nested hierarchy by checking `dataset.groups` or `dataset.children`.
```


---


## 5. Visualizing the cube

Plotting is one of the fastest ways to verify data integrity. Does the spatial pattern look like Earth? Is the seasonal cycle visible? Are there extreme outliers? 

`xarray` acts as a highly intelligent wrapper around the `matplotlib` library. Because your data cube contains named dimensions, coordinates, and metadata, `xarray` can automatically label your axes, generate color bars, and format dates without you having to write dozens of lines of visualization code. 

Keep these initial plots focused on data validation and exploration.

### 5.1 Checking the distribution
To spot erroneous values (like a sensor error recording `-9999` instead of a real temperature), it is highly useful to plot a histogram of all the values in the cube. `xarray` flattens the 3D data automatically to generate the distribution.

```{code-cell} python
# Plot a histogram with 50 bins to check the overall data distribution
ds_clean["temperature"].plot.hist(bins=50)
```

:::{figure} images/02_histogram.png
:alt: A histogram showing a bell-shaped distribution of temperature values.
:width: 600px
:align: center

*A standard histogram of the temperature data. This quick check helps ensure there are no extreme erroneous values skewing the dataset.*
:::

### 5.2 Extracting and plotting time series
If your data has only one dimension (for example, if you drill down into a single coordinate over time), `xarray` will automatically detect this and generate a **line plot**. 

This is incredibly useful for verifying temporal patterns. Here, we select a specific location and plot the resulting 1D time series. Notice how `xarray` automatically formats the X-axis as readable dates!

```{code-cell} python
# Select a specific coordinate and plot the temperature over time
ds_clean["temperature"].sel(lat=40.0, lon=260.0, method="nearest").plot()
```

:::{figure} images/02_timeseries.png
:alt: A line chart showing fluctuating temperature values over a two-year period.
:width: 600px
:align: center

*Extracting a 1D time series at a single coordinate location. `xarray` automatically formats the X-axis with the datetime labels.*
:::

### 5.3 Slicing a single map
You cannot plot a full 3D cube on a flat 2D screen. To map the spatial data, you must isolate a single slice of time. `xarray` automatically recognizes the two remaining spatial dimensions and generates a color mesh (heatmap). 

```{code-cell} python
# Isolate the first time step and plot it as a 2D map
ds_clean["temperature"].isel(time=0).plot()
```

:::{figure} images/02_single_map.png
:alt: A 2D heatmap showing temperature variations across a spatial grid.
:width: 600px
:align: center

*A single time slice plotted as a 2D map. Notice how the coordinates and metadata units are automatically applied to the axes and color bar.*
:::

```{admonition} Handling extreme outliers
:class: tip

If your dataset contains a few extreme outliers, your color bar will stretch to accommodate them, making the rest of your map look completely washed out. You can add `robust=True` inside the `.plot()` method. This tells `xarray` to calculate the color range based on the 2nd and 98th percentiles, cleanly hiding extreme anomalies.
```

### 5.4 Faceting (Small Multiples)
What if you want to visualize the third dimension without slicing it away completely? 

**Faceting** is the art of presenting "small multiples" of your data. Instead of one single map, `xarray` can generate a grid of subplots. You simply tell the `.plot()` method which dimension should be spread across the columns (`col`). 

```{code-cell} python
# Select the first 4 time steps and plot them side by side
ds_clean["temperature"].isel(time=slice(0, 4)).plot(col="time")
```

:::{figure} images/02_faceted_map.png
:alt: Four small maps arranged in a row, showing temperature progression over four consecutive time steps.
:width: 800px
:align: center

*Faceted subplots (small multiples) allow you to easily compare spatial patterns across the time dimension while sharing the exact same color scale.*
:::

This ensures all panels share the exact same color scale, making it incredibly easy to track spatial changes over time. If you have many slices, you can add `col_wrap=2` to force the grid to wrap onto new rows.

### 5.5 Geographic plotting with Cartopy
So far, our 2D plots are just colored matrices. While `xarray` labels the axes with latitude and longitude, the plot lacks geographic context. Is the hot spot over land or ocean? 

Since `xarray` builds directly on `matplotlib`, you can seamlessly integrate the **Cartopy** library to project your matrices onto real Earth cartography. This requires three specific steps:
1. Specify a `projection` for the plot axes using `subplot_kws`.
2. Specify the original Coordinate Reference System of your raw data using `transform`.
3. Add geographic features (like coastlines) to the resulting map.

```{code-cell} python
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# 1. Create a plot with a specific map projection (e.g., Orthographic)
p = ds_clean["temperature"].isel(time=0).plot(
    subplot_kws={"projection": ccrs.Orthographic(-90, 40)},
    transform=ccrs.PlateCarree(), # 2. Tell Cartopy the raw data is in Lat/Lon
    robust=True
)

# 3. Add coastlines to the generated axes to provide geographic context
p.axes.coastlines()

plt.show()
```

:::{figure} images/02_cartopy_orthographic.png
:alt: A map of North America projected onto a 3D globe with coastlines drawn, overlaid with a temperature heatmap.
:width: 500px
:align: center

*By combining `xarray` with `cartopy`, the raw data matrix is projected onto a recognizable Earth surface, verifying its geographic accuracy.*
:::

By adding just a few lines of `cartopy` code, your raw matrix instantly transforms into a professional, recognizable geographic map, giving you complete confidence in the spatial integrity of your data cube.

### 5.6 Animating the time dimension (GIFs)

Faceted plots are great for comparing a few time steps, but if you want to visualize an entire year of data, a static image is no longer sufficient. Because your data cube inherently understands the progression of time, you can easily generate an animated GIF. 

The standard approach uses the `matplotlib.animation` tool. The logic is simple: you create an empty figure, define an `update` function that plots a single time slice, and then tell Python to loop that function across a set number of frames.

```{code-cell} python
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# 2. Define the function that will update the map for every frame
def animate_frame(i):
    ax.clear() # Clear the previous map
    
    # Isolate the current time step and plot it
    # We set add_colorbar=False so it doesn't draw a new one every frame
    ds_clean["temperature"].isel(time=i).plot(ax=ax, add_colorbar=False, robust=True)
    
    # Add a dynamic title showing the exact date
    current_date = ds_clean["temperature"].time.values[i]
    ax.set_title(f"Temperature on {str(current_date)[:10]}")

# 3. Create the animation (e.g., for the first 20 time steps)
ani = animation.FuncAnimation(fig, animate_frame, frames=20, interval=200)

# 4. Save the result as a GIF using the Pillow writer
ani.save("temperature_timelapse.gif", writer="pillow")

plt.close() # Prevents the static plot from showing up in the notebook
```

:::{figure} images/02_animated_gif_placeholder.png
:alt: An animated GIF showing temperature patterns shifting across the globe over 20 consecutive days.
:width: 600px
:align: center

*By animating the time dimension, you can visually track dynamic environmental processes like the progression of seasons, the movement of storm systems, or the expansion of urban heat waves.*
:::

```{admonition} Performance warning
:class: warning

Generating a GIF is computationally heavy because Python has to render a brand new map for every single frame. Start by testing your animation on a small slice of time (e.g., `frames=10`) before trying to animate an entire multi-year data cube!
```

---

## 6. Exercise: Your first inspection

It is time to practice the complete ingestion and preview workflow. `xarray` provides another built in tutorial dataset containing a climate model output called `rasm`. 

**Your task:**
1. **Open:** Load the `rasm` dataset using `xr.tutorial.open_dataset()`.
2. **Rename:** Inspect the data variables. You will find a variable named `Tair`. Rename this variable to `air_temp`.
3. **Check memory:** Calculate and print the total memory size of your renamed dataset in Megabytes (MB).
4. **Check metadata:** Programmatically access and print the `units` attribute of your new `air_temp` variable.
5. **Validate:** Plot a 50-bin histogram of the `air_temp` data to verify its overall distribution.
6. **Visualize:** Plot a 2D map of the `air_temp` variable for the very first time step (`time=0`).

**Starter code:**

```{code-cell} python
# Install the required library for climate calendars
!pip install cftime 

import xarray as xr
import matplotlib.pyplot as plt

# 1. Open the 'rasm' dataset
# ...

# 2. Rename 'Tair' to 'air_temp'
# ...

# 3. Print the memory size in MB
# ...

# 4. Print the units attribute
# ...

# 5. Plot a histogram
# ...

# 6. Plot the first time step as a 2D map
# ...
```

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
!pip install cftime

import xarray as xr
import matplotlib.pyplot as plt

# 1. Open the dataset
rasm_ds = xr.tutorial.open_dataset("rasm")

# 2. Rename the variable
rasm_clean = rasm_ds.rename({"Tair": "air_temp"})

# 3. Check memory size
memory_mb = rasm_clean.nbytes / (1024 ** 2)
print(f"Total size: {memory_mb:.2f} MB")

# 4. Check metadata
print(f"Temperature units: {rasm_clean['air_temp'].attrs.get('units')}")

# 5. Plot a histogram to validate the data
rasm_clean["air_temp"].plot.hist(bins=50)
plt.show() # Display the histogram before drawing the map

# 6. Plot the first time step using index selection (isel)
rasm_clean["air_temp"].isel(time=0).plot()
plt.show()
```

:::{figure} images/09_exercise_histogram.png
:alt: A histogram showing a left-skewed distribution of surface air temperatures in Celsius, peaking around 15 degrees.
:width: 600px
:align: center

*Output 1: A histogram validating the overall distribution of the surface air temperature variable.*
:::

:::{figure} images/09_exercise_map.png
:alt: A 2D heatmap showing surface air temperatures across the Northern Hemisphere for September 16, 1980, with cold blue temperatures in the Arctic center and warmer red temperatures at the edges.
:width: 600px
:align: center

*Output 2: A 2D map of the first time step (`1980-09-16`). The `rasm` dataset is an Arctic climate model projected over the Northern Hemisphere, which is why the geographical features are warped to fit the model's native grid indices rather than standard latitudes and longitudes.*
:::
```

Notice the shape of the resulting map! The `rasm` dataset is an Arctic climate model projected over the Northern Hemisphere, which is why the coordinates do not look like a standard flat rectangular grid. Because `xarray` understands the underlying spatial coordinates, it handles this warping seamlessly for quick visualizations.
````

---

## 7. Summary

Whenever you receive a new multidimensional dataset, you should apply the standardized ingestion and preview workflow learned in this chapter:

1. **Open:** Load the file using the appropriate tool (`xr.open_dataset` for NetCDF/HDF5, `xr.open_zarr` for cloud stores, or the `rioxarray` engine for GeoTIFFs).
2. **Read:** Explore the interactive HTML display to understand the shape, dimension coordinates, physical variables, and underlying metadata.
3. **Format:** Clean up the dataset by renaming messy variables with `.rename()`, reassigning coordinate values, and updating missing attributes (like physical units).
4. **Check:** Programmatically verify the object's properties, including its memory footprint (`.nbytes`), dimension lengths (`.sizes`), and spatial projections using the `.rio` accessor.
5. **Visualize:** Rapidly validate data integrity by plotting distributions (`.plot.hist()`), 1D time series, 2D heatmaps (`.isel()`), faceted grids, Cartopy projections, or animated GIFs.

With a clean, memory-safe, and visually verified dataset in memory, you are now ready to start slicing, aggregating, and extracting deeper environmental insights in the next chapter.