---
title: Crunching Numbers with NumPy

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
Meeting the mathematical engine behind raster data
</div>

---

```{admonition} Big idea
:class: tip

A raster band is, at its core, just a grid of numbers. NumPy gives you the tools to inspect, slice, transform, and analyse that grid quickly and efficiently.
```

--- 

## 1. From Lists to Arrays

To work with raster data in Python, you first need to understand the data structure that powers it. NumPy, short for Numerical Python, is the core library for numerical computing in Python. Its central object is the **array**, a fast and efficient structure for storing and manipulating large grids of numbers.

This matters because a raster band is, at its core, just a two dimensional array of values. Each cell stores a measurement for one location, such as elevation, temperature, or reflectance. If you want to work with raster data effectively, you need to be comfortable working with arrays.

You could store pixel values in ordinary Python lists, but lists are not designed for large scale numerical work. NumPy arrays are. They make calculations faster, cleaner, and easier to express.

The most important shift in thinking is this: operations on NumPy arrays are usually applied **element by element**. If you multiply an array by `2`, NumPy multiplies every value in the grid by `2`. This lets you transform entire surfaces at once without writing repetitive loops.

--- 

## 2. Creating Arrays and Grids

By convention, NumPy is usually imported with the alias `np`.

```{code-cell} python
import numpy as np
````

### Understanding dimensions

A useful way to think about a NumPy array is as a structured grid of values.

* A **one dimensional** array looks much like a list.
* A **two dimensional** array looks like a table.
* A **three dimensional** array can be imagined as a stack of tables.

NumPy generalizes this idea to any number of dimensions. That is why its core array class is called `ndarray`, short for **N dimensional array**.

Most NumPy arrays follow a few important rules:

* all elements have the same data type
* the overall size does not change after creation
* the shape is regular, not jagged

These restrictions are helpful. They allow NumPy to store data efficiently and perform calculations much faster than standard Python lists.

### Creating arrays

You can create a NumPy array directly from a Python list using `np.array()`.

```{code-cell} python
arr_1d = np.array([1, 2, 3, 4])
arr_2d = np.array([[1, 2], [3, 4]])

print("1D array:")
print(arr_1d)

print("\n2D array:")
print(arr_2d)
```

When working with raster like data, you often want to begin with a blank grid. NumPy provides simple ways to generate these starting structures:

* `np.zeros()` creates an array filled with zeros
* `np.ones()` creates an array filled with ones
* `np.arange()` creates a regular numeric sequence

```{code-cell} python
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
sequence = np.arange(0, 10, 2)

print("Zeros:\n", zeros)
print("\nOnes:\n", ones)
print("\nSequence:\n", sequence)
```

### `arange()` vs. `linspace()`

Both `np.arange()` and `np.linspace()` create sequences, but they work a little differently.

* Use **`np.arange()`** when you want to control the **step size**
* Use **`np.linspace()`** when you want to control the **number of values**

Here is a simple example with `linspace()`:

```{code-cell} python
values = np.linspace(0, 10, num=5)
print(values)
```

```text
[ 0.   2.5  5.   7.5 10. ]
```

This creates five evenly spaced values between `0` and `10`, including both endpoints.

```{admonition} arange() vs. linspace()
:class: note

`np.arange(0, 10, 2)` asks:
**Start at 0, move in steps of 2, and stop before 10.**

`np.linspace(0, 10, num=5)` asks:
**Start at 0, end at 10, and create exactly 5 evenly spaced values.**

``` 

### Reshaping arrays

Once you have created a one dimensional sequence, you can reorganize it into a two dimensional grid using `reshape()`.

This is especially useful when flat data need to be turned into a matrix.

:::{figure} images/02_np_reshape.png
:alt: Diagram illustrating a 1D array of numbers 1 through 6 being reshaped into a 2x3 matrix and a 3x2 matrix.
:width: 700px
:align: center

*Visualizing array restructuring: A one dimensional sequence of 6 elements can be instantly reshaped into a grid of 2 rows and 3 columns, or 3 rows and 2 columns. Source: [Numpy](https://numpy.org/devdocs/user/absolute_beginners.html#transposing-and-reshaping-a-matrix)*
:::

```{code-cell} python
# Create a 1D sequence from 1 to 6
sequence = np.arange(1, 7)

# Reshape the sequence into a 2x3 grid
grid_2x3 = sequence.reshape((2, 3))
print("2x3 grid:\n", grid_2x3)

# Reshape the same sequence into a 3x2 grid
grid_3x2 = sequence.reshape((3, 2))
print("\n3x2 grid:\n", grid_3x2)
```

```text
2x3 grid:
 [[1 2 3]
  [4 5 6]]

3x2 grid:
 [[1 2]
  [3 4]
  [5 6]]
