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

Operators allow you to combine values into expressions.  
Expressions are evaluated when code is executed and produce new values.
```

So far, you have learned how to store values in variables, how to name them clearly, and how Python distinguishes between different data types.

In this section, we focus on **how values interact**.
We start with simple calculations, then build up to comparisons, logic, and function based expressions.

---

## 1. Expressions as Calculations

An **expression** is a combination of values and operators that produces a result.

In Python, expressions are evaluated when code is **executed**.  
This makes Python usable as a simple calculator and as a language for building more complex calculations.

---

### A First Mental Model

Think of an expression as a question you ask Python:

> What is the result of this calculation right now?

For example:

```python
1 + 1
```

```python
5 * 7
```

When you run the cell, Python evaluates the expression and returns the result.

---

### Expressions Are Evaluated at Execution Time

An important idea is that expressions are not evaluated when you write them, but **when you run the cell**.

If you change an expression and run the cell again, Python recalculates the result.

```python
10 / 2
```

If you edit this to `10 / 4` and re run the cell, the result changes accordingly.

This behaviour is fundamental for working with variables later on.

---

```{admonition} Note
:class: note

Python does not remember expressions.  
It only evaluates them and returns a value.

If you want to keep a result, you must store it in a variable.
```

Next, we will look at **arithmetic operators** and how they are used inside expressions.

---

## 2. Arithmetic Operators

Arithmetic operators allow you to perform **calculations with numeric values**.
They are used inside expressions to combine values and produce new results.

At this stage, we focus only on **numeric operations**.

---

### Basic Arithmetic

Python supports the common arithmetic operators you already know.

```python
2 + 2
```

```python
5 - 3
```

```python
4 * 6
```

```python
10 / 2
```

Each expression is evaluated when the cell is executed and returns a numeric result.

---

### Using Variables as Operands

Arithmetic operators do not only work with literal numbers.
They also work with **variables that store numbers**.

```python
x = 7
y = 3
```

```python
x + y
```

```python
x * y
```

Here, `x` and `y` are **operands**.
An operand is simply a value or a variable that an operator acts on.

---

### Exponentiation

Python uses `**` to raise a value to a power.

```python
2 ** 3
```

This means two to the power of three.

---

### Optional but Useful Operators

Some additional arithmetic operators are useful in practice.

```python
7 % 3
```

The modulus operator returns the remainder of a division.

```python
7 // 3
```

Floor division returns the number of whole divisions.

You will encounter these operators later in loops, indexing, and data processing.

---

### Overview of Arithmetic Operators

| Operator | Meaning        | Example  | Result |
| :------: | -------------- | :------: | :----: |
|      `+` | addition       | `2 + 3`  | `5`    |
|      `-` | subtraction    | `5 - 2`  | `3`    |
|      `*` | multiplication | `4 * 6`  | `24`   |
|      `/` | division       | `10 / 2` | `5.0`  |
|     `**` | exponentiation | `2 ** 3` | `8`    |
|      `%` | remainder      | `7 % 3`  | `1`    |
|     `//` | floor division | `7 // 3` | `2`    |

---

```{admonition} Info
:class: info

Operators act on operands.

Operands can be:
- literal values such as `3` or `10`
- variables that store numeric values

The data type of the operands determines whether an operation is allowed.
```

Arithmetic operators are the basis for all numeric work in Python.
Next, we will look at **assignment and comparison operators**, which allow us to store results and compare values.

---

## 3. Assignment and Update Operators

So far, we have used expressions to **compute values**.
Now we look at how those results are **stored and updated** using assignment operators.

This section connects operators back to variables.

---

### Assignment with `=`

The assignment operator `=` stores the result of an expression in a variable.

```python
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

```python
y = 2 + 3
```

```python
y
```

The expression `2 + 3` is evaluated first.
Only the resulting value is stored.

Python does not remember how the value was computed.

---

### Update Operators as Shorthand

Python provides **update operators** that combine calculation and assignment.

```python
x += 3
```

This is a shorter way of writing:

```python
x = x + 3
```

Other common update operators follow the same pattern.

```python
x -= 1
```

```python
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

```python
speed = 50
speed = 80
```

