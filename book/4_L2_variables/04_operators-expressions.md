---
title: Operators & Expressions

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Doing Things with Values
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/04_operators-expressions.ipynb)

```{admonition} Big idea
:class: tip

Operators allow you to combine values into **expressions**.  
Expressions are evaluated when code is executed to produce new values.

```

So far, you have learned how to store values in variables, how to name them clearly, and how Python distinguishes between different data types.

In this section, we focus on **how values interact**. We start with simple calculations, then build up to comparisons, logic, and module-based mathematical expressions.

---

## 1. Expressions as Calculations

An **expression** is a combination of values (operands) and operators that produces a result.

:::{figure} images/06_operation.png
:alt: The anatomy of a Python expression: operators combine operands to evaluate to a single new value.
:width: 300px
:align: center

The anatomy of a Python expression: operators combine operands to evaluate to a single new value.
:::

Think of an expression as a question you ask Python: *"What is the result of this calculation right now?"*

```{code-cell} python
# Python evaluates this expression and returns 35
5 * 7

```

An important idea is that expressions are evaluated **when you run the cell**, not when you type them. If you change a variable and run the cell again, Python recalculates the result using the newest values in memory.

```{admonition} Memory
:class: note
Python does not remember the expression itself. It only evaluates it and returns a value. If you want to keep that result for later, you must store it in a variable using `=`.

```

---

## 2. Arithmetic Operators

Arithmetic operators allow you to perform **calculations with numeric values**.
They are used inside expressions to combine values and produce new results.

At this stage, we focus only on **numeric operations**.

---

### Basic Arithmetic

Python supports the common arithmetic operators you already know.

```{code-cell} python
2 + 2
```

```{code-cell} python
5 - 3
```

```{code-cell} python
4 * 6
```

```{code-cell} python
10 / 2
```

Each expression is evaluated when the cell is executed and returns a numeric result.

---

### Using Variables as Operands

Arithmetic operators do not only work with literal numbers.
They also work with **variables that store numbers**.

```{code-cell} python
x = 7
y = 3
```

```{code-cell} python
x + y
```

```{code-cell} python
x * y
```

Here, `x` and `y` are **operands**.
An operand is simply a value or a variable that an operator acts on.

---

### Exponentiation

Python uses `**` to raise a value to a power.

```{code-cell} python
2 ** 3
```

This means two to the power of three.

---

### Optional but Useful Operators

Some additional arithmetic operators are useful in practice.

```{code-cell} python
7 % 3
```

The modulus operator returns the remainder of a division.

```{code-cell} python
7 // 3
```

Floor division returns the number of whole divisions.

You will encounter these operators later in loops, indexing, and data processing.

---

### Overview of Arithmetic Operators

| Operator | Meaning | Example | Result | Useful for... |
| --- | --- | --- | --- | --- |
| `+` | Addition | `2 + 3` | `5` | Combining distances |
| `-` | Subtraction | `5 - 2` | `3` | Finding elevation differences |
| `*` | Multiplication | `4 * 6` | `24` | Scaling coordinates |
| `/` | Division | `10 / 2` | `5.0` | Calculating average speeds |
| `**` | Exponentiation | `2 ** 3` | `8` | Squaring values (e.g., $x^2$) |
| `%` | Modulus (Remainder) | `7 % 3` | `1` | Finding even/odd numbers |
| `//` | Floor division | `7 // 3` | `2` | Counting whole segments |

```{admonition} Operands
:class: info

Operators act on operands.

Operands can be:
- literal values such as `3` or `10`
- variables that store numeric values

The data type of the operands determines whether an operation is allowed.
```
---

## 3. Assignment and Update Operators

So far, we have used expressions to **compute values**.
Now we look at how those results are **stored and updated** using assignment operators.

This section connects operators back to variables.

---

### Assignment with `=`

The assignment operator `=` stores the result of an expression in a variable.

```{code-cell} python
x = 5
```

Here, Python:

1. evaluates the expression on the right
2. stores the resulting value
3. assigns it to the variable name on the left

Assignment itself does not produce output.
It only changes what value a variable refers to.

---

### Assignment Stores Results

You can assign the result of any expression.

```{code-cell} python
y = 2 + 3
```

```{code-cell} python
y
```

The expression `2 + 3` is evaluated first.
Only the resulting value is stored.

Python does not remember how the value was computed.

---

### Update Operators as Shorthand

Python provides **update operators** that combine calculation and assignment.

```{code-cell} python
x += 3
```

This is a shorter way of writing:

```{code-cell} python
x = x + 3
```

Other common update operators follow the same pattern.

```{code-cell} python
x -= 1
```

```{code-cell} python
x *= 2
```

Each update:

* evaluates the expression
* replaces the old value
* stores the new value in the variable

---

### What Actually Changes

An important mental model is this:

> **Variables do not remember previous values.**

After reassignment, the old value is gone.

```{code-cell} python
speed = 50
speed = 80
```

After the second line, `speed` refers only to `80`.
The value `50` is no longer stored anywhere.

---

```{admonition} Update operators
:class: note

Update operators are only shorthand.
They simply replace the stored value with a new one.
```

---

## 4. Comparison Operators

Comparison operators allow you to **compare values**. Instead of producing numbers, comparisons produce **logical boolean results**: `True` or `False`.

These operators are essential for filtering spatial data (e.g., "find all cities with a population greater than 100,000").

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | **Equal to** (Note the double equals!) | `3 == 3` | `True` |
| `!=` | **Not equal to** | `3 != 5` | `True` |
| `>` | **Greater than** | `5 > 3` | `True` |
| `<` | **Less than** | `2 < 1` | `False` |
| `>=` | **Greater than or equal to** | `5 >= 5` | `True` |
| `<=` | **Less than or equal to** | `4 <= 3` | `False` |

**Data Types Matter:** Comparisons depend heavily on data types. `5 == "5"` will evaluate to `False` because an integer is never equal to a string!

---

```{admonition} Comparisons
:class: info

Comparison operators describe relationships between values.

They do not perform calculations.
They do not modify data.
They only answer yes or no questions.
```

Comparison operators are used to control program flow, filter data and make decisions based on conditions.

---

## 5. Logical Operators

Logical operators allow you to **combine multiple comparison results** into a single `True` or `False` answer.

:::{figure} images/07_logical-operations.png
:alt: Visualizing logical operators: `and` requires all conditions to be true, `or` requires at least one, and `not` reverses the condition.
:align: center

*Visualizing logical operators: `and` requires all conditions to be true, `or` requires at least one, and `not` reverses the condition.*
:::

Python provides three logical operators:

* **`and`**: Returns `True` only if **both** conditions are true.
```{code-cell} python
x = 7
(x > 5) and (x < 10)  # Returns True because 7 is between 5 and 10

```

* **`or`**: Returns `True` if **at least one** condition is true.
```{code-cell} python
(x < 5) or (x > 6)    # Returns True because 7 > 6

```


* **`not`**: **Reverses** the boolean value.
```{code-cell} python
not (x == 7)          # Returns False, because x IS 7

```

Logical operators allow you to express complex reasoning in code. Instead of asking one question, you can combine several and get a single, definitive answer.

---

## 6. Operator Behaviour & Data Types

Operators do not behave the same way for all data types. What an operator does depends entirely on **what kind of values** it is applied to.

When applied to numbers (`int`, `float`), the `+` and `*` operators perform standard arithmetic. But look what happens when we apply them to strings (`str`):

```{code-cell} python
# Concatenation: Joins strings together
"Hot" + "Cold"   # Returns "HotCold"

# Repetition: Multiplies the string
"Hot" * 3        # Returns "HotHotHot"
3 * "Hot"        # Returns "HotHotHot"
```

If you try to mix incompatible data types, the operation will fail:

```{code-cell} python
2 + "Hot"        # Raises a TypeError!

```

