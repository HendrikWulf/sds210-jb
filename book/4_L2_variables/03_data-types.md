---
title: Data Types

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
What Kind of Values Variables Can Store
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/03_data-types.ipynb)


```{admonition} Big idea
:class: tip

Variables store values.  
**Data types** describe what kind of values those are and what operations make sense for them.

While variables hold values in memory, data types determine how Python interprets those values when they are used in expressions and calculations.
```

In this section, you will learn how Python classifies values, how to inspect their data types, and how data types explain both successful operations and common errors.

Understanding data types is essential for debugging and for writing code that behaves predictably.
These ideas will form a foundation for calculations, comparisons, and logical decisions later in the course.

---

## 1. What Is a Data Type?

**Learning focus:** mental model

A **data type** describes what kind of value a variable stores.  
It also defines how that value behaves when Python uses it in expressions or calculations.

Every variable in Python has a data type, even if you do not specify it explicitly.  
The data type controls two important things:

* which operations are allowed  
* how Python interprets an expression  

This explains why some lines of code work as expected while others fail, even if the syntax looks correct.

Think of the data type as the *role* of a value.  
The same symbol can behave very differently depending on what type of value it represents.

For example, text behaves differently from numbers.

```python
weather_forecast = "Hot"
```

Here, the variable stores **text**, not a number.
Because of this, Python will treat the value as a word rather than something that can be used in calculations.

You do not need to memorize all data types yet.
The key idea is this:

> Variables store values.
> Data types define how those values behave.

In the next sections, we will look at common data types and see how Python reacts when we combine them.

---

## 2. The Four Basic Data Types in Python

Python provides several data types, but we begin with the **four basic types** that store **single values**.

| Data type name | Description               | Example |
|---------------|---------------------------|---------|
| `int`         | Whole integer values      | `4`     |
| `float`       | Decimal values            | `3.1415`|
| `str`         | Character strings         | `'Hot'` |
| `bool`        | True or false values      | `True`  |

These types are often called *primitive* data types.  
They represent individual values rather than collections of values.

At this stage, your goal is to **recognise** them when you see them in code:

* identify the type of a value  
* understand what kind of information it represents  
* develop an intuition for typical use cases  

Do not worry yet about all possible operations.  
Those will come later.

---

### 2.1 Integers (int)

Integers are **whole numbers**.  
They do not contain a decimal point.

They are commonly used for:

* counts  
* indices  
* IDs  
* quantities that must be exact  

Example:

```python
num_points = 120
```

The value `120` is a whole number, so Python assigns it the data type `int`.

---

### 2.2 Floating Point Numbers (float)

Floating point numbers represent **decimal values**.
They can store numbers with a fractional part.

Typical uses include:

* measurements
* coordinates
* temperatures
* calculated values

Example:

```python
temp_celsius = 37.6
```

Because the value contains a decimal point, Python interprets it as a `float`.

---

### 2.3 Strings (str)

Strings represent **text data**.
They are written inside quotation marks.

Strings are often used for:

* labels
* names
* categories
* metadata and descriptions

Example:

```python
weather_forecast = "Hot"
```

Even though `"Hot"` looks simple, Python treats it as text, not as a value that can be used in calculations.

---

### 2.4 Booleans (bool)

Booleans represent **logical values**.
They can only have one of two values: `True` or `False`.

Typical uses include:

* flags
* conditions
* yes or no states
* on or off decisions

Example:

```python
is_georeferenced = True
```

Booleans are especially important when making decisions in code, which you will explore later.

---

At this point, focus on **recognition**:

* Is the value a number or text?
* Does it include a decimal point?
* Does it represent a logical state?

In the next section, we will learn how to check the data type of a variable directly in Python.

---

## 3. Checking Data Types with `type()`

**Learning focus:** inspection and debugging

When working with variables, it is often not obvious what data type a value has.  
This is especially true once values come from calculations, user input, or data files.

Python provides a simple diagnostic tool for this purpose: the `type()` function.

The function does not change a variable.  
It only **inspects** it and reports how Python interprets the stored value.

Here is a first example:

```python
type(weather_forecast)
```

Python returns the data type of the variable.
In this case, it tells us that `weather_forecast` is a string.

Now compare this with a numeric value:

```python
type(temp_celsius)
```

Even though both variables may look simple, Python treats them very differently because their data types are different.

Checking the data type is especially useful when:

* a calculation does not work as expected
* Python raises an error message
* a result looks strange or unexpected

In many cases, the **first step in debugging** is to ask:

> What data type does this variable actually have?

Understanding the data type often explains why an operation works, fails, or behaves in an unexpected way.

In the next section, we will see what happens when incompatible data types are used together.

---

## 4. Mismatch of Data Types: `TypeError`

**Learning focus:** controlled failure

Not all operations are allowed for all data types.  
When Python encounters an operation that is not defined for the given types, it refuses to execute it.

Consider the following expression:

```python
temp_celsius + weather_forecast
```

At first glance, this may look harmless.
However, `temp_celsius` is a number, while `weather_forecast` is text.

Python tries to interpret what the `+` operation should mean here and then stops.