After the second line, `speed` refers only to `80`.
The value `50` is no longer stored anywhere.

---

```{admonition} Note
:class: note

Update operators are only shorthand.
They simply replace the stored value with a new one.
```

---

## 4. Comparison Operators

Comparison operators allow you to **compare values**.
Instead of producing numbers, comparisons produce **logical results**.

These results are boolean values: `True` or `False`.

---

### Equality and Inequality

The equality operator `==` checks whether two values are equal.

```python
3 == 3
```

```python
3 == 5
```

The inequality operator `!=` checks whether two values are different.

```python
3 != 5
```

---

### Greater Than and Less Than

You can compare numeric values using relational operators.

```python
5 > 3
```

```python
2 < 1
```

You can also use combinations such as `greater than or equal` to.

```python
5 >= 5
```

```python
4 <= 3
```

---

### Using Variables in Comparisons

Comparisons work the same way with variables.

```python
x = 7
y = 3
```

```python
x > y
```

```python
x == 3
```

The values stored in the variables are substituted into the comparison when it is evaluated.

---

### What Comparisons Return

Every comparison expression returns a boolean value.

```python
result = x > y
result
```

Important points to remember:

* comparisons produce `True` or `False`
* comparisons do not change variable values
* variables keep their original values after a comparison

---

### Data Types Matter

Comparisons depend on data types.

```python
5 == "5"
```

Although the values look similar, the comparison returns `False` because the data types are different.

---

```{admonition} Info
:class: info

Comparison operators describe relationships between values.

They do not perform calculations.
They do not modify data.
They only answer yes or no questions.
```

Comparison operators are used to control program flow, filter data and make decisions based on conditions.
In the next section, we will combine comparison results using **logical operators**.

---

## 5. Logical Operators

Logical operators allow you to **combine comparison results**.
They work with boolean values and always return a boolean result.

This makes it possible to express more complex conditions in a clear way.

---

### The Three Logical Operators

Python provides three logical operators:

* `and`
* `or`
* `not`

Each of them works on boolean values.

---

### Using `and`

The operator `and` returns `True` only if **both conditions are true**.

```python
x = 7
```

```python
x > 5 and x < 10
```

If one of the conditions is false, the result is `False`.

```python
x > 5 and x < 6
```

---

### Using `or`

The operator `or` returns `True` if **at least one condition is true**.

```python
x < 5 or x > 10
```

```python
x < 5 or x > 6
```

---

### Using `not`

The operator `not` **reverses** a boolean value.

```python
not (x > 5)
```

```python
not (x < 5)
```

---

### Combining Expressions

Logical operators are typically used together with comparisons.

```python
(x > 5 and x < 10) or x == 20
```

Even though the expression looks complex, the result is still a single boolean value.

---

### What Logical Operators Return

Important points to remember:

* logical operators work on boolean values
* results are always `True` or `False`
* values stored in variables are not modified

---

```{admonition} Note
:class: note

Logical operators allow you to express reasoning in code.
Instead of asking one question, you can combine several and get a single clear answer.
They are essential for filtering data, defining conditions and making decisions in code.
```

Next, we will look at how operator behaviour can change depending on **data types**.

---

## 6. Operator Behaviour & Data Types

Operators do not behave the same way for all data types.
What an operator does depends on **what kind of values** it is applied to.

This section connects operators back to data types and explains why some results are expected while others raise errors.

---

### Numbers and Arithmetic

When operators are applied to numbers, Python performs arithmetic.

```python
2 + 3
```

```python
4 * 5
```

The result is a numeric value, based on mathematical rules.

---

### Strings and Concatenation

When the same operator is applied to strings, the behaviour can change.

```python
"Hot" + "Cold"
```

Here, the `+` operator **joins strings together** instead of adding numbers.

This is called `string concatenation`.

---

### Repeating Strings with Numbers

Some operations work only in one direction.

```python
"Hot" * 3
```

This repeats the string.

However, reversing the operands does not work.

```python
3 * "Hot"
```

The data types and their order matter.

---

### Operations That Fail

Some combinations are not defined at all.

```python
2 + "Hot"
```

Python raises a `TypeError` because adding a number and a string does not make sense.

