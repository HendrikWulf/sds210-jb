---
title: Practical L2 - solutions

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

You will start with **single variables**, then group values into **lists**, and finally organise
everything into **dictionaries**, ending with distance calculations between cities.

This mirrors how spatial data handling evolves in real projects.

---

## Part 1 – Single-value variables

Single variables store exactly one value.
They are useful for names, labels, and individual measurements.

### Code

```python
# City names
z = "Zurich"
g = "Geneva"
l = "Lugano"

print(z, g, l)
```

### Tasks

1. Change the order of the printed city names.
2. Add a short comment explaining what each variable represents.

---

````{admonition} Sample solution – Part 1
:class: dropdown

```{code-cell} python
# City names
z = "Zurich"    # name of the city Zurich
g = "Geneva"    # name of the city Geneva
l = "Lugano"    # name of the city Lugano

# Print in a different order
print(l, z, g)
```

Each variable stores exactly one value (a city name) and the variable name describes what the value represents.

````

---

## Part 2 – Variables and formatted output

Variables can also store numeric values, which can be combined with text.

### Code

```python
# Approximate travel distances (km)
dist_zurich_geneva = 280
dist_zurich_lugano = 205
dist_geneva_lugano = 370

print("The distance from " + z + " to " + g + " is " + str(dist_zurich_geneva) + " km")
```

### Tasks

1. Modify the print statement to show the distance from Zurich to Lugano.
2. Rewrite the print statement using an **f-string**.

---

````{admonition} Sample solution – Part 2
:class: dropdown

```{code-cell} python
# Approximate travel distances (km)
dist_zurich_geneva = 280
dist_zurich_lugano = 205
dist_geneva_lugano = 370

# Using an f-string
print(f"The distance from {z} to {l} is {dist_zurich_lugano} km")
```

F-strings allow variables and text to be combined in a readable and compact way.

````

---

## Part 3 – Expressions and data types

Numeric variables can be combined using operators.

### Code

```python
x = 2
y = x ** 2
z_val = y ** 0.5

print(f"{x} squared is {y} and the square root of {y} is {z_val}")
print(f"{x} is of type {type(x)}, {y} is of type {type(y)}, and {z_val} is of type {type(z_val)}")
```

### Tasks

1. Change the value of `x` and rerun the cell.
2. Observe how the **data types** change.
3. Explain (in a comment) why the square root is a float.

---

````{admonition} Sample solution – Part 3
:class: dropdown

```{code-cell} python
x = 5
y = x ** 2
z_val = y ** 0.5

print(f"{x} squared is {y} and the square root of {y} is {z_val}")
print(f"{x} is of type {type(x)}, {y} is of type {type(y)}, and {z_val} is of type {type(z_val)}")
```

The square root is a float because not all square roots are whole numbers, even if the result looks like one.

````

---

## Part 4 – Coordinates as lists

Some values naturally belong together, such as coordinates.

### Code

```python
# CH1903+ coordinates (example values)
zurich_coords = [26, 12]
geneva_coords = [25, 11]
lugano_coords = [27, 10]
```

```python
# Access individual coordinate values
print("Zurich x:", zurich_coords[0])
print("Zurich y:", zurich_coords[1])
```

### Tasks

