---
title: Methods driven behavior

site: 
    outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Turning geospatial objects into active, reusable tools
</div>
<!-- markdownlint-enable MD033-->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/13_L11_object-oriented/03_methods.ipynb)

---

```{admonition} Big idea
:class: tip

A class becomes truly useful when it does not only store data, but also provides the behaviors that make sense for that data. In geospatial programming, methods allow an object like a point, route, or bounding box to act on its own state in clear and reusable ways. 
```

```{admonition} Chapter Relevance
:class: dropdown

**Project Relevance:** ★★★ (Crucial for building logical, maintainable, and interactive spatial systems for your independent projects.)  
**Foundation:** ★★★ (Teaches the core logic of `self` and internal state management.)  

**Time to Read:** 15 minutes  
**In a nutshell:** Learn how to bring classes to life by attaching methods that read, update, and enable collaborative interactions between geospatial objects.  
**Skip this if:** You already understand how to define instance methods, safely update object state, and implement dunder methods like `__str__` and `__gt__`.

```

In the previous chapter, you learned how to define a class and how to create **{term}`objects <Object>`** from it. You saw that a class gives structure to your data by bundling related **{term}`attributes <Attribute>`** into one coherent entity.

However, storing data is only half of the story.

A geospatial point is not interesting just because it has coordinates. It becomes useful when it can **describe itself**, **move**, **measure distance**, or **test a spatial relationship**. This is where methods enter the picture.

Methods are **{term}`functions <Function>**` that belong to a class. They allow an object to act on its own data through **{term}`self <self parameter>`**, turning passive storage into active behavior. This is one of the central ideas of **{term}`Object-Oriented Programming <Object-oriented programming>`**: you do not only store data together, you also attach the operations that naturally belong to that data.

In this chapter, you will extend your first geospatial classes by adding methods that read object state, update it, and interact with other objects. You will also meet a few special Python methods that make your custom objects behave more naturally in notebooks and scripts.

---

## 1. Methods as functions inside a class

In the previous chapter, we defined a `GeoPoint` class with coordinates and a name. That was already a big improvement over scattering variables across a script. However, an object with only attributes is still just a passive storage container.

In spatial data science, you likely want your objects to *do* things. A bounding box may need to calculate its area. A sensor may need to update its calibration. A point may need to report its location. While you could write standalone procedural functions for these tasks, it is much cleaner to attach the behavior directly to the data it operates on.

```{admonition} From passive storage to active objects
:class: important

Attributes answer the question: **What does this object know?**  
Methods answer the question: **What can this object do?**
```

If you have ever used `list.append()` or `geodataframe.plot()`, you have already used methods. A method is simply a function that is defined inside a class block and operates specifically on the data of that class.

The syntax for creating a method is almost identical to creating a standard function. We use the `def` keyword. The crucial difference is that its first **{term}`parameter <Parameter>`** must always be `self`.

Let us revisit our `GeoPoint` blueprint and add a basic method:

```{code-cell} python
class GeoPoint:
    def __init__(self, latitude, longitude, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    # A simple method attached to the class
    def report_status(self):
        print(f"Station {self.name} is online at ({self.latitude}, {self.longitude})")
```

Because `report_status` belongs to the `GeoPoint` class, you cannot call it floating on its own. You must call it *through* a specific instantiated object using dot notation:

```{code-cell} python
station_zrh = GeoPoint(47.3769, 8.5417, "Zurich_Main")

# The object executes its own internal logic
station_zrh.report_status()
```

Notice that we did not manually pass `self` inside the parentheses when calling `.report_status()`. Just as we saw with `__init__()`, Python automatically passes the `station_zrh` object in as that first argument. Inside the method, `self` acts as the bridge, giving the logic direct access to that specific object's stored state.

---

## 2. Reading object state

The most basic role of a method is to read, format, or analyze the object's internal state. Because the method has access to `self`, it can look inside the object's memory and use those attributes without requiring you to pass them in manually.

### Formatting State

Imagine we are building a `WeatherStation` class. We might want a method that neatly formats the current temperature for a dashboard.

```{code-cell} python
class WeatherStation:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def get_dashboard_readout(self):
        # The method reads its own state and returns a formatted string
        return f"{self.name} Current Temp: {self.temperature}°C"

station1 = WeatherStation("Alps_High", -4.5)
print(station1.get_dashboard_readout())
```