This is not a bug.
It is Python protecting you from an undefined operation.

---

### Making Behaviour Predictable

The key idea is:

* operators are defined for specific data type combinations
* the same symbol can behave differently depending on the data types
* errors often mean that data types are incompatible

---

```{admonition} Note
:class: note

When an operation fails, check the data types of the values involved.
Once you know the data types, the behaviour of operators becomes predictable.
```

Next, we will look at how **functions** can be used inside expressions and combined with operators.

---

## 7. Using Functions in Expressions

So far, expressions have combined **values and operators**.
Python also allows you to use **functions inside expressions**.

Functions extend what expressions can do, while keeping the same mental model.

---

### Importing a Module

Some functions are not available by default and need to be imported from a module.

For mathematical functions, Python provides the `math` module.

```python
import math
```

Once imported, the functions in the module are available for use.

---

### Calling Functions

A function is called by writing its name followed by parentheses.

```python
math.sqrt(4)
```

```python
math.sin(3)
```

When a function is called, it:

* takes input values
* performs a calculation
* returns a result

---

### Using Constants

Modules can also provide constant values.

```python
math.pi
```

Constants are values, not functions, so they do not use parentheses.

---

### Functions Behave Like Values

The key idea is that **functions return values**.

This means the result of a function call can be used just like any other value.

```python
math.sqrt(4) + 2
```

```python
2 * math.sin(1)
```

---

### Nesting Expressions

Expressions can be nested by combining functions, operators, and values.

```python
math.sqrt(2 + 2)
```

```python
math.sin(math.pi / 2)
```

Python evaluates the inner expressions first, then works outward.

---

```{admonition} Note
:class: note

A function call is just another expression.
Once evaluated, the returned value behaves exactly like a number, string, or boolean.

Using functions inside expressions allows you to perform more complex calculations and build powerful logic from simple pieces.
```

Next, we will focus on **printing and inspecting expression results**, which helps you understand and debug your code.

---

## 8. Inspecting Expression Results

Expressions often produce values that you want to **see and check**.
Printing results makes calculations visible and helps you understand what your code is doing.

This is a normal and important part of programming.

---

### Printing Expression Results

You can print the result of any expression using the `print()` function.

```python
print(2 + 2)
```

```python
print(math.sqrt(9))
```

The expression is evaluated first, and the result is then printed to the screen.

---

### Combining Text and Results

Printing becomes especially useful when you want to explain what a value represents.

```python
print("The square root of 9 is", math.sqrt(9))
```

This makes output easier to read and interpret, especially when working with many values.

---

### Inspecting Intermediate Values

When expressions become more complex, it is often helpful to inspect intermediate results.

```python
x = 7
y = 3

print("x + y =", x + y)
print("x * y =", x * y)
```

This helps you verify that each part of a calculation behaves as expected.

---

### Printing as a Debugging Tool

Printing values is one of the simplest debugging techniques.

You can use it to:

* check whether a variable has the expected value
* verify intermediate steps in a calculation
* understand why a result looks wrong

This approach is especially useful when learning and experimenting.

---

### Improving Readability with Formatting

Well formatted output makes results easier to understand.

```python
value = math.pi
print("The value of pi is approximately", round(value, 3))
```

Clear output supports both debugging and communication with others.

---

```{admonition} Note
:class: note

Printing is not only for final results.
It is a tool for thinking, checking, and understanding what your code is doing at each step.

Being able to inspect expression results helps you build confidence in your calculations and find and fix mistakes quickly.
```

---

## 9. Short Exercises

### Exercise 1: Expressions as Calculations

**Focus:** understanding expressions and execution  
**Difficulty:** easy

#### Task

1. Write three different arithmetic expressions:

   * one using addition
   * one using multiplication
   * one using exponentiation
2. Run each expression in its own code cell and observe the output.
3. Change one number in each expression and re-run the cell.

#### Questions to think about

* When is the expression evaluated?
* Does Python remember the expression or only the result?
* What happens if you change the code but do not re-run the cell?

```python
# Simple arithmetic expressions

# After changing one number and re-running the cell

```

````{admonition} Sample solution (click to compare with your results)
:class: dropdown

