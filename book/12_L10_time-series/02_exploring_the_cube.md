---
title: Exploring the Cube

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

Before you begin applying map algebra or calculating time series trends, you must know exactly what your data contains. This chapter provides a standard, reliable workflow for ingesting, inspecting, formatting, processing geospatial metadata, and exporting any multidimensional dataset using `xarray`.

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
  # !pip install rioxarray
  import rioxarray
  
  # Method 1: Using the xarray engine
  da_tif = xr.open_dataarray("satellite_image.tif", engine="rasterio")
  
  # Method 2: Using the rioxarray wrapper
  da_tif = rioxarray.open_rasterio("satellite_image.tif")
  ```

```{admonition} Do I need to import rioxarray?
:class: note

Notice that Method 1 (`engine="rasterio"`) will actually work even if you delete the `import rioxarray` line. This is because `xarray` automatically finds the installed engine in the background to read the file. 

However, if you want to use any specific GIS tools later, like checking the projection (`.rio.crs`) or saving a new map (`.rio.to_raster()`), you **must** explicitly import `rioxarray` in your script to unlock those capabilities.
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

````{admonition} Hierarchical Data (Groups)
:class: tip

Some complex formats like HDF5 and NetCDF4 act like full file systems containing nested folders (called groups). If you encounter a dataset like this, standard `xr.open_dataset()` will only load the root level. 

Instead, you can use `xr.open_datatree("file.nc")`. This returns a `DataTree` object, allowing you to inspect the full nested hierarchy by checking `dataset.groups` or `dataset.children`.
````

---

## 5. Geospatial operations

`xarray` is easily extensible. Third party packages can plug directly into `xarray` using a feature called **accessors**. Accessors allow you to use familiar dot notation (like `.plot()` or `.dt()`) to access entirely new toolkits.

The `rioxarray` package provides the `.rio` accessor. It acts as a bridge between the multidimensional power of `xarray` and the foundational geospatial algorithms of the `rasterio` and GDAL libraries.

### Loading geospatial metadata
Let us load a new dataset to explore these features: a Copernicus Digital Elevation Model (DEM) subset over New Zealand. We will use the `rasterio` engine to open the GeoTIFF.

```{code-cell} python
import xarray as xr
import rioxarray

filepath = "data/Copernicus_DEM_NZ_subset.tif"
da_dem = xr.open_dataarray(filepath, engine="rasterio")
```

When `rioxarray` opens a file, it automatically parses the spatial metadata embedded in the GeoTIFF. You unlock a powerful suite of GIS metadata checks using the `.rio` accessor.

```{code-cell} python
# Check the Coordinate Reference System (CRS)
print(da_dem.rio.crs)

# Check the spatial resolution (pixel width and height)
print(da_dem.rio.resolution())

# Check the geographic bounding box (xmin, ymin, xmax, ymax)
print(da_dem.rio.bounds())

# Check the designated 'nodata' value used for missing pixels
print(da_dem.rio.nodata)
```

The output for the CRS typically reveals an EPSG code (European Petroleum Survey Group). Understanding your resolution and bounding box is critical before merging this DEM with other datasets, as they must align perfectly in space.

### Reprojection
If you want to map this data alongside standard web maps or datasets in a different coordinate system, you must reproject the dataset into a new CRS. For example, converting it to Web Mercator (`EPSG:3857`).

```{code-cell} python
# Reproject to Web Mercator
da_reprojected = da_dem.rio.reproject("EPSG:3857")

print(da_reprojected.rio.crs)
```

If you print the sizes of `da_dem` and `da_reprojected`, you will notice that the dimensions have changed. This is an important rule of spatial data science: **reprojection resamples your data**. The original grid must be warped and interpolated to fit the newly defined spatial grid.

### Handling NoData values
Elevation models and satellite imagery frequently contain missing pixels around the edges of the swath or over the ocean. These are recorded using a designated NoData value. You can assign and clean these values so they do not skew your mathematical calculations or color ramps later.

```{code-cell} python
# Explicitly assign a NoData value to the dataset memory
da_clean = da_reprojected.rio.set_nodata(-9999)

# Mask the NoData values (writes them safely to the object attributes)
da_clean = da_clean.rio.write_nodata(-9999, inplace=True)
```

---

## 6. Exporting data

Once you have renamed your variables, reprojected your coordinates, and cleaned your NoData values, you will likely want to save the processed data back to disk. Xarray makes writing data just as easy as reading it. 

### Exporting to multidimensional formats
The recommended way to store standard `xarray` data structures (like the climate datasets from earlier in the chapter) is NetCDF. This format guarantees that all your variables, coordinates, and metadata attributes are perfectly preserved in a single file. 

If you are working with massive datasets or cloud environments, you should export to Zarr instead. Zarr implements chunked, compressed arrays that stream beautifully from services like Amazon S3 or Google Cloud Storage.

