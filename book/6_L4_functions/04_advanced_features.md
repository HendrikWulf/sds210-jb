---
title: Function Interfaces

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Handling arbitrary inputs and metadata
</div>

---

```{admonition} Big Idea
:class: tip

Real-world spatial data is messy and unpredictable. You might not know how many waypoints are in a GPS track, or exactly what metadata fields a geographic feature will contain. Python's variable argument features (`*args` and `**kwargs`) allow you to build flexible functions that adapt to whatever data you throw at them.

```

Up to now, our functions have had a rigid structure: a fixed number of inputs, each with a predefined name. But what if you need to write a function that can accept *any* number of coordinates? Or a function that processes spatial features with a completely unpredictable set of attributes?

In this section, we will unlock the power of flexible function interfaces and anonymous functions.

---

## 1. Collecting Positional Arguments with `*args`

Imagine you want to write a function that calculates the average elevation from a set of GPS points. You don't know in advance if the user will provide 3 points, 10 points, or 100 points.

You *could* force the user to put all the points into a single list before passing them to the function. But Python offers a cleaner way: the unpacking operator (`*`).

When you place an asterisk before a parameter name in a function definition, Python collects an arbitrary number of positional arguments into a **tuple**. By convention, we name this parameter `*args`.

```python
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

**Key Concept:** There is nothing special about the word "args". You could write `*elevations` or `*numbers`, and it would work exactly the same. It is the single asterisk `*` that gives the parameter its superpower.

---

## 2. Collecting Keyword Arguments with `**kwargs`

Just as `*args` collects unknown positional arguments, `**kwargs` collects an arbitrary number of **keyword** arguments.

This is incredibly useful in spatial data science when dealing with metadata. A geographic point must have a latitude and longitude, but it might *also* have an elevation, a Coordinate Reference System (CRS), a name, or a category.

When you place a double asterisk before a parameter name (conventionally `**kwargs`), Python collects any remaining keyword-value pairs into a **dictionary**.

```python
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
describe_point(47.37, 8.54)

# Call 2: Coordinates PLUS arbitrary metadata
describe_point(
    47.37, 
    8.54, 
    city="Zürich", 
    crs="EPSG:4326", 
    elevation=408
)

```

---

## 3. Unpacking Collections

The asterisk operators can also be used *outside* of function definitions to do the exact opposite: **unpacking** lists or dictionaries into separate variables.

Consider a bounding box stored as a list of four coordinates: `[min_lon, min_lat, max_lon, max_lat]`. If you have a function that expects four separate arguments, you can use the `*` operator to unpack the list directly into the function call.

```python
def calculate_area(min_lon, min_lat, max_lon, max_lat):
    width = max_lon - min_lon
    height = max_lat - min_lat
    return width * height

# Our data is trapped inside a list
bbox = [8.5, 47.3, 8.6, 47.4]

# WITHOUT unpacking (Messy):
area = calculate_area(bbox[0], bbox[1], bbox[2], bbox[3])

# WITH unpacking (Clean!):
area = calculate_area(*bbox)

```

### Advanced Unpacking

You can also use the asterisk to elegantly split lists into variables. Notice how the `*rest` variable below scoops up everything in the middle of the list:

```python
# Unpacking a route into start, middle, and end waypoints
first, *rest, last = ["Point A", "Point B", "Point C", "Point D", "Point E"]

print(f"Start: {first}")
print(f"Middle segments: {rest}")
print(f"End: {last}")

```

---

## 4. The Lambda Function

Sometimes you need a tiny, single-use function for a quick calculation (like converting units or formatting text). Defining a full function block with `def` and `return` can feel like overkill.

For these situations, Python offers **lambda functions**. A lambda function is a small, anonymous function (a function without a name) written in a single line.

The syntax is: `lambda arguments : expression`

Here is a comparison for converting meters to feet:

**Named Function:**

```python
def to_feet(meters):
    return meters * 3.28084

```

**Lambda Function:**

```python
# It takes an argument (meters), evaluates the math, and automatically returns it
to_feet_lambda = lambda meters: meters * 3.28084

print(to_feet_lambda(100))

```

Lambda functions shine brightest when used inside other functions. For example, if you have a list of metadata dictionaries and you want to quickly sort them by a specific key, a lambda function does the job in one line:

```python
stations = [
    {"name": "Station A", "elevation": 1200},
    {"name": "Station B", "elevation": 400},
    {"name": "Station C", "elevation": 850}
]

# Sort the list based on the "elevation" value of each dictionary
stations.sort(key=lambda station: station["elevation"])

print(stations)

```

---

## 5. Exercises

Test your understanding of flexible interfaces!

### Exercise 1: The Trail Aggregator (Core)

Write a function called `total_trail_distance()` that accepts any number of trail segment lengths (in kilometers) using `*args`. It should return the total summed distance of the trail.

``````
{admonition} Sample solution
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

``````
{admonition} Sample solution
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

``````
{admonition} Sample solution
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