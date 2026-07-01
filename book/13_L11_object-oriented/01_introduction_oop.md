---
title: Introduction to OOP

site: 
    outline_maxdepth: 1

---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Moving beyond sequential scripts
</div>
<!-- markdownlint-enable MD033-->

---

```{admonition} Big idea
:class: tip

Before writing advanced, modular Python code, you should understand the conceptual shift from organizing your code around *actions* to organizing your code around *objects*.
```

```{admonition} Chapter Relevance
:class: dropdown

**Project Relevance:** ★☆☆ (Provides the mental model for structuring projects 1 and 2, but contains no executable code necessary for your final submission)  
**Foundation:** ★★★ (Represents a fundamental paradigm shift required for advanced Python development and building custom packages)  

**Time to Read:** 5 minutes  
**In a nutshell:** Discover how Object-Oriented Programming bundles disconnected variables and functions into smart, self-managing entities.  
**Skip this if:** You are already confident with the conceptual differences between procedural and object-oriented paradigms, and understand what classes and instances are.

```

---

## 1. From variables and functions to objects

Let us elevate the working definition of programming you have practiced so far. At its core, programming consists of two fundamental tasks: **managing state** (storing data) and **executing logic** (doing things with that data).

In **{term}`Procedural programming`** (the paradigm you have primarily used until now), these two concepts are kept strictly isolated. You store state in discrete {term}`variables <Variable>` - like {term}`strings <String>`, {term}`dictionaries <Dictionary>`, or {term}`NumPy` {term}`arrays <Array>` - and you pass those variables through a pipeline of standalone {term}`functions <Function>`.

```python
# The Procedural Approach
my_raster = rioxarray.open_rasterio("dem.tif")  # The State
slope = calculate_slope(my_raster)              # The Logic
```

**{term}`Object-oriented programming` (OOP)** forcibly merges these two concepts. Instead of floating independently, state and logic are bundled together into a single, cohesive software entity known as an **{term}`object <Object>`**.

The data variables stored inside the object are called **{term}`attributes <Attribute>`**, and the functions that belong exclusively to the object are called **{term}`methods <Method>`**. Instead of passing raw data into an external function, you ask the object to perform an action on itself using {term}`dot notation <Dot notation>`.

```python
# The Object-Oriented Approach
my_raster = rioxarray.open_rasterio("dem.tif")
slope = my_raster.calculate_slope()             # The Object acts upon its own state
```

While this might initially look like a mere syntactic shortcut (moving the variable to the front of the function) it represents a profound shift. Rather than writing scripts that micromanage data pipelines, you are now architecting systems of self-contained entities that know exactly what they are and how to manage themselves.

---

## 2. When procedural code starts to break

To understand why this architectural shift is necessary, consider how procedural code scales. Imagine you are writing a script to track live data from weather stations across Switzerland.

In a purely procedural style, you might attempt to manage the state of these stations using multiple parallel lists:

```python
# A procedural approach using parallel lists
station_names = ["Zurich", "Geneva", "Lugano"]
latitudes = [47.37, 46.20, 46.00]
longitudes = [8.54, 6.14, 8.95]
elevations = [408, 375, 273]
temperatures = [12.5, 14.2, 16.1]
```

To update the temperature for Zurich, you must find its index and carefully modify the corresponding list:

```python
# Finding the index and updating the specific state
idx = station_names.index("Zurich")
temperatures[idx] = 13.0
```

This approach works for a quick script, but it is structurally fragile. What happens when you scale to 500 stations and need to execute more complex logic, such as calibrating temperatures based on elevation?

```python
def calibrate_temp(temp, elevation):
    # Standard environmental lapse rate calibration
    return temp - (elevation * 0.006)

# Applying logic requires manually synchronizing disconnected state variables
new_temp = calibrate_temp(temperatures[idx], elevations[idx])
temperatures[idx] = new_temp
```

