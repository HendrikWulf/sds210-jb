---

title: The Python Standard Library

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Using batteries included with Python
</div>

---

Python is famous for having "batteries included." This means that when you install Python, you also get the Python Standard Library. This library is a large collection of powerful modules that provide ready to use solutions for common programming tasks. Because these modules are bundled directly with Python, you do not need to download or install anything extra to use them.

You just have to unlock them using the `import` command.

---

## 1. Importing modules

To use a module from the Standard Library, you must import it at the top of your script or notebook. Once imported, you can access all the functions inside it by typing the module name, a dot, and the function name.

```{code-cell} python
import math

# Use the square root function from the math module
result = math.sqrt(25)
print(result)

```

If you only need a specific tool, you can import just that part. This allows you to use the tool directly without typing the module name every time.

```{code-cell} python
from math import pi

print(f"The value of pi is approximately {pi:.44f}")

```

---

## 2. Advanced math and statistics

The `math` module provides access to advanced mathematical functions and constants. A great spatial data science example is calculating the exact distance between two coordinates on the spherical Earth using the Haversine formula.

```{code-cell} python
import math

san_francisco = (37.77, -122.41)
new_york = (40.66, -73.94)

def haversine_distance(origin, destination):
    """Calculates spherical distance between two coordinates in meters."""
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371000 # Earth radius in meters
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return radius * c

dist = haversine_distance(san_francisco, new_york)
print(f"Distance: {dist / 1000:.1f} km")

```

``````{admonition} Useful tools in the math module
:class: dropdown

While the `math` module contains dozens of functions, you will likely rely on this core set for most spatial and data science workflows:

| Function / Constant | Description |
| :--- | :--- |
| **Rounding & Absolute Values** | |
| `math.ceil(x)` | Rounds *x* **up** to the nearest integer. |
| `math.floor(x)` | Rounds *x* **down** to the nearest integer. |
| `math.trunc(x)` | Cuts off the fractional part of *x*, leaving just the integer. |
| `math.fabs(x)` | Returns the absolute (positive) value of *x*. |
| **Geometry & Distances** | |
| `math.sqrt(x)` | The square root of *x*. |
| `math.pow(x, y)` | *x* raised to the power of *y* (similar to `x ** y`). |
| `math.dist(p, q)` | Calculates the Euclidean distance between two coordinate points *p* and *q*. |
| `math.hypot(x, y)` | Calculates the length of a hypotenuse (Euclidean norm). |
| **Angles & Trigonometry** | |
| `math.radians(x)` | Converts angle *x* from degrees to radians. |
| `math.degrees(x)` | Converts angle *x* from radians to degrees. |
| `math.sin(x)`, `math.cos(x)` | Sine and cosine of *x* (where *x* is in radians). |
| `math.atan2(y, x)` | Arc tangent of *y/x*, often used to find the angle/bearing between points. |
| **Important Constants** | |
| `math.pi` | The mathematical constant π (3.14159...). |
| `math.nan` | "Not a Number", often used to represent missing data in datasets. |
| `math.inf` | Positive infinity. |

