---
title: Writing Professional Functions

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Documentation, introspection, and avoiding common pitfalls
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/6_L4_functions/05_documentation.ipynb)

---

```{admonition} Big Idea
:class: tip

In data science, code is read far more often than it is written. Writing a function that merely *works* is not enough; a professional function must be self-explanatory, reproducible, and safe. Proper documentation ensures that you (and your colleagues) can understand and reuse your tools months after you wrote them.

```

By this point, you know how to build powerful, flexible spatial tools. But as your scripts grow into larger pipelines, relying solely on memory to remember what each function does becomes impossible. In this final section, we will learn how to formally document our code and review the most common mistakes that break pipelines.

---

## 1. Docstrings: The Standard of Reproducibility

When you write functions, it is best practice to include built-in documentation that explains what the function does, what inputs it expects, and what output it returns.

In Python, this is done using a **docstring** (documentation string). A {term}`docstring` is a multi-line string enclosed in triple double quotes (`""" """`) placed immediately below the `def` statement.

While there are several formatting styles for docstrings, the **NumPy style** is the gold standard in the data science community. It uses clear, readable sections.

Let's document our `haversine` distance calculator:

```{code-cell} python
import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculates the great-circle distance between two geographic coordinates.
    
    This function assumes a spherical Earth with a radius of 6371.0 km and 
    uses the Haversine formula to compute the shortest distance over the 
    earth's surface.

    Parameters
    ----------
    lat1 : float
        Latitude of the first point in decimal degrees.
    lon1 : float
        Longitude of the first point in decimal degrees.
    lat2 : float
        Latitude of the second point in decimal degrees.
    lon2 : float
        Longitude of the second point in decimal degrees.

    Returns
    -------
    float
        The distance between the two points in kilometers.
        
    Examples
    --------
    >>> haversine(47.37, 8.54, 46.20, 6.14)
    224.21
    """
    # (Math implementation goes here...)
    pass

```

A professional docstring typically contains:

1. **A Brief Summary:** One or two sentences explaining the tool's purpose.
2. **Parameters:** A list of the expected arguments, including their data types (e.g., `float`, `list`, `str`) and any default values.
3. **Returns:** An explanation of the data that the function hands back to the program.
4. **Examples (Optional):** Quick usage examples demonstrating how to call the function.

---

## 2. Introspection with `help()`

Why go through the effort of writing docstrings instead of just using regular `#` comments?

Because Python actively reads docstrings and makes them available to the user interactively. This is known as **introspection**. If you forget how your own function works, or if you are using a function written by a colleague, you do not need to open their source code to read it.

You can simply pass the function's name into Python's built-in `help()` function:

```{code-cell} python
# Ask Python how the function works
help(haversine)

```

**Output:**

```text
Help on function haversine in module __main__:

haversine(lat1, lon1, lat2, lon2)
    Calculates the great-circle distance between two geographic coordinates.
    
    This function assumes a spherical Earth with a radius of 6371.0 km and 
    uses the Haversine formula to compute the shortest distance over the 
    earth's surface.

    Parameters
    ----------
    lat1 : float
        Latitude of the first point in decimal degrees.
    ...

```

Furthermore, modern Integrated Development Environments (IDEs) like VS Code or PyCharm automatically read these docstrings. When you start typing `haversine(` in your editor, a tooltip will pop up displaying your documentation, helping you remember the correct order of the latitudes and longitudes!

---

## 3. The Common Mistakes Checklist

Before you move on to the exercises, review this checklist. These are the most frequent, high-impact bugs that catch beginners off guard when building functions.

```{admonition} Common Function Pitfalls
:class: error

1. **Printing instead of Returning:** If your function uses `print(result)` instead of `return result`, the data is displayed to the human but lost to the computer. If you try to save the output to a variable, it will be `None`.
   
2. **Forgetting the `return` statement entirely:** Functions that reach the end of their indented block without a `return` keyword automatically return `None`, crashing downstream calculations.

3. **Using Global Variables Accidentally:** If your function relies on a variable defined outside of its local scope (the "White Room"), it is no longer a self-contained, reproducible tool. Always pass required data in as a parameter.

4. **The Mutable Default Trap:** Never use `[]` or `{}` as a default parameter (e.g., `def add_point(pt, route=[])`). It creates a single shared object in memory that accumulates data across every function call. Always use `None` and initialize the list inside the function.

5. **Mixing Positional and Keyword Arguments Incorrectly:** When calling a function, positional arguments (e.g., `47.3`) must *always* come before keyword arguments (e.g., `lon=8.5`). If you mix them up, Python raises a `SyntaxError`.

6. **Wrong Indentation:** Everything inside the function must be indented. If you accidentally un-indent your `return` statement, or leave code hanging outside the block, your function will terminate early or fail to compile.

```

