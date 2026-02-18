---
title: Multi-item Variables

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
When one value is not enough
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/07_multi-item-variables.ipynb)


```{admonition} Big idea
:class: tip

Single variables store one value.  
Multi-item variables store **collections of related values** in a single container.
```

So far, each variable stored exactly one value.
In practice, we often work with groups of values that belong together, such as coordinates, lists of cities, or attribute information.
In this section, you will learn how Python stores multiple values in one variable and how to access and inspect them safely.

---

## 1. What Are Multi-item Variables?

Multi item variables store **more than one value** in a single variable.
You will also see them called **collections** or **data structures**.

They help you group related values, keep data organised, and work with sequences and attributes.

In geospatial work, this comes up all the time.
A coordinate pair, a list of cities, or a set of unique IDs are all examples where one value is not enough.

---

### Built in collection types

Python provides four built in collection types that we will use throughout the course:

| Collection  | Brackets | Key property                | Example |
|------------|----------|-----------------------------|---------|
| List       | `[]`     | ordered and changeable      | `["Bari", "Harare", "Manila"]` |
| Tuple      | `()`     | ordered and fixed           | `(14.6007, 120.9746)` |
| Set        | `{}`     | unordered and unique values | `{"Asia", "Africa"}` |
| Dictionary | `{}`     | key value pairs             | `{"name": "Bari", "population": 315473}` |

Each type has a specific purpose.
Choosing the right one improves clarity and correctness.

```{admonition} Note
:class: note

A quick intuition for when to use what:

* A **list** is useful when order matters and the content may change (e.g., a sequence of GPS waypoints along a hiking route).  
* A **tuple** is useful when values belong together and should stay fixed (e.g., a coordinate pair like `(latitude, longitude)`).  
* A **set** is useful when you only care about unique values (e.g., a set of land cover classes present in a satellite scene).  
* A **dictionary** is useful when values need meaningful names, not positions (e.g. attributes of a weather station such as name, ID, elevation).
```

---

## 2. Lists: Ordered and Changeable

Lists store **ordered sequences of values**.
They are the most commonly used collection type in Python.

A list groups related values and keeps their order.
This makes lists ideal for data where **sequence matters** or where values **change over time**.

```python
cities = ["Bari", "Harare", "Manila"]
```

Lists:

* are written using square brackets `[]`
* preserve order
* allow duplicate values
* are **mutable**, meaning their contents can change

---

### A Geoscience Example Dataset

We will work with a simple list of **elevations in meters** measured along a hiking transect.

```python
elevations_m = [450, 470, 515, 560, 545, 580]
```

Each value represents the elevation at a measurement point.
The order reflects the order along the transect.

---

### Accessing List Elements

List items are accessed by their **index position**, starting at `0`.

```python
elevations_m[0]
```

This returns the **first** elevation value.

You can also count from the end using **negative indexing**.

```python
elevations_m[-1]
```

This returns the **last** elevation value.

Indexing allows you to retrieve individual values from a sequence.

---

### Slicing Lists

Slicing lets you extract **ranges of values**.

```python
elevations_m[1:4]
```

This returns a new list containing items at indices `1`, `2`, and `3`.

Some useful slicing patterns:

```python
elevations_m[:3]   # first three values
elevations_m[3:]   # values from index 3 to the end
```

Slicing is useful for working with **segments** of a profile or time series.

---

### Changing List Values

Lists are **mutable**, which means you can change individual elements.

```python
elevations_m[2] = 520
```

The value at index `2` is replaced.
The list keeps its length and order.

You can also replace multiple values at once using slicing.

```python
elevations_m[3:5] = [565, 550]
```

This updates a range of values in place.

---

```{admonition} Note
:class: note

Lists are mutable.  
You change the contents of the same list object, not a copy.
```

---

### Adding Items to a List

Lists can grow dynamically.

To add an item at the end, use `append()`.

```python
elevations_m.append(600)
```

To insert an item at a specific position, use `insert()`.

