---
title: Inheritance and extension

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Reusing shared geospatial designs and specializing them for new tasks
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/13_L11_object-oriented/04_inheritance.ipynb)

---

```{admonition} Big idea
:class: tip

Inheritance lets you build a more specific class on top of a more general one. A child class reuses what is already defined in a parent class and then extends or refines that behavior for a more specialized geospatial purpose.
```

In the previous chapters, you learned how to create a class from scratch, define its initial state using `__init__()`, and attach logic to it using methods. We built standalone spatial entities like a `GeoPoint` and a `BoundingBox`.

However, Object Oriented Programming becomes more powerful when you stop thinking only about isolated classes and begin thinking about **relationships between classes**.  

As your geospatial applications grow, writing every class from scratch becomes highly inefficient. Imagine you are modeling a transportation network. You might need a `Road` class, a `River` class, and a `Railroad` class. All three are line features. All three need to calculate their length, store a name, and list their coordinate vertices. If you write three separate classes from scratch, you will type the exact same code three times.

Object Oriented Programming solves this through **inheritance**. If several classes share the same core structure, rewriting that shared code is wasteful. Inheritance provides a much cleaner solution: you design a "parent" class with generic functionality, and then create specialized "child" classes that automatically absorb the parent's logic while adding their own unique features.

---

## 1. Parent and child classes

Suppose you already have a class that represents a generic geographic point. It stores coordinates, knows its Coordinate Reference System, and can compute distances to other points.

Now imagine that you want to represent a city, a sensor station, and a mountain summit. All of them are fundamentally points. They all need coordinates, and they all benefit from a distance method. However, each of them also needs something more specific—a city needs a population count, while a sensor needs an operational status.

You could copy and paste the same coordinate handling code into every single class. That would work at first. But the moment you improve the point logic, you would need to manually update several separate classes. This is exactly the kind of brittle duplication that Object Oriented Programming helps avoid.

Inheritance is the process by which one class (the **child class** or derived class) takes on the attributes and methods of another class (the **parent class** or base class). It is best understood as **reuse plus specialization**. The parent class captures the common structure, while the child class keeps that structure and adds something more specific.
```{admonition} The "is-a" relationship
:class: important

You should use inheritance when the child class is genuinely a more specific version of the parent class. In geospatial design, this is known as an "is-a" relationship:
* A `NamedPoint` *is a* `PointFeature`.  
* A `SensorStation` *is a* `PointFeature`.

This is very different from simply saying that two classes happen to share a few variables.
```

The syntax for inheritance in Python is remarkably straightforward. You place the parent class inside parentheses after the child class name:
```{code-cell} python
class PointFeature:
    pass

class NamedPoint(PointFeature):
    pass
```

The line `class NamedPoint(PointFeature):` tells Python to link these two blueprints. 

The core mechanism making this work is a fallback search. If a `NamedPoint` object is asked to read an attribute or execute a method, Python looks inside the `NamedPoint` class first. If it cannot find the logic there, it automatically climbs the hierarchy and searches inside `PointFeature`. This means the child class can safely reuse the parent's behavior without you having to redefine a single line of code.

---

## 2. A geospatial example

Let us look at the syntax for inheritance. To make a child class inherit from a parent class, you simply put the name of the parent class in parentheses when defining the child class.

We begin with a parent class called `PointFeature`. It represents a generic point in geographic space, stores coordinates, and can calculate distances.
```{code-cell} python
import math

# 1. The Parent Class
class PointFeature:
    def __init__(self, x, y, crs="EPSG:4326"):
        self.x = x
        self.y = y
        self.crs = crs

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
```

Now, let us create a specialized child class called `NamedPoint` to represent a city or landmark. Notice the `(PointFeature)` in the class definition. For the moment, we will manually redefine the setup logic in the child class. 
```{code-cell} python
# 2. The Child Class (inherits from PointFeature)
class NamedPoint(PointFeature):
    def __init__(self, x, y, name, crs="EPSG:4326"):
        self.x = x
        self.y = y
        self.crs = crs
        self.name = name
```

