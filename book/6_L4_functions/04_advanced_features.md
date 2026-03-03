---
title: Flexible Function Interfaces

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Handling arbitrary inputs and metadata
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/6_L4_functions/04_advanced_features.ipynb)

---

```{admonition} Big Idea
:class: tip

Real-world spatial data can be messy and unpredictable. You might not know how many waypoints are in a GPS track, or exactly what metadata fields a geographic feature will contain. Python's variable argument features (`*args` and `**kwargs`) allow you to build flexible functions that adapt to whatever data you throw at them.

```

Up to now, our functions have had a rigid structure: a fixed number of inputs, each with a predefined name. But what if you need to write a function that can accept *any* number of coordinates? Or a function that processes spatial features with a completely unpredictable set of attributes?

In this section, we will unlock the power of flexible function interfaces and anonymous functions.

---

## 1. Collecting Positional Arguments with `*args`

Imagine you want to write a function that calculates the average elevation from a set of GPS points. You don't know in advance if the user will provide 3 points, 10 points, or 100 points.

You *could* force the user to put all the points into a single list before passing them to the function. But Python offers a cleaner way: the unpacking operator (`*`).

When you place an asterisk before a parameter name in a function definition, Python collects an arbitrary number of positional arguments into a **tuple**. By convention, we name this parameter `*args`.

:::{figure} images/11_args.png
:alt: Diagram showing multiple individual values being packed into a single tuple using the `*args` syntax.
:width: 600px
:align: center

Visualizing `*args`: Multiple individual inputs are collected and packed into a single tuple.
:::

```{code-cell} python
def average_elevation(*args):
    """Calculates the average of an arbitrary number of elevations."""
    # args is just a tuple containing all the inputs!
    if len(args) == 0:
        return 0
        
    total = sum(args)
    num_items = len(args)
    return total / num_items

# We can pass any number of arguments!
avg_1 = average_elevation(1500, 1520, 1490)
print(f"Average 1: {avg_1} meters")

avg_2 = average_elevation(100, 105, 102, 98, 110, 101, 99)
print(f"Average 2: {avg_2} meters")

```

```{admonition} Key Concept
:class: important

There is nothing special about the word "args". You could write `*elevations` or `*numbers`, and it would work exactly the same. It is the single asterisk `*` that gives the parameter its superpower.

```

---

## 2. Collecting Keyword Arguments with `**kwargs`

Just as `*args` collects unknown positional arguments, `**kwargs` collects an arbitrary number of **keyword** arguments.

This is incredibly useful in spatial data science when dealing with metadata. A geographic point must have a latitude and longitude, but it might *also* have an elevation, a Coordinate Reference System (CRS), a name, or a category.

When you place a double asterisk before a parameter name (conventionally `**kwargs`), Python collects any remaining keyword-value pairs into a **dictionary**.

:::{figure} images/12_kwargs.png
:alt: Diagram showing multiple keyword-value pairs being packed into a single dictionary using the `**kwargs` syntax.
:width: 600px
:align: center

Visualizing `**kwargs`: Multiple keyword-value pairs are collected and packed into a single dictionary.
:::

```{code-cell} python
def describe_point(lat, lon, **kwargs):
    """Prints a point's coordinates and any associated metadata."""
    print(f"Point Coordinates: {lat} N, {lon} E")
    
    # kwargs is a dictionary, so we can loop through its items!
    if kwargs:
        print("Metadata:")
        for key, value in kwargs.items():
            print(f"  - {key}: {value}")
    print("-" * 20)

# Call 1: Just the required coordinates
describe_point(45.936928, 7.866760)

# Call 2: Coordinates PLUS arbitrary metadata
describe_point(
    45.936928,
    7.866760,
    name="Dufourspitze",
    crs="EPSG:4326",
    elevation=4633,
    country="Switzerland"
)

```

```{admonition} Key Concept
:class: important

Just like with `*args`, there is nothing special about the word "kwargs". You could write `**metadata` or `**properties`, and it would work exactly the same. It is the double asterisk `**` that gives the parameter its superpower, automatically packing the extra key-value pairs into a dictionary.

```

---

## 3. Unpacking Collections

The asterisk operators can also be used *outside* of function definitions to do the exact opposite: **unpacking** lists or dictionaries into separate variables.

Consider a bounding box stored as a list of four coordinates: `[min_lon, min_lat, max_lon, max_lat]`. If you have a function that expects four separate arguments, you can use the `*` operator to unpack the list directly into the function call.

```{code-cell} python
def calculate_area(min_lon, min_lat, max_lon, max_lat):
    width = max_lon - min_lon
    height = max_lat - min_lat
    return width * height

# Our data is trapped inside a list
bbox = [2634400, 1137300, 2652000, 1159800]

# WITHOUT unpacking (Messy):
area = calculate_area(bbox[0], bbox[1], bbox[2], bbox[3])

# WITH unpacking (Clean):
area = calculate_area(*bbox)
print(f'The area of the bounding box is {area} square meters')

```

