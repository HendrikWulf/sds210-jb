---
title: Printing & Formatting Output

site:
 outline_maxdepth: 1
---


<div class="page-subtitle">
Seeing results clearly
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/06_formatting-output.ipynb)


```{admonition} Big idea
:class: tip

Printing makes results visible.  
Formatting makes results understandable.

Clear output supports debugging, communication, and learning.
```

So far, you have worked with values, expressions, and strings.  
In many cases, Python already shows results automatically in a notebook.

In this section, you will learn **when and why to print values explicitly** and how to format output so it is readable and meaningful.

---

## 1. Notebook Output vs `print()`

In a Jupyter Notebook, the **last expression in a code cell** is displayed automatically.

```python
2 + 3
```

This works without using `print()` and is convenient when you are exploring values interactively.

However, automatic display has clear limitations and should not be relied on in all situations.

---

### When Automatic Display Works

Automatic display is useful when you are:

* exploring values
* testing expressions
* checking intermediate results

Keep in mind:

* only the **last expression** in a cell is shown
* only **one value** is displayed
* this behaviour exists **only in notebooks**

---

### Using `print()`

The `print()` function sends output to the screen explicitly.

```python
print(2 + 3)
```

Printing works consistently:

* in notebooks
* in scripts
* in larger programs

This makes `print()` essential for debugging, explanations, and clear communication of results.

---

```{admonition} Key idea
:class: note

Automatic display is a **notebook feature**.  
`print()` is a **Python feature**.

When clarity matters, rely on `print()`.
```

---

## 2. Printing Multiple Values

The `print()` function can display **multiple values at once**.

```python
distance_km = 120
speed_kmh = 80

print(distance_km, speed_kmh)
```

Python automatically inserts spaces between the values.
This makes `print()` useful for quick inspection of several variables at the same time.

---

### Labels Improve Readability

Output becomes much clearer when you add text labels.

```python
print("Distance:", distance_km, "Speed:", speed_kmh)
```

This simple habit helps others and your future self understand what each value represents.

Clear labels turn raw numbers into meaningful information.

---

## 3. Formatting Output with f-strings

For more readable output, Python provides **f-strings**.
They allow you to embed variable values directly into text.

```python
travel_time_h = distance_km / speed_kmh
print(f"Travel time: {travel_time_h} hours")
```

The `f` before the string tells Python to evaluate expressions inside `{}` and insert their values.  
The `f` stands for *formatted*.

Anything that produces a value can go inside `{}`.

```python
print(f"Double speed: {speed_kmh * 2} km/h")
```

---

### Formatting Numbers

You can control **how numbers are displayed** using formatting inside f-strings.

```python
print(f"Travel time: {travel_time_h:.2f} hours")
```

The part after the colon `:` defines the formatting rule:

* `.2` specifies **two digits after the decimal point**
* `f` formats the value as a **floating-point number**

Together, `.2f` means:

> *Display this number as a decimal with exactly two digits after the decimal point.*

For example, a value like `1.23456` is shown as `1.23`.

---

### Other Common Number Formats

Different format specifiers change how numbers appear:

```python
value = 1.2345

print(f"{value:.2f}")   # decimal format
print(f"{value:.2e}")   # scientific notation
print(f"{value:.2%}")   # percentage

x = 1.2345
y = 5
```

| Format | Meaning                              | What it does                             | Example f-string | Displayed result |
| -----: | ------------------------------------ | ---------------------------------------- | ---------------- | ---------------- |
|    `f` | fixed-point decimal (floating point) | Displays the number as a decimal value   | `f"{x:.2f}"`     | `1.23`           |
|    `e` | scientific notation                  | Displays the number in exponential form  | `f"{x:.2e}"`     | `1.23e+00`       |
|    `%` | percentage                           | Multiplies the value by 100 and adds `%` | `f"{x:.2%}"`     | `123.45%`        |
|    `d` | integer (whole numbers only)         | Displays a whole number without decimals | `f"{y:d}"`       | `5`              |

This affects **only the output**, not the stored value.

---

```{admonition} Note
:class: note

Formatting is about presentation, not calculation.

The value in memory stays the same.  
Only the displayed text changes.
```

This distinction is essential when presenting results, debugging, or comparing outputs.

---

## 4. Why Formatting Matters

Clear output helps you:

* understand what your code is doing
* communicate results to others
* spot mistakes more easily

Poorly formatted output forces the reader to guess meaning.
Well formatted output makes intent obvious.

---

### Printing as a Debugging Tool

Printing intermediate values is one of the simplest and most effective debugging techniques.

```python
print("Distance:", distance_km)
print("Speed:", speed_kmh)
print("Time:", travel_time_h)
```

You can also use an f-string to make the output more readable.

```python
print(f"Distance = {distance_km} km, Speed = {speed_kmh} km/h, Time = {travel_time_h:.2f} h")
```

This allows you to verify that values are correct at each step and to quickly identify where something goes wrong.

---

## 5. Short Exercise

Many migratory birds travel long distances over several days.
To understand such movements, we often estimate **travel time** from distance and average **airspeed**.

Assume a migratory bird flying from Northern Europe to Southern Europe.
The estimated migration distance is:

```python
distance_km = 1800
```

Two possible average airspeeds are:

* **10 m/s** (slower sustained flight)
* **15 m/s** (faster sustained flight)

---

### Task

1. Convert the airspeed from **m/s to km/h**.
2. Compute the estimated **travel time in hours** for **both speeds**.
3. Display the results using **clear, formatted output** that:

   * states the distance and airspeed
   * includes correct units
   * rounds travel time to **two decimal places**
4. Add **one print statement** that would help you debug the calculation if the result looks implausible.

---

````{admonition} Sample solution (click to compare with your results)
:class: dropdown

```{code-cell} python
# Migration distance
distance_km = 1800

# Airspeeds in meters per second
speed_ms_slow = 10
speed_ms_fast = 15

# Convert airspeed from m/s to km/h
speed_kmh_slow = speed_ms_slow * 3.6
speed_kmh_fast = speed_ms_fast * 3.6

# Calculate travel times
time_h_slow = distance_km / speed_kmh_slow
time_h_fast = distance_km / speed_kmh_fast

# Formatted output
print(
    f"At an airspeed of {speed_ms_slow} m/s ({speed_kmh_slow:.1f} km/h), "
    f"the migration takes about {time_h_slow:.2f} hours."
)

print(
    f"At an airspeed of {speed_ms_fast} m/s ({speed_kmh_fast:.1f} km/h), "
    f"the migration takes about {time_h_fast:.2f} hours."
)
```

```{code-cell} python
# Debugging output to verify unit conversion
print("DEBUG → speeds (km/h):", speed_kmh_slow, speed_kmh_fast)
```

**Explanation:**

* Airspeed must be converted from meters per second to kilometers per hour before calculating travel time.
* The conversion factor is *1 m/s = 3.6 km/h*.
* Higher airspeed results in shorter travel time.
* Debug output helps confirm that unit conversion happened correctly.
* Formatting improves readability without affecting the calculation itself.

````

---

## 6. Summary

After this section, you should understand that:

* notebooks display the last expression in a cell automatically
* `print()` makes output explicit and works in all Python contexts
* multiple values can be printed together in a single statement
* f-strings make output more readable and expressive
* formatting affects how values are shown, not how they are stored
* printing is a key tool for debugging and communication

---

### Looking Ahead

You now know how to see and present results clearly.

Next, we move on to **multi item variables**, which allow a single variable to store multiple values such as coordinates, paths, or attributes.