The computer has no concept that `station_names[0]`, `elevations[0]`, and `temperatures[0]` belong to the same physical entity. You, the programmer, are solely responsible for keeping these disconnected arrays perfectly synchronized.

If you sort, filter, or delete an item from one list without perfectly replicating that action across the other four lists, your entire dataset is corrupted. As your analytical pipelines become more complex, it becomes increasingly difficult to manually track these invisible relationships.

---

## 3. A spatial motivation

To resolve this structural fragility, Object-Oriented Programming allows us to model the real-world entity directly. Instead of scattering the properties of a weather station across five disconnected arrays, we encapsulate them into a single, cohesive unit: a `WeatherStation` object.

If we architected our code around objects, the workflow would look very different:

```python
# An object-oriented approach (Conceptual)
zurich_station = WeatherStation(name="Zurich", lat=47.37, lon=8.54, elev=408, temp=12.5)

# The object executes logic upon its own internal state
zurich_station.calibrate_temp()
print(zurich_station.temp)
```

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L11_ch01_oop_explorer/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Classes and Instances.</b><br>
    Click the "Instantiate Object" button to create new <code>WeatherStation</code> objects in memory. Notice how the class acts as a single blueprint, but each instantiated object maintains its own independent state (elevation and temperature) that can be individually manipulated using the encapsulated <code>.calibrate_temp()</code> method. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L11_ch01_oop_explorer/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033-->

Notice the architectural change. We no longer pass raw elevation and temperature data into a free-floating function. The `zurich_station` object already *knows* its own internal state, and it encapsulates the logic required to calibrate itself without external micromanagement.

In spatial data science, this paradigm is inescapable. You have actually been relying on it since you drew your first map:

* A **Coordinate** is an object managing an X and Y state.
* A **{term}`GeoDataFrame`** is an object managing a tabular attribute table and an underlying geometry array, with built-in methods to `.plot()` or `.to_crs()` (reproject) itself.
* A **{term}`Data Cube <Data cube>`** (`xarray.Dataset`) is a highly complex object managing an n-dimensional matrix, coordinate reference systems, and temporal indices, offering methods to efficiently calculate a `.mean()` across time.

---

## 4. Python is already object-oriented

If the `my_raster.calculate_slope()` syntax feels familiar, it is because **you have been using objects all along**. Python is fundamentally an object-oriented programming language, meaning that almost every entity you interact with is an object.

When you create a simple list, you are instantiating an object of the {term}`list <List>` {term}`class <Class>`. It encapsulates its own internal state (the items) and exposes built-in methods (logic) to modify that state.

```python
my_cities = ["Zurich", "Geneva"]

# The list object executes internal logic to modify its own state
my_cities.append("Lugano") 
```

When you load a GeoDataFrame, you are working with a highly complex spatial object. The developers of GeoPandas already did the heavy lifting of encapsulating coordinate arrays, tabular data, and geometric algorithms into a single interface.

Because it is an object, it cleanly separates its **state** (attributes) from its **actions** (methods):

```python
import geopandas as gpd
cantons = gpd.read_file("swiss_cantons.shp")

# Accessing internal state (Attributes do not use parentheses)
cantons_area = cantons.area 

# Executing internal logic (Methods require parentheses)
cantons_projected = cantons.to_crs(epsg=2056)
```

You did not have to write a complex geometric algorithm to calculate areas or reproject coordinates. The developers bundled those algorithms directly into the object.

By mastering {abbr}`OOP (Object-Oriented Programming)`, you will transition from merely *consuming* objects engineered by other developers, to *architecting* your own custom objects tailored to your specific scientific needs.

---

#### Concept Check: Identifying the Paradigm

You are reading through a colleague's script and spot the following line of code used to clean a tabular dataset:

`cleaned_data = dataset.dropna().reset_index()`

Based on the syntax, what paradigm is predominantly being used here?

A. Procedural Programming
B. Object-Oriented Programming