```python
elevations_m.insert(1, 460)
```

To add multiple items at once, use `extend()`.

```python
new_measurements = [610, 625]
elevations_m.extend(new_measurements)
```

You can also combine two lists using `+`.

```python
all_elevations = elevations_m + [640, 655]
```

---

### Removing Items from a List

There are several ways to remove items.

Remove a value by content:

```python
elevations_m.remove(460)
```

This removes the **first matching value**.

Remove an item by position:

```python
elevations_m.pop(2)
```

If no index is given, `pop()` removes the last item.

```python
elevations_m.pop()
```

You can also delete items using `del`.

```python
del elevations_m[0]
```

---

### Inspecting Lists

To check how many items a list contains, use `len()`.

```python
len(elevations_m)
```

This is useful when looping over data or validating inputs.

---

### Sorting and Reordering Lists

Lists can be sorted in place.

```python
elevations_m.sort()
```

To sort in reverse order:

```python
elevations_m.sort(reverse=True)
```

You can also reverse the current order without sorting.

```python
elevations_m.reverse()
```

Sorting is useful for summaries.
Reversing is useful when order already has meaning.

---

### Copying Lists

Assigning a list to a new variable does **not** create a copy.

```python
a = elevations_m
```

Both variables now refer to the same list.

To create an independent copy, use `copy()`.

```python
b = elevations_m.copy()
```

Now changes to `b` do not affect `elevations_m`.

---

```{admonition} Note
:class: note

Copying lists explicitly avoids subtle bugs.  
When in doubt, make a copy.
```

---

### Key Takeaway for Lists

Lists are the right choice when:

* order matters
* values may change
* data grows or shrinks
* you work with sequences such as profiles, routes, or time series

They are the workhorse data structure in Python and will appear throughout the course.

---

## 3. Tuples: Ordered and Fixed

Tuples are similar to lists, but with one crucial difference:

**Their contents cannot be changed after creation.**

Tuples are used when values belong together and should remain fixed.
A very common example in geospatial work is a **coordinate pair**.

```python
manila_coords = (14.6007, 120.9746)
```

Once created, the values inside a tuple stay the same.

---

### When Tuples Are the Right Choice

Use tuples when:

* values represent a single logical entity
* the order matters
* the values should not change accidentally

Examples include:

* latitude and longitude pairs
* bounding box corners
* fixed parameters passed to functions

Tuples make your intention clear:
**this group of values is not meant to change.**

---

### Accessing Tuple Elements

Tuple elements are accessed using **indexing**, just like lists.

```python
latitude = manila_coords[0]
```

```python
longitude = manila_coords[1]
```

Important points:

* indexing starts at `0`
* order is preserved
* negative indexing also works

```python
manila_coords[-1]
```

The behaviour is the same as for lists.

---

### Immutability in Practice

Because tuples are **immutable**, you cannot change their elements.

```python
manila_coords[0] = 14.7
```

This raises a `TypeError`.

Python protects the tuple from being modified.

---

```{admonition} Note
:class: note

Tuples are immutable.  
This is a feature, not a limitation.

It prevents accidental changes to values that should remain constant.
```

---

### Tuple Unpacking

Tuples can be unpacked into separate variables in a single step.

```python
lat, lon = manila_coords
```

This assigns:

* `lat` to the first value
* `lon` to the second value

Tuple unpacking is very common in:

* coordinate handling
* function return values
* structured data processing

It improves readability and avoids manual indexing.

---

### Combining Tuples

Tuples can be combined using the `+` operator.

```python
bbox_min = (14.5, 120.9)
bbox_max = (14.7, 121.1)

bbox = bbox_min + bbox_max
```

This bounding box example creates a **new tuple**.
The original tuples remain unchanged.

---

### Duplicates and Order

Like lists, tuples:

* preserve order
* allow duplicate values

```python
repeated_coords = (0, 0, 1, 1)
```

The difference is not *what* they store, but **whether they can be changed**.

---