This is much cleaner than extracting `station1.name` and `station1.temperature` individually every time you want to print an update. Notice that we **return** the string rather than printing it directly; returning a value is usually more powerful because the result can be stored, reused, or passed to a graphical dashboard.

### Calculating Derived State

The true power of reading state comes when an object computes new information based on its raw data.

Consider a spatial bounding box. We only need to store four coordinates (xmin, ymin, xmax, ymax). From those four raw attributes, the object can calculate its own width, height, and area.

```{code-cell} python
class BoundingBox:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def width(self):
        return self.xmax - self.xmin

    def height(self):
        return self.ymax - self.ymin

    def area(self):
        # A method can call other methods using self!
        return self.width() * self.height()
```

To see this in action, let us instantiate a bounding box using projected, metric coordinates:

```{code-cell} python
# Coordinates in meters (e.g., a projected local grid)
study_area = BoundingBox(1000.0, 2000.0, 1500.0, 2800.0)

print("Width (m):", study_area.width())
print("Height (m):", study_area.height())
print("Area (sq m):", study_area.area())
```

Notice how the `area()` method calls two other methods belonging to the same object: `self.width()` and `self.height()`. This is a highly common architectural pattern. Methods are not isolated entities; they build on each other to create complex behaviors.

```{admonition} A good first question
:class: tip

When designing a new spatial class, ask yourself:  
**What information should this object be able to compute and report about itself?**
```

### Interactive Concept Check: Derived State

Use the interactive visualizer below to explore how an object calculates derived state. As you adjust the raw instance attributes (`xmin`, `ymin`, `xmax`, `ymax`), watch how the object's internal methods automatically recalculate its `width()`, `height()`, and `area()`.

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L11_ch03_02_derived_state/"
    width="100%"
    title="Derived State Explorer"
    frameborder="0"
    style="height: 650px; min-height: 650px; border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
    allowfullscreen>
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Derived State.</b><br>
    Adjust the raw instance attributes (X/Y Min/Max) using the sliders to see how the <code>BoundingBox</code> object dynamically recalculates its derived state in real-time. Notice how the <code>area()</code> method internally calls the <code>width()</code> and <code>height()</code> methods to compute its final result. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L11_ch03_02_derived_state/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033-->

---

## 3. Updating object state

Methods become truly powerful when we use them to modify the internal data of an object. This is known as **changing state**.

For a spatial object, a natural state change is movement. If a sensor is relocated, we can write a method to physically translate its coordinates:

```{code-cell} python
class GeoPoint:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def move(self, dx, dy):
        # Updates the existing state by adding the shift (delta x and delta y)
        self.x += dx
        self.y += dy
```

```{code-cell} python
point = GeoPoint(8.54, 47.37, "Zurich")
print("Before:", point.x, point.y)

point.move(0.1, -0.2)
print("After: ", point.x, point.y)
```

Notice that the `move()` method does not return a brand new point. It directly updates the existing one in memory.

### Methods as gatekeepers

You might ask: "Why bother with a method? Why not just write `point.x = 8.64` directly?"

While direct assignment works, methods act as **gatekeepers**. They provide one clear place to define *how* state changes are allowed, letting you validate inputs, enforce rules, or log changes.

Consider a `WeatherStation` class. If a faulty sensor tries to record a physically impossible temperature, a method can catch the error before the object's data is corrupted:

```{code-cell} python
class WeatherStation:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    # A method designed to change the state safely
    def record_new_temperature(self, new_temp):
        if new_temp < -89.2 or new_temp > 56.7:
            print("Error: Temperature reading defies Earth records. Ignoring.")
        else:
            self.temperature = new_temp
            print(f"{self.name} successfully updated to {self.temperature}°C")
```

```{code-cell} python
station1 = WeatherStation("Alps_High", -4.5)

# Attempting a valid update
station1.record_new_temperature(-6.0)

# Attempting a corrupted sensor reading
station1.record_new_temperature(999.0)
```

By routing the update through `record_new_temperature()`, the object protects its own data integrity.

```{admonition} Design principle: Encapsulation
:class: important

Direct attribute access is simple, but methods give you a cleaner, safer interface. This is the core of **encapsulation**: bundling data and behavior together so the object not only stores values, but also dictates the proper ways those values can be read or modified as your programs grow more complex.
```

