---
title: Variables

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Storing and Reusing Values
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/01_variables.ipynb)

```{admonition} Big idea
:class: tip
Variables allow us to store values, reuse results, and build readable workflows instead of repeating calculations.
```

In this section, you will learn how Python uses variables to keep track of values in memory and how those values can be reused and updated throughout a program. You will also see how variables behave in a Jupyter Notebook, why execution order matters, and how small changes to one variable affect (or do not affect) others.

These concepts form the foundation for all later programming tasks in this course, from simple calculations to more complex geospatial workflows.

---

## 1. What Is a Variable?

A **variable** is a way to **store a value in memory** so that it can be reused later in your code.

You can think of a variable as:

* a **label** (the variable name)
* that **points to a value** stored somewhere in memory

Once a value is stored in a variable, you can use it in calculations instead of typing the value again and again.

A variable is **not** the value itself, and it is **not** a container that remembers history. It always points to **one current value**.

---

### Assigning a Value to a Variable

To create a variable, you use the **assignment operator** `=`.

```python
temp_celsius = 10.0
```

* `temp_celsius` is the **variable name**
* `=` assigns a value
* `10.0` is the **stored value**

```{admonition} Important
:class: note
Assigning a variable does **not** produce any output.  
The value is stored silently in memory.
```

---

### Why Variables Are Useful

Instead of repeating values like `10.0` in multiple places, you can:

* give the value a **meaningful name**
* reuse it in calculations
* change it later in one place

You will use variables constantly when working with coordinates, distances, and other geospatial values.

---

## 2. Seeing Variable Values

In a **Jupyter Notebook**, you can display the value of a variable simply by writing its name as the last line of a code cell.

```python
temp_celsius
```

When you run this cell, Jupyter automatically displays the value stored in the variable.

---

### Why Does This Work?

Jupyter Notebooks have a special behaviour:

> *The output of the last expression in a code cell is displayed automatically.*

Because `temp_celsius` is an expression that evaluates to a value, Jupyter shows it for you.

This is very convenient for interactive work and quick checks.

```{admonition}
:class: note
In Jupyter, only the **last expression** in a cell is shown automatically.
Everything else must be displayed explicitly (for example using `print()`).
```

---

### Using `print()`

You can also display a variable using the `print()` function:

```python
print(temp_celsius)
```

This works in any Python environment, including scripts and notebooks.

In Jupyter Notebooks, `print()` is usually only needed when:

* you want **formatted output** (e.g. text + values)
* you want to display **multiple values** in a single cell

```python
print("Temperature in Celsius:", temp_celsius)
```

---

## 3. Using Variables in Calculations

Once a value is stored in a variable, you can use that variable **just like a number** in calculations.

For example, we can convert the temperature from Celsius to Fahrenheit using `temp_celsius`:

```python
print("Temperature in Fahrenheit:", 9 / 5 * temp_celsius + 32)
```

When this cell is executed, Python:

* looks up the current value stored in `temp_celsius`
* substitutes that value into the expression
* evaluates the full calculation
* displays the result

> *Python stores values, not formulas. Once an expression is evaluated, only the result is stored.*

---

### Why This Is Powerful

Variables allow you to:

* **reuse values** in many different calculations
* avoid repeating numbers throughout your code
* change a value once and reuse it everywhere it appears

You can use `temp_celsius` again later without redefining it.

---

### When Are Expressions Evaluated?

An important detail to understand is that:

> **Expressions are evaluated when the code cell is executed.**

Python stores **values**, not **relationships**.
It uses the current value of a variable at the moment the cell is run.

This becomes especially important when variables are updated, which we will look into after this small exercise.

---

## 4. Define Your Own Variable

Let’s pause briefly and try this yourself.

### Task

1. Define **one variable of your choice**.
2. Assign it any value you like.
3. Display its value in the notebook.

Try to:

* use a **meaningful variable name**
* follow **`snake_case`** naming (words separated by underscores)

For example, your variable could represent:

* a temperature
* a distance
* a number of locations
* any value that makes sense to you

```python
# Define your variable here
```

There is no “right” or “wrong” value here. This task is only meant to help you get comfortable creating and inspecting variables.

Next, we will look at **updating variables** and what happens when their values change.

---

## 5. Updating Variables

Variables are **not fixed**. Their values can be changed by assigning a new value to the same variable name.

This is called **reassignment**.

```python
temp_celsius = 17.0
print("temperature in Celsius is now:", temp_celsius)
```

When this cell is executed:

* the new value `17.0` is stored in `temp_celsius`
* the previous value is **replaced**
* the old value is no longer available

---

### An Important Mental Model

> **Variables do not remember past values.**

A variable always points to **one current value** — the most recent one that was assigned.

This explains why execution order and inspection are so important, which we will look at next.

---

## 6. Execution Order and `NameError`

In a Jupyter Notebook, **code cells are executed in the order you run them**, not in the order they appear on the page.

Let’s see what happens if we try to use a variable that has **not been defined yet**.

```python
print(5 / 9 * (temp_fahrenheit - 32))
```

Running this cell raises a `NameError`.

---

### Why Does This Error Occur?

This happens because:

* the variable `temp_fahrenheit` does **not exist yet**
* variables are only created **after** their defining cell has been executed
* Jupyter allows cells to be run **out of order**

Python has no value to substitute for `temp_fahrenheit`.

```{admonition}
:class: warning
If you see a NameError, it often means:
- the variable has not been defined yet, or
- the cell that defines it has not been run

In notebooks, the order you run cells matters more than the order you see them.
```

