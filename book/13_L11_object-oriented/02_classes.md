---
title: The idea of a class

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
From blueprints to geospatial objects
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/13_L11_object-oriented/02_classes.ipynb)

---

```{admonition} Big idea
:class: tip

A class is a blueprint for building reusable objects that bundle related data and behavior. In geospatial programming, this helps you model meaningful entities such as points, stations, or bounding boxes instead of scattering their properties across many separate variables.
```

In the previous section, we established why Object Oriented Programming is a powerful paradigm for managing complexity. We discussed how organizing code around entities (nouns) rather than standalone actions (verbs) prevents spatial data pipelines from becoming brittle. 

Now, it is time to build those entities. In this chapter, we will unpack the foundational concept of a **class**, construct our first spatial objects, and understand how they manage their own internal data.

---

## 1. Class vs. object vs. instance

Before writing the code, we must establish a clear distinction between a class and an object. To understand the difference, consider how you might store geographic points using the procedural style you already know:

```{code-cell} python
lon1 = 8.54
lat1 = 47.37
name1 = "Zurich"

lon2 = 7.45
lat2 = 46.95
name2 = "Bern"
```

While this works, the computer has no idea that `lon1`, `lat1`, and `name1` belong together as a single meaningful entity. As you add more cities or attempt to calculate distances between them, your variables begin to scatter and become difficult to track. 

To solve this, we use object-oriented programming to group related data and behavior together. This introduces three core terms that represent different stages of the programming lifecycle:

* **The Class (The Blueprint):** A class is a template. It specifies what attributes an entity *should* have (like a name, a latitude, and a longitude), but it does not contain any actual data itself. It is the abstract definition of a "City."
* **The Object (The Instance):** An object is a concrete entity built from that class that holds specific, real data. When you populate the blueprint with the actual coordinates for Zurich or Bern, you have *instantiated* the class. These real, memory-backed entities are instances. (The terms "object" and "instance" are used interchangeably).

```{admonition} Key distinction
:class: important

A class defines a *kind* of thing. An instance is one *specific example* of that thing.

`City` is the class.  
`zurich = City(...)` is the instance.
```

You have actually been working with objects all along. `10` is an object of the `int` class, `"hello"` is an object of the `str` class, and `[1, 2, 3]` is an object of the `list` class. 

The paradigm shift here is that you will no longer be restricted to Python's default options. By defining a class, you are effectively creating a brand new data type tailored to your specific analytical needs.

```{admonition} A spatial way to think about classes
:class: note

Many geospatial entities are natural candidates for custom classes: a coordinate point, a bounding box, a delivery route, a sensor station, or a raster tile. Each has distinct properties, and each supports specific operations.
```

---

## 2. Defining a first class

Creating a class in Python is remarkably straightforward. We use the `class` keyword followed by the name we wish to give our new data type. By convention, class names use CapitalizedWords (CamelCase) notation. 

Let us define a minimalistic `GeoPoint` class to represent a geographic coordinate:

```{code-cell} python
class GeoPoint:
    pass
```

The `pass` statement is simply a placeholder indicating that no further action needs to be taken right now. Even though this class currently lacks data or behavior, the blueprint is fully functional. We can immediately instantiate objects from it by calling the class name followed by parentheses:

```{code-cell} python
point_a = GeoPoint()
point_b = GeoPoint()
```

We have now created two distinct `GeoPoint` objects. To prove that these are completely unique, memory-backed entities, we can inspect their types and test their identity using the `is` operator:

```{code-cell} python
print(type(point_a))
# Output: <class '__main__.GeoPoint'>

print(point_a is point_b)
# Output: False
```

Because `point_a is point_b` evaluates to `False`, we know they occupy completely different addresses in your computer's memory. 

However, a blueprint that does not specify any internal state is not very useful for spatial analysis. To make our points meaningful, we need to initialize them with real geographic data.

---

## 3. The `__init__()` method

To make our `GeoPoint` blueprint useful, it needs a starting state. If we do not explicitly set the coordinate positions, we end up with an empty object with no geographic meaning. 