While this initialization repeats some code from the parent (a flaw we will fix in the very next section), the true power of inheritance is immediately visible when we test the methods.
```{code-cell} python
zurich = NamedPoint(8.5417, 47.3769, "Zurich")
bern = NamedPoint(7.4474, 46.9480, "Bern")

print(zurich.name)

# We call the method inherited from the parent
dist = zurich.distance_to(bern)
print(f"Distance: {dist:.2f} degrees")
```

When we call `zurich.distance_to()`, Python first looks inside the `NamedPoint` class. When it does not find a `distance_to()` method there, it climbs the inheritance tree, finds the method in the parent `PointFeature` class, and executes it. 

```{admonition} What was inherited?
:class: note

The `NamedPoint` class did not define `distance_to()`, but it can still use it. The child class automatically gains access to all methods defined in the parent.
```

You can prove this "is a" relationship directly using Python's built in `isinstance()` function. 
```{code-cell} python
print(isinstance(zurich, NamedPoint))
# Output: True

print(isinstance(zurich, PointFeature))
# Output: True
```

Because `NamedPoint` inherits from `PointFeature`, the `zurich` object is recognized as belonging to both categories. The child class is more specific, but it still belongs to the broader parent category.

<iframe 
    src="../_static/mro_explorer.html" 
    width="100%" 
    height="650px" 
    frameborder="0" 
    style="border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc;">
</iframe>

<figcaption>
    <b>Interactive Explorer: Method Resolution Order (MRO)</b>. <br>
    Click the buttons above to visualize how Python searches the inheritance tree to execute your code. Notice how it always checks the specific instance first before falling back to the parent blueprints.
</figcaption>

---

## 3. Using super() to extend initialization

In the previous section, our `NamedPoint` class repeated the coordinate setup code (`self.x = x`, `self.y = y`) that was already defined in `PointFeature`. That is not ideal. A specialized child class usually needs to initialize its own unique data *in addition* to the parent's data, but it should never rewrite the parent's logic.

To achieve this cleanly, Python provides the built in `super()` function. `super()` allows a child class to explicitly call a method from its parent class. Most commonly, it is used inside the child's `__init__()` method to ensure the parent initializes the shared attributes before the child sets up its specific ones.

Let us rewrite our `NamedPoint` class to use `super()`:
```{code-cell} python
class NamedPoint(PointFeature):
    # The child requires four arguments
    def __init__(self, x, y, name, crs="EPSG:4326"):
        
        # 1. Pass the shared attributes up to the parent to handle
        super().__init__(x, y, crs)
        
        # 2. Handle the specialized attribute locally
        self.name = name
```

Now let us test it:

```{code-cell} python
geneva = NamedPoint(6.1432, 46.2044, "Geneva")

# Inherited from parent
print("Coordinates:", geneva.x, geneva.y)
print("CRS:", geneva.crs)

# Specific to child
print("Name:", geneva.name)
```

The line `super().__init__(x, y, crs)` tells Python to run the parent class initialization first. After the parent has securely stored the coordinates and the CRS, the child class takes over to add its own new attribute, `name`.
```{admonition} Why super() matters
:class: important

`super()` is not just a shorter way to write parent class names. It makes child classes highly modular and easier to maintain. 

If the parent `PointFeature` class later evolves to require a Z-coordinate (elevation), you only need to update the parent logic. You do not have to hunt down and rewrite the initialization sequence in every single child class.
```

---

## 4. Overriding methods

Sometimes, a child class needs to perform the exact same action as the parent, but do it differently. This is called **overriding** a method. 

If you define a method in the child class with the *exact same name* as a method in the parent class, the child's method will take precedence. Python will find it first and stop looking up the inheritance tree.

Let us define a `Geometry` parent class that has an abstract way to describe itself. Then we will create a `Polygon` child class that completely overrides that description to provide more specific spatial details.
```{code-cell} python
class Geometry:
    def __init__(self, crs):
        self.crs = crs

    def describe(self):
        return f"A generic geometry in {self.crs}"

class Polygon(Geometry):
    def __init__(self, crs, area):
        super().__init__(crs)
        self.area = area

    # This method completely overrides the parent's method
    def describe(self):
        return f"A Polygon covering {self.area} sq units in {self.crs}"
```

