---

title: Practical L2 - Solutions

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
From single variables to structured spatial calculations
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/09_practical-L2-solution.ipynb)

## Learning objectives

After completing this practical, you will be able to:

- define and name variables clearly
- choose appropriate data types for spatial attributes
- group related values using lists and dictionaries
- perform simple numeric expressions on spatial data
- calculate **Manhattan** and **Euclidean** distances using coordinates
- store computed results in a structured and reusable way

---

## Practical storyline

In this practical, you will gradually build a **small spatial data model** for three Swiss cities  
(**Zurich, Lugano, Geneva**).

You will start with **single variables**, then group values into **lists**, and finally organise everything into **dictionaries**, ending with distance calculations between cities.

This mirrors how spatial data handling evolves in real projects.

---

## Part 1 – Single-value variables

Single variables store exactly one value. They are useful for names, labels, and individual measurements.

### Code

```{code-cell} python
# City names
z = "Zurich"
g = "Geneva"
l = "Lugano"

print(z, g, l)

```

### Tasks

1. Change the order of the printed city names.
2. The variable names `z`, `g`, and `l` are poor choices. Rename them to better follow the descriptive naming conventions learned earlier in this chapter.
3. Add a short comment explaining what each variable represents.

---

``````{admonition} Sample solution – Part 1
:class: dropdown

```{code-cell} python
# Renamed variables to be clear and descriptive
city_zurich = "Zurich"    # name of the city Zurich
city_geneva = "Geneva"    # name of the city Geneva
city_lugano = "Lugano"    # name of the city Lugano

# Print in a different order
print(city_lugano, city_zurich, city_geneva)
```

Each variable now clearly describes what it stores, making the code much easier to read for someone else (or yourself in six months!).

``````

---

## Part 2 – Variables and formatted output

Variables can also store numeric values, which can be combined with text to create human-readable output.

### Code

```{code-cell} python
# Approximate travel distances (km)
dist_zurich_geneva = 280
dist_zurich_lugano = 205
dist_geneva_lugano = 370

# Old-style concatenation (assuming you used the updated variable names from Part 1)
print("The distance from " + city_zurich + " to " + city_geneva + " is " + str(dist_zurich_geneva) + " km")

```

### Tasks

1. Modify the print statement to show the distance from Zurich to Lugano.
2. Rewrite the print statement using a modern **f-string** for better readability.

---

``````{admonition} Sample solution – Part 2
:class: dropdown

```{code-cell} python
# Approximate travel distances (km)
dist_zurich_geneva = 280
dist_zurich_lugano = 205
dist_geneva_lugano = 370

# Using an f-string
print(f"The distance from {city_zurich} to {city_lugano} is {dist_zurich_lugano} km")
```

F-strings allow variables and text to be combined in a readable and compact way without having to manually convert numbers to strings using `str()`.

``````

---

## Part 3 – Expressions and data types

Numeric variables can be combined using operators to perform calculations.

### Code

```{code-cell} python
x = 2
y = x ** 2
z_val = y ** 0.5

print(f"{x} squared is {y} and the square root of {y} is {z_val}")
print(f"{x} is of type {type(x)}, {y} is of type {type(y)}, and {z_val} is of type {type(z_val)}")

```

### Tasks

1. Change the value of `x` and rerun the cell.
2. Observe how the **data types** change.
3. Explain (in a comment) why the square root results in a `float` data type even if the answer is a whole number.

---

``````{admonition} Sample solution – Part 3
:class: dropdown

```{code-cell} python
x = 5
y = x ** 2
z_val = y ** 0.5

print(f"{x} squared is {y} and the square root of {y} is {z_val}")
print(f"{x} is of type {type(x)}, {y} is of type {type(y)}, and {z_val} is of type {type(z_val)}")
```

The square root always results in a `float` because square roots inherently involve fractional calculations. Python defaults to a `float` to guarantee accuracy, as not all square roots result in perfect whole numbers.

``````

---

## Part 4 – Coordinates as lists

Some values naturally belong together, such as coordinates. Lists are a great way to group them.

### Code

```{code-cell} python
# CH1903+ coordinates (example values)
zurich_coords = [26, 12]
geneva_coords = [25, 11]
lugano_coords = [27, 10]

# Access individual coordinate values using indexing
print("Zurich x:", zurich_coords[0])
print("Zurich y:", zurich_coords[1])

```