---

## 4. Methods with arguments

A method does not need to work exclusively with its own object. It can also accept additional inputs, including completely different objects. This is where Object Oriented Programming becomes genuinely spatial, allowing complex entities to interact.

### Distance to another point

A classic example is a point that measures its distance to another point. We can pass a second `GeoPoint` instance directly into the method.

For now, we will use a simple Euclidean distance formula:

```{code-cell} python
class GeoPoint:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def distance_to(self, other_point):
        # self is the active object calling the method
        # other_point is the second object passed as an argument
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        
        return (dx**2 + dy**2) ** 0.5
```

```{code-cell} python
# Coordinates in a projected metric grid
zurich = GeoPoint(2683000, 1248000, "Zurich")
bern = GeoPoint(2600000, 1200000, "Bern")

# Zurich calculates the distance to Bern
dist_z_to_b = zurich.distance_to(bern)
print(f"Distance: {dist_z_to_b:.2f} meters")
```

In the `distance_to` method, `self` represents `zurich`, while `other_point` represents `bern`. The method seamlessly reads the attributes from both objects to perform the math.

```{admonition} Geospatial Caution
:class: warning

This Euclidean formula is appropriate for projected coordinates or abstract Cartesian space. If your point coordinates are longitude and latitude in degrees, this will **not** calculate a correct real world distance on the Earth's surface. In that case, you need a projected Coordinate Reference System (CRS) or a specialized geodesic distance formula like Haversine.
```

### Testing spatial relationships

Methods can also express topological relationships between completely different types of objects.

Let us build a `BoundingBox` class. We can give it a method that accepts a `GeoPoint` as an argument and evaluates whether that point falls within the box's boundaries:

```{code-cell} python
class BoundingBox:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def contains(self, point):
        # The method tests the incoming point's attributes against its own boundaries
        return (self.xmin <= point.x <= self.xmax) and (self.ymin <= point.y <= self.ymax)
```

```{code-cell} python
# Create a study area and two points
study_area = BoundingBox(0, 0, 10, 10)

point_a = GeoPoint(3, 4, "A")
point_b = GeoPoint(15, 2, "B")

# Ask the bounding box if it contains the points
print("Contains A?", study_area.contains(point_a))
print("Contains B?", study_area.contains(point_b))
```

This is a highly natural object oriented pattern. The bounding box is responsible for deciding whether a point lies inside it. You can see how classes start to collaborate to build richer systems: a `GeoPoint` measures distance to another `GeoPoint`, while a `BoundingBox` tests containment of a `GeoPoint`.

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L11_ch03_01_collaborating_objects/"
    width="100%"
    title="Spatial System Explorer"
    frameborder="0"
    style="height: 650px; min-height: 650px; border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
    allowfullscreen>
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Collaborating Objects.</b><br>
    Drag the points and the bounding box across the grid to dynamically update their internal attributes[cite: 24]. Watch the dashboard recalculate and display the results of their encapsulated methods, such as distance and containment, to see how the objects process spatial relationships in real-time[cite: 24]. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L11_ch03_01_collaborating_objects/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033-->

---

## 5. Why methods can be cleaner functions

At this point, you might ask a highly practical design question: "Why not just write ordinary standalone functions?"

For example, we could define distance like this:

```{code-cell} python
def distance(point_a, point_b):
    dx = point_a.x - point_b.x
    dy = point_a.y - point_b.y
    return (dx**2 + dy**2) ** 0.5

# Calling the standalone function
distance(zurich, bern)
```

That is perfectly valid. However, compare it with the method based style:

```python
zurich.distance_to(bern)
```

The second version reads more naturally because the behavior is clearly attached to the object it belongs to. The same comparison applies to spatial containment: `bbox.contains(point)` is structurally clearer than `contains(bbox, point)`.

### The architectural payoff

Method based design answers an important question: **Which object is responsible for this behavior?** By attaching the behavior directly to the responsible data, object oriented design offers distinct advantages:

1. **Discoverability:** If you have a free function, a new programmer has to search your entire codebase to find it. If it is a method, typing `zurich.` in an IDE will automatically pop up a menu showing `distance_to()`. The capabilities of the object travel *with* the object.
2. **Context:** `zurich.distance_to(bern)` reads like an English sentence. The subject (Zurich) performs an action (calculates distance) on a target (Bern).
3. **Encapsulation:** If you change how a point stores its coordinates internally, you only have to update the `distance_to` method inside that specific class. You do not have to hunt down and fix every standalone function that ever interacted with a coordinate.

