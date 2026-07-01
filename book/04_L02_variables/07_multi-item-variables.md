---
title: Multi-item Variables

site:
 outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
When one value is not enough
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/04_L02_variables/07_multi-item-variables.ipynb)

```{admonition} Big idea
:class: tip

Single variables store one value.  
Multi-item variables store **collections of related values** in a single container.

```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★★★ (An absolute bottleneck; required to complete Part 4: Coordinates as lists, Part 5: Organising cities, and Part 8: Storing distance results.)  
**Project Relevance:** ★★★ (Nested dictionaries map exactly to the JSON API data required for project 2, and lists are mandatory for time-series extraction in project 4.)  
**Foundation:** ★★★ (The core data structures that govern all advanced Python logic.)  

**Time to Read:** 25 minutes  
**In a nutshell:** Collections like lists, tuples, sets, and dictionaries allow you to group related spatial data into powerful, queryable structures.  
**Skip this if:** You know exactly when to use a dictionary vs. a list, understand nested indexing, and know how `.copy()` prevents shared memory reference bugs.

```

So far, each variable has stored exactly one value. In practice, we constantly work with groups of values that belong together, such as coordinate pairs, lists of cities, or sets of unique IDs.

In this section, you will learn how Python stores multiple values in one variable (often called collections or data structures) and how to choose the right one for your spatial workflows.

---

## 1. The Four Built-in Collections

Python provides four built-in collection types that we will use throughout the course. We will explore each in detail, but keeping this summary handy will help you navigate them:

| Collection | Brackets | Key property | Example |
| --- | --- | --- | --- |
| **List** | `[ ]` | ordered and changeable | `["Bari", "Harare", "Manila"]` |
| **Tuple** | `( )` | ordered and fixed | `(14.6007, 120.9746)` |
| **Set** | `{ }` | unordered and unique values | `{"Asia", "Africa"}` |
| **Dictionary** | `{ }` | named key-value pairs | `{"name": "Bari", "population": 315473}` |

Choosing the right collection type improves the clarity and correctness of your code.

```{admonition} Quick intuition guide
:class: note
* Use a **list** when order matters and the content may change (e.g., GPS waypoints along a route).  
* Use a **tuple** when values belong together and should stay fixed (e.g., a `(lat, lon)` coordinate).  
* Use a **set** when you only care about unique values (e.g., finding unique land cover classes).  
* Use a **dictionary** when values need meaningful names, not numeric positions (e.g., the attributes of a weather station).

```

---

## 2. Lists: Ordered and Changeable

**{term}`Lists <List>`** are the workhorse data structure in Python, written using square brackets `[]`. They are designed to store ordered sequences of values, meaning Python will always preserve the exact order in which you added the items. Crucially, lists are **{term}`mutable <Mutable>`**; you can seamlessly add, remove, or alter individual elements long after the list is created, making them ideal for datasets that grow or change over time.

For example, imagine we are recording a sequence of elevations (in meters) along a hiking transect:

```{code-cell} python
elevations_m = [450, 470, 515, 560, 545, 580]

```

### Accessing and Slicing Lists

You can retrieve individual values using their numeric **{term}`index <Index>`** position, always starting at `0`. You can also extract a segment (or "slice") of the list using a colon `:`. This is highly useful for isolating specific chunks of a spatial profile or time series without modifying the original data.

```{code-cell} python
# Indexing retrieves a single item
print("Start of transect:", elevations_m[0])   # 450
print("End of transect:", elevations_m[-1])    # 580 (negative index counts backward)

# Slicing retrieves a new list of items
print("Middle segment:", elevations_m[1:4])    # [470, 515, 560]

```

### Building Lists Dynamically

In spatial data science, you rarely type out lists manually. Instead, you often start with an **empty list** and populate it dynamically as you process data (for example, reading coordinates from a file one by one).

```{code-cell} python
# Create an empty list
processed_elevations = []

# Dynamically add items to the end
processed_elevations.append(450)
processed_elevations.append(470)

print("Dynamically built list:", processed_elevations)

```

### Modifying and Expanding Lists

Because lists are mutable, you can change their contents in place. You can overwrite existing values using their index, or dynamically add new measurements to the transect using methods like `.append()`, `.insert()`, and `.extend()`. You can even combine two separate lists using the `+` operator.

```{code-cell} python
# Overwrite a specific value
elevations_m[2] = 520

# Add a single new measurement to the very end
elevations_m.append(600)

