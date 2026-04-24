---
title: The Data Cube Model

site: 
  outline_maxdepth: 1
---

<div class="page-subtitle">
Moving from 2D grids to labeled multidimensional spaces
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/12_L10_time-series/01_data_cube_model.ipynb)

---

```{admonition} Big idea
:class: tip

A raster becomes far more powerful once it is no longer just a 2D grid, but a labeled data cube that can be explored across space, time, bands, and variables. 
```

In the previous lesson, you learned how to read spatial grids using Rasterio and process them using NumPy. That workflow is perfect for analyzing a single snapshot of the environment. However, Earth observation is fundamentally about change. 

To analyze climate patterns, vegetation growth, or urban heat, you cannot look at one image. You need to process hundreds of repetitive observations simultaneously. This chapter introduces the **Data Cube Model**, a conceptual shift that prepares you to handle massive, multidimensional environmental datasets using the `xarray` library.

---

## 1. Why xarray after Rasterio?

Rasterio is an excellent translator. It reads a GeoTIFF file from your hard drive and hands you a pure NumPy array. While NumPy is incredibly fast at math, it is completely blind to context. 

If you load a massive climate dataset, NumPy might tell you the array shape is `(2920, 25, 53)`. But that raw matrix does not tell you which axis is time, which axis is latitude, or what the units are. If you want to find the temperature for Zurich on July 1st, you have to mentally calculate the exact numeric index for that day, row, and column. This leads to code that is difficult to read and highly prone to silent errors.

The `xarray` library solves this exact problem. It brings the intuitive labeling power of Pandas directly into the multidimensional matrix operations of NumPy. 

Just as `geopandas` makes tabular data spatially aware, a companion library called `rioxarray` provides robust GIS capabilities on top of `xarray`. Together, they allow you to read, project, and manipulate raster data using named dimensions (`time`, `lat`, `lon`) and coordinates, rather than raw numerical indices.

---

## 2. The third dimension and beyond

To understand `xarray`, you must shift your perspective from a flat map to a multidimensional cube.

A traditional satellite image or Digital Elevation Model exists in two spatial dimensions: X (longitude) and Y (latitude). Imagine taking a new satellite image of the exact same location every day for a year. If you physically stack these images on top of one another like pages in a book, the depth of that stack becomes a third dimension: **Time**.

The resulting structure is a Data Cube. 

Within this cube, every single geographic pixel is no longer just a static value. If you select a specific coordinate and drill straight down through the layers of the cube, you extract a complete time series showing exactly how that location changed over the year.

However, environmental data cubes often go beyond just time. A single `xarray` object can align multiple components perfectly over the same geographic grid:
* **Spatial Dimensions:** The X (longitude) and Y (latitude) axes.
* **Temporal Dimensions:** The same raster repeated across days, months, or years.
* **Spectral Dimensions:** Multiple sensor bands (Red, Green, Near-Infrared) stacked together.
* **Data Variables:** Entirely different physical measurements (e.g., temperature, precipitation, and wind speed) sharing the exact same dimensions.

To visualize how a 2D grid transforms into a 3D time series, explore the interactive widget below.

<iframe 
    src="data_cube_visualizer.html"
    width="100%"
    title="Interactive Data Cube Explorer"
    frameborder="0"
    style="height: 750px; min-height: 750px; border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
    allowfullscreen>
</iframe>