We guarantee this structure using a special initialization method called `__init__()`. Methods that begin and end with double underscores are known as dunder methods, signaling that they have a special built in behavior in Python. 

Let us upgrade our `GeoPoint` class to require coordinates upon creation:

```{code-cell} python
class GeoPoint:
    def __init__(self, latitude, longitude, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
```

You do not call `__init__()` directly. When you construct a new `GeoPoint` instance, Python creates the object and then automatically runs the `__init__()` method behind the scenes to assign the starting data.

```{code-cell} python
point1 = GeoPoint(35.6895, 139.6917, "Tokyo")
point2 = GeoPoint(47.3769, 8.5417)

print(point1.latitude, point1.longitude, point1.name)
print(point2.latitude, point2.longitude, point2.name)
```

Notice that `name` has a default value of `None`. This allows us to create unnamed points (like `point2`) while still keeping the class definition flexible and preventing the program from throwing an error if a name is omitted.

```{admonition} Why initialization matters
:class: important

Without an `__init__()` method, your object has no guaranteed structure. You might forget to attach a latitude value to one of your points, which would cause your spatial calculations to crash later on. A robust `__init__()` method ensures that every new object starts in a valid, consistent state, making your code safer and easier to debug.
```

---

## 4. The role of `self`

You may have noticed a mathematical discrepancy in our previous example. When we defined the initialization method, it had four parameters: `def __init__(self, latitude, longitude, name)`. However, when we instantiated the object, we only passed three arguments: `GeoPoint(35.6895, 139.6917, "Tokyo")`. 

What happened to the first argument?

The keyword `self` is one of the most common sources of confusion when transitioning to object oriented programming, but its purpose is highly logical. `self` simply refers to the **current active object**.

When you instantiate a class, Python automatically passes the newly created instance into the method as the very first argument. You never pass it manually. 

### A dynamic placeholder

Inside the class blueprint, Python does not yet know whether you are building Zurich, Tokyo, or a sensor station in the Alps. It uses `self` as a dynamic placeholder that effectively means "this specific object right here."

When the code executes `self.latitude = latitude`, it is instructing Python: "Take the raw geographic value passed by the user, and securely bind it to *this specific point's* internal state." This mechanism ensures that Tokyo's coordinates do not accidentally overwrite Zurich's coordinates.

### Proving encapsulation

We can visualize this independent state management by inspecting `__dict__`, a special built in attribute that exposes the internal memory dictionary of any Python object.

```{code-cell} python
tokyo = GeoPoint(35.6895, 139.6917, "Tokyo")
zurich = GeoPoint(47.3769, 8.5417, "Zurich")

print("Tokyo's state:", tokyo.__dict__)
print("Zurich's state:", zurich.__dict__)
```

The output will show two completely separate dictionaries. By routing the incoming data through `self`, each object securely maintains its own independent namespace.

```{admonition} A Strong Convention
:class: note

Unlike `def`, `class`, or `if`, the word `self` is not a strictly reserved keyword in Python. You could technically name that first parameter `this_point` or `me` and the code would still execute. However, using `self` is a universally accepted convention among Python developers. You should always use it to ensure your code remains readable to the broader scientific community.
```

---

## 5. Instance attributes and class attributes

When designing spatial objects, it is critical to distinguish between data that belongs to a specific, unique entity and data that belongs to the class as a whole.

### Instance attributes
Variables created inside the `__init__()` method and attached to `self` are called instance attributes. Their values belong to each individual object. In our `GeoPoint` class, `latitude`, `longitude`, and `name` must be instance attributes because Tokyo and Zurich have completely different coordinates and names.

```{code-cell} python
print(tokyo.name)
print(zurich.name)
```

### Class attributes
Class attributes are variables that have the exact same value for all instances of the class. You define them directly beneath the class declaration, outside of any methods.

For example, if our application exclusively processes GPS data, we might want every single `GeoPoint` to share the same default Coordinate Reference System (CRS).

```{code-cell} python
class GeoPoint:
    # Class attribute: Shared by all instances
    crs = "EPSG:4326" 

    def __init__(self, latitude, longitude, name=None):
        # Instance attributes: Unique to each instance
        self.latitude = latitude  
        self.longitude = longitude
        self.name = name
```