### The List Workaround

Sometimes you start with a tuple but later realise it needs to change.
The standard workaround is:

1. convert the tuple to a list
2. modify the list
3. convert it back to a tuple

```python
colors = ("red", "green", "blue")

temp = list(colors)
temp.append("yellow")

colors = tuple(temp)
```

This creates a **new tuple** with updated values.

---

```{admonition} Note
:class: note

If you find yourself doing this often,  
a list may be the better data structure from the start.
```

---

### Key Takeaway for Tuples

Tuples are the right choice when:

* order matters
* values belong together
* the data should not change
* you want to protect important values

In geospatial workflows, tuples are especially common for **coordinates**, **fixed parameters**, and **return values** from functions.

Lists and tuples look similar, but choosing between them communicates **intent** and helps prevent errors later.

---

## 4. Sets: Unique Values Only

Sets store **unique values** and **do not preserve order**.

They are designed for one main purpose:

> To answer the question: *Is this value present or not?*

Order and position do not matter in a set.

```python
regions = {"Asia", "Africa", "Asia"}
```

Even though `"Asia"` appears twice, it is stored only once.

---

### What Makes Sets Different

Sets are:

* unordered
* mutable as a collection
* free of duplicates

This makes them fundamentally different from lists and tuples.

A set is not a sequence.
It is a **collection of unique elements**.

---

### When Sets Are the Right Choice

Use sets when:

* you care about **uniqueness**
* duplicates should be ignored automatically
* order is irrelevant
* you want fast membership checks

Typical geospatial examples include:

* land cover classes in a raster tile
* unique region names in a dataset
* distinct sensor IDs or station codes
* unique coordinate reference systems used in a project

---

### Creating Sets

Sets are written using **curly brackets** `{}`.

```python
land_covers = {"forest", "water", "urban"}
```

A set can contain any data type and can also mix types, although this is rarely useful in practice.

```python
mixed_set = {1, "river", 3.14}
```

---

### Creating a Set from Another Collection

A very common pattern is to create a set from a list or tuple to remove duplicates.

```python
regions_list = ["Asia", "Africa", "Asia", "Europe"]
regions_set = set(regions_list)
regions_set
```

All duplicates are removed automatically.

This is an easy way to clean categorical data.

---

```{admonition} Note
:class: note

Using `set()` is one of the simplest ways to remove duplicates from a collection.
```

---

### Membership Testing

One of the main strengths of sets is **fast membership testing**.

```python
"Asia" in regions_set
```

This expression returns either `True` or `False`.

Membership checks are:

* faster than in lists
* independent of collection size
* a core reason why sets exist

---

### No Indexing in Sets

Sets **do not support indexing**.

This will fail:

```python
regions_set[0]
```

Because sets are unordered, there is no “first” or “last” element.

To access values, you must **iterate**.

```python
for region in regions_set:
    print(region)
```

The order of printed values may vary.

---

```{admonition} Note
:class: note

If you need indexing or order, a set is the wrong data structure.
```

---

### Updating Sets

Although individual items cannot be modified, **items can be added or removed**.

Add a single item:

```python
regions_set.add("Oceania")
```

Add multiple items from another collection:

```python
new_regions = {"Antarctica", "Europe"}
regions_set.update(new_regions)
```

The `update()` method works with lists, tuples, or other sets.

---

### Removing Items

Items can be removed using either `remove()` or `discard()`.

```python
regions_set.remove("Europe")
```

If the item does not exist, `remove()` raises an error.

```python
regions_set.discard("Mars")
```

`discard()` does nothing if the value is missing.

---

```{admonition} Note
:class: note

Use `discard()` when you are unsure whether the value exists.
Use `remove()` when absence should be treated as an error.
```

---

### Key Takeaway for Sets

Sets are the right choice when:

* uniqueness matters
* order does not
* you want fast membership tests
* duplicates should be ignored automatically

In geospatial workflows, sets are ideal for **categories, labels, IDs, and classes**.