```{code-cell} python
# Simple arithmetic expressions

2 + 3        # addition
```

```{code-cell} python
4 * 5        # multiplication
```

```{code-cell} python
2 ** 3       # exponentiation
```

```{code-cell} python
# After changing one number and re-running the cell

2 + 10
```

```{code-cell} python
4 * 6
```

```{code-cell} python
2 ** 4
```

**Explanation**

* Each line is an expression.
* Python evaluates the expression only when the cell is executed.
* Python does not remember the expression itself, only the result.
* Changing the code has no effect until the cell is run again.

````

---

### Exercise 2: Operators, Variables, and Data Types

**Focus:** variables, arithmetic, comparisons, data types  
**Difficulty:** medium

#### Task

You are given the following variables:

```python
distance_km = 180
time_hours = 2.5
```

1. Compute the average speed in km per hour and store it in a new variable.
2. Check whether the speed is greater than 70 km per hour.
3. Print a readable message that includes:

   * the computed speed
   * the result of the comparison

``` python
# The average speed is … km/h. Speed above 70 km/h: …
```

#### Questions to think about

* Which expressions produce numbers and which produce booleans?
* What data types are involved in each step?
* What changes if you update `time_hours` and re-run the calculations?

````{admonition} Sample solution (click to compare with your results)
:class: dropdown

```{code-cell} python
# Given values
distance_km = 180
time_hours = 2.5
```

```{code-cell} python
# Compute average speed
speed_kmh = distance_km / time_hours
speed_kmh
```

```{code-cell} python
# Comparison produces a boolean
speed_above_70 = speed_kmh > 70
speed_above_70
```

```{code-cell} python
# Print a readable message
print(
    "The average speed is",
    speed_kmh,
    "km/h. Speed above 70 km/h:",
    speed_above_70,
)
```

**Explanation**

* The division expression produces a numeric value (`float`).
* The comparison expression produces a boolean (`True` or `False`).
* Printing does not change values, it only makes results visible.
* If `time_hours` is updated and the cells are re-run, all dependent results change.

````

---

### Exercise 3: Combining Comparisons, Logic, and Functions (challenge)

**Focus:** logical operators, functions, nested expressions  
**Difficulty:** higher

#### Task

1. Import the `math` module.
2. Define a variable `angle_deg` with a value in degrees.
3. Convert the angle to radians using `math.pi`.
4. Compute the sine of the angle.
5. Check whether the sine value is:

   * greater than 0
   * smaller than 1
6. Combine both checks using a logical operator.
7. Print a clear message that shows:

   * the sine value
   * the result of the combined logical expression

#### Questions to think about

* Which parts of your code are expressions?
* Which expressions are nested inside others?
* Why does the final result still reduce to a single boolean value?

````{admonition} Sample solution (click to compare with your results)
:class: dropdown

```{code-cell} python
import math
```

```{code-cell} python
# Define angle in degrees
angle_deg = 30
```

```{code-cell} python
# Convert degrees to radians
angle_rad = angle_deg * math.pi / 180
angle_rad
```

```{code-cell} python
# Compute sine of the angle
sin_value = math.sin(angle_rad)
sin_value
```

```{code-cell} python
# Logical checks
greater_than_zero = sin_value > 0
less_than_one = sin_value < 1
```

```{code-cell} python
# Combine conditions
valid_range = greater_than_zero and less_than_one
valid_range
```

```{code-cell} python
# Print result
print(
    "Sine value:",
    sin_value,
    "| In valid range (0 < sin < 1):",
    valid_range,
)
````

---

## 10. Summary

After completing this section, you should understand that:

* **expressions combine values and operators**
* expressions always produce a result
* **expressions are evaluated when code is executed**
* arithmetic operators work with numeric values
* comparison and logical operators produce boolean values
* operator behaviour depends on data types
* functions return values that can be used in expressions

Together, these ideas explain how Python works with values and how results are created step by step.

---

### Looking Ahead

Expressions are the foundation for making decisions in code.

In the next section, you will learn about **strings and basic string operations**.
Strings behave differently from numbers, especially when combined, repeated, or formatted.

Isolating these behaviours early helps keep numeric reasoning clear while building confidence with text handling.