In this architecture, both points share the same CRS because that attribute belongs to the class itself.

```{code-cell} python
tokyo = GeoPoint(35.6895, 139.6917, "Tokyo")
zurich = GeoPoint(47.3769, 8.5417, "Zurich")

print(tokyo.crs)
print(zurich.crs)
print(GeoPoint.crs)
```

```{admonition} Rule of thumb
:class: note

Use **instance attributes** for properties that vary from object to object (like temperatures, coordinates, or timestamps). Use **class attributes** for properties that should consistently be the same for all objects of that class (like a default projection, a specific sensor name, or a mathematical constant).
```

---

## 6. Accessing and changing attributes

Once an object is instantiated, you interact with its internal state using **dot notation** (`object.attribute`). 

```{code-cell} python
print(tokyo.latitude)
print(tokyo.name)
```

One of the biggest advantages of Object Oriented Programming is that custom objects are **mutable** by default. This means you can dynamically alter their state after they are created. Objects are not just static containers; they represent real world entities that evolve over time. If a physical weather station is relocated, you can update its coordinate attributes directly:

```{code-cell} python
# Inspect the state before the change
print("Before:", tokyo.__dict__)

# Update the state dynamically
tokyo.latitude = 35.6900
tokyo.name = "Tokyo Relocated"

# Inspect the state after the change
print("After:", tokyo.__dict__)
```

By defining the blueprint, setting the initial state, and using `self` to manage internal data, we have successfully created a self contained spatial entity. 

---

## 7. Exercise: Modeling an Earthquake

It is time to put your blueprint-building skills to the test. Imagine you are tasked with tracking global seismic activity. 

**Your tasks:**
1. Define a class called `EarthquakeEvent`.
2. Give it a **class attribute** called `planet` set to the string `"Earth"`.
3. Create an `__init__()` method that requires three **instance attributes**: `latitude`, `longitude`, and `magnitude`.
4. Instantiate two distinct earthquakes (e.g., one in California, one in Japan) and assign them to variables.
5. Print the `magnitude` of your first earthquake, and the `planet` attribute of your second earthquake.
6. Dynamically update the magnitude of your first earthquake to a new value.

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
# 1. & 2. Define the class and class attribute
class EarthquakeEvent:
    planet = "Earth"
    
    # 3. Define the initialization method and instance attributes
    def __init__(self, latitude, longitude, magnitude):
        self.latitude = latitude
        self.longitude = longitude
        self.magnitude = magnitude

# 4. Instantiate two distinct objects
california_quake = EarthquakeEvent(36.7783, -119.4179, 4.5)
japan_quake = EarthquakeEvent(35.6762, 139.6503, 6.1)

# 5. Access internal state using dot notation
print(f"California Quake Magnitude: {california_quake.magnitude}")
print(f"Japan Quake Planet: {japan_quake.planet}")

# 6. Dynamically alter the state
california_quake.magnitude = 4.8
print(f"Updated California Quake Magnitude: {california_quake.magnitude}")
```
````

---

## 8. Summary and Outlook

* **Class vs. Instance:** A **class** is the abstract blueprint that defines a *kind* of entity. An **instance** (or object) is the concrete, memory-backed entity built from that blueprint. 
* **The `__init__()` method:** The specialized function executed automatically upon object creation. It guarantees that every object starts with a valid, structured baseline.
* **The `self` convention:** A dynamic placeholder that refers to the "current active object." It ensures that incoming data is encapsulated securely within the specific object being instantiated.
* **Attributes (State):** Variables belonging to the object. **Instance attributes** are unique to each object (like latitude), while **Class attributes** are shared universally across all objects of that class (like a default CRS).

**Outlook:** You have successfully mastered the "Noun" side of Object Oriented Programming—architecting entities and managing their state. However, a weather station that just sits there holding coordinates isn't doing much work. In the next chapter, we will introduce **Methods** (the "Verbs") to unlock the true power of classes: allowing objects to calculate, process, and interact with the geospatial world around them.