This is not a bug; it is Python protecting you from an undefined operation. If an operation fails, check your data types!

---

## 7. Using Functions in Expressions

Expressions can also include **functions**. Functions take an input, perform a complex calculation behind the scenes, and return a value that you can use mathematically.

To access advanced mathematical functions, we must `import` the `math` module (a built-in library of extra Python tools).

```{code-cell} python
import math

# Functions return values that can be used inside expressions
diagonal = math.sqrt(16) + 2
print(diagonal)  # Returns 6.0

```

Modules also provide useful constants, which do not require parentheses because they are stored values, not functions:

```{code-cell} python
area = math.pi * (radius ** 2)

```

---

## 8. Inspecting Expression Results

When expressions become complex, it is helpful to inspect intermediate results to ensure your logic is correct.

You can use the `print()` function to combine text and expression results for highly readable debugging output:

```{code-cell} python
distance = 150
time = 2

# We can perform the expression directly inside the print statement!
print("The average speed is", distance / time, "km/h")

```

Well-formatted output makes checking your work significantly easier and is a fundamental debugging habit.

---

## 9. Short Exercises

### Exercise 1: Expressions as Calculations

**Focus:** Understanding expressions and execution

**Task:**

1. Write three different arithmetic expressions (one addition, one multiplication, one exponentiation).
2. Run each expression in its own code cell.
3. Change one number in the code and *do not* re-run the cell yet. Does the output change automatically?

``````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
2 + 3        # addition
4 * 5        # multiplication
2 ** 3       # exponentiation
```
Changing the code has no effect until the cell is run again. Python does not remember the formula, it only evaluates the cell on command.

``````

---

### Exercise 2: Operators, Variables, and Data Types

**Focus:** Variables, arithmetic, comparisons

**Task:**
Given the following variables:

```{code-cell} python
distance_km = 180
time_hours = 2.5

```

1. Compute the average speed in km/h and store it in a new variable.
2. Create a boolean variable that checks whether the speed is greater than 70 km/h.
3. Print a readable message that includes both the speed and the boolean result.

``````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
# Compute average speed
speed_kmh = distance_km / time_hours

# Comparison produces a boolean
speed_above_70 = speed_kmh > 70

# Print a readable message
print("The average speed is", speed_kmh, "km/h. Speed above 70 km/h:", speed_above_70)
```

``````

---

### Exercise 3: Combining Comparisons, Logic, and Functions

**Focus:** Logical operators, modules, nested expressions

**Task:**

1. Import the `math` module.
2. Define a variable `angle_deg = 30`.
3. Convert the angle to radians (Formula: `angle * math.pi / 180`).
4. Compute the sine of the angle using `math.sin()`.
5. Use logical operators to check if the sine value is **both** greater than 0 **and** less than 1.

``````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
import math

angle_deg = 30
angle_rad = angle_deg * math.pi / 180

sin_value = math.sin(angle_rad)

# Combine conditions using 'and'
valid_range = (sin_value > 0) and (sin_value < 1)

print("Sine value:", sin_value, "| Is valid:", valid_range)
```

``````

---

## 10. Summary

After completing this section, you should understand that:

* **Expressions combine values and operators** to produce a single result.
* **Expressions are evaluated when code is executed.**
* **Arithmetic operators** (`+`, `-`, `*`, `/`, `**`, `%`, `//`) act as a calculator.
* **Comparison operators** (`==`, `>`, `<=`) always produce boolean values (`True` or `False`).
* **Logical operators** (`and`, `or`, `not`) combine boolean conditions to build complex reasoning.
* Operator behavior changes depending on data types (e.g., `+` adds numbers but joins strings).

### Looking Ahead

Expressions are the foundation for making decisions in code. In the next section, we will take a deeper dive into **Strings**. Strings behave uniquely, especially when combined, sliced, or formatted. Isolating these behaviors early helps keep numeric reasoning clear while building your confidence with text handling.