If you catch yourself wanting to index a set or care about order, switch to a list or tuple instead.

---

## 5. Dictionaries: Named Values

Dictionaries store data as **key value pairs**.

They are ideal when values belong together but should be accessed using **meaningful names** rather than numeric positions.

```python
city_info = {
    "name": "Bari",
    "population": 315473,
    "coordinates": (41.1311, 16.8701),
}
```

Each key describes what the value represents.
This makes dictionaries easier to read and less error prone than collections that rely on positions.

---

### How to Think About Dictionaries

A dictionary answers the question:

> *Given this name, what is the corresponding value?*

Unlike lists or tuples, dictionaries do **not** store values in a sequence.
They store **associations**.

This is why dictionaries are sometimes described as **lookup tables** or **hash maps**.

---

### Typical Geoscience Use Cases

Dictionaries are common in geospatial work when handling:

* attributes of a city, station, or feature
* metadata of a dataset
* configuration settings
* results returned from an API
* records from a table where each column has a name

For example, a weather station record:

```python
station = {
    "id": "CH-BRN",
    "name": "Bern",
    "elevation_m": 540,
    "temperature_C": 12.4,
}
```

---

### Accessing Dictionary Values

Dictionary values are accessed using their **keys**, written in square brackets.

```python
city_info["name"]
```

```python
city_info["population"]
```

This avoids the need to remember index positions, which is required for lists and tuples.

---

### Keys and Values

Important rules for dictionary keys:

* keys must be **unique**
* keys are usually strings
* keys cannot be changed once created
* values can be changed freely

Values can be of any type, including:

* numbers
* strings
* tuples
* lists
* even other dictionaries

```python
city_info["districts"] = ["Murattiano", "Japigia", "Libertà"]
```

---

### Safe Access with `get()`

Accessing a missing key using square brackets raises an error.

```python
city_info["area_km2"]  # KeyError
```

To avoid this, use `get()`.

```python
city_info.get("area_km2", "not available")
```

If the key exists, its value is returned.
If not, the default value is returned instead.

This pattern is especially useful when working with:

* incomplete datasets
* optional attributes
* external data sources

---

```{admonition} Note
:class: note

Use `[]` when a missing key should be an error.  
Use `get()` when missing values are acceptable.
```

---

### Modifying Dictionary Values

You can update values by assigning to an existing key.

```python
city_info["population"] = 320000
```

You can also add new key value pairs the same way.

```python
city_info["area_km2"] = 116
```

---

### Updating Multiple Values with `update()`

The `update()` method allows you to change or add multiple entries at once.

```python
city_info.update({
    "population": 321000,
    "country": "Italy",
})
```

Existing keys are updated.
New keys are added.

---

### Removing Items

You can remove entries using `pop()`.

```python
city_info.pop("area_km2")
```

The value is removed and returned.

To remove the most recently added item (Python 3.7+):

```python
city_info.popitem()
```

To remove everything from a dictionary:

```python
city_info.clear()
```

---

### Inspecting Dictionary Contents

Dictionaries provide useful methods for exploring their structure.

```python
city_info.keys()
```

```python
city_info.values()
```

```python
city_info.items()
```

These return *views* of the dictionary and are often used when looping.
You will work with these more in the section on loops.

---

### Dictionaries vs Lists

Dictionaries differ fundamentally from lists.

| Lists                           | Dictionaries                  |
| ------------------------------- | ----------------------------- |
| Values are accessed by position | Values are accessed by name   |
| Order matters                   | Order does not define meaning |
| Inserting shifts indices        | Keys remain stable            |
| Best for sequences              | Best for structured records   |

This makes dictionaries the natural choice for **attribute data**.

---

```{admonition} Note
:class: note

Python itself stores variables in dictionaries.  
The variable name is the key, and the value is the stored object.

This is why dictionaries are so central to the language.
```

---

### Key Takeaway for Dictionaries

Use dictionaries when:

* values belong together conceptually
* each value has a clear meaning
* access by name is safer than access by position
* you are modelling real world objects or records

In geospatial programming, dictionaries are the backbone of **feature attributes, metadata, and configuration**.

If you find yourself remembering numbers like `data[3]` or `data[7]`, a dictionary is usually the better choice.

---

## 6. Indexing and Referencing

To work with values stored inside collections, Python uses **indexing and referencing**.

All collections use **square brackets**, but what goes inside the brackets depends on the collection type.

---

### Numeric indexing for lists and tuples

Lists and tuples store values in a fixed order.
You access elements by their **position**, starting at index `0`.

```python
cities[0]
```

```python
cities[-1]
```

The first example returns the first element.
The second example returns the last element.

Tuples work exactly the same way.

---

### Key based access for dictionaries

Dictionaries do not use numeric positions.
Instead, values are accessed using **keys**.

```python
city_info["coordinates"]
```

The key describes what you want, which makes dictionary access explicit and readable.

---

### Sets do not support indexing

Sets do not preserve order.
Because of this, you **cannot** access set elements by index.

This will not work:

```python
# regions[0]
```

Sets are designed for membership testing, not positional access.

---

```{admonition} Note
:class: note

If you need ordered access, use a list or tuple.  
If you need named access, use a dictionary.  
If you need fast uniqueness checks, use a set.
```

---


### Multi dimensional collections

Collections can contain **other collections**.
This is called **nesting**.

A common example is a list of lists.

```python
grid = [
    [1, 2, 3],
    [7, 8, 9],
    [6, 5, 4],
]
```

This structure has **two levels**:

* the outer list contains rows
* each inner list contains values

---

### Indexing across multiple levels

Indexing works **one level at a time**, from left to right.

```python
grid[1]
```

This returns the second inner list:

```text
[7, 8, 9]
```

You can then index into that list.

```python
grid[1][0]
```

This returns:

```text
7
```

The logic is:

1. `grid[1]` selects the second row
2. `[0]` selects the first value in that row

Each index always starts at `0`, **at every level**.

---

### Thinking in dimensions

A collection with:

* one level is one dimensional
* two levels is two dimensional
* three levels is three dimensional

For example:

* list of values → one dimensional
* list of coordinate pairs → two dimensional
* list of time steps, each with a grid → three dimensional

You do not need special syntax.
You just apply indexing repeatedly.

---

```{admonition} Note
:class: note

Indexing always works **from the outside in**.

Each pair of square brackets selects one level.
Start with the outer collection, then move inward.
```

---

Understanding how indexing and referencing work is essential when handling spatial data, tables, and collections of coordinates.
It allows you to retrieve exactly the value you intend to work with.

---

## 7. Copying vs Referencing Collections

How assignment works depends on **what kind of value** you are working with.

This difference is subtle but very important, and it is a common source of confusion and bugs.

---

### Single values are copied

With single item values such as numbers or strings, assignment creates a copy.

```python
a = 5
b = a
```

After this:

* `a` and `b` store the same value
* changing one does not affect the other

Single values behave independently.

Strings behave the same way.

Even though a string contains multiple characters, it is **immutable**, so assignment behaves like copying.

```python
s1 = "abc"
s2 = s1
```

Changing one string variable does not affect the other.

---

### Collections are assigned by reference

With collections, assignment does **not** create a copy.
Instead, both variables point to the **same object in memory**.

```python
a = [1, 2]
b = a

a.append(3)
```

Now both variables refer to the same list.

```python
a
```

```python
b
```

Both show the updated content.

This behaviour applies to:

* lists
* dictionaries
* sets

---

### Why this happens

Collections are **mutable objects**.
Python avoids copying them automatically to save memory and time.

The consequence is that changes made through one variable are visible through all variables that reference the same object.

This is efficient, but it requires careful thinking.

---

### Equality vs identity

Two variables can:

* have the same value
* refer to the same object
* or both

The equality operator `==` compares **values**.
The identity operator `is` checks whether two variables refer to the **same object**.