```{admonition} Check your understanding
:class: dropdown

**Answer: B. Object-Oriented Programming**
The use of dot notation (`.dropna()`, `.reset_index()`) indicates that the `dataset` variable is actually an object. It is executing its own internal logic (methods) to modify and return its internal state, rather than being passed as raw data into standalone functions.

```

---

## 5. The Four Pillars of OOP

Object-Oriented Programming rests on four foundational pillars. While these terms sound heavily theoretical, they are highly practical architectural rules designed to make your code robust, secure, and scalable.

* **{term}`Encapsulation`:** The bundling of state (attributes) and logic (methods) into a single, secure unit. It acts as a protective shield, restricting direct access and preventing outside, procedural code from accidentally corrupting the object's internal state.
* **{term}`Abstraction`:** The art of hiding complex implementation details behind a simple interface. When you execute `ds.plot()` on an Xarray dataset, the hundreds of lines of underlying Matplotlib code required to render it are abstracted away, insulating you from the complexity.
* **{term}`Inheritance`:** The creation of hierarchical relationships to eliminate redundant code. A specialized "child" class can inherit all the state and logic of a general "parent" class. For example, a specialized `SatelliteRaster` class could inherit the base coordinate-handling logic from a generic `Raster` class, while adding its own unique methods for atmospheric correction.
* **{term}`Polymorphism`:** The ability of a single method name to adapt its behavior based on the object executing it. For instance, calling `.plot()` on a GeoDataFrame draws discrete vector polygons, while calling `.plot()` on an Xarray DataArray draws a continuous pixel mesh. The command remains identical, but the underlying logic morphs to fit the object.

---

## 6. When to use which paradigm?

Python is a multi-paradigm language. You are never forced to write object-oriented code. In fact, you can build highly effective, professional-grade analytical pipelines using purely procedural code and libraries like NumPy or Pandas.

So, how do you know when to make the architectural shift?

```{admonition} The Verbs vs. Nouns Heuristic
:class: note

When deciding between procedural and object oriented code, look at the core of your problem:
*   **Procedural architecture organizes Verbs:** Use it when your primary goal is a linear sequence of transformations (e.g., cleaning, calculating, filtering).
*   **Object Oriented architecture organizes Nouns:** Use it when your program needs to model complex real world systems (e.g., weather stations, sensors, catchments).
```

If you are building a data cleaning pipeline, performing a one off spatial calculation, or running a simple raster math script, procedural code is perfectly fine. The focus is simply moving data from point A to point B.

However, if you are tracking a network of weather stations, managing a fleet of satellite sensors, or simulating a hydrological catchment, you need robust entities. OOP allows these entities to securely maintain their own internal **state** and execute their own **logic** over time.

As you transition from writing standalone analysis scripts to building your own reusable spatial tools, custom Python packages, or complex simulation models, Object Oriented Programming will become an indispensable part of your software engineering toolkit.

---

## 7. Summary

* **The Architectural Shift:** Procedural programming strictly isolates data from functions. Object-Oriented Programming (OOP) merges them, bundling internal **state** (attributes) and **logic** (methods) together into self-contained **objects**.
* **Solving Structural Fragility:** As analytical pipelines scale, manually synchronizing disconnected parallel arrays becomes a massive liability. Objects allow you to encapsulate related state into a single, secure entity.
* **Python is inherently Object-Oriented:** You have been consuming objects all along. Every time you call `.append()` on a list or `.to_crs()` on a GeoDataFrame, you are executing an object's internal logic to modify its state.
* **The Four Pillars:** The OOP paradigm rests on Encapsulation (securing state), Abstraction (hiding implementation complexity), Inheritance (eliminating redundancy across hierarchies), and Polymorphism (methods adapting dynamically to different objects).
* **The Golden Rule:** Use procedural architecture to organize **verbs** (linear data pipelines and transformations). Use object-oriented architecture to model **nouns** (complex, real-world systems that must track their own behavior over time).