It raises a **TypeError**.

This error tells you something important:

* the operation is not defined for these data types
* numbers and strings behave differently
* Python will not guess what you meant

A `TypeError` is not a mistake you should fear.
It is Python being precise and protective.

Think of it as Python saying:

> I know what addition means for numbers.
> I know what it means for text.
> But I do not know what it means for this combination.

Errors like this are **informative**, not bad.
They help you understand how Python interprets your code.

In practice, encountering a `TypeError` often means you should check:

* the data type of each variable
* whether the operation makes sense for those types

In the next section, you will learn how to make different data types work together when needed.

---

## 5. What Works with Strings?

**Learning focus:** exploration, not rules

Before learning formal rules, it is useful to **observe what Python actually does**.  
In this short exploration, you will try a few operations with strings and see what happens.

Start by defining two string variables:

```python
a = "Hot"
b = "Cold"
```

Now try the following operations **one at a time** and observe the result.

### Add two strings

```python
a + b
```

Look closely at the output.
What happened to the two words?

---

### Subtract two strings

```python
a - b
```

Does Python allow this operation?
If not, what kind of message do you get?

---

### Multiply a string by a number

```python
a * 3
```

This one may be surprising.
Observe the result carefully.

---

At this stage, do not try to memorise rules.
Instead, focus on **patterns**:

* some operations work
* some do not
* Python is consistent in how it behaves

This kind of small experiment helps build confidence and intuition.
It also mirrors earlier exercises where you defined your own variables and explored what Python allows.

In the next section, we will summarise what these observations tell us about data types and operations.

---

## 6. Combining Different Data Types

**Learning focus:** compatibility

Different data types are not automatically compatible, but they can often be made compatible.

Before fixing a problem, it is important to **inspect** what you are working with.  
This means checking data types before trying to change anything.

Consider the following realistic example:

```python
forecast_bahnhofstrasse = "39.0"
```

At first glance, this value looks like a number.
However, it is stored as **text**.

The first step is inspection:

```python
type(forecast_bahnhofstrasse)
```

Python tells us that the variable is a string.
This explains why we cannot use it directly in numeric calculations.

Now imagine we want to compare this value with a temperature stored as a number.
Before doing anything else, we check the data types involved.

Inspection comes **before** fixing.

This sequence is important:

* observe the value  
* check the data type  
* decide what needs to change

Once you understand what each variable represents, you can make them compatible by converting one data type into another.

At this stage, the key idea is not how to convert yet, but **why** conversion is needed.

In the next section, you will learn how to convert values between data types safely and intentionally.

---

## 7. Converting Data Types

**Learning focus:** explicit control

Sometimes values have the *right information* but the *wrong data type*.  
In these cases, Python does not guess what you want to do.  
You must tell it explicitly.

This is called **type casting**.

Type casting creates a **new value** with a different data type.  
The original variable is not changed unless you assign the result back to it.

---

### 7.1 Converting to `float()`

Recall the earlier example:

```python
forecast_bahnhofstrasse = "39.0"
```

The value looks numeric, but it is stored as text.
To use it in calculations, we convert it explicitly:

```python
forecast_high = float(forecast_bahnhofstrasse)
```

Now inspect the result:

```python
type(forecast_high)
```

The value is now a floating point number.

Because the data types are compatible, we can reuse earlier variables and perform calculations:

```python
forecast_high - temp_celsius
```

This works because both values are numeric.

The key idea is:

> Conversion creates a **new value** of a different type.
> Python does nothing automatically unless you ask it to.

---

### 7.2 Converting to `int()` and a Subtle Pitfall

You can also convert numeric values to integers:

```python
temp_celsius_int = int(temp_celsius)
```

At first glance, this looks harmless.
However, something important happens.

If the original value contains a decimal part, Python **truncates** it.

This means:

* the decimal part is removed
* the value is **not rounded**

For example, `62.9` becomes `62`, not `63`.

This distinction matters, especially for scientific and spatial data:

* truncation can silently reduce precision
* small errors can accumulate
* results may look plausible but be wrong

Because of this, type conversion should always be a **conscious decision**.

Before converting, ask yourself:

* Do I want an exact value or an approximation?
* Is losing the decimal part acceptable here?

Understanding this pitfall early helps prevent subtle and hard to detect errors later on.

---

## 8. When Conversion Fails: `ValueError`

**Learning focus:** limits of conversion

Type conversion only works when the **content** of a value makes sense for the requested data type.

Consider this example:

```python
float("Cold")
```

Here, we explicitly ask Python to convert a string into a floating point number.
Python attempts the conversion and then stops.

It raises a **ValueError**.

This error means something different from a `TypeError`.

A `ValueError` tells you that:

* the conversion itself is allowed
* but the *value* does not make sense in this context

Not all strings represent numbers.
Only strings that contain numeric content, such as `"77.0"` or `"12"`, can be converted to numeric types.

Strings like `"Cold"` or `"Hot"` do not contain numeric information, so conversion fails.

You can think of a `ValueError` as Python saying:

> I understand what you want to do.
> But this value cannot be interpreted as that data type.