---

## 4. Exercises

Put your professional coding skills to the test by documenting and debugging these spatial tools!

### Exercise 1: The Documentation Intern (Core)

You have been handed a poorly documented tool written by a former colleague. It converts a speed from knots (nautical miles per hour) to kilometers per hour, which is useful for tracking marine wildlife.

**Your Task:** Write a complete, professional **NumPy-style docstring** for this function. Ensure you include a brief description, the `Parameters`, the `Returns`, and at least one `Examples` block.
*(Hint: 1 knot = 1.852 km/h)*

```{code-cell} python
def knots_to_kmh(speed_knots):
    return speed_knots * 1.852

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
def knots_to_kmh(speed_knots):
    """
    Converts a speed from knots to kilometers per hour (km/h).
    
    Parameters
    ----------
    speed_knots : float
        The speed of the object in knots (nautical miles per hour).
        
    Returns
    -------
    float
        The converted speed in kilometers per hour.
        
    Examples
    --------
    >>> knots_to_kmh(10)
    18.52
    """
    return speed_knots * 1.852

# You can now test it with help(knots_to_kmh)
```

``````

### Exercise 2: The Bug Hunt (Stretch)

The following script contains three different spatial functions that try to calculate the area of a square parcel of land based on side length (`L`). However, they each break one rule from our **Common Mistakes Checklist**.

**Your Task:**

1. Read the code and identify which specific mistake each function makes.
2. Fix all three functions so they work correctly and safely.

```{code-cell} python
# Function A
def get_area_a(L):
    area = L * L

# Function B
def get_area_b(L, factor=1.0, precision):
    return (L * L * factor)

# Function C
global_side_length = 50

def get_area_c():
    return global_side_length * global_side_length

```

``````{admonition} Sample solution
:class: dropdown

**The Mistakes:**
* **Function A** forgets the `return` statement. It will run, but `area` will vanish, returning `None`.
* **Function B** places a required parameter (`precision`) *after* an optional default parameter (`factor=1.0`). Python will throw a `SyntaxError`.
* **Function C** uses a global variable instead of taking an input parameter. If someone changes `global_side_length` elsewhere in the script, this tool breaks.

**The Fixes:**

```{code-cell} python
# Fixed A: Add return
def get_area_a(L):
    area = L * L
    return area

# Fixed B: Reorder parameters (required first)
def get_area_b(L, precision, factor=1.0):
    return (L * L * factor)

# Fixed C: Pass as a parameter
def get_area_c(side_length):
    return side_length * side_length
```

``````

### Exercise 3: The Refactoring Challenge (Challenge)

A researcher wrote a quick script to track the GPS coordinates of a tagged wolf pack over time. Every time the pack moves, they want to log the new coordinates to a list.

Look at their code below. It uses the dangerous "Mutable Default Trap," and it prints its result instead of returning it.

**Your Task:** 1. **Refactor** (rewrite) the function `log_movement` so it is safe.
2. Use `None` for the default `track` parameter, initializing the empty list properly inside the function block.
3. Change the function so it `returns` the updated list instead of `printing` it.
4. Add a basic NumPy-style docstring explaining what the function does.

```{code-cell} python
# The Dangerous Script
def log_movement(coord, track=[]):
    track.append(coord)
    print("New track logged:", track)

# Tracking the wolf pack
log_movement([46.770343, 8.886892]) 
log_movement([46.770352, 8.886903])

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
def log_movement(coord, track=None):
    """
    Logs a new geographic coordinate to an existing track list.
    
    Parameters
    ----------
    coord : list
        A two-item list containing the [lat, lon] of the new movement.
    track : list, optional
        An existing list of coordinates to append to. Defaults to None, 
        which initializes a brand new, empty track list.
        
    Returns
    -------
    list
        The updated track list containing the new coordinate.
    """
    # Fix the mutable default trap
    if track is None:
        track = []
        
    track.append(coord)
    
    # Fix the missing return statement
    return track

# Safely testing the tracking tool
wolf_track = log_movement([46.770343, 8.886892])
wolf_track = log_movement([46.770352, 8.886903], track=wolf_track)

print(f"Final safe track: {wolf_track}")
```

``````

---


## 5. Summary

Congratulations! You have mastered the core mechanics of functional programming.

You now know how to:

* Package repeatable spatial math into modular `def` blocks.
* Safely manage variable scope and memory.
* Handle unpredictable data streams using `*args` and `**kwargs`.
* Document your tools using professional, reproducible NumPy-style docstrings.

### What comes next?

In the upcoming practical exercises, you will:

* build reusable spatial tools by turning mathematical logic into well-structured functions
* compare geometric models programmatically using nested loops and formatted output 
* design flexible, professional tools using `*args`, `**kwargs`, and NumPy-style docstrings