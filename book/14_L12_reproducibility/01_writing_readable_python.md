---
title: Writing readable Python

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
Code style as a tool for clarity, debugging, and scientific trust
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/14_L12_reproducibility/01_writing_readable_python.ipynb)

---

```{admonition} Big idea
:class: tip

Readable code reduces errors, speeds up debugging, and makes spatial workflows easier to understand, maintain, and rerun.
```

By now, you can write Python that reads data, processes vectors and rasters, builds data cubes, and models objects with classes. That is a major step. But there is an important difference between code that merely **works** and code that is genuinely **good to work with**.

In spatial data science, you rarely write code only once. Often, you come back to it later. You adapt it for a new study area. You share it with classmates, project partners, instructors, or your future self. At that point, readability stops being cosmetic. It becomes a scientific advantage.

This chapter introduces practical conventions for writing clearer Python. These are not arbitrary rules. They are small design decisions that make code easier to scan, easier to debug, and easier to trust. The central reference for this is **PEP 8**, the [official Python style guide](https://peps.python.org/pep-0008/), but we will keep the discussion grounded in real geospatial examples rather than extended formatting rules.

---

## 1. Readability first

A useful starting point for this chapter is a famous "Easter egg" built directly into the language, known as *The Zen of Python*:

```{code-cell} python
import this
```

Among the philosophical guidelines printed by `import this`, two are especially relevant here:

* **Readability counts.**
* **Simple is better than complex.**

These are not just slogans for beginners. They are practical, everyday design principles. 

In geospatial analysis, unreadable code creates real friction:

* you forget what a vaguely named variable actually contains
* you mix up $x$ (Easting) and $y$ (Northing) coordinate orders
* you lose track of which variables are projected and which are in geographic degrees
* you spend more time debugging your naming conventions than your actual spatial logic
* you hesitate to reuse your own code because it feels too opaque

Readable code eliminates that friction.

```{admonition} Style is not decoration
:class: important

Code style is not mainly about making notebooks look pretty. It is about reducing ambiguity. Clear code helps other people understand your logic, but it also helps you think more clearly while writing it.
```

---

## 2. Naming conventions

Most readability problems begin with naming. Choosing good names for your variables, functions, and classes is one of the most impactful things you can do for your code. A good name tells the reader exactly what the object contains or what the function does, without needing a comment. 

Python has specific capitalization conventions to help readers instantly understand what type of object they are looking at:

### Variables and functions: `snake_case`

Use all lowercase, separated by underscores. This is the standard style for almost all the day-to-day code you will write.

```{code-cell} python
station_id = "ZH_001"
mean_temperature_c = 14.2

def calculate_bbox_area(width_m, height_m):
    return width_m * height_m
```

### Classes: `CamelCase`

Capitalize each word, with no underscores. This visually separates your custom object templates from standard variables.

```{code-cell} python
class WeatherStation:
    pass

class RasterTile:
    pass
```

### Constants: `UPPER_SNAKE_CASE`
Values that should not change during the execution of your script are defined at the top of the file in all caps.

```{code-cell} python
TARGET_CRS = "EPSG:2056"
MAX_CLOUD_COVER = 20
```

### Geospatial naming and intent

When dealing with spatial data, it is incredibly easy to end up with a mess of single-letter variables like `x`, `p`, `b`, and `c`. If a variable name is vague, every later line becomes harder to interpret. 

Instead, use descriptive names that specify the data type, context, or units.

**Bad: Cryptic and requires the reader to guess the context**
```{code-cell} python
b = [2500000, 2750000, 1150000, 1300000]
r = "landsat.tif"
df = gpd.read_file("data.shp")
```

**Good: Explicit, clear, and context-rich**
```{code-cell} python
study_area_bbox = [2500000, 2750000, 1150000, 1300000]
landsat_raster_path = "landsat.tif"
roads_gdf = gpd.read_file("roads_epsg2056.shp")
```

Adding `_gdf` for GeoDataFrames, `_df` for standard DataFrames, or specifying units like `_m` or `_c` directly in the variable name saves your collaborators (and your future self) from constantly checking the source data. 

A good variable name does not merely describe the data type; it describes its *role* in the workflow.

```{admonition} A practical test
:class: note

If someone saw your variable name in isolation, would they know roughly what it represents? If not, the name is probably too vague.
```

---

## 3. Indentation, whitespace, & line length

Readable code is not only about naming. It is also about visual structure. Python enforces indentation syntactically, but it does not force you to format the inside of your blocks clearly. That part is your responsibility.

### Use four spaces per indentation level

PEP 8 recommends exactly four spaces for each indentation level.

```{code-cell} python
for city in ["Zurich", "Bern", "Basel"]:
    if city.startswith("B"):
        print(city)
```

**Prefer spaces over tabs:** Tabs can display differently across different text editors and operating systems. Spaces are universally reliable. Most modern editors (like Jupyter or VS Code) are already configured to convert the Tab key into 4 spaces automatically.

### Use whitespace to reveal structure

Whitespace helps the eye separate concepts. Surround mathematical and assignment operators with a single space.

**Bad: Cramped and hard to read**
```{code-cell} python
xmin=2550000
ymin=1080000
xmax=2750000
ymax=1180000
width=xmax-xmin
height=ymax-ymin
area=width*height
```

**Good: Space allows the eye to parse operations naturally**
```{code-cell} python
xmin = 2550000
ymin = 1080000
xmax = 2750000
ymax = 1180000

width = xmax - xmin
height = ymax - ymin
area = width * height
```

The second version is much easier to scan because the spacing makes the mathematical operations visually distinct.

### Use blank lines to separate logical blocks

A long, uninterrupted code cell is hard to read, even if every line is technically correct. Use blank lines to separate the logical "steps" of your workflow.

```{code-cell} python
xmin = 2550000
ymin = 1080000
xmax = 2750000
ymax = 1180000

width = xmax - xmin
height = ymax - ymin

area_sq_km = (width * height) / 1_000_000

print(f"Area: {area_sq_km} sq km")
```

Those blank lines act like paragraphs, signaling meaningful steps:

1. define inputs
2. compute intermediate dimensions
3. compute final result
4. display result

### Keep lines reasonably short

PEP 8 traditionally recommends a maximum line length of 79 characters. In practice, many modern data science teams relax this to 88 or 100 characters. Regardless of the exact limit, scrolling horizontally to read a long line of code is universally frustrating.

There are two great ways to fix long lines in spatial workflows:

**1. Break expressions cleanly using parentheses**
When you pass multiple arguments to a spatial function, do not let them run off the screen. Break the expression across multiple lines. Python automatically joins lines that are wrapped inside parentheses `()`, brackets `[]`, or braces `{}`.

```{code-cell} python
# Bad: A long, unbroken line that runs off the screen
intersected_gdf = gpd.overlay(buildings_gdf, study_area_gdf, how="intersection", keep_geom_type=True)

# Good: Cleanly broken inside parentheses for high visibility
intersected_gdf = gpd.overlay(
    buildings_gdf, 
    study_area_gdf, 
    how="intersection", 
    keep_geom_type=True
)
```

Notice how we avoid using the backslash `\` line continuation character. Relying on parentheses is cleaner, safer, and explicitly recommended by Python style guides.

**2. Extract intermediate variables**
Sometimes, a line is too long because it is doing too much math at once.

```{code-cell} python
# Bad: Too much logic crammed into one line
mean_ndvi = (nir_band.astype("float32") - red_band.astype("float32")) / (nir_band.astype("float32") + red_band.astype("float32"))
```

```{code-cell} python
# Good: Conceptually clearer with intermediate steps
nir = nir_band.astype("float32")
red = red_band.astype("float32")

mean_ndvi = (nir - red) / (nir + red)
```

```{admonition} Readability often improves the logic
:class: tip

When a line becomes too long, the problem is sometimes not just formatting. It may be a sign that too much is happening at once. Splitting a long expression into intermediate variables can make the code easier to understand and the analysis easier to explain.
```

---

## 4. Comments vs docstrings

Comments and docstrings both explain code, but they serve entirely different purposes. Understanding when to use which keeps your codebase clean and professional.

### Comments explain *why*

Inline comments (starting with `#`) should help the reader understand your intent, scientific assumptions, or unusual logic. They should *not* state the obvious. A bad comment simply translates the Python syntax into English.

**Bad: Repeats the code**
```{code-cell} python
# Create a list called summer_months
summer_months = [6, 7, 8]
```

**Good: Explains the scientific intent**
```{code-cell} python
# Use only summer scenes to reduce snow contamination in the optical bands
summer_months = [6, 7, 8]
```

Use a comment when you need to clarify a tricky line of code, explain a methodological choice, or warn a future developer about a potential edge case.

### Docstrings explain *what* and *how to use*

As you learned in the [chapter on Functions](https://hendrikwulf.github.io/sds210-jb/book/l04-functions/documentation/#id-1-docstrings-the-standard-of-reproducibility), a docstring (enclosed in triple quotes `"""`) acts as the official manual for a function, method, or class. 

For spatial data science, the **NumPy docstring style** is the gold standard. It uses clean, readable headers to define the inputs and outputs. Let us write an NDSI (Normalized Difference Snow Index) calculator to meet this standard of reproducibility:

```{code-cell} python
def calculate_ndsi(green_band, swir1_band):
    """
    Calculates the Normalized Difference Snow Index (NDSI).
    
    Parameters
    ----------
    green_band : numpy.ndarray
        Green band array.
    swir1_band : numpy.ndarray
        Shortwave-infrared (SWIR1 at 1.6 µm) band array.
        
    Returns
    -------
    numpy.ndarray
        NDSI values ranging from -1 to 1.
    """
    import numpy as np
    
    # Suppress divide-by-zero warnings for NoData pixels or edge cases
    np.seterr(divide='ignore', invalid='ignore')
    
    return (green_band - swir1_band) / (green_band + swir1_band)
```

### When to use which: A combined example

The best geospatial scripts use docstrings and comments together in harmony. 

Look at this bounding box function. The **docstring** acts as the instruction manual for the user, while the **comment** acts as a clarifying note for anyone modifying the source code:

```{code-cell} python
def point_in_bbox(x, y, bbox):
    """
    Return True if a point lies inside a bounding box.

    Parameters
    ----------
    x, y : float
        Point coordinates in the same CRS as the bounding box.
    bbox : dict
        Dictionary with keys 'xmin', 'ymin', 'xmax', 'ymax'.
        
    Returns
    -------
    bool
        True if the point is inside, False otherwise.
    """
    # Use <= instead of < to ensure points exactly on the boundary are included
    return (
        bbox["xmin"] <= x <= bbox["xmax"]
        and bbox["ymin"] <= y <= bbox["ymax"]
    )
```

```{admonition} A useful distinction
:class: note

**Comments** are mainly for *readers* and *maintainers* of the source code.  
**Docstrings** are mainly for *users* of the function, method, or class.
```

---

## 5. Consistency within a project

PEP 8 includes a famous piece of advice: *"A foolish consistency is the hobgoblin of little minds."* While the guidelines in this chapter represent industry best practices, the ultimate goal is always readability. If you join an existing geospatial project where the team uses a slightly different naming convention, or prefers 100-character line lengths, follow their style. **Consistency *within* a single project or script is always more important than strict adherence to a global rule.**

A project becomes much easier to navigate when the same ideas are expressed in the exact same way throughout.

### Be consistent with names

If you use `bbox` in one notebook, do not switch to `extent`, `window`, and `area_box` later unless they genuinely mean different things. 

If you use `x` and `y` for projected coordinates, do not silently switch to `lon` and `lat` unless the CRS has actually changed to geographic degrees.

### Be consistent with units

A variable like `distance` is ambiguous. A variable like `distance_m` is immediately clear. 

Appending units to your spatial variables helps the reader instantly understand the math:
* `elevation_m`
* `temperature_c`
* `area_sq_km`

### Be consistent with CRS handling

Spatial code becomes unreadable very quickly when CRS logic is implicit or vaguely named.

**Bad: Forces the reader to remember which is which**
```{code-cell} python
crs1 = "EPSG:4326"
crs2 = "EPSG:2056"
```

**Good: Explicitly defines the workflow's intent**
```{code-cell} python
source_crs = "EPSG:4326"
target_crs = "EPSG:2056"
```

### Be consistent with notebook structure

In spatial data science, a typical notebook works best when it follows a predictable pattern. Establishing a standard flow reduces friction for anyone reading your work:

1. Imports and environment setup
2. Defining global constants (e.g., `TARGET_CRS`, file paths)
3. Reading input data
4. Preprocessing and cleaning
5. Spatial analysis
6. Visualization and export

### A small project style guide helps

Even for student work, it is worth deciding early with your project partners:
* how variables will be named
* how CRS strings will be represented
* whether file paths are relative or absolute
* how outputs will be named

Choose a readable style, apply it consistently, and free up your mental energy to focus on solving spatial problems!

```{admonition} Consistency beats novelty
:class: important

In a project, it is always better to follow one simple naming and formatting pattern consistently than to use a slightly different, "clever" pattern in every file.
```

---

## 6. Exercise: A geospatial makeover

To see these principles in action, it is time to perform a "code makeover." 

Spatial analysis often produces long, complex expressions like chained pandas methods or multi-condition masks. It is very easy to write a script that technically works but is a nightmare to read.

### Warm-up example

Look at this incredibly dense one-liner. It uses semicolons to cram multiple commands onto a single line, completely hiding the spatial logic:

**Before (Hard to read and debug):**
```{code-cell} python
import geopandas as gpd
gdf=gpd.read_file("data/buildings.gpkg").to_crs("EPSG:2056");gdf["area_m2"]=gdf.geometry.area;gdf=gdf[gdf["area_m2"]>100];gdf.plot(column="area_m2",legend=True)
```

**After (Clean and reproducible):**
```{code-cell} python
import geopandas as gpd

buildings_gdf = gpd.read_file("data/buildings.gpkg")
buildings_gdf = buildings_gdf.to_crs("EPSG:2056")

# Calculate area and filter out small sheds/artifacts
buildings_gdf["area_m2"] = buildings_gdf.geometry.area
large_buildings_gdf = buildings_gdf[buildings_gdf["area_m2"] > 100]

large_buildings_gdf.plot(column="area_m2", legend=True)
```
Both versions execute exactly the same mathematical operations. But the second version is infinitely easier to read, debug, and hand over to a colleague.

---

### Task

Below is a deliberately messy geospatial code snippet. Your task is to rewrite it into a clearer version **without changing what it does**. 

Apply the ideas from this chapter, focusing specifically on:
1. Clearer variable names (e.g., using `_gdf` or `_m` suffixes).
2. Proper spacing and indentation.
3. Breaking up long, cramped logic.
4. Adding strategic comments to explain the *why*.

#### The messy code

```{code-cell} python
import geopandas as gpd
fp="data/stations.gpkg"
d=gpd.read_file(fp).to_crs("EPSG:2056")
d["d"]=d.geometry.distance(d.geometry.iloc[0])
d=d[d["d"]<50000]
print(d[["station_id","d"]])
```

#### Starter code

```{code-cell} python
import geopandas as gpd

# Rewrite the messy workflow here...
```

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
import geopandas as gpd

# Read the station data and project it to the Swiss coordinate system
stations_gdf = gpd.read_file("data/stations.gpkg")
stations_gdf = stations_gdf.to_crs("EPSG:2056")

# Calculate the distance from each station to the first station in the dataset
reference_geom = stations_gdf.geometry.iloc[0]
stations_gdf["distance_m"] = stations_gdf.geometry.distance(reference_geom)

# Filter the dataset to keep only stations within a 50 km radius
nearby_stations_gdf = stations_gdf[stations_gdf["distance_m"] < 50000]

print(nearby_stations_gdf[["station_id", "distance_m"]])
```
````

```{admonition} Reflection
:class: note

Notice that the improved version is slightly longer than the original messy script. When writing readable Python, the goal is not to use as few lines as possible. Most of the additional lines do not add complexity—they add clarity.
```

---

## 7. Summary

Readable Python is easier to debug, easier to explain, and easier to trust.

In this chapter, you learned that:
* **Good names make code self-explanatory:** Using descriptive spatial names and explicit suffixes (like `_gdf` or `_m`) prevents ambiguity and cognitive load.
* **Visual structure matters:** Consistent spacing, indentation, and cleanly broken expressions reveal the logical flow of your operations.
* **Comments and docstrings serve different purposes:** Inline comments explain the *why* behind a specific scientific choice, while docstrings explain the *what* and *how* for anyone using your tools.
* **Consistency is key:** Establishing clear, project-wide patterns for CRS handling, units, and notebook structure is more important than strict adherence to external rulebooks.

These habits may seem small, but they have massive effects. In spatial data science, many bugs and misunderstandings stem not from complex algorithms, but from code that is simply too cluttered to read clearly.

### What comes next

Readable code is the foundation of reproducible work. In the next chapter, we will move from code style to project structure and scientific reproducibility: how to organize analysis so that others can follow it, rerun it, and trust the results.