Like other errors, a `ValueError` is informative.
It points directly to a mismatch between **content** and **expected type**.

When you see a `ValueError`, it is often useful to check:

* what the value actually contains
* whether the conversion makes sense conceptually

In the next section, we will briefly summarise the key ideas from this chapter and connect them to practical debugging strategies.

---

## 9. Short Exercises

These exercises build on each other.  
Focus on understanding what Python does and *why*.

---

### Exercise 1: Recognising Data Types

Consider the following variables:

```python
a = 25
b = 25.0
c = "25"
d = False
```

1. For each variable, write down what data type you expect.
2. Use `type()` to check your answers.
3. Identify which variables *look similar* but behave differently.

Goal: build confidence in recognising basic data types.

````{admonition} Sample solution (click to expand)
:class: dropdown

### Exercise 1: Recognising Data Types

```{code-cell} python
a = 25
b = 25.0
c = "25"
d = False
```

Expected and confirmed data types:

```{code-cell} python
type(a)   # int
type(b)   # float
type(c)   # str
type(d)   # bool
```

Explanation:

* `a` is an integer because it is a whole number
* `b` is a float because it includes a decimal point
* `c` is a string because the value is enclosed in quotation marks
* `d` is a boolean because it represents a logical state

Variables `a`, `b`, and `c` may look similar, but they behave differently because their data types are different.

````

---

### Exercise 2: Inspection Before Fixing

You are given two variables:

```python
temp_celsius = 37.6
forecast_bahnhofstrasse = "39.0"
```

1. Check the data type of each variable.
2. Predict what will happen when you run:

```python
forecast_bahnhofstrasse - temp_celsius
```

3. Run the code and observe the error.
4. Explain in one or two sentences **why** Python refuses this operation.

Goal: practise inspection and interpretation of error messages.

````{admonition} Sample solution (click to expand)
:class: dropdown

### Exercise 2: Inspection Before Fixing

```{code-cell} python
temp_celsius = 37.6
forecast_bahnhofstrasse = "39.0"
```

Checking data types:

```{code-cell} python
type(temp_celsius)              # float
type(forecast_bahnhofstrasse)   # str
```

Running the operation:

```{code-cell} python
forecast_bahnhofstrasse - temp_celsius
```

Result:

Python raises a **TypeError**.

Explanation:

Python refuses this operation because subtraction is not defined between a string and a number.
Even though `"39.0"` looks like a number, it is stored as text and cannot be used directly in a calculation.

````
---

### Exercise 3: Making Values Compatible

Continue with the variables from Exercise 2.

1. Convert `forecast_bahnhofstrasse` into a numeric value.
2. Subtract `temp_celsius` from it.
3. Convert `temp_celsius` to an integer and inspect the result.

```python
forecast_bahnhof = float(forecast_bahnhofstrasse)
temp_celsius_int = int(temp_celsius)
```

4. Compare the values before and after conversion.
5. Explain why this difference could matter in scientific or spatial analysis.

Goal: understand explicit conversion and its consequences.

````{admonition} Sample solution (click to expand)
:class: dropdown

### Exercise 3: Making Values Compatible

Converting the string to a numeric value:

```{code-cell} python
forecast_bahnhof = float(forecast_bahnhofstrasse)
```

Now the subtraction works:

```{code-cell} python
forecast_bahnhof - temp_celsius
```

Converting the temperature to an integer:

```{code-cell} python
temp_celsius_int = int(temp_celsius)
```

Inspecting the result:

```{code-cell} python
temp_celsius        # 37.6
temp_celsius_int    # 37
```

Explanation:

* Converting to `float` creates a new numeric value that is compatible with calculations
* Converting to `int` **truncates** the decimal part rather than rounding

This matters in scientific and spatial analysis because truncation can reduce precision and introduce small but significant errors.

Key takeaway:

Type conversion gives you control, but it also carries responsibility.

````

---

You are now ready to summarise what data types are, how Python uses them, and how they affect calculations and errors.

---

## 10. Summary

This section introduced the idea of **data types** and why they matter when writing and reading Python code.

At this point, you should understand the following core ideas.

Every variable has a data type.  
Even if you do not specify it explicitly, Python assigns one based on the stored value.

Data types control which operations are allowed.  
They determine how Python interprets expressions and why some combinations work while others do not.

The `type()` function helps diagnose problems.  
When something behaves unexpectedly, checking the data type is often the first useful step.

Incompatible data types cause a `TypeError`.  
This happens when an operation is not defined for the given combination of types.

Explicit conversion can make values compatible.  
Functions like `float()` and `int()` allow you to control how values are interpreted.

Conversion may change values in unexpected ways.  
Truncation and loss of precision are common pitfalls, especially in scientific contexts.

Taken together, these ideas form a foundation for writing robust and understandable code.  
They also provide a practical strategy for debugging problems as they arise.

---

### What Comes Next

So far, you have focused on **what values are** and **how Python understands them**.  
The next step is to focus on **what you can do with those values**.

In the next section, you will build on this foundation by applying data types in more complex expressions and operations.
Understanding operators and expressions will let you move from *storing values* to *doing things with values*, which is the core of programming.