```

A result like this is already starting to look like a tiny raster band: a regular grid of values arranged by rows and columns. At this stage, however, it is still just a numerical array. The spatial meaning comes later, when coordinates, resolution, and other raster metadata are added.

--- 

## 3. Array Properties: First Checks

Whenever you create or load a new array, it is good practice to inspect its basic structure first. This helps you confirm exactly what kind of object you are working with and how the data is organized.

You can use the built in Python `type()` function to confirm that the object is indeed a NumPy array. After that, four key attributes will tell you everything you need to know about the array's geometry:

* **`.ndim`**: Tells you the number of dimensions the array has. For example, a flat sequence is 1D, while a spatial grid is 2D.
* **`.shape`**: Returns a tuple specifying the number of elements along each dimension. For a 2D array, this represents the number of rows and columns (for example, `(3, 4)`).
* **`.size`**: Tells you the fixed, total number of individual elements inside the entire array.
* **`.dtype`**: Because NumPy arrays are typically homogeneous (containing elements of only one data type), this attribute tells you exactly what kind of data is stored inside, such as integers or floats.

This quick "first check" is one of the most useful debugging habits you can build before you start performing map algebra on large raster datasets.

```{code-cell} python
print(f"Type: {type(grid_3x2)}")
print(f"Dimensions: {grid_3x2.ndim}")
print(f"Shape: {grid_3x2.shape}")
print(f"Size: {grid_3x2.size}")
print(f"Data type: {grid_3x2.dtype}")
```

```text
Type: <class 'numpy.ndarray'>
Dimensions: 2
Shape: (3, 2)
Size: 6
Data type: int64
```

--- 

## 4. Indexing, Slicing, and Updating

One of NumPy’s greatest strengths is that it makes it easy to access, extract, and modify selected parts of an array. This is essential for raster work, where you often want to inspect a single cell, extract an analysis window, or update a group of pixels.

NumPy arrays are **zero indexed**, so the first row and first column both start at index `0`.

```{admonition} Big idea
:class: tip

Indexing selects one position. Slicing selects a range of positions. In raster terms, indexing gives you a single cell, while slicing gives you an entire row, column, or spatial window.
```

### Indexing in one dimension

Before working with grids, it helps to recall how indexing works in a simple one dimensional array.

```{code-cell} python
data = np.array([1, 2, 3])

print(data[0])    # first value
print(data[1])    # second value
print(data[0:2])  # first two values
print(data[1:])   # everything from index 1 onward
print(data[-2:])  # last two values
```

```text
1
2
[1 2]
[2 3]
[2 3]
```

:::{figure} images/03_np_indexing.png
:alt: Diagram showing how a 1D array can be sliced using indices like data[0:2], data[1:], and data[-2:].
:width: 700px
:align: center

*Visualizing array slicing: You can use start and end indices to extract specific sections of an array. Source: [Numpy](https://numpy.org/devdocs/user/absolute_beginners.html#indexing-and-slicing)*
:::

A few useful patterns appear here:

* `data[0]` selects the first value
* `data[0:2]` selects from index `0` up to, but not including, index `2`
* `data[1:]` means from index `1` to the end
* `data[-2:]` means the last two values

The most important rule in Python slicing is that the **stop value is excluded**. So `data[0:2]` includes indices `0` and `1`, but never `2`.

### Accessing single values in two dimensions

In a two dimensional array, you specify both the row and column position inside one pair of square brackets.

```{code-cell} python
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Access the element in the first row and second column
value = grid[0, 1]
print(value)
```

```text
2
```

The index order is always `[row, column]`. Therefore, `grid[0, 1]` means row `0` and column `1`, which returns the value `2`.

```{admonition} Note
:class: note

For two dimensional arrays, it is helpful to always read the indices out loud as `[row, column]`. This exactly matches how raster grids are accessed in spatial algorithms.
```

### Slicing rows, columns, and windows

Slicing lets you extract subsets of an array using the `:` symbol. In two dimensions, you can slice rows and columns at the very same time.

```{code-cell} python
# Slice the first two rows and all columns
top_rows = grid[:2, :]

# Slice from row 1 onward, and the first two columns
bottom_left_window = grid[1:, :2]

# Slice a 2x2 window from the upper left
window = grid[:2, :2]

print("Top rows:\n", top_rows)
print("\nBottom left window:\n", bottom_left_window)
print("\n2x2 window:\n", window)
```

```text
Top rows:
 [[1 2 3]
  [4 5 6]]

Bottom left window:
 [[4 5]
  [7 8]]

2x2 window:
 [[1 2]
  [4 5]]
```

This is the foundational pattern for extracting analysis windows or cropping regions of interest from large raster files. A few common patterns include:

* `grid[:2, :]` → first two rows, all columns
* `grid[:, :2]` → all rows, first two columns
* `grid[1:, :]` → everything from row `1` onward
* `grid[1:3, 1:3]` → a rectangular inner window

### Updating values

You can use indexing and slicing not only to read values, but also to instantly change them.

```{code-cell} python
# Set a specific cell to 10
grid[2, 2] = 10

