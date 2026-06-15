---
title: L11 - Object-Oriented Programming

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Moving beyond sequential scripts to build scalable spatial tools
</div>

---

:::{figure} images/L11_oop.png
:alt: ...
:width: 700px
:::

---

Up to this point, you have been writing Python scripts that execute line by line, defining variables and passing them into functions. You have learned how to use powerful libraries to handle multidimensional data cubes and map complex spatial trends. However, as your scripts grow from 50 lines to 500 lines, you will likely hit a structural limit. How do you keep track of dozens of variables? What happens when multiple functions need to modify the exact same geographic dataset?

This lesson introduces **Object-Oriented Programming (OOP)**, a paradigm shift in how you design your code. Object-Oriented Programming empowers developers to build modular, maintainable and scalable applications. We will transition from simply writing functions that *do things to data*, to creating self-contained objects that *own their data and know what to do with it*.

---

## 1. From actions to entities

Programming complex spatial workflows requires a major shift in your mental model. In Procedural Programming, state (storing data) and logic (doing things with data) are kept strictly isolated. You store state in discrete variables and pass those variables through a pipeline of standalone functions.

Object-Oriented Programming forcibly merges these two concepts. Instead of floating independently, state and logic are bundled together into a single, cohesive software entity known as an object. Rather than writing scripts that micromanage data pipelines, you are now architecting systems of self-contained entities that know exactly what they are and how to manage themselves.

---

## 2. Why this matters for {abbr}`SDS (Spatial Data Science)`

In spatial data science, this paradigm is inescapable.

You have actually been relying on it since you drew your first map: A Coordinate is an object managing an X and Y state. A GeoDataFrame is an object managing a tabular attribute table and an underlying geometry array, with built-in methods to `.plot()` or `.to_crs()` (reproject) itself. A Data Cube (`xarray.Dataset`) is a highly complex object managing an n-dimensional matrix, coordinate reference systems, and temporal indices, offering methods to efficiently calculate a `.mean()` across time.

By mastering OOP, you will transition from merely *consuming* objects engineered by other developers, to *architecting* your own custom objects tailored to your specific scientific needs.

---

## 3. Learning objectives

After this lesson, you will be able to:

* **Shift to the Object-Oriented mental model**
    Understand the conceptual shift from organizing code around actions to organizing code around objects.
* **Design blueprints and instantiate objects**
    Use classes as templates to build reusable objects that bundle related data and behavior. Utilize the `__init__()` method to guarantee a valid starting state and safely manage independent object data using `self`.
* **Drive behavior with methods**
    Attach functions directly to your classes to read, format, or analyze internal state. Turn passive storage into active spatial tools that can measure distances, test topological relationships, and control their own state changes.
* **Specialize through inheritance**
    Build specialized child classes on top of general parent classes. Reuse shared geospatial designs and extend their behaviors using the `super()` function and method overriding.
* **Make architectural judgments**
    Compare procedural and object-oriented designs to identify when to use standalone functions for simple transformations and when to model complex entities with classes.

---

## 4. Lesson structure

This lesson is structured to take you from the theoretical foundations of OOP to making high-level architectural decisions for your spatial workflows:

1. **Introduction to OOP**: Moving beyond sequential scripts and exploring the core pillars of object-oriented design.
2. **The Idea of a Class**: Distinguishing between blueprints and instances, and constructing geospatial objects with distinct attributes.
3. **Methods-Driven Behavior**: Equipping passive data containers with internal logic, spatial interaction methods, and magic dunder methods.
4. **Inheritance and Extension**: Creating class hierarchies to eliminate redundant code and specialize geographic features.
5. **Procedural vs. OOP**: Evaluating both paradigms side-by-side to choose the right design strategy for specific spatial problems.

---

## 5. Looking ahead

Lesson 11 is about **architecting systems**.

You will learn not only *how to write scripts*, but how to:

* bundle data and behavior into secure, cohesive entities
* scale complex geospatial workflows without losing track of variables
* reuse code intelligently across specialized geographic features

If previous lessons were about *analyzing the world using existing tools*, this lesson is about **building the very tools themselves**.

The object-oriented principles you master here form the foundation of professional software engineering and open-source development. By organizing your thoughts around entities rather than just actions, you are now equipped to build sophisticated, maintainable, and scalable spatial applications.
