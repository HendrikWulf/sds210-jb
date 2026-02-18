---
title: List Comprehension

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
A compact way to build lists
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/6_list-comprehension.ipynb)

```{admonition} Big idea
:class: tip

List comprehension is a **compact loop pattern**.

It combines:
- iteration  
- optional filtering  
- optional transformation  

into a single readable expression.
````

List comprehension does **not** introduce new logic.
It repackages patterns you already understand
into a shorter and often clearer form.

---

## 1. Why list comprehension exists

### From loops to patterns

So far, you have created new lists using:

* a `for` loop
* an empty list
* repeated calls to `.append()`

This pattern is correct and explicit.

```python
values = [1, 2, 3, 4, 5]
even_values = []

for v in values:
    if v % 2 == 0:
        even_values.append(v)
```

List comprehension exists because this pattern is **very common**.

---

### A refinement, not a replacement

List comprehension:

* does not replace `for` loops
* does not introduce new behaviour
* only shortens a well-understood pattern

You should always be able to rewrite a list comprehension
as a normal `for` loop.

---

## 2. The basic structure

### One loop in one expression

The simplest form is:

```python
[new_value for item in collection]
```

Example:

```python
values = [2, 4, 6]
squared = [v ** 2 for v in values]
```

This reads as:

> Create a new list by taking each value
> squaring it, and storing the result.

---

### Relation to a for loop

The following two blocks are equivalent:

```python
cubed = []
for v in values:
    cubed.append(v ** 3)
```

```python
cubed = [v ** 3 for v in values]
```

The logic is the same.
Only the **form** is different.

---

## 3. Filtering values with conditions

### Adding an if clause

List comprehensions can include a condition:

```python
[new_value for item in collection if condition]
```

Example:

```python
values = [1, 2, 3, 4, 5]
even_values = [v for v in values if v % 2 == 0]
```

Only values that satisfy the condition
are included in the new list.

---

### Example: valid measurements

```python
temperatures = [3, -5, 7, 42, 9]
valid = [t for t in temperatures if -20 <= t <= 40]
```

This expresses a **data quality filter** in one line.

---

```{admonition} Tip
:class: tip

Use list comprehension for  
**selecting values**, not for printing or side effects.
```

---

## 4. Transforming values

### Changing values while building the list

The expression part can modify values:

```python
values = [1, 2, 3]
doubled = [v * 2 for v in values]
```

---

### Example: unit conversion

```python
temperatures_c = [0, 5, 10, 15]
temperatures_k = [t + 273.15 for t in temperatures_c]
```

This is a clean way to express
a systematic transformation of data.

---

## 5. If–else inside list comprehension

### Conditional transformation

List comprehension can also express:

> If condition is true, use one value
> otherwise, use another value

```python
[new_value_if_true if condition else new_value_if_false
 for item in collection]
```

Example:

```python
values = [3, -1, 5, -2]
labels = ["valid" if v >= 0 else "invalid" for v in values]
```

---

### Readability rule

If the expression becomes hard to read,
prefer a normal `for` loop.

```{admonition} Attention
:class: attention

Shorter code is not better  
if it is harder to understand.
```

---

## 6. When to use list comprehension

### Good use cases

List comprehension works well when:

* building a new list
* applying a simple transformation
* filtering values
* logic fits comfortably on one line

---

### When not to use it

Avoid list comprehension when:

* the logic is complex
* multiple actions are needed
* readability suffers

In those cases, use a normal `for` loop.

---

## 7. Exercises


The following exercises help you practice **reading, writing, and deciding**
when list comprehension is appropriate.

Focus on **clarity first**, compactness second.

---

### Exercise 1: Rewrite a loop as list comprehension

You are given the following loop:

```python
rainfall = [0, 5, 12, 0, 8, 20]
non_zero = []

for r in rainfall:
    if r > 0:
        non_zero.append(r)
```

Rewrite this using **one list comprehension**.

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
rainfall = [0, 5, 12, 0, 8, 20]
non_zero = [r for r in rainfall if r > 0]
```

**Explanation:**

- the loop iterates over values  
- the condition filters values  
- the result is a new list  
````

---

### Exercise 2: Transform values with context

You are working with elevation values in meters:

```python
elevation_m = [450, 1200, 50, 3200]
```

Create a new list that converts these values to **kilometres**
and rounds them to **one decimal place**.

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
elevation_m = [450, 1200, 50, 3200]
elevation_km = [round(e / 1000, 1) for e in elevation_m]
```

**Explanation:**

- the expression transforms each value  
- the loop structure is implicit  
- the result is clean and readable  
````

---

### Exercise 3: Classify measurements

Given temperature measurements:

```python
temperatures = [-5, 3, 18, -12, 25]
```

Create a list of labels:

* `"cold"` for values below `0`
* `"warm"` for values `0` or above

Use **one list comprehension with if–else**.

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
temperatures = [-5, 3, 18, -12, 25]
labels = ["cold" if t < 0 else "warm" for t in temperatures]
```

**Explanation:**

- the condition decides the output value  
- every input value produces exactly one label  
````

---

```{admonition} Tip
:class: tip

If you struggle to read a list comprehension,
rewrite it as a normal `for` loop first.
```

---

## 8. Summary 

### Key ideas

* List comprehension is a **compact loop pattern**
* It combines looping, filtering, and transformation
* It depends on full understanding of loops and conditions
* It improves clarity **only when used carefully**

---

### Choosing the right loop

```text
for loop  → “Repeat for each value”
while loop → “Repeat until a condition changes”
list comprehension → “Build a new list from existing data”
```

---

### What comes next

In the upcoming **practical exercises**, you will:

* combine loops, conditions, and list comprehension
* process small environmental datasets
* detect invalid values and thresholds
* prepare data structures for later analysis