# Insert a new measurement at a specific position (index 1)
elevations_m.insert(1, 460)

# Add multiple new measurements at once
new_measurements = [610, 625]
elevations_m.extend(new_measurements)

# Combine lists to create a completely new list
all_elevations = elevations_m + [640, 655]

```

### Removing and Organizing Items

Python also provides built-in methods to clean and organize your lists. You can remove items by their specific value (`.remove()`), or by their index position (`.pop()` or `del`). Once your data is clean, you can reorganize it using `.sort()` or `.reverse()`. To check how many items remain in your list, use the `len()` function.

```{code-cell} python
# Remove the first matching value of '460'
elevations_m.remove(460)

# Remove and return an item by its specific position
elevations_m.pop(2)

# If no index is given, pop() automatically removes the last item
elevations_m.pop()

# Delete an item outright by its position
del elevations_m[0]

# Check the total number of items remaining
print("Total measurements:", len(elevations_m))

```

Lists can be sorted in place. You can sort them normally, in reverse, or just flip the current order entirely.

```{code-cell} python
# Sort the measurements from lowest to highest elevation
elevations_m.sort()

# Sort in reverse order (highest to lowest)
elevations_m.sort(reverse=True)

# Reverse the current order directly without sorting
elevations_m.reverse()

```

---

## 3. Tuples: Ordered and Fixed

**{term}`Tuples <Tuple>`** look and behave very similarly to lists, but with one absolute difference: they are **{term}`immutable <Immutable>`**. Once a tuple is created using parentheses `()`, its contents can never be changed, added to, or removed.

You use tuples when values represent a single logical entity that should be permanently protected. The most common geospatial example is a coordinate pair (latitude, longitude) or a bounding box. Modifying half of a coordinate pair accidentally would ruin your spatial analysis, so storing it as a tuple makes your intention strictly clear: *this group of values is fixed*.

```{code-cell} python
manila_coords = (14.6007, 120.9746)

# Attempting to change a value will instantly raise a TypeError
# manila_coords[0] = 14.7  <-- This fails!

```

### Combining and Unpacking Tuples

While you cannot alter the contents of a tuple, you *can* combine two tuples together using the `+` operator to create a brand new tuple (for example, combining `bbox_min` and `bbox_max` into a single bounding box).

Tuples also offer a highly readable feature called "unpacking." Unpacking allows you to extract the contents of a tuple into distinct variables in a single, elegant line of code.

```{code-cell} python
# Combining tuples
bbox_min = (14.5, 120.9)
bbox_max = (14.7, 121.1)
bbox = bbox_min + bbox_max

# Tuple unpacking
lat, lon = manila_coords

print(f"Latitude: {lat}, Longitude: {lon}")

```

### The List Workaround

Sometimes you start with a tuple but later realize the data actually *does* need to change. Because you cannot change the tuple directly, the standard workaround is to convert it to a list using `list()`, modify the list, and then convert it back to a tuple using `tuple()`.

```{code-cell} python
colors = ("red", "green", "blue")

temp = list(colors)
temp.append("yellow")
colors = tuple(temp)

```

If you find yourself converting tuples to lists often, you likely chose the wrong data structure to begin with. Use a list from the start!

---

## 4. Sets: Unique Values Only

**{term}`Sets <Set>`** are designed for one main purpose: answering the question, *"Is this value present or not?"* Written with curly brackets `{}`, sets automatically discard duplicates and entirely ignore order. They are not sequences; they are purely collections of unique elements.

This makes sets the absolute best choice when you need to extract unique categories from messy data, such as identifying the distinct land cover classes in a regional survey.

```{code-cell} python
# A messy list containing duplicates
messy_list = ["forest", "water", "urban", "water", "forest"]

# Converting to a set instantly strips all duplicates!
unique_classes = set(messy_list)
print(unique_classes)

```

### Modifying Sets and Membership Testing

Because sets ignore order, you **cannot** access their items using an index (e.g., `unique_classes[0]` will fail). However, the trade-off is incredible speed. Checking if a specific value exists inside a set using the `in` keyword is significantly faster than checking a list. You can easily add items, update the set with multiple new items, or remove them.

When removing items, Python gives you two choices: `.remove()` will throw an error if the item doesn't exist, while `.discard()` will silently ignore the request if the item is missing.

```{code-cell} python
# Check if a category exists (Returns True/False)
print("water" in unique_classes)

