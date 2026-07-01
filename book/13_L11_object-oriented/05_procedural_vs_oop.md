---
title: Procedural vs OOP

site:
  outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Choosing the right design for spatial problems
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/13_L11_object-oriented/05_procedural_vs_oop.ipynb)

---

```{admonition} Big idea
:class: tip

{term}`Procedural programming <Procedural programming>` and {term}`object-oriented programming <Object-oriented programming>` solve the same problems in different ways. The key question is not which style is better in general, but which one makes a specific spatial task clearer, safer, and easier to extend.
```

```{admonition} Chapter Relevance
:class: dropdown

**Project Relevance:** ★★★ (Crucial for scoring well on the "Code Quality" and "Logical Workflow" assessment criteria across all projects 1, 2, 3, and 4)  
**Foundation:** ★★★ (Builds core architectural judgment for choosing between standalone functions, classes, and mixed designs)  

**Time to Read:** 15 minutes  
**In a nutshell:** Compare Procedural and Object-Oriented design side-by-side to understand when to use standalone functions and when to build self-contained classes.  
**Skip this if:** You can already confidently explain, using a spatial data science example, exactly when to use a procedural script versus when to architect a class-based system.

```

In the previous chapters, you defined {term}`classes <Class>`, created {term}`object instances <Instance>`, and explored how {term}`inheritance <Inheritance>` allows you to build complex spatial relationships. You might be wondering: should you write absolutely everything as a class from now on?

The short answer is no. Object-oriented programming is a powerful design choice, but it is not the one correct way to write Python. Python is a multi-paradigm language. It supports several different programming styles, and strong programmers move fluidly between them depending on the task at hand.

This matters immensely in {term}`spatial data science <Spatial data science>`.

Sometimes a short, standalone {term}`function <Function>` is exactly the right tool. If you only need to transform a {term}`list <List>` of coordinates, compute a single distance, or clip a raster {term}`array <Array>`, writing a full class adds unnecessary complexity. In other situations, however, the data and the behavior belong together so naturally that procedural code starts to feel scattered and fragile. This is especially true when you represent real spatial entities—like a sensor network or a moving GPS track—that have multiple related {term}`properties <Property>` that must stay consistent over time.

This chapter compares both design styles using the same geospatial problems to help you understand their relative strengths. The goal is not to crown a winner. The goal is to build your architectural judgment.

---

## 1. Why compare styles?

So far in this course, you have learned Python mainly through {term}`variables <Variable>`, {term}`loops <Loop>`, conditionals, functions, and then classes. That progression can create the impression that classes are simply the "next level" and should always replace earlier tools.

That is not how good design works.

A programming style is a way of organizing thought. Procedural code organizes workflows around **actions** (verbs). Object-oriented code organizes workflows around **entities** (nouns). Both can be excellent. Both can also be misused.

```{mermaid}
flowchart TD
    subgraph Procedural ["Procedural Paradigm (Separated)"]
        direction LR
        P_Data[("Data<br>(e.g., Dictionary)")]
        P_Func[["Standalone Function<br>calculate_distance()"]]
        
        P_Data -->|"passed into"| P_Func
    end

    subgraph OOP ["Object-Oriented Paradigm (Bundled)"]
        direction LR
        subgraph Entity ["Point Object"]
            direction LR
            O_Data[("State<br>(self.x, self.y)")]
            O_Meth[["Method<br>.distance_to()"]]
            
            O_Data ~~~ O_Meth
        end
    end

    classDef default fill:#f8fafc,stroke:#94a3b8,stroke-width:2px,color:#0f172a;
    classDef object fill:#e0f2fe,stroke:#3b82f6,stroke-width:2px,color:#0f172a,stroke-dasharray: 5 5;
    class Entity object;
```