```{code-cell} python
base_geom = Geometry("EPSG:4326")
lake_poly = Polygon("EPSG:4326", 500)

print(base_geom.describe())
print(lake_poly.describe())
```

### Extending instead of replacing

Sometimes a child class should not completely replace the parent's behavior, but rather **extend** it. Just as we used `super()` in `__init__()`, we can use it to call the parent's version of any method and then build on top of it.

For example, imagine a `SensorStation` that inherits from a generic `PointFeature`. When asked to format its state via the `__str__` dunder method, it can grab the parent's basic coordinate string and simply append the sensor readings to it:
```{code-cell} python
class PointFeature:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Location: ({self.x}, {self.y})"

class SensorStation(PointFeature):
    def __init__(self, x, y, station_id, variable):
        super().__init__(x, y)
        self.station_id = station_id
        self.variable = variable

    # Extending the parent's method
    def __str__(self):
        # 1. Get the baseline string from the parent
        parent_text = super().__str__()
        # 2. Add the child-specific data
        return f"{parent_text} | ID: {self.station_id} | Measuring: {self.variable}"
```

```{code-cell} python
station = SensorStation(8.55, 47.37, "ZH001", "Temperature")
print(station)
```

```{admonition} Three possibilities for child methods
:class: note

When dealing with a method from a parent class, a child class has three options:
1. **Inherit unchanged:** Do nothing; simply use the parent's method as is.
2. **Override completely:** Define a method with the same name and replace the logic entirely.
3. **Extend:** Define a method with the same name, but use `super()` inside it to combine the parent's logic with new child logic.
```

Overriding is a powerful feature because it allows systems to be flexible. If another part of your code expects to call `.describe()` on *any* piece of geometry, it does not need to know if the object is a generic geometry, a polygon, or a line. It just calls `.describe()` and trusts that the specific object will handle the request correctly based on its own overridden logic.

---

## 5. Designing useful hierarchies

Now that you know the syntax, the more important issue is architectural design. 

Because inheritance is so powerful, it is tempting to use it everywhere to avoid typing. However, the key question is not just "Do these classes share code?" but rather "Does the child class represent a more specific form of the parent class?"
```{admonition} The golden rule of inheritance
:class: tip

If you cannot naturally complete the sentence **"A [Child] is a kind of [Parent]"**, then inheritance is probably the wrong design choice.
```

### Good inheritance design

Applying this rule to geospatial objects makes the boundaries clear. These are strong candidates for inheritance:

* An `ElevationRaster` **is a** `RasterLayer`
* A `TemperatureSensor` **is a** `Sensor`
* A `NamedPoint` **is a** `PointFeature`

In each case, the child truly is a more specific subtype of the parent. Inheritance fits perfectly here.

### Weak inheritance design and Composition

Sometimes two classes interact closely, but one is not a subtype of the other. 

For example, a `Route` is composed of points, and a `Map` contains raster layers. However:
* A `Route` **is not a** `PointFeature`
* A `Map` **is not a** `RasterLayer`

If the relationship is better described by the phrase **"has a"** (a route *has a* sequence of points, a map *has a* raster layer), you should use **composition**. Instead of inheriting, simply pass the objects as attributes into the new class.

```{mermaid}
flowchart TD
    subgraph Inheritance ["Inheritance (Is-A)"]
        Parent[PointFeature]
        Child1[NamedPoint]
        Child2[SensorStation]
        
        Child1 -->|"is a"| Parent
        Child2 -->|"is a"| Parent
    end

    subgraph Composition ["Composition (Has-A)"]
        Container[Route]
        Component[GeoPoint]
        
        Container -->|"has a"| Component
    end

    classDef default fill:#f8fafc,stroke:#94a3b8,stroke-width:2px,color:#0f172a;
    classDef parent fill:#e0f2fe,stroke:#3b82f6,stroke-width:2px,color:#0f172a;
    class Parent,Container parent;
```

### A caution on complexity

Inheritance helps reduce redundant code, but too much inheritance can make designs incredibly difficult to understand. If you create many layers of parent, child, and grandchild classes, the path of attribute lookup becomes impossible to follow. 