*Tip: You can view the complete list of mathematical functions anytime by visiting the [official Python documentation](https://docs.python.org/3/library/math.html).*

``````

If you need to analyze lists of numbers, the `statistics` module is incredibly useful. It provides functions for calculating the mean, median, and mode of your data without writing loops yourself.

```{code-cell} python
import statistics

elevations = [450, 1200, 890, 2300, 1200, 500]

print(f"Average: {statistics.mean(elevations)} m")
print(f"Median: {statistics.median(elevations)} m")

```

``````{admonition} Useful tools in the statistics module
:class: dropdown

The `statistics` module provides robust functions for calculating mathematical statistics of numeric data. Here are the most common functions you will use when analyzing datasets:

| Function | Description |
| :--- | :--- |
| **Averages & Central Location** | |
| `statistics.mean(data)` | Calculates the arithmetic mean ("average") of the data. |
| `statistics.median(data)` | Returns the middle value of the data (half the values are above, half are below). |
| `statistics.mode(data)` | Returns the single most common data point from the dataset. |
| `statistics.multimode(data)`| Returns a list of the most frequently occurring values (useful if there's a tie). |
| **Measures of Spread** | |
| `statistics.stdev(data)` | Calculates the sample standard deviation (a measure of how spread out the numbers are). |
| `statistics.variance(data)` | Calculates the sample variance. |
| `statistics.quantiles(data)`| Divides continuous data into equal-probability intervals (e.g., quartiles or percentiles). |

*Tip: You can view the complete list of statistical functions anytime by visiting the [official Python documentation](https://docs.python.org/3/library/statistics.html).*

``````

---

## 3. Adding unpredictability

The `random` module is used to generate random numbers and make random selections. This is especially useful in spatial sampling, simulations, or creating dummy data for testing.

```{code-cell} python
import random

# Pick a random integer between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number: {random_number}")

# Pick a random item from a list
cities = ["Zurich", "Geneva", "Basel", "Bern"]
random_city = random.choice(cities)
print(f"Randomly selected city: {random_city}")

```

``````{admonition} Useful tools in the random module
:class: dropdown

The `random` module offers many ways to generate random numbers and make random selections. Here are the most common functions for spatial analysis and data science:

| Function | Description |
| :--- | :--- |
| **Generating Numbers** | |
| `random.random()` | Returns a random float number between 0.0 and 1.0. |
| `random.randint(a, b)` | Returns a random integer between *a* and *b* (inclusive). |
| `random.uniform(a, b)` | Returns a random float number between *a* and *b*. |
| **Selecting & Shuffling** | |
| `random.choice(seq)` | Returns a single randomly selected item from a list. |
| `random.choices(seq, k=n)` | Returns a list of *n* items chosen from *seq* **with replacement** (duplicates allowed). |
| `random.sample(seq, k=n)` | Returns a list of *n* unique items chosen from *seq* **without replacement** (no duplicates). |
| `random.shuffle(seq)` | Shuffles the items in a list randomly in place. |
| **Reproducibility** | |
| `random.seed(value)` | Sets a starting seed. Using the same seed guarantees you get the exact same sequence of "random" numbers every time you run your script. |

*Tip: You can view the complete list of random functions anytime by visiting the [official Python documentation](https://docs.python.org/3/library/random.html).*

``````

---

## 4. Navigating your computer

When working with local data, you often need to know exactly which folder your Python code is running in. The `os` module (Operating System) and the `pathlib` module help you interact with your computer files.

```{code-cell} python
import os

# Get the current working directory
current_folder = os.getcwd()
print(f"Python is currently looking for files in: {current_folder}")

```

``````{admonition} Useful tools in the os module
:class: dropdown

The `os` module and its submodule `os.path` provide essential tools for navigating folders and managing files. Here are the most common functions you will use when organizing your spatial data projects:

| Function | Description |
| :--- | :--- |
| **Directories & Folders** | |
| `os.getcwd()` | Returns the Current Working Directory (the folder Python is currently looking in). |
| `os.chdir(path)` | Changes the current working directory to the specified *path*. |
| `os.listdir(path)` | Returns a list of all files and folders inside the specified *path*. |
| `os.mkdir(path)` | Creates a new single folder at the specified *path*. |
| `os.makedirs(path)` | Creates a new folder and any missing parent folders along the *path*. |
| **Working with Paths** | |
| `os.path.join(path, *paths)` | Intelligently joins folder and file names together using the correct slash (`\` or `/`) for your operating system. |
| `os.path.exists(path)` | Returns `True` if the file or folder at the given *path* actually exists. |
| `os.path.basename(path)` | Returns the final file name from a long path (e.g., returns `data.csv` from `C:/folder/data.csv`). |
| `os.path.dirname(path)` | Returns the directory name from a long path (e.g., returns `C:/folder` from `C:/folder/data.csv`). |
| **File Operations** | |
| `os.rename(src, dst)` | Renames or moves a file or folder from the source (*src*) to the destination (*dst*). |
| `os.remove(path)` | Deletes a file. |

*Tip: You can view the complete list of OS functions anytime by visiting the [official Python documentation](https://docs.python.org/3/library/os.html).*

``````

---

## 5. Formatting data with JSON

JSON (JavaScript Object Notation) is a lightweight text format used to store and transport data. It looks almost exactly like Python dictionaries and lists. The `json` module allows you to convert text data into usable Python objects.

This is a critical skill for working with Web APIs, which almost always return data in JSON format.

```{code-cell} python
import json

# A string of text formatted as JSON
api_response_text = '{"city": "Zurich", "coordinates": [47.37, 8.54], "population": 415000}'

# Convert the text string into a real Python dictionary
data = json.loads(api_response_text)

# Now we can access it using standard dictionary keys
print(data["city"])
print(data["coordinates"])

```

``````{admonition} Useful tools in the json module
:class: dropdown

The `json` module provides straightforward functions for reading and writing JSON data. Here are the core functions you will use when interacting with APIs or saving your data:

| Function | Description |
| :--- | :--- |
| **Reading JSON (Decoding)** | |
| `json.loads(string)` | Parses a JSON-formatted **text string** into a Python dictionary or list. |
| `json.load(file)` | Reads JSON data directly from an opened **file** and converts it into a Python object. |
| **Writing JSON (Encoding)** | |
| `json.dumps(obj)` | Converts a Python object (like a dictionary) into a JSON-formatted **text string**. |
| `json.dump(obj, file)` | Writes a Python object directly into an opened **file** in JSON format. |
| **Helpful Parameters** | |
| `indent=4` | Used inside `dumps()` or `dump()` to "pretty-print" the JSON with 4 spaces of indentation, making it much easier for humans to read. |

*Tip: You can view the complete documentation anytime by visiting the [official Python documentation](https://docs.python.org/3/library/json.html).*
``````

```{admonition} Python Easter Eggs
:class: tip
Programmers like to hide secret jokes in their code. Try running `import this` in a new cell to see the guiding philosophy of Python, or try `import antigravity` to see where Python can take you!

```

---

## 6. Exercises

To practice using the Standard Library, complete the following tasks.

---

### Exercise 1: Random coordinates

Using the `random` module, write a loop that generates 3 random coordinate pairs. Assume the latitude must be an integer between 45 and 47, and the longitude must be an integer between 6 and 9. Print each pair.

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
import random

for i in range(3):
    lat = random.randint(45, 47)
    lon = random.randint(6, 9)
    print(f"Coordinate {i+1}: [{lat}, {lon}]")
```

**Key idea:**
The `randint` function requires a start and end value and generates a new random integer every time it is called inside the loop.

``````

---

### Exercise 2: Parsing JSON

You downloaded a small JSON string representing a feature collection. Use the `json` module to parse it into a Python dictionary, then print the name of the feature.

```{code-cell} python
geojson_string = '{"type": "Feature", "properties": {"name": "Matterhorn"}, "geometry": {"type": "Point", "coordinates": [7.65, 45.97]}}'

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
import json

geojson_string = '{"type": "Feature", "properties": {"name": "Matterhorn"}, "geometry": {"type": "Point", "coordinates": [7.65, 45.97]}}'

# Parse the string into a dictionary
parsed_data = json.loads(geojson_string)

# Extract the nested value
mountain_name = parsed_data["properties"]["name"]
print(mountain_name)
```

**Key idea:**
`json.loads()` converts a raw text string into a standard Python dictionary. Once converted, you can chain brackets `[][]` to access nested information.

``````

---

## 7. Summary

In this section, you learned how to leverage the Python Standard Library to solve common programming tasks without installing external tools. You discovered how to:

* Import entire modules (`import math`) or specific tools (`from math import pi`).
* Use `math` and `statistics` for complex calculations and data summaries.
* Use `random` to generate unpredictable numbers and selections.
* Use `os` to check your current working directory.
* Use `json` to parse structured text strings into usable Python dictionaries.

### What comes next?

The Standard Library is powerful, but it does not contain everything. What if you want to pull live routing data or weather forecasts directly from the internet? In the next section, we will explore **Third Party Modules and Web APIs**, where you will learn how to install external packages to connect Python to the rest of the world.