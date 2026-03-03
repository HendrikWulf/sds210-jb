---
title: Function Design Concepts

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Managing scope, defaults, and side effects
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/6_L4_functions/03_design_concepts.ipynb)

---

```{admonition} Big Idea
:class: tip

Writing a function is not just about making the code run; it is about making the code **safe and predictable**. To design professional spatial tools, you must understand where variables "live" (scope), how to make your tools flexible (optional parameters), and how to avoid hidden memory traps (mutable defaults).


```

In the previous section, we built our first functions. Now, we will look at how functions actually behave in your computer's memory. This section covers critical design concepts that may save you hours of debugging when building more complex spatial data pipelines.

---

## 1. Scope and Namespaces

A common point of confusion for new programmers is understanding how variable names inside functions relate to those defined elsewhere in their notebooks.

Think of your main Python script as a giant "White Room." When you define a function, you are building a smaller, soundproof room inside it.

:::{figure} images/06_the-white-room.png
:alt: Diagram showing nested local and global scopes.
:width: 700px
:align: center

A visual analogy of scope: a function creates a "soundproof" local scope inside the main global scope. Variables inside the function can "see" out to the global scope, but the global scope cannot "see" into the function.
:::

### Local Variables Stay Local

When you create a variable *inside* a function, it is a **local variable**. It only exists within that specific function's room. Once the function finishes running, the room is demolished, and the variable disappears.

```{code-cell} python
def calculate_area():
    # This variable only exists inside this function
    area = 1500
    return area

# We call the function
calculate_area()

# Guess the output if we try to print the variable from the main script...
print(area)


```

**Output:**

```text
NameError: name 'area' is not defined


```

This is actually a brilliant feature! It means you can use simple variable names like `area`, `distance`, or `x` inside your functions without worrying about accidentally overwriting variables with the same names in your main script.

### The Danger of Global Variables

Python searches for variables from the inside out. If it cannot find a variable inside the function (local scope), it will peek outside into the main script (global scope) to see if it exists there.

This can lead to incredibly dangerous bugs. Look at this example:

```{code-cell} python
# A global variable defined at the top of our notebook
base_elevation = 1500

def calculate_relative_elevation(elevation):
    # BAD: This function uses a global variable instead of a parameter!
    return elevation - base_elevation

print(calculate_relative_elevation(2000))  # Outputs: 500


```

This code *works*, but it is poor software design. The function `calculate_relative_elevation` is no longer a standalone tool. It secretly relies on `base_elevation` existing elsewhere in the notebook. If you copy this function into a new script, or if you accidentally change `base_elevation` in a different cell, your pipeline will break, and it might be hard to figure out why.

```{admonition} Rule of Thumb
:class: warning

**Don't rely on global variables inside a function.** If a function needs data to do its job, you should pass that data in explicitly as a parameter.


```

---

## 2. Required vs. Optional Parameters

Up to this point, every parameter we have created has been a **required parameter**. If the user forgets to provide an argument, the program crashes.

However, we can design our tools to be much more flexible by providing **optional parameters** with default values.

### Setting Default Values

Imagine a function that checks if a GPS point is within a certain accuracy threshold. Most of the time, our acceptable threshold is 5 meters. We can set that as the default!

```{code-cell} python
# 'threshold' is now an optional parameter with a default of 5
def check_accuracy(point_accuracy, threshold=5):
    if point_accuracy <= threshold:
        return True
    else:
        return False


```

Now, the user has a choice:

```{code-cell} python
# Option 1: Provide one argument. Python uses the default threshold (5).
check_accuracy(3)

# Option 2: Override the default by providing a second argument.
check_accuracy(3, threshold=2)


```

### The Ordering Rule

There is a strict grammatical rule in Python regarding defaults: **Required parameters must always come before optional parameters in the function definition**.

```{code-cell} python
# GOOD: Required comes first
def create_buffer(geometry, buffer_size=50): 

# ERROR: Required comes after an optional default
def create_buffer(buffer_size=50, geometry): 


```

---

## 3. The Mutable Default Trap

This is a high-value moment. Understanding this concept separates beginners from professional data scientists.

We just learned that we can set default values (like `threshold=5`). But what happens if we set a default value to a **mutable** object, like an empty list (`[]`)?

Let's write a function that takes a new GPS waypoint and adds it to a route list. If no route list is provided, it should default to an empty list.

```{code-cell} python
# THE DANGEROUS WAY
def add_waypoint(waypoint, route=[]):
    route.append(waypoint)
    return route


```

Watch what happens when we use it to track two different animals:

```{code-cell} python
track_bear = add_waypoint("Point A")
print(f"Bear Track: {track_bear}")

track_wolf = add_waypoint("Point X")
print(f"Wolf Track: {track_wolf}")


```

**Output:**

```text
Bear Track: ['Point A']
Wolf Track: ['Point A', 'Point X']


```