### Unpacking Dictionaries with `**`

You can use the double asterisk (`**`) to unpack a dictionary directly into a function's keyword arguments. For this to work, the keys in your dictionary must match the parameter names in the function exactly.

Imagine you have a function to style and plot a map marker, and your styling data is stored in a dictionary:

:::{figure} images/13_unpacking.png
:alt: Diagram showing a dictionary being unpacked into separate keyword arguments for a function call.
:width: 600px
:align: center

Visualizing dictionary unpacking: A dictionary's key-value pairs are unpacked and match the function's parameter names.
:::

```{code-cell} python
def plot_marker(lat, lon, label, color="red", size=10):
    print(f"Plotting {label} at ({lat}, {lon}) | Color: {color}, Size: {size}")

# Our data is trapped in a dictionary
marker_data = {
    "lat": 47.37, 
    "lon": 8.54, 
    "label": "Zürich", 
    "color": "blue"
}

# WITHOUT unpacking (repetitive):
plot_marker(
    lat=marker_data["lat"], 
    lon=marker_data["lon"], 
    label=marker_data["label"], 
    color=marker_data["color"]
)

# WITH unpacking (elegant):
plot_marker(**marker_data)

```

Notice how Python automatically matches the `"lat"` key in the dictionary to the `lat` parameter in the function!

### Advanced Unpacking

You can also use the asterisk to elegantly split lists into variables. Notice how the `*rest` variable below scoops up everything in the middle of the list:

```{code-cell} python
# Unpacking a route into start, middle, and end waypoints
first, *rest, last = ["Point A", "Point B", "Point C", "Point D", "Point E"]

print(f"Start: {first}")
print(f"Middle segments: {rest}")
print(f"End: {last}")

```

---

### The Dual Nature of Asterisks

The hardest part about `*` and `**` is that they do the **exact opposite** depending on where you use them.

1. **When DEFINING a function (Packing):**
If you put an asterisk in the `def` statement (e.g., `def my_func(*args)`), it acts like a vacuum. It sucks up many loose arguments and packs them tightly into a single tuple (or dictionary for `**`).
2. **When CALLING a function (Unpacking):**
If you put an asterisk in the function call (e.g., `my_func(*my_list)`), it acts like an explosion. It takes a packed collection (like a list or dictionary) and blows it apart into many separate, loose arguments.

:::{figure} images/14_un-packing.png
:alt: Side-by-side diagram comparing the packing behavior of asterisks in function definitions versus their unpacking behavior in function calls.
:width: 800px
:align: center

The dual nature of asterisks: They **pack** arguments when defining a function and **unpack** collections when calling a function.
:::

---

## 4. The Lambda Function

Sometimes you need a tiny, single-use function for a quick calculation (like converting units or formatting text). Defining a full function block with `def` and `return` can feel like overkill.

For these situations, Python offers **lambda functions**. A lambda function is a small, anonymous function (a function without a name) written in a single line.

The syntax is: `lambda arguments : expression`

Here is a comparison for converting meters to feet:

**Named Function:**

```{code-cell} python
def to_feet(meters):
    return meters * 3.28084

```

**Lambda Function:**

```{code-cell} python
# It takes an argument (meters), evaluates the math, and automatically returns it
to_feet_lambda = lambda meters: meters * 3.28084

print(to_feet_lambda(100))

```

Lambda functions shine brightest when used inside other functions. For example, if you have a list of metadata dictionaries and you want to quickly sort them by a specific key, a lambda function does the job in one line:

:::{figure} images/15_lambda.png
:alt: Diagram illustrating how a lambda function acts as a key extractor for sorting a list of dictionaries.
:width: 800px
:align: center

Visualizing lambda sorting: The lambda function extracts a specific value (e.g., 'elevation') from each item, which is then used to determine the sort order of the original list.
:::

```{code-cell} python
stations = [
    {"name": "Station A", "elevation": 1200},
    {"name": "Station B", "elevation": 400},
    {"name": "Station C", "elevation": 850}
]

# Sort the list based on the "elevation" value of each dictionary
stations.sort(key=lambda station: station["elevation"])

print(stations)

```

``````{admonition} Click here for a more detailed breakdown of this lambda example.
:class: dropdown

**1. The Problem with Sorting Dictionaries**

If you have a simple list of numbers, Python knows exactly how to sort them:

```{code-cell} python
numbers = [1200, 400, 850]
numbers.sort() 
# Result: [400, 850, 1200]
```

But in our spatial example, `stations` is not a list of numbers. It is a list of **dictionaries**:

```{code-cell} python
stations = [
    {"name": "Station A", "elevation": 1200},
    {"name": "Station B", "elevation": 400},
    {"name": "Station C", "elevation": 850}
]
```