```{admonition} Not a strict rule
:class: note

Object oriented design is not about forcing every single function into a class. Some generic operations are still clearer as standalone functions. The goal is not ideology; the goal is readable and well organized code.
```

### A geospatial example: Routes collaborating with Points

You can really see the power of methods when different classes begin to collaborate. A route is a sequence of points. One of its obvious behaviors is to calculate its total length.

Rather than writing a massive function that extracts all the coordinates and does the math from scratch, a `Route` object can simply ask its `GeoPoint` objects to calculate the distances themselves:

```{code-cell} python
class Route:
    def __init__(self, points, name=None):
        self.points = points
        self.name = name

    def total_length(self):
        total = 0
        # Loop through all points in the route except the last one
        for i in range(len(self.points) - 1):
            # The Route uses the GeoPoint's distance_to() method!
            total += self.points[i].distance_to(self.points[i + 1])
        return total
```

```{code-cell} python
# Create our points
a = GeoPoint(0, 0, "A")
b = GeoPoint(3, 4, "B")
c = GeoPoint(6, 4, "C")

# Pass the points into a Route object
my_route = Route([a, b, c], "Delivery Route")

# Calculate the summary
length = my_route.total_length()
print(f"Total route length: {length}")
```

This perfectly captures the essence of object oriented spatial programming. The `Route` manages the overarching list, but it relies on the encapsulated methods of its `GeoPoint` objects to compute the larger spatial summary.

---

## 6. Dunder (Magic) Methods

Python has a secret tier of methods known as "dunder" methods (because their names start and end with a **d**ouble **under**score). You have already used the most important one: `__init__()`.

These methods are rarely called directly. Instead, Python triggers them automatically in response to standard operations, allowing you to customize how your objects behave on a fundamental level and making them feel like native Python types.

### Controlling Representation (`__str__` and `__repr__`)

If you try to print a custom object, Python's default behavior is not very helpful. It just shows a generic memory address:

```{code-cell} python
print(zurich)
# Output: <__main__.GeoPoint object at 0x106702d30>
```

You can fix this by defining the `__str__` dunder method. Whenever you use `print()`, Python secretly looks for `__str__` and executes it to get a readable string.

```{code-cell} python
class GeoPoint:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5
        
    # Customizing the readable print output
    def __str__(self):
        return f"{self.name or 'Unnamed point'} ({self.x}, {self.y})"

    # Customizing the formal developer output
    def __repr__(self):
        return f"GeoPoint(x={self.x}, y={self.y}, name='{self.name}')"
```

```{code-cell} python
p = GeoPoint(8.54, 47.37, "Zurich")

# Triggers __str__
print(p) 

# Triggers __repr__ (often seen when evaluating variables in Jupyter)
p
```

While `__str__` is meant to be user friendly and readable, `__repr__` is meant to be a formal representation of the object, often formatted exactly like the code you would type to recreate the object. This makes `__repr__` incredibly useful for debugging.

### Operator Overloading (`__gt__`, `__add__`)

Dunder methods can also define how standard operators behave with your custom objects. This is called **operator overloading**.

For example, if you wanted to quickly determine which of two delivery routes is longer, you could define the `__gt__` (greater than) method.

```{code-cell} python
class Route:
    def __init__(self, points, name=None):
        self.points = points
        self.name = name

    def total_length(self):
        total = 0
        for i in range(len(self.points) - 1):
            total += self.points[i].distance_to(self.points[i + 1])
        return total

    # Define what the ">" symbol means for Routes
    def __gt__(self, other):
        # A route is "greater than" another if its total length is longer
        return self.total_length() > other.total_length()
```

```{code-cell} python
# Assuming r1 and r2 are instantiated Route objects
r1 = Route([GeoPoint(0, 0), GeoPoint(3, 4)], "Route 1")
r2 = Route([GeoPoint(0, 0), GeoPoint(1, 1)], "Route 2")

# Python secretly calls r1.__gt__(r2)
if r1 > r2:
    print(f"{r1.name} is the longer route.")
```