### Tasks

1. Replace the example coordinates above with real Swiss CH1903+ values by looking them up on [map.geo.admin.ch](https://map.geo.admin.ch).
2. Add a comment explaining why a **list** (or a **tuple**) is a suitable data structure for coordinates.

---

``````{admonition} Sample solution – Part 4
:class: dropdown

```{code-cell} python
# CH1903+ coordinates (realistic values from map.geo.admin.ch)
zurich_coords = [2682217, 1247945]
geneva_coords = [2499959, 1117840]
lugano_coords = [2720031, 1098728]

# Access values
print("Zurich x:", zurich_coords[0])
print("Zurich y:", zurich_coords[1])

# A list (or tuple) is highly suitable because spatial coordinates 
# always belong together as a pair, and their specific order (x, y) is critical.
```

``````

---

## Part 5 – Organising cities

Dictionaries allow us to link **keys** (names) to **values** (coordinates), making our data much easier to query.

### Code

```{code-cell} python
cities = {
    "Zurich": zurich_coords,
    "Geneva": geneva_coords,
    "Lugano": lugano_coords
}

print(cities)

# Show what is stored in our keys and values
print(cities.keys())
print(cities.values())

# Retrieve coordinates from the dictionary
cz = cities["Zurich"]
cg = cities["Geneva"]
cl = cities["Lugano"]

```

### Tasks

1. Print the coordinates of Geneva explicitly using the dictionary.
2. Explain (in a comment) why dictionaries are more flexible and powerful than storing individual variables for every city.

---

``````{admonition} Sample solution – Part 5
:class: dropdown

```{code-cell} python
cities = {
    "Zurich": zurich_coords,
    "Geneva": geneva_coords,
    "Lugano": lugano_coords
}

# Access Geneva coordinates directly
print(cities["Geneva"])

# Retrieve and store coordinates
cz = cities["Zurich"]
cg = cities["Geneva"]
cl = cities["Lugano"]

# Dictionaries are more flexible because they allow us to look up 
# values by meaningful, structured names instead of forcing us 
# to memorize dozens of individual variable names.
```

``````

---

## Part 6 – Manhattan distance

:::{figure} images/11_distances.png
:alt: *Euclidean distance represents the shortest straight-line path between two points, while Manhattan distance calculates the distance strictly along a grid.*
:width: 500px
:align: center

*Euclidean distance represents the shortest straight-line path between two points, while Manhattan distance calculates the distance strictly along a grid.*
:::

The **Manhattan distance** measures distance by strictly following a grid (like walking city blocks). The formula is the sum of the absolute differences of their Cartesian coordinates:

$$d = |x_1 - x_2| + |y_1 - y_2|$$

> **Mathematical Trick:** To calculate the absolute value (removing any negative signs) using only basic operators, we square the difference (which forces it to be positive), and then take the square root (`** 0.5`).

### Code

```{code-cell} python
# Manhattan distance: Zurich – Lugano

dx = cz[0] - cl[0]
dx = dx ** 2
dx = dx ** 0.5  # Square root to get absolute value

dy = cz[1] - cl[1]
dy = dy ** 2
dy = dy ** 0.5  # Square root to get absolute value

manhattan_zl = dx + dy

print(f"Manhattan distance from Zurich to Lugano is {manhattan_zl}")

```

### Tasks

1. Calculate the Manhattan distance between Zurich & Geneva, and Lugano & Geneva.
2. Store the results in appropriately named new variables.

---

``````{admonition} Sample solution – Part 6
:class: dropdown

```{code-cell} python
# Manhattan distance: Zurich – Geneva
dx = cz[0] - cg[0]
dx = dx ** 2
dx = dx ** 0.5

dy = cz[1] - cg[1]
dy = dy ** 2
dy = dy ** 0.5

manhattan_zg = dx + dy

# Manhattan distance: Lugano – Geneva
dx = cl[0] - cg[0]
dx = dx ** 2
dx = dx ** 0.5

dy = cl[1] - cg[1]
dy = dy ** 2
dy = dy ** 0.5

manhattan_lg = dx + dy

print(f"Manhattan distance Zurich–Geneva: {manhattan_zg}")
print(f"Manhattan distance Lugano–Geneva: {manhattan_lg}")
```

``````

---

## Part 7 – Euclidean distance

The **Euclidean distance** calculates the straight-line distance between two points using the Pythagorean theorem:

$$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

### Code

```{code-cell} python
# Euclidean distance: Zurich – Lugano

dx = cz[0] - cl[0]
dy = cz[1] - cl[1]

euclidean_zl = (dx**2 + dy**2) ** 0.5

print(f"Euclidean distance from Zurich to Lugano is {euclidean_zl}")

```

### Tasks

1. Compute the Euclidean distance between Zurich & Geneva, and Lugano & Geneva.
2. Print both Manhattan and Euclidean distances clearly using f-strings. Which one is always shorter?

---

``````{admonition} Sample solution – Part 7
:class: dropdown

```{code-cell} python
# Euclidean distance: Zurich – Geneva
dx = cz[0] - cg[0]
dy = cz[1] - cg[1]
euclidean_zg = (dx**2 + dy**2) ** 0.5

# Euclidean distance: Lugano – Geneva
dx = cl[0] - cg[0]
dy = cl[1] - cg[1]
euclidean_lg = (dx**2 + dy**2) ** 0.5

print(f"Euclidean distance Zurich–Geneva: {euclidean_zg}")
print(f"Euclidean distance Lugano–Geneva: {euclidean_lg}")

print("\nThe Euclidean distance is always shorter (or equal) because it represents the direct, straight-line path rather than a grid-based path.")
```

``````

---

## Part 8 – Storing distance results

Computed values are also data and should be stored systematically so we can look them up later.

### Code

```{code-cell} python
distances = {
    "Zurich_Lugano": {
        "manhattan": manhattan_zl,
        "euclidean": euclidean_zl
    }
}

print(distances)

```

### Tasks

1. Extend this dictionary to include the distances for Zurich–Geneva.
2. Add the distances for Lugano–Geneva.
3. Inspect the structure and explain (in a comment) how this resembles an attribute table in GIS.

---

``````{admonition} Sample solution – Part 8
:class: dropdown

```{code-cell} python
distances = {
    "Zurich_Lugano": {
        "manhattan": manhattan_zl,
        "euclidean": euclidean_zl
    },
    "Zurich_Geneva": {
        "manhattan": manhattan_zg,
        "euclidean": euclidean_zg
    },
    "Lugano_Geneva": {
        "manhattan": manhattan_lg,
        "euclidean": euclidean_lg
    }
}

print(distances)

# This structure resembles an attribute table: 
# each outer key represents a unique entity or "row" (the city pair), 
# and the inner dictionary stores multiple attributes or "columns" for that pair.
```

``````

---

## Reflection

Take a moment to review what you've built. Answer briefly in comments or markdown:

1. Why are **lists** (or tuples) suitable for coordinates?
2. Why are **dictionaries** useful for spatial data?
3. Which step helped you most to understand how Python executes mathematical distance calculations?

---

```{admonition} Sample solution – Reflection
:class: dropdown

1. **Why are lists suitable for coordinates?** Coordinates consist of multiple values that strictly belong together. A list or tuple keeps these values in a fixed order, guaranteeing that index `0` is always X and index `1` is always Y.

2. **Why are dictionaries useful for spatial data?** Dictionaries link meaningful names (keys) to data, such as city names to coordinates or distances. This makes the data easier to query, extend, and understand, functioning exactly like attributes in a spatial dataset.

3. **Which step helped you most to understand distance calculations?** Breaking the distance calculation into separate x- and y-components (dx, dy) helped clarify how distances are mathematically derived from spatial coordinates before combining them into a final equation.

```

---

## Optional challenge

Design a single comprehensive dictionary that stores:

* city name
* coordinates
* distances to other cities

You do **not** need to automate anything yet. Focus solely on structure and clarity. How would you design the "perfect" data structure to hold all this information?

``````{admonition} Sample solution – Optional challenge
:class: dropdown

```{code-cell} python
# A highly structured dictionary centralizing all information per city
city_data = {
    "Zurich": {
        "coords": zurich_coords,
        "distances": {
            "Geneva": euclidean_zg,
            "Lugano": euclidean_zl
        }
    }
}
```

The focus here is not automation, but choosing a **clear and meaningful hierarchy**. If we added Geneva to this dictionary, it would have its own `"coords"` and `"distances"` sub-dictionary, keeping our data extremely organized.

``````