If you just type `stations.sort()`, Python will crash. It will say: *"I don't know how to compare two dictionaries! Should I sort them alphabetically by their names? Or numerically by their elevations?"*

**2. The `key` Parameter (The Referee)**

To fix this, the `.sort()` method has a special optional parameter called `key`.

Think of the `key` parameter as a referee. You must hand the referee a **function**. The referee will then apply that function to every single item in the list to extract a simple value (like a number or string) that it *can* sort.

If we didn't use `lambda`, we would have to write a full, named function to act as our extractor:

```{code-cell} python
# 1. We write a function that takes ONE dictionary and returns its elevation
def get_elevation(station_dict):
    return station_dict["elevation"]

# 2. We hand that function to the sort method
stations.sort(key=get_elevation)
```

**3. What the `lambda` Function Does (The Shortcut)**

Writing a full `def` block just to extract a single dictionary value is tedious. This is exactly where **lambda functions** shine. They allow us to write that extractor function directly inside the `.sort()` parentheses in a single line.

Let's look at our line again:

```{code-cell} python
stations.sort(key=lambda station: station["elevation"])
```

Here is exactly what the lambda function is doing:

1. `lambda`: "I am creating a quick, nameless function right here."
2. `station:`: "This function takes one argument. Let's call it `station`. (During the sort, Python will pass each dictionary into this variable one by one)."
3. `station["elevation"]`: "I will look inside that dictionary, grab the value attached to the 'elevation' key, and return it to the sorting referee."

**Step-by-Step: What happens behind the scenes?**

When Python executes that line, it does a multi-step process in a fraction of a millisecond:

1. It looks at the first item: `{"name": "Station A", "elevation": 1200}`.
2. It passes this to the lambda. The lambda returns `1200`.
3. It looks at the second item: `{"name": "Station B", "elevation": 400}`.
4. It passes this to the lambda. The lambda returns `400`.
5. It looks at the third item: `{"name": "Station C", "elevation": 850}`.
6. It passes this to the lambda. The lambda returns `850`.
7. Now that it has a list of simple numbers (`1200, 400, 850`), Python sorts them from lowest to highest (`400, 850, 1200`).
8. Finally, it rearranges the original dictionaries to match that new order!

**Final Output:**

```{code-cell} text
[
    {'name': 'Station B', 'elevation': 400}, 
    {'name': 'Station C', 'elevation': 850}, 
    {'name': 'Station A', 'elevation': 1200}
]
```


``````

---

## 5. Exercises

Test your understanding of flexible interfaces!

### Exercise 1: The Trail Aggregator (Core)

Write a function called `total_trail_distance()` that accepts any number of trail segment lengths (in kilometers) using `*args`. It should return the total summed distance of the trail.

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
def total_trail_distance(*segments):
    # 'segments' is a tuple of all provided arguments
    return sum(segments)

# Testing the function with 4 segments
print(total_trail_distance(5.2, 3.1, 4.0, 1.5)) 
```

``````


### Exercise 2: Building GeoJSON Properties (Stretch)

In web mapping, spatial features use a format called GeoJSON, which stores data in a `"properties"` dictionary.
Write a function `create_feature(name, **kwargs)` that takes a required `name` and any number of keyword arguments. It should return a dictionary formatted like this:
`{"name": name, "properties": {all_the_kwargs}}`

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
def create_feature(name, **kwargs):
    # kwargs is automatically a dictionary containing the extra arguments
    feature = {
        "name": name,
        "properties": kwargs
    }
    return feature

# Testing the function
site = create_feature("Site 42", status="active", soil_type="clay", ph=6.5)
print(site)
```

``````


### Exercise 3: Lambda Sorting (Challenge)

You have a list of coordinate pairs: `coords = [[8.54, 47.37], [6.14, 46.20], [7.44, 46.94]]`.
Using the `.sort()` method and a `lambda` function, sort this list based *only* on the latitude (the second item in each pair, index `1`).

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
coords = [[8.54, 47.37], [6.14, 46.20], [7.44, 46.94]]

# The lambda takes one item (a coordinate pair like [8.54, 47.37]) 
# and returns index 1 (the latitude) to use as the sorting key
coords.sort(key=lambda pair: pair[1])

print(coords)
# Output should be ordered by latitude: Geneva, Bern, Zürich
```

``````

---

## 6. Summary

In this section, you learned how to break free from rigid function definitions:

* **`*args`**: Collects an arbitrary number of positional arguments into a tuple.
* **`**kwargs`**: Collects an arbitrary number of keyword arguments into a dictionary, perfect for flexible metadata.
* **Unpacking (`*`)**: Extracts items from lists or dictionaries directly into function arguments or separate variables.
* **Lambda functions**: Provide a concise, one-line syntax for simple operations, often used as arguments inside other functions.

### What comes next?

Next, we will look at how to construct **Professional Functions** by focusing on standard documentation (docstrings), introspection (`help()`), and learning how to avoid the most common function-related bugs in data science pipelines.