# Update a 2x2 window to 5
grid[0:2, 0:2] = 5

print(grid)
```

```text
[[ 5  5  3]
 [ 5  5  6]
 [ 7  8 10]]
```

This kind of targeted updating is highly useful when simulating terrain anomalies, applying nodata masks, or fixing selected raster cells.

### Boolean indexing

NumPy also allows you to select values based on specific mathematical conditions. This is called **boolean indexing**.

```{code-cell} python
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(a[a < 5])
print(a[a >= 5])
```

```text
[1 2 3 4]
[ 5  6  7  8  9 10 11 12]
```

A condition such as `a < 5` actually creates a temporary boolean array of the exact same shape, filled entirely with `True` and `False` values. NumPy then applies that mask over your original array to return only the matching values.

This technique is extremely useful in spatial data science. For example, you can use it to:

* Select all elevation values above a specific height threshold
* Find all pixels representing snow cover
* Isolate all cells containing missing or invalid sensor data

You can also combine multiple conditions using `&` (and) or `|` (or):

```{code-cell} python
selected = a[(a > 2) & (a < 11)]
print(selected)
```

```text
[ 3  4  5  6  7  8  9 10]
```

This kind of targeted updating is useful when simulating terrain, applying masks, or changing selected raster cells.

--- 

## 5. Array Math, Functions, and Summaries

NumPy is powerful because it lets you apply mathematical operations to entire arrays at once.

### Scalar and element wise math

If you combine an array with a single number, that operation is applied to every value in the array.

```{code-cell} python
# Scalar math: multiply all pixels by 2
doubled_grid = grid * 2

# Scalar math: add 10 to all pixels
offset_grid = grid + 10

print(doubled_grid)
print(offset_grid)
```

You can also combine two arrays of the same shape in an element wise way.

### Mathematical functions

NumPy also includes many ready made mathematical functions that work directly on arrays. For example, you can take square roots with `np.sqrt()` or apply a logarithmic transformation with `np.log1p()`.

This is especially useful in spatial data science, where raster processing often involves transforming values before analysis or visualization.

### Summary statistics

Once you have a grid of values, you often want quick summaries. NumPy makes this easy.

```{code-cell} python
print(f"Min elevation: {grid.min()}")
print(f"Max elevation: {grid.max()}")
print(f"Mean elevation: {grid.mean()}")
print(f"Median elevation: {np.median(grid)}")
print(f"Standard deviation: {np.std(grid)}")
```

These kinds of summaries are common in raster analysis, for example when describing elevation, temperature, or vegetation values across a study area.

--- 

## 6. Missing Data and Filtering

Real world spatial data is rarely complete. Some cells may have no valid value because of sensor failure, clouds, shadows, or gaps at the edge of a dataset.

In many datasets, missing values are stored using special placeholder numbers such as `-999`. In NumPy, a more standard way to represent missing numerical values is `np.nan`, which stands for “Not a Number”.

Another important idea is **filtering**. NumPy allows you to create Boolean masks by comparing the array to a condition. The result is an array of `True` and `False` values, which you can then use to select only the cells that meet your condition.

```{code-cell} python
# Create a boolean mask and filter values greater than 4
high_values = grid[grid > 4]
print(high_values)
```

This is a simple example, but the idea is extremely important. Boolean masks are the foundation for many raster operations, such as thresholding, classification, and masking unwanted areas.

---

## 7. Exercise: A Tiny Elevation Raster

You are given a tiny elevation raster for a mountain valley. Your task is to build the grid, inspect its structure, and identify the higher ground that might remain dry during heavy rainfall.

**Tasks:**

1. Create a `6 x 6` array filled with zeros.
2. Raise the center `2 x 2` cells to an elevation of `5`.
3. Set one center cell to `9` as the highest point.
4. Check the array’s `.shape`, `.ndim`, and `.dtype`.
5. Slice out the center `4 x 4` area.
6. Raise the terrain by `2` meters everywhere.
7. Calculate the minimum, maximum, and mean elevation.
8. Create a Boolean mask for all cells with elevation greater than `4`.
9. Assign `np.nan` to one corner cell to represent missing data.

```{code-cell} python
# --- Your Solution Here ---
```

---

## 8. Summary: Arrays Before Spatial Metadata

At this point, you have learned the core mechanics of NumPy arrays:

* how to create them
* how to inspect their structure
* how to slice and update selected values
* how to apply mathematical operations across entire grids
* how to summarise and filter them

This is the numerical foundation of raster processing in Python. A basic NumPy array can already behave like a tiny raster band: it is a regular grid of values that can be manipulated and analysed as a surface.

What it still lacks is the spatial context. At the moment, your array knows nothing about where it is in the world, how large each cell is, or which coordinate reference system it belongs to.

That is the next step. You are not leaving arrays behind. You are simply about to add spatial metadata and geographic file handling on top of the same array mechanics you now understand.