# Add a single new category
unique_classes.add("agriculture")

# Add multiple new categories from another collection
unique_classes.update({"shrubland", "bare_rock"})

# Remove safely (fails silently if "urban" is not present)
unique_classes.discard("urban")

# Remove strictly (throws an error if "Europe" is not present)
# unique_classes.remove("Europe") 

```

---

## 5. Dictionaries: Named Values

**{term}`Dictionaries <Dictionary>`** store data as **key-value pairs**. Instead of looking up a value by its numerical position (like in a list), you look it up using a meaningful name (the "key").

Dictionaries are the backbone of attribute data in Python. Whenever you need to represent the properties of a real-world object—such as the metadata of a weather station, the configuration settings of an algorithm, or a GeoJSON feature—a dictionary is the correct choice.

```{code-cell} python
station = {
    "id": "CH-BRN",
    "name": "Bern",
    "elevation_m": 540,
    "temperature_C": 12.4
}

```

### Accessing, Modifying, and Safe Lookup

You retrieve values by passing the exact string name of the key inside square brackets `[]`. If you need to update an attribute or add a completely new one, you simply assign a new value to that key.

If you try to access a key that does not exist using square brackets (e.g., `station["precipitation"]`), Python will raise a `KeyError`. When working with real-world datasets that might have missing attributes, it is much safer to use the `.get()` method. It allows you to request a key and provide a default fallback value just in case the key is missing.

```{code-cell} python
# Update an existing value
station["elevation_m"] = 542

# Add a completely new key-value pair
station["active"] = True

# Safely request precipitation. If it's missing, return "No data"
precip = station.get("precipitation", "No data")

```

### Advanced Dictionary Methods

Dictionaries come with powerful methods to manage their contents and explore their structure. You can update multiple key-value pairs at once using `.update()`. When you want to explore the dictionary without knowing the keys in advance, you can use *views*: `.keys()` shows all the labels, `.values()` shows the raw data, and `.items()` shows both together as tuples.

```{code-cell} python
# Update multiple values at once
station.update({"population": 133000, "country": "Switzerland"})

# View the structure of the dictionary
print("Keys:", station.keys())
print("Values:", station.values())
print("Key-Value Pairs:", station.items())

```

```{admonition} Extracting Dictionary Views
:class: tip
When you use `.keys()` or `.values()`, Python returns a dynamic *view*. If you need to manipulate these keys like a normal sequence (e.g., accessing the first key by its index position `[0]`), you must convert the view into a true list first: 
`city_names = list(station.keys())`

```

If you need to remove data, you have multiple options depending on your needs.

```{code-cell} python
# Remove a specific key and return its value
station.pop("temperature_C")

# Remove the most recently added item (Python 3.7+)
station.popitem()

# Wipe the entire dictionary clean
station.clear()

```

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L02_ch07_02_python_collections_visualizer/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Python Collections Visualizer.</b><br>
    Select the different tabs to explore Lists, Tuples, Sets, and Dictionaries. Click the action buttons to see how mutability, order, and uniqueness dictate exactly what operations Python will allow—and which operations will trigger an error. For improved visibility of the explorer, follow this <a href="[https://hendrikwulf.github.io/sds210_assets_L02_ch07_02_python_collections_visualizer/]" target="_blank">link</a>.</em>
</figcaption>

<!-- markdownlint-enable MD033 -->

---

#### Concept Check: The Nested Weather Record

You are tracking daily temperature readings for a specific weather station and have organized the data into the following nested structure:

```python
weather_record = {
    "station_name": "Zurich",
    "temperatures_C": [12.5, 14.1, 13.8, 15.2]
}

```

You want to extract the *last* temperature reading recorded (`15.2`). Which code snippet successfully achieves this?

A) `weather_record[-1]["temperatures_C"]`

B) `weather_record["temperatures_C"][-1]`

C) `weather_record["temperatures_C"]`

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
When navigating nested data, you must evaluate the structure from the outside in. First, you access the dictionary using the named key `"temperatures_C"`. This returns the entire list, allowing you to then apply the numeric index `[-1]` to grab the very last item in that sequence. Option A will crash with a `KeyError` because dictionaries are not accessed by numeric positions, and Option C returns the entire list rather than the single targeted value.

```

---

## 6. Indexing and Referencing

To work with values stored inside collections, Python relies heavily on **indexing and referencing**. While all collections use square brackets `[]` to retrieve data, *what* goes inside the brackets depends on the collection:

* **Lists and Tuples:** Use numeric positions (`elevations_m[0]`).
* **Dictionaries:** Use named keys (`station["name"]`).
* **Sets:** Do not support brackets at all!

### Multi-dimensional Collections (Nesting)

Collections can easily contain other collections. This is called **nesting**, and it is how we build multidimensional matrices (like grids of pixels or lists of coordinates). To access data buried inside nested collections, you simply chain the brackets together. Python evaluates indexing **one level at a time, from the outside in**.

```{code-cell} python
# A 2D list representing a 3x3 grid
grid = [
    [1, 2, 3],
    [7, 8, 9],
    [6, 5, 4]
]

# Step 1: grid[1] selects the second row -> [7, 8, 9]
# Step 2: [0] selects the first item in that row -> 7
value = grid[1][0]
print(value)

```

You do not need special syntax for higher dimensions; you just keep applying brackets for each level you want to drill into.

---

## 7. Copying vs Referencing Collections

How Python handles assignment (`=`) depends entirely on the type of data you are working with. This subtle difference is one of the most common sources of bugs in data science.

When you assign a **single value** (like an integer or string) to a new variable, Python creates an independent copy. However, when you assign a **mutable collection** (like a list, dictionary, or set) to a new variable, Python does **not** create a copy. Instead, it creates a shared reference: both variables now point to the exact same object in computer memory.

```{code-cell} python
list_a = [1, 2, 3]
list_b = list_a

# Modify the original list
list_a.append(4)

# The "second" list changed too!
print(list_b) # Output: [1, 2, 3, 4]

```

Because Python wants to save memory and processing time, it assumes you just want two name tags (`list_a` and `list_b`) pointing at the same underlying box of data.

### Equality (`==`) vs Identity (`is`)

This distinction is why Python has two different comparison operators. `==` checks if two variables have the same *value* inside them. `is` checks if they are literally the same object in memory. `list_a is list_b` will return `True`, because they are the same underlying object!

### Making an Independent Copy

If you actually want a separate, safe backup of a collection before you manipulate it, you must explicitly tell Python to clone the memory block using `.copy()` or by wrapping it in the collection constructor (e.g. `list()`).

```{code-cell} python
list_a = [1, 2, 3]

# Create a true, independent clone
list_c = list_a.copy()

# Alternatively: list_c = list(list_a)

list_a.append(4)
print("Original:", list_a)
print("Independent Clone:", list_c)

```

```{admonition} Copying Nested Objects
:class: warning

Using `.copy()` only clones the **outermost structure**. If your list contains *other* lists (like a nested grid), those inner lists will still be shared references! We will revisit this advanced concept later when dealing with nested spatial data.

```

---

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L02_ch07_01_memory_reference_visualizer/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Memory Reference Visualizer.</b><br>
    Click the Run button to simulate changing a list. Notice how assigning <code>b = a</code> causes <code>b</code> to update instantly because it points to the exact same shared memory block (<code>0x1A</code>) as <code>a</code>. In contrast, <code>c = a.copy()</code> gives <code>c</code> its own completely independent memory block (<code>0x2B</code>). For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L02_ch07_01_memory_reference_visualizer/" target="_blank">link</a>.</em>
</figcaption>

<!-- markdownlint-enable MD033 -->

---

#### Concept Check: The Shared Memory Trap

You are organizing a list of sample coordinates and want to create a backup before making changes. You write the following code:

```python
original_samples = [12, 15, 18]
backup_samples = original_samples

original_samples.append(21)

```

If you print `backup_samples` right now, what will Python output?

A) `[12, 15, 18]`

B) `[12, 15, 18, 21]`

C) `[12, 15, 18], [21]`

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
Because lists are mutable collections, assigning `backup_samples = original_samples` does *not* create a copy. Instead, it creates a second label pointing to the exact same list in memory. When you appended `21` to the original, the underlying shared object changed, meaning `backup_samples` shows the change too! To avoid this, you must use `.copy()`.

```

---

## 8. Short Exercise

You have received raw field information and need to organise it into the **appropriate data structures** so it can be used reliably later.

### Given Data

```{code-cell} python
raw_cities = ["Bari", "Harare", "Manila", "Harare"]
coords = (41.1311, 16.8701)   

raw_attributes = {
    "station": "Bari",
    "elevation_m": 315,
    "crs": "EPSG:4326"
    # Note: "discharge_m3s" is missing
}

