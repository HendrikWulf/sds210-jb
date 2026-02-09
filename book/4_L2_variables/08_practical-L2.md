---
title: Practical L2

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
From single variables to structured spatial calculations
</div>

---


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/08_practical-L2.ipynb)


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

## Reflection

Answer briefly in comments or markdown:

1. Why are **lists** suitable for coordinates?
2. Why are **dictionaries** useful for spatial data?
3. Which step helped you most to understand distance calculations?

---

## Optional challenge

Design a dictionary that stores:

* city name
* coordinates
* distances to other cities

You do **not** need to automate anything yet. Better focus on structure and clarity.

---

### What Comes Next

So far, you have learned how to **store** and **access** multiple values.
The next step is to **process collections automatically**.

Next, you will learn about **loops and conditional logic**, which allow your code to:

* work through collections element by element
* make decisions based on values and conditions
* apply the same operation to many items in a structured way
