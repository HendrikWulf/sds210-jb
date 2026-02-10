---
title: L2 - Variables & Values

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
How Python represents data
</div>

---

In the first lesson, you focused on **getting started**: running Python code, working in notebooks, and understanding how code cells behave.

In this lesson, the focus shifts from *how Python runs* to *how Python stores information*.

At the heart of this lesson are **variables**.

A {term}`variable` is more than just a name. It is a way to **represent data**, give it meaning, and make it usable for analysis.

---

## Learning objectives

After this lesson, you will be able to:

- **Represent data using variables**  
  Store values in Python using clear names, appropriate data types, and suitable data structures.

- **Group and access related values**  
  Work with lists and dictionaries to organise data, access individual elements, and understand copying and indexing.

- **Compute and present results**  
  Perform simple calculations using operators and display results clearly using formatted output.

---

## From values to data

At first, variables store **single values**:
- a number
- a piece of text
- a logical state (true or false)

Very quickly, however, real-world problems require more than one value at a time.

Spatial data is a good example:
- a location has **coordinates**
- a city has **multiple attributes**
- distances are **derived** from other values

To handle this, Python provides **multi-item variables**, such as lists and dictionaries, which allow you to group related values and give structure to your data.

---

## Why this matters for {abbr}`SDS (Spatial Data Science)`

In spatial data science, almost everything is structured data:

- coordinates belong together
- attributes belong to features
- results should be stored, not just printed

The way you choose and organise variables determines:
- how readable your code is
- how easy it is to extend your analysis
- how naturally your work scales to tables, rasters, and spatial objects later on

This lesson introduces the **building blocks** you will reuse throughout the course.

---

## Looking ahead

The data structures you learn here are essential for the next steps in the course.

In the following lessons, you will use them to:
- process collections automatically using loops
- work with tabular data using Pandas
- represent spatial features using GeoDataFrames

If Lesson 1 was about *getting started*, Lesson 2 is about **thinking in data**.