```{admonition} Keep inheritance flat
:class: warning

In the Python community, there is a strong guiding principle: **Flat is better than nested.** 

While Python supports complex architectural patterns (like inheriting from multiple parents at once), you should prefer small, shallow, and readable hierarchies. A flat structure with one parent and a few child classes is always easier to debug and maintain than a deep, highly nested family tree.
```

---

## 6. Exercise: Building a Spatial Hierarchy

It is time to practice inheritance directly by building a small system of cooperating classes.

**The Scenario:** You are managing a network of wildlife tracking collars. Every collar is fundamentally a point in space, but it also has specialized hardware properties like an ID and a battery level. 

**Your Tasks:**

**A. The Parent Class (`PointFeature`)**
1. Define the class. Its `__init__` method should accept and store `x` and `y` coordinates.
2. Provide a `distance_to(other)` method that calculates the Euclidean distance to another point. *(Hint: `math.hypot(self.x - other.x, self.y - other.y)`)*.
3. Provide a `__str__` method that returns `"Location: (x, y)"`.

**B. The Child Class (`MobileSensor`)**
1. Inherit from `PointFeature`.
2. The `__init__` method should accept `x`, `y`, `sensor_id`, and `battery`. Use `super()` to handle the coordinate initialization.
3. Add a completely new method called `record_movement(dx, dy)`. It should update the `x` and `y` coordinates by the given deltas, and decrease the `battery` attribute by 1.
4. Override the `__str__` method to *extend* the parent's string. Call `super().__str__()` to get the location text, and append the sensor ID and battery percentage to it.

**C. The Simulation**
1. Instantiate two sensors at different coordinates.
2. Print the distance between them.
3. Move one of the sensors.
4. Print both sensors to see the final output.

**D. Reflection**
Look at the code you just wrote and ask yourself:
* Which methods were inherited without any changes?
* Which methods were extended using `super()`?
* Which methods were entirely unique to the child class?

```{code-cell} python
import math

# Write your code here
```

````{admonition} Sample Solution & Reflection
:class: dropdown

```python
import math

# A.
class PointFeature:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Location: ({self.x}, {self.y})"

# B.
class MobileSensor(PointFeature):
    def __init__(self, x, y, sensor_id, battery):
        # Extend initialization
        super().__init__(x, y)
        self.sensor_id = sensor_id
        self.battery = battery

    def record_movement(self, dx, dy):
        # New child specific behavior
        self.x += dx
        self.y += dy
        self.battery -= 1

    def __str__(self):
        # Extend the parent string
        parent_text = super().__str__()
        return f"Sensor {self.sensor_id} | {parent_text} | Battery: {self.battery}%"

# C.
sensor_1 = MobileSensor(10, 10, "Collar_A", 100)
sensor_2 = MobileSensor(15, 20, "Collar_B", 100)

print(f"Initial distance: {sensor_1.distance_to(sensor_2):.2f}")

sensor_1.record_movement(-2, 5)

print("\nFinal State:")
print(sensor_1)
print(sensor_2)
```

**Reflection Answers:**
* `distance_to()` was inherited completely unchanged from the parent.
* `__init__()` and `__str__()` were extended using `super()` to combine shared parent logic with specific child logic.
* `record_movement()` is entirely unique to the `MobileSensor` child class.
````

---

## 7. Summary and Outlook

Inheritance allows one class to build seamlessly on another. A parent class captures the shared spatial structure, and a child class reuses that structure while adding more specific attributes or behavior. 

In this chapter, you learned that:
* **Parent and child classes:** A parent class defines shared structure and behavior, which a child class inherits automatically.
* **The `super()` function:** This built in function lets child classes reuse parent initialization cleanly, preventing redundant code.
* **Overriding methods:** By redefining a parent's method, a child class can behave more specifically to suit its specialized role.
* **Architectural restraint:** Inheritance is most useful when the child is genuinely a more specific kind of the parent. In geospatial programming, a simple and shallow hierarchy is almost always better than an elaborate one.

**Outlook:** You now understand the core mechanics of Object Oriented Programming: classes, state, methods, and inheritance. But when should you actually use them? In spatial data science, you do not always need to build a complex system of classes. In the next chapter, we will broaden the design picture by looking at **Procedural vs. Object Oriented Design**, exploring when to use simple standalone functions and when to commit to a full class based architecture.