1. Replace the example coordinates with real CH1903+ values using [https://map.geo.admin.ch](https://map.geo.admin.ch).
2. Add comments explaining why a **list** is suitable for coordinates.

---

````{admonition} Sample solution – Part 4
:class: dropdown

```{code-cell} python
# CH1903+ coordinates (example realistic values)
zurich_coords = [2680000, 1240000]
geneva_coords = [2500000, 1120000]
lugano_coords = [2720000, 1080000]

# Access values
print("Zurich x:", zurich_coords[0])
print("Zurich y:", zurich_coords[1])
```

A list is suitable because coordinates belong together and their order (x, y) matters.

````

---

## Part 5 – Organising cities

Dictionaries allow us to link **keys** (names) to **values** (coordinates).

### Code

```python
cities = {
    "Zurich": zurich_coords,
    "Geneva": geneva_coords,
    "Lugano": lugano_coords
}

print(cities)
```

```python
# Show what is stored in our keys and values
cities.keys()
cities.values()
```

```python
# Retrieve coordinates from the dictionary
cz = cities["Zurich"]
cg = cities["Geneva"]
cl = cities["Lugano"]
```

### Tasks

1. Print the coordinates of Geneva using the dictionary.
2. Explain (in a comment) why dictionaries are more flexible than individual variables.

---

````{admonition} Sample solution – Part 5
:class: dropdown

```{code-cell} python
cities = {
    "Zurich": zurich_coords,
    "Geneva": geneva_coords,
    "Lugano": lugano_coords
}

# Access Geneva coordinates
print(cities["Geneva"])

# Retrieve and store coordinates
cz = cities["Zurich"]
cg = cities["Geneva"]
cl = cities["Lugano"]
```

Dictionaries allow us to look up values by meaningful names instead of remembering variable names.

````

---

## Part 6 – Manhattan distance

The Manhattan distance between two points is:

|x₁ − x₂| + |y₁ − y₂|

### Code

```python
# Manhattan distance: Zurich – Lugano

# We need to convert these to absolute values.
# There are simpler ways but let rely on the tools we know already.
dx = cz[0] - cl[0]
dx = dx ** 2
dx = dx ** 0.5

dy = cz[1] - cl[1]
dy = dy ** 2
dy = dy ** 0.5

manhattan_zl = dx + dy

print(f"Manhattan distance from Zurich to Lugano is {manhattan_zl}")
```

### Tasks

1. Calculate the Manhattan distance between Zurich & Geneva and Lugano & Geneva.
2. Store the results in new variables.

---

````{admonition} Sample solution – Part 6
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
````

---

## Part 7 – Euclidean distance

The Euclidean distance is:

√((x₁ − x₂)² + (y₁ − y₂)²)

### Code

```python
# Euclidean distance: Zurich – Lugano

dx = cz[0] - cl[0]
dy = cz[1] - cl[1]

euclidean_zl = (dx**2 + dy**2) ** 0.5

print(f"Euclidean distance from Zurich to Lugano is {euclidean_zl}")
```

### Tasks

1. Compute the Euclidean distance between Zurich & Geneva and Lugano & Geneva.
2. Print both Manhattan and Euclidean distances clearly.

---

````{admonition} Sample solution – Part 7
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
```

````

---

## Part 8 – Storing distance results

Computed values are also data and should be stored systematically.

### Code

```python
distances = {
    "ZurichLugano": {
        "manhattan": manhattan_zl,
        "euclidean": euclidean_zl
    }
}

print(distances)
```

### Tasks

1. Extend the dictionary to include Zurich–Geneva.
2. Add Lugano–Geneva distances.
3. Inspect the structure and explain how this resembles an attribute table.

---

````{admonition} Sample solution – Part 8
:class: dropdown

```{code-cell} python
distances = {
    "ZurichLugano": {
        "manhattan": manhattan_zl,
        "euclidean": euclidean_zl
    },
    "ZurichGeneva": {
        "manhattan": manhattan_zg,
        "euclidean": euclidean_zg
    },
    "LuganoGeneva": {
        "manhattan": manhattan_lg,
        "euclidean": euclidean_lg
    }
}

print(distances)
```

This structure resembles an attribute table:
each key represents an entity (city pair) and each value stores multiple attributes.

````

---

## Reflection

Answer briefly in comments or markdown:

1. Why are **lists** suitable for coordinates?
2. Why are **dictionaries** useful for spatial data?
3. Which step helped you most to understand distance calculations?

---

````{admonition} Sample solution – Reflection
:class: dropdown

1. **Why are lists suitable for coordinates?**  
   Coordinates consist of multiple values that belong together (e.g. x and y).  
   A list keeps these values in a fixed order and allows easy access to individual components.

2. **Why are dictionaries useful for spatial data?**  
   Dictionaries link meaningful names (keys) to values, such as city names to coordinates or distances.  
   This makes the data easier to organise, access, and extend, similar to attributes in a spatial dataset.

3. **Which step helped you most to understand distance calculations?**  
   Breaking the distance calculation into separate x- and y-components helped clarify how distances are derived from coordinates, before combining them into a final result.

````

---

## Optional challenge

Design a dictionary that stores:

* city name
* coordinates
* distances to other cities

You do **not** need to automate anything yet — focus on structure and clarity.

````{admonition} Sample solution – Optional challenge
:class: dropdown

```{code-cell} python
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

The focus here is not automation, but choosing a **clear and meaningful data structure**.

````