```{code-cell} python
# Save a cleaned Dataset container to a local NetCDF file
ds_clean.to_netcdf("processed_climate_data.nc")

# Save to a local Zarr store (directory)
ds_clean.to_zarr("processed_climate_data.zarr", mode="w")
```

### Exporting to geospatial formats
If you isolated a single 2D spatial variable (like our New Zealand DEM) and need to share it with a colleague who uses standard GIS software like QGIS or ArcGIS, you should export it as a GeoTIFF. 

Because standard `xarray` does not understand GeoTIFF formatting natively, you must use the `.rio` accessor to handle the export.

```{code-cell} python
# Save the reprojected and cleaned DEM back to a GeoTIFF file
da_clean.rio.to_raster("reprojected_nz_dem.tif")
```

---

## 7. Exercise

It is time to practice the complete ingestion, inspection, and export workflows for both multidimensional climate data and geospatial raster data. 

**Task A: The Climate Workflow (NetCDF)**
1. **Open:** Load the `rasm` tutorial dataset using `xr.tutorial.open_dataset()`.
2. **Rename:** Inspect the data variables. Rename `Tair` to `air_temp`.
3. **Check memory:** Calculate and print the total memory size of your renamed dataset in Megabytes (MB).
4. **Export:** Save your cleaned dataset to a new NetCDF file named `rasm_cleaned.nc`.

**Task B: The Geospatial Workflow (GeoTIFF)**
1. **Open:** Load the New Zealand DEM (`data/Copernicus_DEM_NZ_subset.tif`) using the `rasterio` engine.
2. **Inspect CRS:** Programmatically print the original Coordinate Reference System of the DEM.
3. **Reproject:** Reproject the data to WGS 84 (`EPSG:4326`).
4. **Export:** Save the reprojected array to a new GeoTIFF named `nz_dem_wgs84.tif`.

**Starter code:**

```{code-cell} python
# Install required libraries
!pip install cftime rioxarray

import xarray as xr
import rioxarray

# --- TASK A: Climate Workflow ---
# 1. Open the 'rasm' dataset
# ...

# 2. Rename 'Tair' to 'air_temp'
# ...

# 3. Print the memory size in MB
# ...

# 4. Export to NetCDF
# ...


# --- TASK B: Geospatial Workflow ---
filepath = "data/Copernicus_DEM_NZ_subset.tif"

# 1. Open the DEM
# ...

# 2. Print the CRS
# ...

# 3. Reproject to EPSG:4326
# ...

# 4. Export to GeoTIFF
# ...

```

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
!pip install cftime rioxarray

import xarray as xr
import rioxarray

# --- TASK A: Climate Workflow ---

# 1. Open the dataset
rasm_ds = xr.tutorial.open_dataset("rasm")

# 2. Rename the variable
rasm_clean = rasm_ds.rename({"Tair": "air_temp"})

# 3. Check memory size
memory_mb = rasm_clean.nbytes / (1024 ** 2)
print(f"Task A - Total size: {memory_mb:.2f} MB")

# 4. Export to NetCDF
rasm_clean.to_netcdf("rasm_cleaned.nc")
print("Task A - Exported to rasm_cleaned.nc")


# --- TASK B: Geospatial Workflow ---
filepath = "data/Copernicus_DEM_NZ_subset.tif"

# 1. Open the DEM
da_dem = xr.open_dataarray(filepath, engine="rasterio")

# 2. Print the CRS
print(f"Task B - Original CRS: {da_dem.rio.crs}")

# 3. Reproject to EPSG:4326
da_dem_wgs84 = da_dem.rio.reproject("EPSG:4326")
print(f"Task B - New CRS: {da_dem_wgs84.rio.crs}")

# 4. Export to GeoTIFF
da_dem_wgs84.rio.to_raster("nz_dem_wgs84.tif")
print("Task B - Exported to nz_dem_wgs84.tif")
```
````

---

## 8. Summary

Whenever you receive a new dataset, you should apply a standardized workflow to safely ingest, clean, format, and export your data cubes before diving into deep analysis:

1. **Ingest:** Load the file using the appropriate tool (`xr.open_dataset` for NetCDF/HDF5, `xr.open_zarr` for cloud stores, or the `rasterio` engine for GeoTIFFs).
2. **Inspect:** Explore the interactive HTML display to understand the shape, dimension coordinates, physical variables, and underlying metadata. Always check the memory footprint (`.nbytes`) to ensure your computer can handle the arrays.
3. **Format:** Clean up the dataset by renaming messy variables with `.rename()`, reassigning coordinate values, and updating missing attributes (like physical units).
4. **Process Geospatial Data:** Use the `.rio` accessor to inspect spatial properties, mask NoData pixels, and use `.rio.reproject()` to warp grids into matching Coordinate Reference Systems.
5. **Export:** Save your verified and cleaned data safely to disk using `.to_netcdf()`, `.to_zarr()`, or `.rio.to_raster()`.

With a clean, memory-safe, and spatially aligned dataset sitting on your hard drive, you are now ready to start slicing, aggregating, and analyzing the cube in the upcoming chapters.