**What happened?!** The wolf is somehow inheriting the bear's GPS points!

When you define a function, Python evaluates the default arguments **only once**. It creates that single empty list `[]` and stores it in memory. Every time you call the function without providing a route, it grabs that **exact same list**. The state carries over (a "side effect"), destroying the reproducibility of your data.

### The Fix: Use `None`

To fix this, we must use `None` as our default value, and create the fresh list *inside* the function block.

```{code-cell} python
# THE SAFE WAY
def add_waypoint(waypoint, route=None):
    if route is None:
        route = []  # Creates a brand new, empty list every time it runs!
        
    route.append(waypoint)
    return route


```

```{admonition} The Mutable Default Rule
:class: danger

**Never use `[]` or `{}` as default parameter values.** Always use `None`, and initialize the empty list or dictionary inside the function body. Understanding how state and side effects operate in memory is crucial for reproducible spatial data science.


```

``````{admonition} Click here for a more detailed breakdown of the Mutable Default Trap
:class: dropdown

### 1. The Core Problem: Definition vs. Execution

In Python, a function's default arguments are evaluated **only once**, at the exact moment the `def` statement is read by the computer (the "definition phase"). They are *not* evaluated every time you call the function (the "execution phase").

When Python reads this line of code:

```{code-cell} python
def add_waypoint(waypoint, route=[]):

```

It says: *"Okay, I'm creating a new function. The default value for `route` is an empty list. I will create a single, empty list in my memory **right now**, and attach it to this function permanently."*



Let's use a "Shared Backpack" analogy:

1. When the function is defined, Python creates a single backpack (the default list `[]`) and leaves it at the door of the function.
2. **The Bear's turn:** You call `add_waypoint("Bear Point")` without providing a list. Python says, "Use the default backpack!" The function puts the bear's GPS point inside the backpack. The backpack now contains `["Bear Point"]`.
3. **The Wolf's turn:** You call `add_waypoint("Wolf Point")` without providing a list. Python says, "Use the default backpack!" It hands the wolf the **exact same backpack from step 1**. But wait—the bear's GPS point is still inside it! The function adds the wolf's point, and the backpack now contains `["Bear Point", "Wolf Point"]`.

Because lists are **mutable** (they can be changed in place), any changes made to the default list are permanent. Every subsequent call to the function uses that exact same, increasingly contaminated list.

### 2. Why doesn't this happen with numbers or strings?

You might wonder why we don't have this problem when we set defaults to numbers, like `buffer=5`.

Numbers, strings, and booleans (`True`/`False`) are **immutable** in Python. You cannot alter them in place. If you change a number, Python actually throws the old number away and creates a brand-new number in memory. Therefore, they cannot accumulate "state" or carry over contamination from previous function calls.

Because lists (`[]`) and dictionaries (`{}`) are **mutable**, they can be modified without losing their original identity in memory.

### 3. How the `None` Fix Actually Works

To fix the shared backpack problem, we need to force Python to create a brand-new list *every single time the function runs*, rather than just once when the function is defined.

Here is the safe code again:

```{code-cell} python
def add_waypoint(waypoint, route=None):
    if route is None:
        route = []  # Creates a brand new, empty list every time it runs!
        
    route.append(waypoint)
    return route

```

Let's look at how memory handles this:

1. **Definition phase:** Python reads `route=None`. `None` is an immutable placeholder. It just means "nothing." Python attaches `None` to the function permanently.
2. **The Bear's turn:** You call `add_waypoint("Bear Point")`. The `route` is `None`. The `if` statement triggers: `route = []`. **Because this line is inside the function body, it runs during the execution phase.** Python creates a brand new list in memory, adds the bear's point, and returns it. Once the function finishes, that specific `[]` creation step is over.
3. **The Wolf's turn:** You call `add_waypoint("Wolf Point")`. The `route` defaults back to `None`. The `if` statement triggers again: `route = []`. Python creates a *second, entirely separate* new list in memory. It adds the wolf's point and returns it.

:::{figure} images/07_mutable-default-trap.png 
:alt: Diagram comparing shared memory vs. independent memory allocation for default arguments.
:width: 700px
:align: center

Visualizing the "Mutable Default Trap." Using `[]` as a default argument creates a single, shared list object in memory (top), leading to unintended data leakage between function calls. Using `None` and creating a new list inside the function ensures independent lists are created for each call (bottom).
:::


### Summary

By using `None` as the default argument, you are delaying the creation of the list. Instead of creating the list when the function is **defined** (which creates a single shared object), you create the list when the function is **executed** (which creates a fresh, independent object every time).


``````

---

## 4. Exercises

Test your understanding of function design and scope!

### Exercise 1: The Scope Bug (Core)

A junior analyst wrote the following code to convert a list of elevations from feet to meters. When they try to run `print(converted)`, Python throws a `NameError`.

