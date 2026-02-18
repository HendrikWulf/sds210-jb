---
title: Naming Variables

site:
 outline_maxdepth: 1
---


<div class="page-subtitle">
Choosing Clear and Meaningful Names
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/02_naming-variables.ipynb)

```{admonition} Big idea
:class: tip

Variable names do not change how Python runs your code.  
They change how well **humans understand it**, including your future self.
```

In this section, you will learn how to choose clear and meaningful variable names in Python.
Good naming makes your code easier to read, debug, and share, even months after you first wrote it.

---

## 1. Why Variable Names Matter

Variable names are primarily for **people**, not for Python.

Python only cares that a name is valid.
Humans care whether the name explains what a value represents.

Consider these two variables:

```python
x = 42.36
latitude = 42.36
```

Both store the same value.
Only one clearly communicates what that value means.

Code is usually read many more times than it is written.
Good variable names reduce mental effort and make your intentions clear.

---

## 2. What Python Allows as Variable Names

Before thinking about style, it helps to know what Python allows.

A valid variable name:

* starts with a letter or an underscore
* can contain letters, numbers, and underscores
* is case sensitive
* cannot start with a number
* cannot contain special characters

Examples of valid names:

```python
num_points = 120
_point_count = 120
station_id2 = "101533"
```

Examples of invalid names:

```python
# 2points = 120      # starts with a number
# station-id = 42    # contains a special character
# total$sum = 10     # contains a special character
```

---

## 3. Reserved Words and Built-in Names

Some names are **reserved** by Python and cannot be used as variable names.

These include keywords such as `for`, `if`, `else`, and `while`.
Using them would confuse Python, so they are not allowed.

You can inspect the list of reserved keywords:

```python
import keyword
keyword.kwlist
```

In addition, avoid using names of built-in functions such as `print`, `list`, or `type` as variables.
Even if Python allows it, doing so makes code harder to read and debug.

---

## 4. What Makes a Good Variable Name

A good variable name should be:

* clear and concise
* descriptive without being overly long
* written in English
* free of special characters
* unambiguous

Compare these examples:

```python
s = "101533"
finnishmeteorologicalinstituteobservationstationidentificationnumber = "101533"
fmi_station_id = "101533"
```

The first is too vague.  
The second is technically descriptive but hard to read and use.  
The third strikes a good balance.

```{admonition} Note
:class: note

A good variable name should answer one question clearly:  
*What does this value represent?*
```

---

## 5. Naming Conventions in This Course

Python supports different naming styles.
What matters most is **consistency**.

In this course, we recommend using **snake_case** for variables and functions, as it is the most common and readable convention in Python.

Snake case uses lowercase letters with words separated by underscores:

```python
temp_celsius = 20.0
fmi_station_id = "101533"
coordinate_system = "WGS 84"
```

You may encounter other styles such as camelCase in existing code.
You are not required to rewrite such code, but in your own work you should follow a single convention consistently.

| Convention          | Style example             | Commonly used for                              |
|---------------------|---------------------------|------------------------------------------------|
| snake_case          | asoziales_netzwerk        | variables, functions, arguments                |
| camelCase           | asozialesNetzwerk         | variables, functions, arguments                |
| kebab-case          | asoziales-netzwerk        | markup languages (e.g. HTML, XML tags)         |
| PascalCase          | AsozialesNetzwerk         | classes and other data structures              |
| UPPER_SNAKE_CASE    | ASOZIALES_NETZWERK        | constants, environment settings                |

---

## 6. Good and Poor Naming Examples

### Good examples

```python
latitude = 55.6761
longitude = 12.5683
elevation_meters = 14.0
city_name = "Copenhagen"
population = 809314
```

These names are clear, descriptive, and easy to understand.

### Poor examples

```python
x = 55.6761          # too generic
data = "Copenhagen" # too vague
temp = 25.6         # ambiguous
l = [55.68, 12.57]  # unclear and hard to read
```

Poor names force the reader to guess what a value represents.

---

## 7. Short Exercise

Look at the following variables and improve their names:

```python
a = 46.948
b = 7.447
c = "urban"
d = "EPSG:2056"
e = 542
```

Rename them so that their meaning becomes clear.
Focus on choosing names that would still make sense if you looked at the code again in a few months.

---

## 8. Summary

After this section, you should understand that:

* Python allows many variable names, but not all are good choices
* good variable names improve readability and maintainability
* names should be clear, descriptive, and consistent
* reserved words and built-in names should be avoided
* this course recommends snake_case for variables

---

### What Comes Next

Variable names describe **what a value represents**.
In the next section, we will look at **data types**, which describe **what kind of value** it is and what operations are possible.

Together, good naming and an understanding of data types form the basis for clear and reliable code.