<!-- markdownlint-disable MD033-->
<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L11_ch05_02_procedural_vs_oop/"
    width="100%" 
    height="600px" 
    frameborder="0" 
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Procedural vs Object-Oriented Design.</b><br>
    Add fields such as CRS, elevation, timestamp, and sensor history to a spatial point and watch how the procedural version separates dictionaries from functions, while the object-oriented version bundles attributes and methods inside one object. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L11_ch05_02_procedural_vs_oop/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

Consider a simple spatial question:

> What is the distance between two cities?

You can solve this procedurally by focusing on the action:

* store the coordinates in {term}`tuples <Tuple>`, lists, or {term}`dictionaries <Dictionary>`
* write a standalone function for the distance
* pass the coordinates into that function

Or you can solve it with {term}`objects <Object>` by focusing on the entity:

* represent each city as a `Point`
* attach a {term}`method <Method>` such as `.distance_to()`
* ask one point directly for the distance to another

In code, that philosophical shift looks like this:

```python
# Procedural: The function acts on the data
dist = calculate_distance(zurich, bern)

# Object-Oriented: The object performs the action on itself
dist = zurich.distance_to(bern)
```

Both solutions will return the exact same number. The difference lies in **how the code is structured**, **how easy it is to read**, and **how well it scales when the task becomes larger**.

```{admonition} A useful rule of thumb
:class: note

Functions are often best when you mainly want to transform inputs into outputs.

Classes are often best when you want to represent something that has both state and behavior.
```

---

## 2. A procedural design

Let us begin with the most direct solution: plain data structures plus standalone functions.

Imagine we want to represent named locations and compute distances between them. We will use the Swiss projected coordinate system (EPSG:2056 / LV95), where coordinates are measured in meters.

```{code-cell} python
# Coordinates in EPSG:2056 (LV95)
zurich = {"x": 2682217, "y": 1247945, "name": "Zurich"}
bern = {"x": 2598634, "y": 1200387, "name": "Bern"}
basel = {"x": 2611415, "y": 1267104, "name": "Basel"}
```

Each city is stored as a dictionary. This is an improvement over scattering the information across separate variables because the values that belong together are grouped into one structure.

Now we can write a standalone distance function:

```{code-cell} python
import math

def distance(point1, point2):
    dx = point1["x"] - point2["x"]
    dy = point1["y"] - point2["y"]
    return math.sqrt(dx**2 + dy**2)
```

```{code-cell} python
# Calculate distance and convert to kilometers
dist_m = distance(zurich, bern)
print(f"Distance Zurich-Bern: {dist_m / 1000:.1f} km")

dist_m = distance(zurich, basel)
print(f"Distance Zurich-Basel: {dist_m / 1000:.1f} km")
```

```{admonition} Why projected coordinates matter
:class: note

Because our data is projected (EPSG:2056), the $x$ (Easting) and $y$ (Northing) coordinates form a flat Cartesian grid measured in meters. This allows us to use simple {term}`Euclidean math <Euclidean distance>` (the Pythagorean theorem) to accurately calculate the real-world ground distance. If we had used standard latitude/longitude degrees, this simple math would have produced distorted and meaningless results.
```

This is procedural code in a very normal Python sense:

* The **data** live in passive structures (dictionaries).
* The **behavior** lives in free functions.
* We pass all required inputs explicitly into those functions.

### Extending the procedural approach

Let us add another spatial entity: a bounding box representing the Swiss Plateau, again using a dictionary.

```{code-cell} python
study_area = {
    "xmin": 2500000,
    "xmax": 2750000,
    "ymin": 1150000,
    "ymax": 1300000,
    "name": "Swiss Plateau Window"
}
```

Now we can write a function that checks whether a point lies inside that box:

```{code-cell} python
def point_in_bbox(point, bbox):
    return (
        bbox["xmin"] <= point["x"] <= bbox["xmax"]
        and bbox["ymin"] <= point["y"] <= bbox["ymax"]
    )
```