---

### Fixing the Error

We first need to define the variable:

```python
temp_fahrenheit = 9 / 5 * temp_celsius + 32
```

Once this cell has been run, the variable exists in memory.
You can now rerun the previous cell without getting a `NameError`.

---

### Key Understanding

> In a notebook, **execution order matters**.

```{admonition} Common beginner pitfall
:class: warning
If a value looks “wrong”, it is usually because:
- a variable was not updated
- a dependent value was not recalculated
- a required cell was not run (or was run out of order)
```

> *At this point, you should be able to predict the output before running the cell.*

---

## 7. Checking Multiple Variables Together

When working with several variables, it is often useful to **inspect their values together**.

```python
print(
    "temperature in Celsius:",
    temp_celsius,
    "and in Fahrenheit:",
    temp_fahrenheit,
)
```

This displays the current values side by side.

---

### Why This Is Useful

Inspecting values is a **normal and deliberate programming workflow**.

You will often do this to:

* check whether calculations worked as expected
* confirm that variables were updated correctly
* understand what your code is doing step by step

Printing multiple variables together is therefore a **basic debugging technique**.

When something behaves unexpectedly, a good first step is to check the relevant variables.

---

## 8. Variables Are Independent

An important and sometimes surprising behaviour in Python is that **variables are independent of each other**.

Let’s update `temp_celsius` again:

```python
temp_celsius = 20.0
print(
    "temperature in Celsius is now:",
    temp_celsius,
    "and temperature in Fahrenheit is still:",
    temp_fahrenheit,
)
```

Even though `temp_fahrenheit` was originally calculated from `temp_celsius`, its value does **not** change.

---

### Why Does This Happen?

This happens because:

* Python stores **values**, not **relationships**
* once a calculation is executed, the result is stored as a value
* changing one variable does **not** trigger updates in others

Python does not remember *how* a value was computed, only *what* value was stored.

---

### The Key Takeaway

> **Changing one variable does not update others automatically.**

If you want dependent values to change, you must **recalculate them explicitly**.

This mental model is essential for understanding:

* why functions are useful
* why recalculation is necessary
* how data pipelines work later in the course

---

## 9. Short Exercise

This exercise revises the key ideas from this section.

### Task

1. Define a variable called `distance_km` with a numeric value.
2. Define a second variable `speed_kmh`.
3. Compute the travel time in hours and store it in a new variable.
4. Display the result using both:
   * direct notebook output
   * the `print()` function
5. Update the value of `speed_kmh` and re run the calculation.

### Questions to Think About

* Which values change after reassignment and which do not?
* What happens if you run the calculation cell before defining a variable?
* Why does the notebook sometimes show output without `print()`?

The goal is not speed, but clarity. Make sure you understand why each result appears.

```python
# Do the exercise here

```

Only refer to the sample solution once you have completed the exercise *yourself*. It is important to exercise and build confidence.

````{admonition} Example solution
:class: dropdown

### Step 1: Define the input variables

We start by defining two variables that represent our input values.

```python
distance_km = 120
speed_kmh = 60
```

* `distance_km` stores the travel distance in kilometres
* `speed_kmh` stores the speed in kilometres per hour
* Both variables store numeric values that can be used in calculations

---

### Step 2: Compute travel time

We now compute the travel time using the formula:

time = distance ÷ speed

```python
travel_time_hours = distance_km / speed_kmh
```

This expression is evaluated when the cell is executed.
The result is stored as a new value in `travel_time_hours`.

---

### Step 3: Display the result in two ways

#### Direct notebook output

In a Jupyter Notebook, writing the variable name as the last line displays its value automatically.

```python
travel_time_hours
```

This works because the notebook shows the result of the final expression in a cell.

---

#### Using the print function

The `print()` function is useful when you want formatted output or multiple values.

```python
print("Travel time in hours:", travel_time_hours)
```

This works in all Python environments, not just notebooks.

---

### Step 4: Update a variable and rerun the calculation

Now we change the speed and recompute the travel time.

```python
speed_kmh = 80
travel_time_hours = distance_km / speed_kmh
travel_time_hours
```

Only the value of `speed_kmh` changed.
The distance stayed the same.
The travel time changed because it was **recalculated**.

---

### Key observations

* Reassigning a variable replaces its old value
* Other variables do not change automatically
* Dependent values only update when you explicitly recompute them
* This is why clear execution order matters in notebooks

---

### Reflection questions answered

**Which values change after reassignment and which do not?**  
Only the variable that is reassigned changes. Other variables keep their stored values until recomputed.

**What happens if you run the calculation before defining a variable?**  
Python raises a `NameError` because the variable does not yet exist in memory.

**Why does the notebook sometimes show output without print()?**  
Because Jupyter automatically displays the result of the last expression in a cell.

These ideas will become especially important when you start working with functions and collections.

````

---

## 10. Summary

After completing this section, you should understand that:

* **variables store values in memory**
* assigning a variable does **not** produce output
* a variable’s value changes **only when it is reassigned**
* **execution order matters** in Jupyter Notebooks
* variables do **not** update each other automatically

These ideas form the foundation for everything that follows in this course.

---

### What Comes Next

So far, we focused on what variables do.
Next, we focus on how to name them well.

In the next section, you will learn:

* why variable names matter for readability and collaboration
* what Python allows and disallows in variable names
* common naming styles such as `snake_case` and `camelCase`

Good naming is not about rules alone.
It is about writing code that you and others can read and trust.

---