```python
a = [1, 2]
b = a

a == b
```

```python
a is b
```

Now compare this with a copy:

```python
c = a.copy()

c == a
```

```python
c is a
```

Key idea:

* use `==` to compare values
* use `is` to check whether two variables point to the same object

---

### Making an independent copy

If you want a separate copy of a collection, you must create it explicitly.

```python
b = a.copy()
```

You can also use the collection constructor.

```python
b = list(a)
```

Both approaches create a **new list** with the same content.

Now changes to one list do not affect the other.

```python
a.append(4)
```

```python
a
```

```python
b
```

---

```{admonition} Note
:class: note

This difference is a common source of bugs.  
When in doubt, make an explicit copy.
```

---

```{admonition} Warning
:class: warning

Copying a collection only copies the **outer structure**.

If a collection contains other collections, those inner objects may still be shared.
We will revisit this later when working with nested data.
```

---

Understanding copying versus referencing is essential when working with collections of coordinates, attributes, or observations.
It helps you avoid unintended side effects and keeps your workflows predictable.

---

## 8. Short Exercise

You receive raw field information and are asked to organise it into **appropriate data structures** so it can be used reliably later.

### Given Data

```python
raw_cities = ["Bari", "Harare", "Manila", "Harare"]
coords = (41.1311, 16.8701)   # reference point (lat, lon)

raw_attributes = {
    "station": "Bari",
    "elevation_m": 315,
    "crs": "EPSG:4326"
    # discharge_m3s is missing
}
```

---

### Task

1. Create a **set** called `unique_cities` from `raw_cities`.

2. Convert the set back into a **sorted list** called `cities_sorted`.

3. Build a **dictionary** called `station_record` with the following keys:

   * `"name"` → station name
   * `"coordinates"` → the coordinate tuple
   * `"cities"` → the sorted list of cities
   * `"crs"` → CRS string
   * `"discharge_m3s"` → use safe access, default to `"not available"`

4. Access and store the latitude and longitude **using indexing**.

5. Create one readable summary string using an f string that accesses values **from the dictionary**, not from the original variables.

---

````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
# 1) Remove duplicates using a set
unique_cities = set(raw_cities)

# 2) Sort cities
cities_sorted = sorted(unique_cities)

# 3) Build a structured station record
station_record = {
    "name": raw_attributes["station"],
    "coordinates": coords,
    "cities": cities_sorted,
    "crs": raw_attributes["crs"],
    "discharge_m3s": raw_attributes.get("discharge_m3s", "not available"),
}

# 4) Index into the coordinate tuple
lat = station_record["coordinates"][0]
lon = station_record["coordinates"][1]

# 5) Build a summary string from the dictionary
summary = (
    f"Station {station_record['name']} at ({lat}, {lon}) | "
    f"CRS: {station_record['crs']} | "
    f"Cities: {', '.join(station_record['cities'])} | "
    f"Discharge: {station_record['discharge_m3s']}"
)

summary
```

**Why this is a data-structure exercise**

* A **set** is used explicitly for uniqueness.
* A **list** is used where order matters.
* A **tuple** stores fixed coordinate data.
* A **dictionary** combines heterogeneous information into one record.
* Indexing and key access are required.
* `get()` is used for safe dictionary access.
* The final output is built **from the structured data**, not from raw inputs.
````

---

## 9. Summary

After completing this section, you should understand that:

* multi item variables store collections of values
* lists are ordered and changeable
* tuples are ordered and fixed
* sets store unique values
* dictionaries map keys to values
* indexing and referencing depend on the collection type
* copying collections requires explicit action

These concepts explain how Python handles groups of related values and why different collection types exist.

---

### What Comes Next

So far, you have learned how to **store** and **access** multiple values.
On their own, these data structures may still feel abstract.

In the next practical, you will **put them to work**.
It shows why multi-item variables are essential for working with **spatial data** and prepares you for automating such workflows with loops and functions later in the course.