```{code-cell} python
print(f"Zurich in study area: {point_in_bbox(zurich, study_area)}")
print(f"Bern in study area: {point_in_bbox(bern, study_area)}")
print(f"Basel in study area: {point_in_bbox(basel, study_area)}")
```

At this point, the procedural approach still feels quite manageable. The functions are clear, and it is easy to track how the data moves through them.

---

## 3. Where procedural code strains

The procedural design becomes harder to manage when the data structure grows and the same kind of logic must be repeated in many places.

Suppose each point should now also store a {term}`Coordinate Reference System`, an elevation, and a timestamp. A dictionary can still do that:

```{code-cell} python
zurich = {
    "x": 2682217,
    "y": 1247945,
    "name": "Zurich",
    "crs": "EPSG:2056",
    "elevation_m": 408,
    "timestamp": "2026-05-06"
}
```

Notice what happens conceptually. The {term}`computer program <Program>` does not inherently know that these data are related to a single concept. Therefore, you need to ensure that all of those links are made manually in the code.

For example, if you want to write a safe, purely procedural function to move a point without destroying the original data, it might look like this:

```{code-cell} python
def move_point(point, dx, dy):
    return {
        "x": point["x"] + dx,
        "y": point["y"] + dy,
        # The following lines are tedious boilerplate
        "name": point["name"],
        "crs": point["crs"],
        "elevation_m": point["elevation_m"],
        "timestamp": point["timestamp"]
    }
```

We are manually rebuilding the structure and manually preserving fields that are not even central to the movement itself. The computer still does not know that these values are meant to form one kind of cohesive entity called a "point". If you accidentally misspell `"elevation_m"` as `"elev_m"` while rebuilding the dictionary, Python will not warn you until another part of your code crashes.

```{admonition} The hidden cost of procedural design
:class: warning

Procedural code often begins very clearly, but it can become fragile when the same kind of entity appears again and again with many related properties. At that point, the structure is maintained mostly by programmer discipline rather than by the design itself.
```

#### Concept Check: When Does a Class Earn Its Keep?

You are building a small project around GPS stations. At first, each station only has `x`, `y`, and `name`. Later, each station must also store a CRS, elevation, timestamp, and a live temperature history. You also need to update values and compute distances repeatedly. Which design choice is most justified?

A. Keep everything procedural because dictionaries can store all these fields.

B. Use a class because the station now has related state and behavior that should stay together.

C. Avoid both functions and classes and write all calculations directly in the notebook cells.

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
A class is justified because the station has multiple related attributes and repeated behavior, so bundling them together makes the code safer and easier to extend. A can still work, but it becomes increasingly fragile; C makes the workflow hardest to read, test, and reuse.

```

---

## 4. An object-oriented design

Now let us rebuild the same problem using classes. While functions group related operations, classes group related data and the operations that work on that data into single cohesive units.

We begin with a `Point` class. Notice how we define all the {term}`attributes <Attribute>` we struggled with in the procedural version:

```{code-cell} python
import math

class Point:
    def __init__(self, x, y, name=None, crs="EPSG:2056", elevation_m=None, timestamp=None):
        self.x = x
        self.y = y
        self.name = name
        self.crs = crs
        self.elevation_m = elevation_m
        self.timestamp = timestamp

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Now we instantiate our Swiss cities:

```{code-cell} python
zurich = Point(2682217, 1247945, "Zurich", elevation_m=408, timestamp="2026-05-06")
bern = Point(2598634, 1200387, "Bern", elevation_m=542)
basel = Point(2611415, 1267104, "Basel", elevation_m=260)
```

The distance calculation is now expressed differently:

```{code-cell} python
dist_m = zurich.distance_to(bern)
print(f"Distance: {dist_m / 1000:.1f} km")
```

This still performs the same mathematics, but the design has changed fundamentally. The point no longer exists as a loose dictionary plus a distant function. Instead, the data and the behavior are **bundled together** in one coherent object.

Remember how tedious it was to move a point procedurally because we had to manually preserve all the unrelated dictionary keys? With an object, the state is managed internally:

```{code-cell} python
# Move Zurich 100 meters East and 50 meters South
zurich.move(100, -50)

# The coordinates changed, but the rest of the data is perfectly safe!
print(f"New X: {zurich.x}, Elevation: {zurich.elevation_m}, CRS: {zurich.crs}")
```

### Adding a bounding box class

Now let us define a `BoundingBox` class:

```{code-cell} python
class BoundingBox:
    def __init__(self, xmin, xmax, ymin, ymax, name=None):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.name = name

    def area_sq_km(self):
        width_m = self.xmax - self.xmin
        height_m = self.ymax - self.ymin
        return (width_m * height_m) / 1_000_000

    def contains(self, point):
        return (
            self.xmin <= point.x <= self.xmax
            and self.ymin <= point.y <= self.ymax
        )
```

```{code-cell} python
study_area = BoundingBox(2500000, 2750000, 1150000, 1300000, "Swiss Plateau Window")

print(f"Area: {study_area.area_sq_km():.1f} sq km")
print(f"Contains Zurich: {study_area.contains(zurich)}")
```

The behavior now clearly belongs to the entity. A bounding box naturally "knows" its area, and it can test whether it contains a point without needing external helper functions.

---

## 5. Comparing both designs

Now that we have both versions, we can compare them directly.

### Readability

The procedural version says:

```python
dist = distance(zurich, bern)
```

The object-oriented version says:

```python
dist = zurich.distance_to(bern)
```

Both are highly readable, but they emphasize different things:

* **Procedural code reads like a command:** *Verb ➔ Objects*. It emphasizes the mathematical operation.
* **Object-oriented code reads like a sentence:** *Subject ➔ Verb ➔ Object*. It emphasizes the entity performing the operation.

### Maintainability and Safety

Imagine that you later decide every point must also store elevation and an acquisition time.

In the procedural version, you must make sure that all functions continue to respect the dictionary structure. If you accidentally misspell `"elevation_m"` as `"elev_m"` somewhere in your script, the dictionary will silently accept it, leading to bugs later on.

In the object-oriented version, that logic is centralized in the class definition. The class acts as a strict formal template for what a point is supposed to contain. By {term}`encapsulating <Encapsulation>` the data inside the object, you protect it from accidental, unstructured modifications.

### Growing complexity

The procedural design is often excellent for one-off calculations, short scripts, and simple transformations. The object-oriented design becomes more useful when there are many related attributes, and the behavior clearly belongs to the data.

### Summary Comparison

| Feature | Procedural Design | Object-Oriented Design |
| :--- | :--- | :--- |
| **Mental Model** | Organizes code around **actions**. | Organizes code around **entities**. |
| **Data Storage** | Standard structures (lists, dictionaries). | Custom Objects (`self.attributes`). |
| **Behavior** | Standalone, free-floating functions. | Methods attached directly to the object. |
| **Scaling** | Can become fragile if complex data is passed through many functions. | Highly scalable; objects manage their own internal state securely. |
| **Best used for...** | Data pipelines, math transformations, simple scripts. | Real-world modeling, complex states, building reusable libraries. |

```{admonition} Important distinction
:class: important

Procedural code organizes actions.

Object-oriented code organizes entities.

In real projects, you will often need both. You might build an object-oriented `SensorNetwork` class, but use procedural functions inside it to calculate statistics on the raw data.
```

---

## 6. A route example: Objects collaborating

The difference becomes even clearer when we model something slightly more complex, such as a spatial route.

If we built this procedurally, a route would simply be a list of dictionaries. We would have to write a `calculate_route_distance()` function that loops through the list, manually extracts the `x` and `y` keys from each dictionary, and processes the math.

An object-oriented version makes the relationship explicit through a concept called {term}`composition <Composition>` (where objects are built out of other objects):