```

### Task

1. Create a **set** called `unique_cities` from `raw_cities` to remove duplicates.
2. Convert that set back into a **sorted list** called `cities_sorted` (Hint: use `sorted(unique_cities)`).
3. Build a final **dictionary** called `station_record` with the following keys:

* `"name"` → extract this from `raw_attributes`
* `"coordinates"` → the coordinate tuple
* `"cities"` → the sorted list you just made
* `"discharge_m3s"` → extract this from `raw_attributes` using `.get()`, defaulting to `"not available"`

1. Use an f-string to print the station name and its latitude (index `0` of the coordinate tuple) from your new dictionary.

````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
# 1 & 2) Remove duplicates and sort
unique_cities = set(raw_cities)
cities_sorted = sorted(unique_cities)

# 3) Build a structured station record
station_record = {
    "name": raw_attributes["station"],
    "coordinates": coords,
    "cities": cities_sorted,
    "discharge_m3s": raw_attributes.get("discharge_m3s", "not available")
}

# 4) Extract and print from the structured dictionary
lat = station_record["coordinates"][0]
name = station_record["name"]

print(f"Station {name} is located at latitude {lat}.")
```

````

---

## 9. Summary

After completing this section, you should understand that:

* **Lists** (`[]`) are ordered and changeable, serving as the workhorse for sequential data.
* **Tuples** (`()`) are ordered and permanently fixed, ideal for protecting coordinate pairs.
* **Sets** (`{}`) store unique values and ignore duplicates, making them perfect for extracting distinct categories.
* **Dictionaries** (`{key: value}`) store data using named labels instead of numeric index positions, forming the backbone of attribute records.
* **Collections are referenced, not copied.** Assigning a list to a new variable just creates a second name tag for the same data in memory. To create a true independent clone, you must explicitly call `.copy()`.

This summary table features the most relevant functions and methods introduced in the chapter.

<!-- markdownlint-disable MD060-->
| Collection Type | Method / Function | Action |
| --- | --- | --- |
| **Lists** | `.append()` | Adds a single item dynamically to the end of the list. |
|  | `.extend()` | Adds multiple new items/measurements at once to the list. |
|  | `.insert()` | Inserts a new item at a specific index position. |
|  | `.remove()` | Removes an item by its specific value, targeting the first matching instance. |
|  | `.pop()` | Removes and returns an item by its specific index position; if no index is given, it automatically removes the last item. |
|  | `del` | Deletes an item outright based on its index position. |
|  | `.sort()` | Reorganizes and sorts the list in place (can be reversed using `reverse=True`). |
|  | `.reverse()` | Reverses the current order of the list directly without sorting. |
|  | `len()` | Returns the total number of items currently remaining in the list. |
| **Tuples** | `list()` | Converts a tuple into a list to apply modifications as a workaround. |
|  | `tuple()` | Converts a list back into an immutable tuple. |
| **Sets** | `.add()` | Adds a single new unique item to the set. |
|  | `.update()` | Updates the set by adding multiple new items from another collection. |
|  | `.discard()` | Removes an item safely, silently ignoring the request if the item is missing. |
|  | `.remove()` | Removes an item strictly, raising an error if the item does not exist in the set. |
| **Dictionaries** | `.get()` | Safely requests a key and allows you to provide a default fallback value just in case the key is missing to avoid a `KeyError`. |
|  | `.update()` | Updates multiple key-value pairs at once. |
|  | `.keys()` | Returns a dynamic view showing all the labels/keys in the dictionary. |
|  | `.values()` | Returns a dynamic view showing all the raw data/values in the dictionary. |
|  | `.items()` | Returns a dynamic view showing both the keys and values together as tuples. |
|  | `.pop()` | Removes a specific key and returns its value. |
|  | `.popitem()` | Removes the most recently added item (in Python 3.7+). |
|  | `.clear()` | Wipes the entire dictionary clean. |
| **General** | `.copy()` | Explicitly tells Python to clone the memory block, creating a true, independent copy of a mutable collection (only clones the outermost structure). |
<!-- markdownlint-enable MD060 -->

### What Comes Next

So far, you have learned how to **store** and **access** single and multiple values. However, doing calculations manually on every item in a list of 10,000 coordinates is impossible.

In the next lesson (after the practical), we will introduce **Loops and Conditional Logic**, which will allow your code to automate tasks, make decisions, and process massive lists of data in milliseconds.
