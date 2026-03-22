---

title: L6 - Data Frames

site:
 outline\_maxdepth: 1

---

\<div class="page-subtitle"\>
Mastering tabular data and time series analysis
\</div\>

---

In the previous lesson, you learned how to **read and write files**, parse local text, and manage data outside of your code.

That was an essential step for handling real-world information, but it raises a new challenge:

> What happens when you successfully load a CSV containing multiple decades of climate records, and you need to calculate statistics across millions of data points?

So far, the only way to process that data in pure Python would be writing `for` loops to examine each row one by one. This lesson introduces a fundamental shift in how you manipulate data. Instead of procedural loops, you will learn how to wield **Pandas**.

What is pandas? The pandas library is a powerful and easy to use toolkit for data analysis. It is widely used across many fields of science and is combining performance tools from libraries like NumPy.

---

## 1. From procedural loops to programmable spreadsheets

Programming data analysis can be fundamentally broken down into two mindsets: procedural and object-oriented.

Up until now, you have been using procedural programming: storing data in basic lists or dictionaries, and then passing that data into separate external functions to do the math.

Pandas introduces an Object-Oriented Programming (OOP) approach to data. By placing your information into **DataFrames** (two-dimensional programmable tables) and **Series** (one-dimensional columns), your data is no longer a passive container. It becomes a powerful object that comes equipped with its own internal tools (methods) to filter, clean, and calculate instantly.

---

## 2. Why this matters for {abbr}`SDS (Spatial Data Science)`

In spatial data science and geoscience, the vast majority of your raw information will be tabular. Whether you are downloading hourly weather station logs, census demographics, or sampling records, you will be dealing with two-dimensional grids of numbers, text, and dates. Next week, we will also add location information to this mix.

Real-world environmental data can also be messy. Sensors go offline and leave missing values (`NaN`), timestamps are formatted unpredictably, and numbers can be recorded as text strings.

Pandas is one industry standard for cleaning and preparing this data. It provides the **vectorization** superpower—the ability to perform complex mathematical formulas across entire datasets simultaneously, without writing a single loop. By mastering Pandas, you transform tedious data-cleaning chores into lightning-fast, automated workflows.

---

## 3. Learning objectives

After this lesson, you will be able to:

* **Shift your data mental model**
  Transition from basic Python lists to manipulating Pandas DataFrames and Series using object-oriented methods.
* **Sanitize and filter messy data**
  Handle real-world anomalies by correcting data types, slicing text strings, safely interpolating missing `NaN` values, and isolating rows using Boolean indexing.
* **Harness the power of vectorization**
  Eliminate `for` loops by performing instantaneous, column-wise mathematics to derive new environmental indicators.
* **Master time-series analysis**
  Convert text strings into time-aware `DatetimeIndex` objects to easily resample high-frequency sensor data, calculate moving averages, and expose long-term climate trends.

---

## 4. Lesson structure

This lesson is structured to take you from basic data ingestion to complex climate analysis:

1. **The Pandas Mental Model**: Shifting from procedural Python to Object-Oriented data structures.
2. **Getting Data In and Out**: Using robust I/O tools to load messy text files and export clean CSVs.
3. **Slicing and Dicing**: Navigating the 2D grid using columns, Boolean filters, and indexers (`.loc` / `.iloc`).
4. **Cleaning the Mess**: Standardizing headers, fixing data types, and safely handling the infamous `NaN`.
5. **Vectorization**: Performing instantaneous math and applying complex logic without loops.
6. **Aggregating and Joining**: Grouping data to extract summary statistics and merging relational tables.
7. **Using Temporal Data**: Parsing dates, extracting components, and time-traveling with `.resample()` and `.rolling()`.
8. **Practical L6**: Applying these skills to sanitize 50 years of Alpine weather data and mathematically quantify climate change.

---

## 5. Looking ahead

Lesson 6 is about **thinking in data structures**.

You will learn not only *how to use Pandas*, but how to:

* confidently sanitize unpredictable environmental datasets
* perform rapid, loopless mathematics on millions of rows
* expose the hidden signals inside noisy time-series data

If Lesson 5 was about *gathering data from the real world*, Lesson 6 is about **taming it**.

The tabular manipulation and time-series skills you build here are the essential foundation for many workflows. In the upcoming lessons, we will expand these exact same DataFrame concepts into the spatial realm using GeoPandas, allowing you to seamlessly merge this tabular logic with geographic geometries and maps.