```{code-cell} python
class Route:
    def __init__(self, points, name=None):
        self.points = points
        self.name = name

    def total_distance(self):
        total = 0
        # Loop through all points except the last one
        for i in range(len(self.points) - 1):
            # The Route delegates the math to the Point object!
            total += self.points[i].distance_to(self.points[i + 1])
        return total
```

Now we can create a route using the Swiss city `Point` objects we instantiated earlier:

```{code-cell} python
route = Route([zurich, bern, basel], "Three Cities Route")

route_dist_m = route.total_distance()
print(f"Route '{route.name}' total distance: {route_dist_m / 1000:.1f} km")
```

Notice how seamlessly classes can collaborate. The `Route` object manages the sequence of the journey, but it does not need to know the mathematical details of how distance is calculated. It simply **delegates** that task by asking each `Point` for the distance to the next one.

This makes the code highly modular. If we later update the `Point.distance_to()` method to account for terrain or elevation, the `Route` class will automatically benefit from that upgrade without us having to change a single line of its code.

---

## 7. When OOP helps and when it is overkill

When you first learn about classes, it can be tempting to use them for everything. But wrapping a simple five-line math calculation into a class usually just makes your code harder to read.

Understanding when to use functions versus when to use classes is the key to writing clean, maintainable spatial workflows.

### When functions are usually enough

A standalone function is often the better choice when your primary goal is to **transform data**:

* **Repetitive operations:** You need to perform the same calculation multiple times with different inputs (e.g., converting a list of coordinates from degrees to radians).
* **Stateless utilities:** You want to create reusable tools for common tasks where the program does not need to "remember" anything after the function finishes (e.g., calculating the {term}`Haversine distance <Haversine formula>` between two raw coordinate pairs).
* **Data pipelines:** You need to validate, filter, or process data in a consistent, one-way flow (e.g., a function that filters out GPS points with high location uncertainty).

### When classes usually help

A class is often the better choice when your primary goal is to **model a system or entity**:

* **Complex entities:** You need to represent things with multiple related attributes (e.g., a `SensorStation` that holds coordinates, an ID, and an ongoing history of temperature readings).
* **Bundling state and behavior:** You want data and operations to travel securely together (e.g., a `Route` that holds a list of points and internally knows how to calculate its own total distance).
* **Simulations and dynamic states:** You need to maintain an entity's changing state over time (e.g., a `Vehicle` moving across a road network, constantly updating its internal `x` and `y` coordinates).

```{admonition} Design advice
:class: note

Object-oriented programming is powerful, but it is not automatically superior. A good Python programmer asks, “What structure makes this problem easiest to understand and extend?”
```

---

## 8. Exercise

It is time to compare the two styles yourself on the same geospatial task.

### Task

You are given a subset of Swiss cities and a designated study area in the Valais/Alps region. Solve the problem in **two different designs**.

#### Part A: Procedural version

1. Represent the cities as dictionaries.
2. Represent the study area as a dictionary.
3. Write standalone functions for:
   * distance between two points (in meters)
   * area of a bounding box (converted to square kilometers)
   * testing whether a point lies inside a bounding box
4. Use your functions to answer:
   * How far is Geneva from Sion?
   * Which cities lie inside the bounding box?
   * What is the area of the bounding box in square kilometers?

#### Part B: Object-oriented version

1. Create a `Point` class.
2. Create a `BoundingBox` class.
3. Add methods for:
   * `distance_to()`
   * `area_sq_km()`
   * `contains()`
4. Instantiate your objects and solve the same three questions again.

#### Part C: Reflection

Write three or four sentences comparing the two versions. Comment on which version was shorter, which was easier to read, and which would be easier to extend if the points also needed to track live temperature readings.

### Starter code