```{admonition} Practical advice
:class: tip

For your first own classes, focus mostly on `__init__()` and `__str__()`. These give the biggest practical benefit. Other dunder methods (like operator overloading) are powerful but should only be used when they express a genuinely clear and natural behavior. If the meaning of `>` or `+` is ambiguous for your object, stick to explicit named methods instead.
```

---

## 8. Exercise: The Expanding Study Region

It is time to build your own small geospatial object system from scratch.

**The Scenario:** You are tracking a mobile sensor (like an animal GPS collar) that is moving toward a defined study region. You need to simulate the sensor's movement, dynamically expand the study region, and test when the sensor enters the region.

**Your Tasks:**

**A. The `MobileSensor`**

1. Define the class. Its `__init__` method should store `x` and `y` coordinates.
2. Provide a `move(dx, dy)` method that updates the coordinates.
3. Provide a `__str__` dunder method to cleanly print the sensor's current location.

**B. The `StudyRegion`**

1. Define the class. Its `__init__` method should store `xmin`, `ymin`, `xmax`, and `ymax`.
2. Provide an `expand_by(amount)` method that grows the box in all directions (subtract the amount from the minimums, add the amount to the maximums).
3. Provide a `contains(sensor)` method that accepts a `MobileSensor` object and returns `True` if it is inside the boundaries, and `False` otherwise.

**C. The Simulation**

1. Instantiate a sensor at `(10, 10)` and a study region bounded by `(0, 0)` and `(5, 5)`.
2. Print whether the region contains the sensor (should be `False`).
3. Move the sensor by `(-3, -3)`.
4. Expand the study region by `3` units.
5. Print whether the region contains the sensor now (should be `True`).

**D. Reflection**
Look at the methods you just wrote and ask yourself:

* Which of your methods only **read** object state?
* Which methods **changed** object state?
* Which methods required **another custom object** as input?

```{code-cell} python
# Write your code here
```

````{admonition} Sample Solution & Reflection
:class: dropdown

```python
class MobileSensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Sensor at ({self.x}, {self.y})"


class StudyRegion:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def expand_by(self, amount):
        self.xmin -= amount
        self.ymin -= amount
        self.xmax += amount
        self.ymax += amount

    def contains(self, sensor):
        return (self.xmin <= sensor.x <= self.xmax) and (self.ymin <= sensor.y <= self.ymax)

# 1. Instantiate objects
fox_tracker = MobileSensor(10, 10)
forest_zone = StudyRegion(0, 0, 5, 5)

# 2. Initial check
print("Initial containment:", forest_zone.contains(fox_tracker))

# 3 & 4. Modify state
fox_tracker.move(-3, -3)
forest_zone.expand_by(3)

# 5. Final check
print(fox_tracker)
print("Expanded boundary:", forest_zone.xmin, forest_zone.ymin, forest_zone.xmax, forest_zone.ymax)
print("Final containment:", forest_zone.contains(fox_tracker))
```

**Reflection Answers:**
* `__str__()` and `contains()` read object state without changing it.
* `move()` and `expand_by()` permanently change the internal state of their objects.
* `contains()` requires another custom object (`sensor`) to perform its logic.
````

---

## 9. Summary and Outlook

* **Methods are active behavior:** A method is a function defined inside a class that dictates what an object can do, turning passive data containers into active spatial tools.
* **The `self` parameter:** Because methods belong to the class blueprint, their first parameter must always be `self`. This grants the logic direct access to read or update the specific object's internal state.
* **Controlled state changes:** Instead of manually overwriting variables, methods allow you to design safe, validated pathways for an object to evolve (like a sensor recording a new temperature or moving to a new coordinate).
* **Collaborating objects:** Methods can accept other custom objects as arguments, allowing discrete entities to interact mathematically and logically (like a bounding box checking if it contains a specific point).
* **Dunder methods:** Special methods like `__str__` or `__gt__` deeply integrate your custom objects with standard Python syntax, allowing you to use functions like `print()` or math operators naturally.

**Outlook:** You now have the tools to build fully functional, interactive spatial entities. However, as your systems grow, you will eventually find yourself writing the exact same attributes and methods across multiple similar classes (for example, a `River` class and a `Road` class that both rely on line geometry and length calculations). In the next chapter, we will introduce **Inheritance**, an architectural technique that allows specialized classes to inherit logic from generic parent classes, saving you from writing redundant code.