*For an alternative standalone version of the explorer, follow this [link](https://hendrikwulf.github.io/sds210_assets_L10_ch01_data_cube_visualizer/).*

---

## 3. DataArray and Dataset

When working with data cubes in Python, `xarray` provides two core data structures. Both of these build directly upon the logic of the `pandas` and `geopandas` libraries you have seen in previous lessons. 

Understanding the relationship between these two structures is the foundation of multidimensional analysis.

### The DataArray

A `DataArray` is a single labeled variable. You can think of it as the `xarray` equivalent of a `pandas.Series`, but designed to handle multidimensional raster matrices instead of flat columns.

Every `DataArray` consists of four key properties:
* **Values:** The underlying NumPy array containing the raw numbers (e.g., the actual temperature readings).
* **Dimensions (dims):** The named axes of the data (e.g., `time`, `lat`, `lon`).
* **Coordinates (coords):** The specific tick labels along those dimensions (e.g., `2024-05-30`, or `47.3°N`).
* **Attributes (attrs):** A dictionary holding arbitrary metadata (e.g., units, sensor type, or data source).

:::{figure} images/xarray_terminology.png
:alt: Diagram showing Xarray terminology including dimensions, coordinates, and attributes attached to an array of data.
:width: 600px
:align: center

*A DataArray bundles the raw numerical data with named dimensions, coordinate labels, and metadata attributes. Source: [SpatialThoughts](https://courses.spatialthoughts.com/python-dataviz.html#xarray-basics)*
:::

### The Dataset

A `Dataset` is a container that holds multiple DataArrays together. 

In environmental science, you rarely measure just one variable. A weather model might predict temperature, precipitation, and wind speed simultaneously. A `Dataset` aligns all these different variables perfectly along the same shared coordinates. 

You can think of a `Dataset` as the `xarray` equivalent of a `geopandas.GeoDataFrame`. Just as a GeoDataFrame stores multiple columns of data over the same exact geographic shapes, a Dataset stores multiple physical variables over the exact same multidimensional cube.

:::{figure} images/dataset-diagram.png
:alt: Diagram of an Xarray Dataset showing multiple variables like temperature and precipitation sharing the same latitude, longitude, and time dimensions.
:width: 600px
:align: center

*A Dataset aligns multiple variables (DataArrays) inside a single container, sharing the exact same geographic and temporal dimensions. Source: [xarray](https://docs.xarray.dev/en/stable/user-guide/data-structures.html#dataset)*
:::

### A first look in Python

The built in `air_temperature` tutorial dataset is a perfect way to see how this structure looks in practice. 

When you open the file, `xarray` loads the entire container:

```{code-cell} python
import xarray as xr

# Open the tutorial dataset container
ds = xr.tutorial.open_dataset("air_temperature")
ds
```

This object is a **Dataset**. In your Jupyter output, you will see it lists the dimensions (`time`, `lat`, `lon`), the coordinates, and a section called "Data variables". Inside that data variables section, there is a single entry called `air`. 

If you extract that specific variable using dictionary syntax, you pull out the **DataArray**:

```{code-cell} python
# Extract the single variable from the container
air_temperature_array = ds["air"]
air_temperature_array
```

```{admonition} Key distinction
:class: important

A **DataArray** is one labeled variable (like temperature).  
A **Dataset** is the collection of aligned DataArrays. Most operations you learn will work identically on both structures!
```

---

## 4. Why labels beat indices

The greatest advantage of the Data Cube model is that you stop writing code based on computer logic and start writing code based on human logic. 

Suppose you have a pure NumPy array with the shape `(2920, 25, 53)`. To extract a single value, you must remember the exact numerical position for every single axis.

```python
# Pure NumPy: You must memorize that axis 0 is time, 1 is lat, 2 is lon
temperature = air_matrix[0, 2, 3]
```

That works, but it is highly prone to silent errors. Did you just select the first day, or the first latitude? `xarray` solves the *"what does axis 0 mean again?"* problem by offering extremely flexible routines that combine the speed of NumPy with the labels of Pandas.

### Positional selection (`isel`)

If you know the exact numerical position of your data but do not want to guess the axis order, you use **Index Selection** (`isel`). You provide the integer position, but explicitly name the dimension.

```{code-cell} python
# Using isel: The axis order no longer matters!
air.isel(time=0, lat=2, lon=3)
```

### Label selection (`sel`)

The true superpower of `xarray` is **Label Selection** (`sel`). In label selection, the element position is automatically looked up from the coordinate values. You simply ask for exactly what you want.

```{code-cell} python
# Using sel: Selecting data using explicit human-readable labels
air.sel(time="2013-01-01", lat=73.14, lon=52.53, method="nearest")
```

This labeled approach is infinitely safer. It documents your code naturally and allows you to easily take geographic or temporal "slices" (for example, requesting all temperatures from `slice("2013-01-01", "2013-01-10")`).

```{admonition} What does the asterisk (*) mean?
:class: note

When you print a Dataset or DataArray, you will often see an asterisk `*` next to the coordinate names (e.g., `* time`). 

This indicates it is an **Indexed Coordinate**. Under the hood, `xarray` has built a highly optimized search index (similar to a database) for that specific dimension. This is what allows the `.sel()` method to find your specific dates and latitudes instantly without slowing down your computer. 
```

### Why this matters in practice

Named dimensions become especially valuable when:
* datasets have many overlapping axes
* you are combining multiple variables
* you resample or aggregate data across time
* you return to your code after a few weeks and still want to understand it

If your spatial analysis depends on remembering what each axis integer means, your code is already more fragile than it needs to be.

---

## 5. Multidimensional data formats


`xarray` is domain agnostic. It acts as a universal translator that reads from and writes to a variety of scientific file formats. Because multidimensional environmental datasets are massive and often heterogeneous, these file formats use hierarchical structures—meaning they organize data into "groups" that act exactly like folders on your computer.

Depending on your project, you will encounter four major storage formats:

* **GeoTIFF and COG (`.tif`)**: You already know GeoTIFFs from the previous lesson. They map perfectly to a single `xarray.Variable`. However, TIFFs are inherently two dimensional per band. They have no native concept of a time axis or a vertical altitude axis. If you need 4D data, you must move beyond TIFFs. A Cloud Optimized GeoTIFF (COG) is a modern upgrade that allows you to stream specific geographic windows over the internet, which `xarray` handles transparently.
* **HDF5 (`.h5` or `.hdf5`)**: The Hierarchical Data Format is a heavy duty, general purpose container for large scientific data. It behaves exactly like a UNIX filesystem. It contains "Groups" (folders), "Datasets" (multidimensional arrays), and "Attributes" (metadata). It supports advanced chunking and compression, making it a powerhouse for complex, nested data structures.
* **NetCDF4 (`.nc`)**: The classic standard in climate and oceanography. Interestingly, modern NetCDF4 is actually built directly on top of HDF5! It is an "opinionated subset" of HDF5 that enforces strict rules about how dimensions and coordinates must be defined. Because it requires explicit dimension scales, it maps perfectly to the `xarray` Dataset structure.
* **Zarr (`.zarr`)**: The modern format built for the cloud. While HDF5 and NetCDF are traditionally single massive files, Zarr stores data as a tree of groups holding arbitrary JSON metadata and thousands of tiny, separate chunked arrays. If you want to analyze a ten year temperature trend for one specific city, Zarr allows `xarray` to stream just the tiny chunks for that specific location directly from a remote server without downloading the rest of the globe.

```{admonition} The core takeaway
:class: note

Your code will use `xarray` to do the thinking, the labeling, and the math in memory, but it will rely on formats like GeoTIFF, HDF5, NetCDF, and Zarr to persistently and safely store those multidimensional results on disk.
```

---

## 6. Exercise: Inspecting a data cube

It is time to see a real data cube in action. `xarray` includes a few built in tutorial datasets so you can practice navigating multidimensional spaces without downloading large files.

Your task is to load the standard air temperature dataset and inspect its structure.

```{code-cell} python
import xarray as xr

# Load the tutorial data cube
ds = xr.tutorial.open_dataset("air_temperature")

# Print the dataset representation to the screen
ds
```

Look closely at the output in your Jupyter notebook. 

**Your task:**
Identify the following components in the printed output:
1. What are the three **Dimensions** of this cube?
2. What are the specific **Coordinates** defining the spatial resolution?
3. What is the name of the **Data variable** held inside this container?
4. Can you find the metadata **Attributes** explaining who created the data?

````{admonition} Sample solution
:class: dropdown

When you run the code, you will see an interactive HTML representation of the Dataset. 

1. **Dimensions:** The cube is built on `lat` (latitude), `lon` (longitude), and `time`.
2. **Coordinates:** You can see that `lat` runs from 75.0 down to 15.0, and `time` covers the entire year of 2013 and 2014.
3. **Data variables:** There is one variable inside this container called `air`.
4. **Attributes:** By clicking the document icons on the right side of the output, you can read metadata stating the data comes from the "NMC reanalysis".

**Accessing data programmatically**

While the interactive HTML output is fantastic for exploring visually, you will often need to access this metadata directly in your code to automate your spatial analysis. You can tap into all of this information using the following properties:

```{code-cell} python
# 1. Print the dimensions
print(ds.dims)

# 2. Print the coordinates
print(ds.coords)

# 3. List the data variables
print(list(ds.data_vars))

# 4. Access a specific attribute
print(ds.attrs.get("description"))
```

**Why this is powerful:** In one glance, you understand the entire spatial and temporal scope of the dataset. Because `xarray` makes this context accessible to both your eyes and your code, your scripts can automatically adapt to the data structure. If this were a raw NumPy array, you would only see `(2920, 25, 53)` and have absolutely no idea what those numbers represent or what the matrix contains.
````

---

## 7. Summary

The Data Cube model is a structural paradigm that combines fast matrix operations with explicit spatial and temporal labels using the `xarray` library. 

* **The Third Dimension:** Adding dimensions (like time or altitude) transforms a static 2D raster into a dynamic, multidimensional data cube.
* **Core Structures:** A `DataArray` holds a single variable and its labels (similar to a `pandas.Series`), while a `Dataset` acts as a container for multiple perfectly aligned variables (similar to a `geopandas.GeoDataFrame`).
* **Human Logic:** Using label based selection (`.sel()`) makes spatial querying intuitive, self documenting, and infinitely safer than guessing raw NumPy integer indices.
* **Storage Formats:** While `xarray` handles the math in memory, it relies on advanced hierarchical and cloud optimized formats like GeoTIFF, HDF5, NetCDF, and Zarr to persistently store massive datasets on disk.

Now that you understand the underlying anatomy of a data cube, you are ready to learn how to actively slice, mask, and aggregate these multidimensional arrays in the next chapter.