```{code-cell} python
# City data (EPSG:2056)
geneva = {"x": 2499959, "y": 1117840, "name": "Geneva"}
sion = {"x": 2592607, "y": 1118393, "name": "Sion"}
andermatt = {"x": 2690960, "y": 1163987, "name": "Andermatt"}
lugano = {"x": 2720031, "y": 1098728, "name": "Lugano"}

# Placing them in a list makes it easier to loop through later!
cities = [geneva, sion, andermatt, lugano]

# Alpine Study Area (EPSG:2056)
bbox_data = {
    "xmin": 2550000,
    "xmax": 2750000,
    "ymin": 1080000,
    "ymax": 1180000,
    "name": "Alpine Window"
}

# Your procedural functions here...
```

````{admonition} Sample solution
:class: dropdown

**Part A: Procedural Version**
```python
import math

# 1. Standalone functions
def distance(p1, p2):
    return math.sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

def bbox_area(bbox):
    return ((bbox["xmax"] - bbox["xmin"]) * (bbox["ymax"] - bbox["ymin"])) / 1_000_000

def is_inside(point, bbox):
    return (bbox["xmin"] <= point["x"] <= bbox["xmax"] and 
            bbox["ymin"] <= point["y"] <= bbox["ymax"])

# 2. Answering the questions
dist_m = distance(geneva, sion)
print(f"Geneva to Sion: {dist_m / 1000:.1f} km")

print("Cities inside Alpine Window:")
for city in cities:
    if is_inside(city, bbox_data):
        print(f"- {city['name']}")

print(f"Area: {bbox_area(bbox_data):.1f} sq km")
```

**Part B: Object-Oriented Version**
```python
import math

# 1. Class Definitions
class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class BoundingBox:
    def __init__(self, xmin, xmax, ymin, ymax, name):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.name = name
        
    def area_sq_km(self):
        return ((self.xmax - self.xmin) * (self.ymax - self.ymin)) / 1_000_000
        
    def contains(self, point):
        return (self.xmin <= point.x <= self.xmax and 
                self.ymin <= point.y <= self.ymax)

# 2. Instantiating objects
p_geneva = Point(2499959, 1117840, "Geneva")
p_sion = Point(2592607, 1118393, "Sion")
p_andermatt = Point(2690960, 1163987, "Andermatt")
p_lugano = Point(2720031, 1098728, "Lugano")

city_objs = [p_geneva, p_sion, p_andermatt, p_lugano]
alpine_box = BoundingBox(2550000, 2750000, 1080000, 1180000, "Alpine Window")

# 3. Answering the questions
dist_m = p_geneva.distance_to(p_sion)
print(f"Geneva to Sion: {dist_m / 1000:.1f} km")

print("Cities inside Alpine Window:")
for city in city_objs:
    if alpine_box.contains(city):
        print(f"- {city.name}")

print(f"Area: {alpine_box.area_sq_km():.1f} sq km")
```

**Part C: Reflection**
The procedural version was slightly shorter to write initially because setting up the class templates (`__init__`) takes a few extra lines of code. However, the object-oriented version is much easier to read when answering the questions, as `alpine_box.contains(city)` reads like natural language. If we needed to track live temperature readings, the OOP design would be far superior; we could simply add `self.temperature` to the `Point` class and include an `update_temperature()` method without breaking any of the existing distance or bounding box logic.
````

---

## 9. Summary

Procedural and object-oriented programming are not rivals in a competition. They are two different design strategies for organizing your thought process and your code.

As you saw in this chapter, both approaches can solve the exact same spatial problem correctly. The "better" design simply depends on the scale, repetition, and complexity of the task at hand.

**Key Takeaways:**

* **Procedural code** organizes analysis around **actions** and free functions. It is often the clearest, fastest solution for small spatial utilities, one-off coordinate transformations, and linear data pipelines.
* **Object-oriented code** organizes analysis around **entities** that bundle state and behavior together. It produces code that is easier to maintain and extend when dealing with richer geospatial concepts like routes, bounding boxes, or interactive sensor stations.

Ultimately, strong geospatial programmers do not restrict themselves to just one style. They seamlessly combine both to build scalable, readable workflows.