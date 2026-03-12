---

title: Practical L4

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
From repetitive scripts to reusable spatial tools
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/6_L4_functions/06_practical_L4.ipynb)

---

## Learning objectives

After completing this practical, you will be able to:

* write custom functions for both text processing and spatial math
* understand the difference between local projected distances (Euclidean) and spherical distances (Haversine)
* use the `continue` keyword to skip unwanted loop iterations and print a formatted 2D matrix
* build flexible functions using `*args` and `**kwargs`
* document your tools professionally using NumPy-style docstrings

---

## Practical storyline

Up to now, we have used simple, dummy coordinates. In the real world, spatial data comes in different coordinate reference systems (CRS).

In this practical, you will process a realistic dataset of 10 Swiss cities containing both **Swiss Grid (LV95)** coordinates and **Global Geographic (Lat/Lon)** coordinates. You will build a mini-library of functions to clean the data, calculate distances using different geometric models, compare the results in a matrix, and structure outputs flexibly.

---

## Part 1 – Assembling the realistic dataset

Instead of giving you all the data immediately, let's look at how you find it.

### Task: Find the coordinates

1. Open a new browser tab and navigate to [map.geo.admin.ch](https://map.geo.admin.ch).
2. Search for a location (e.g. "Wienacht"). Right-click on the map to find both their **CH1903+ / LV95** coordinates (meters) and their **WGS 84 (lat/lon)** coordinates (degrees).
3. Complete the dictionary below by filling in the values for your chosen place (the rest are provided to save you time).

---

```{code-cell} python
import math

swiss_cities = {
    "Zurich":   {"lv95": [2682217, 1247945], "latlon": [47.377210, 8.527313]},
    "Geneva":   {"lv95": [2499959, 1117840], "latlon": [46.204559, 6.142456]},
    "Lugano":   {"lv95": [2720031, 1098728], "latlon": [46.029430, 8.988879]},
    "Basel":    {"lv95": [2611415, 1267104], "latlon": [47.554552, 7.590273]},
    "Bern":     {"lv95": [2598634, 1200387], "latlon": [46.954559, 7.420685]},
    "Sion":     {"lv95": [2592607, 1118393], "latlon": [46.216943, 7.342848]},
    "St.Gallen":{"lv95": [2747116, 1254357], "latlon": [47.423584, 9.388511]},
    "Davos":    {"lv95": [2784107, 1182025], "latlon": [46.763954, 9.849066]},
    "Andermatt":{"lv95": [2690960, 1163987], "latlon": [46.620943, 8.626235]},
    "YourPlace":{...}
}
```

---

## Part 2 – Functions for Data Cleaning

Functions are not just for math. They are heavily used to clean and standardise data. Let's create a function that generates a standard 3-letter uppercase ID (a "gazetteer" code) for any city name to make our matrix headers shorter.

### Task: Build a string manipulation function

Write a function called `create_id` that:

* takes a string (`name`) as an argument
* chops the string so it only contains the first three letters
* converts it to uppercase (method: `.upper()`)
* returns the new string

Test it on "Geneva" (it should return "GEN").

---

```{code-cell} python
# Write your code here

```

---

## Part 3 – The Two Distance Functions

We need two different mathematical tools:

1. **Euclidean Distance:** Calculates straight lines on a flat 2D grid (perfect for LV95 coordinates in meters).
2. **Haversine Distance:** Calculates the shortest path over a sphere (required for Lat/Lon coordinates in degrees).

### Task A: The Euclidean Function

Write a function `euclidean(coords1, coords2)` that expects two lists of `[x, y]` coordinates. It should calculate the distance using the Pythagorean theorem and return the result converted from meters to kilometers (divide by 1000).

```{code-cell} python
# Write your code here

```

### Task B: The Haversine Function

The Haversine math is complex. Wrap the provided logic inside a function definition called `haversine(coords1, coords2)` and `return` the `distance`. Note that it expects `[lat, lon]`.

```{code-cell} python
# Wrap this inside a function definition:
lat1, lon1 = coords1[0], coords1[1]
lat2, lon2 = coords2[0], coords2[1]

R = 6371.0 # Earth radius in km

# Convert degrees to radians
phi1, phi2 = math.radians(lat1), math.radians(lat2)
delta_phi = math.radians(lat2 - lat1)
delta_lambda = math.radians(lon2 - lon1)

a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = R * c

```

---

## Part 4 – The Comparison Matrix

Now we will build a distance matrix. We want to iterate through all cities and calculate the distance between them using *both* distance methods to see how much the flat projection (LV95) distorts reality compared to the spherical model (Haversine).

Instead of printing a long list, we will format it as a grid (x-axis and y-axis).

### Task: Loop, compare, and print a matrix

Write a nested loop to create a **Difference Matrix** (Euclidean distance minus Haversine distance, in km).

* Use the `create_id()` function for the row and column headers.
* Use the `continue` keyword: if `city_a` is the same as `city_b`, print a `"-"` and skip to the next iteration.
* *Hint for formatting:* Use `print(f"{value:>8}", end="")` to print items in a neatly padded row without starting a new line. Use `print()` at the end of the inner loop to drop to the next row.

---

Here is a short example of how to format such a table, with explanations.  
If you find that too tricky, you can also print your results as a list.  
The table simply aids the interpretation of your results.

```{code-cell} python
# A simple list of three items
items = ["A", "B", "C"]

# TRICK 1: {:>8} 
# This tells the f-string to reserve exactly 8 spaces and align the text to the Right (>).
# TRICK 2: end=""
# This stops print() from hitting 'Enter'. It keeps the cursor on the exact same line.

print(f"{'':>8}", end="")     # Leave the top-left corner completely empty (8 spaces)
for item in items:
    print(f"{item:>8}", end="") # Print A, B, C side-by-side, each taking exactly 8 spaces
    
# TRICK 3: Empty print()
# When we call print() with nothing inside, it finally drops the cursor to the next line.
print() 
print("-" * 32)               # Print a separator line

# Now let's build the grid!
for row_item in items:
    # Print the row header on the left
    print(f"{row_item:>8}|", end="")
    
    for col_item in items:
        # TRICK 4: Handle identical pairs with a dash
        if row_item == col_item:
            print(f"{'-':>8}", end="") 
        else:
            # TRICK 5: {:>8.2f}
            # >8   = 8 spaces right-aligned
            # .2f  = format as a float with exactly 2 decimal places
            dummy_number = 3.14159
            print(f"{dummy_number:>8.2f}", end="")
            
    # The inner loop finished printing all the columns for this row.
    # Drop down to the next line before the outer loop starts the next row!
    print()

```

This is what the **output** of our example table will look like:

```text
               A       B       C
--------------------------------
       A|       -    3.14    3.14
       B|    3.14       -    3.14
       C|    3.14    3.14       -

```

You can start implementing Part 4 here:

```{code-cell} python
cities = list(swiss_cities.keys())


```

**Reflection Question:** Look at the outputs. Is the distortion uniform, or does the error increase for cities that are further apart?

---

## Part 5 – Flexible routing with `*args`

What if we want to calculate the total length of a road trip that visits multiple cities? A rigid function requires exactly two points.

### Task: Build a multi-stop calculator

Write a function called `route_length` that:

* accepts an arbitrary number of coordinate pairs using `*args`
* loops through the provided points
* calculates the distance between each consecutive point using your `haversine` function
* returns the total accumulated length of the trip

---

```{code-cell} python
# Define your route_length function here
# ...

# Extract Lat/Lon coordinates for our trip
c_basel = swiss_cities["Basel"]["latlon"]
c_bern = swiss_cities["Bern"]["latlon"]
c_sion = swiss_cities["Sion"]["latlon"]

# Test a trip from Basel -> Bern -> Sion
trip_distance = route_length(c_basel, c_bern, c_sion)
print(f"Total trip length (Basel-Bern-Sion): {trip_distance:.2f} km")
```

---

## Part 6 – Flexible metadata with `**kwargs`

Spatial data isn't just coordinates; it's also attributes (metadata) like population, elevation, or language. You can't predict what metadata a user might want to add.

### Task: Build a GeoJSON-style feature creator

Write a function called `create_spatial_feature` that:

* requires a `name` and `coordinates`
* accepts any number of extra attributes using `**kwargs`
* returns a dictionary grouping the core data and the metadata separately

---

```{code-cell} python
# Define your create_spatial_feature function here
# ...

# Let's create Geneva with some unpredictable metadata
geneva_feature = create_spatial_feature(
    "Geneva", 
    swiss_cities["Geneva"]["latlon"], 
    language="French", 
    population=201818, 
    has_lake=True
)

print(geneva_feature)
```

---

## Part 7 – Documentation (Docstrings)

A function is only as good as its documentation. In Python, we use **NumPy-style docstrings** to explain what a function does so that others (and your future self) can use it without reading the source code.

### Task: Document your distance tool

Copy your `euclidean` function from Part 3. Add a complete, formatted docstring to it (including Parameters and Returns), then test it using Python's built-in `help()` function.

---

```{code-cell} python
def euclidean(coords1, coords2):
    """
    ...
    """
   pass

# Check if Python understood your documentation!
help(euclidean)
```

---

## Reflection

Answer briefly in comments or markdown:

1. Why was it useful to turn the complex Haversine math into a function, rather than pasting it inside the nested matrix loops?
2. Explain how the `continue` keyword made your matrix loop more logical.
3. What is the difference between `*args` and `**kwargs` when building tools like `route_length` and `create_spatial_feature`?

```{code-cell} python
# Write your code here

```
---

Congratulations! You now have a solid foundation in core Python programming. You know how to store data (Variables), iterate over it (Loops), make decisions (If-statements), and package logic into reproducible tools (Functions).