**Your Task:** Without running the code, explain why the error occurs, and fix the code so it properly prints the result.

```{code-cell} python
def feet_to_meters(elevation_ft):
    converted = elevation_ft * 0.3048
    return converted

feet_to_meters(5000)
print(converted)


```

``````{admonition} Sample solution
:class: dropdown

**Why it fails:** The variable `converted` is a **local variable**. It was created inside the `feet_to_meters` room, so it ceases to exist the moment the function finishes running.

**The Fix:**
You must catch the returned data in the global scope (the main script) by assigning the function call to a variable!

```{code-cell} python
def feet_to_meters(elevation_ft):
    converted = elevation_ft * 0.3048
    return converted

# Catch the returned data in a new variable in the main script!
final_elevation = feet_to_meters(5000)
print(final_elevation)
```


``````

---

### Exercise 2: The Bounding Box (Stretch)

In spatial analysis, a common operation is to draw a square "bounding box" around a coordinate.

:::{figure} images/08_bounding-box-point.png
:alt: Diagram illustrating how to calculate a simple bounding box from a center point and a buffer.
:width: 700px
:align: center

Calculating a simplified bounding box. By adding and subtracting a buffer value from a center point's latitude and longitude, you can define the minimum and maximum coordinates of a square area.
:::

**Your Task:** Write a function `create_bbox(lat, lon, buffer)` that calculates a simplified bounding box around the point coordinates.

1. Make `lat` and `lon` required parameters.
2. Make `buffer` an **optional** parameter with a default value of `0.5` degrees.
3. The function should **return** a dictionary containing `min_lat`, `max_lat`, `min_lon`, and `max_lon`. (Hint: `min_lat` is `lat - buffer`, `max_lat` is `lat + buffer`, etc.)

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
def create_bbox(lat, lon, buffer=0.5):
    # Calculate the boundaries
    min_lat = lat - buffer
    max_lat = lat + buffer
    min_lon = lon - buffer
    max_lon = lon + buffer
    
    # Return them all packaged neatly in a dictionary
    return {
        "min_lat": min_lat,
        "max_lat": max_lat,
        "min_lon": min_lon,
        "max_lon": max_lon
    }

# Test 1: Using the default buffer
small_box = create_bbox(34.0, -118.0)
print(f"Default box: {small_box}")

# Test 2: Overriding the default buffer
large_box = create_bbox(34.0, -118.0, buffer=5.0)
print(f"Large box: {large_box}")
```


``````

---

### Exercise 3: The Contaminated River (Challenge)

You are writing a code pipeline to track pollution sampling sites along different rivers. Look at the code below.

**Your Tasks:** 

1. Run the code in your head. What will the output look like?
2. Why is this happening?
3. Rewrite the function using best practices so that the Isar and the Inn get their own independent lists of samples.

```{code-cell} python
def log_sample(ph_level, river_samples=[]):
    river_samples.append(ph_level)
    return river_samples

# We take two samples from the Isar
isar_data = log_sample(7.2)
isar_data = log_sample(7.4, isar_data)

# We take one sample from the Inn
inn_data = log_sample(6.8)

print(f"Isar: {isar_data}")
print(f"Inn: {inn_data}")


```

``````{admonition} Sample solution
:class: dropdown

**1. The Output:**
```text
Isar: [7.2, 7.4, 6.8]
Inn: [7.2, 7.4, 6.8]
```

**2. Why it happens:**
Because `river_samples=[]` is a mutable default parameter, Python only created *one* list in memory when the function was defined. Because we didn't pass an existing list for the Inn, it defaulted to using the same list the Isar was using! The Inn data is contaminated with the Isar data.

**3. The Fix:**

```{code-cell} python
# Use None as the default!
def log_sample(ph_level, river_samples=None):
    # Initialize the empty list INSIDE the function
    if river_samples is None:
        river_samples = []
        
    river_samples.append(ph_level)
    return river_samples

isar_data = log_sample(7.2)
isar_data = log_sample(7.4, isar_data)

inn_data = log_sample(6.8)

print(f"Isar: {isar_data}")
print(f"Inn: {inn_data}")
# Now prints correctly: 
# Isar: [7.2, 7.4]
# Inn: [6.8]
```


``````

---

## 5. Summary

In this section, we moved from writing functional code to writing **safe** code:

* **Scope:** Variables created inside a function are destroyed when the function finishes. Do not rely on global variables; always use parameters.
* **Defaults:** Optional parameters make your tools flexible, but they must always be listed *after* required parameters.
* **The Mutable Trap:** Never use `[]` or `{}` as default values. Use `None`, and create the object inside the function block to prevent state leakage and side effects.

### What comes next?

You now know how to build perfectly constrained, safe tools. But Python functions have one more superpower. Next, we will learn how to use `*args` and `**kwargs` to handle an infinite, unpredictable amount of spatial data inputs!
