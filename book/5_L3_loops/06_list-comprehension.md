---
title: List Comprehension

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
A compact way to build lists
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/06_list-comprehension.ipynb)

```{admonition} Big idea
:class: tip

List comprehension is a **compact loop pattern**.

It combines:
- iteration (looping)
- optional filtering (`if`)
- optional transformation (math/logic)

...into a single, readable line of code.

```

List comprehension does **not** introduce new logic to Python. It simply repackages patterns you already understand into a shorter, and often clearer, form.

---

## 1. Why list comprehension exists

### From boilerplate to patterns

So far, whenever you needed to create a new list based on an old list, you used the standard "append pattern":

1. Create an empty list
2. Start a `for` loop
3. Apply a condition or transformation
4. Append the new value to the list

```{code-cell} python
values = [1, 2, 3, 4, 5]
even_values = []

for v in values:
    if v % 2 == 0:
        even_values.append(v)

```

This pattern is correct, explicit, and used constantly. List comprehension exists specifically because this pattern is **so common** that Python created a shortcut for it.

### A refinement, not a replacement

List comprehension:

* does not replace `for` loops entirely
* does not introduce new computational behavior
* simply shortens a well-understood pattern

You should always be able to rewrite a list comprehension as a normal `for` loop, and vice versa.

---

## 2. The basic structure

### One loop in one expression

The simplest form of a list comprehension squashes the loop and the append action into a single line wrapped in square brackets `[]`.

```{code-cell} python
[new_value for item in collection]

```

:::{figure} images/09_list_comp_basic.png
:alt: Syntax breakdown of a basic list comprehension showing the expression, loop variable, and collection.
:width: 700px
:align: center

*Every list comprehension requires these three core parts wrapped in square brackets: the output expression, the loop variable, and the collection to iterate over.*
:::

Example:

```{code-cell} python
values = [2, 4, 6]
squared = [v ** 2 for v in values]

```

To read this easily, read the middle first, then the left:

> "For every `v` in `values`, take `v ** 2` and put it in a new list."

### Relation to a for loop

The following two blocks do the exact same thing:

```{code-cell} python
# Standard Loop
cubed = []
for v in values:
    cubed.append(v ** 3)

```

```{code-cell} python
# List Comprehension
cubed = [v ** 3 for v in values]

```

The logic is identical. Only the **form** is different.

---

## 3. Filtering values with conditions

### Adding an if clause at the end

List comprehensions can also include a condition to filter out unwanted data. When filtering, the `if` statement goes at the **very end** of the expression.

```{code-cell} python
[new_value for item in collection if condition]

```

:::{figure} images/10_list_comp_filtering.png
:alt: Syntax breakdown of a list comprehension with an if-condition at the end for filtering.
:width: 700px
:align: center

*When filtering data, the `if` condition always acts as a gatekeeper at the very end of the expression.*
:::

Example:

```{code-cell} python
values = [1, 2, 3, 4, 5]
even_values = [v for v in values if v % 2 == 0]

```

Only values that satisfy the condition (`v % 2 == 0`) are allowed into the new list.

### Example: Valid environmental measurements

```{code-cell} python
temperatures = [3, -5, 7, 42, 9]
valid = [t for t in temperatures if -20 <= t <= 40]

```

This expresses a **data quality filter** cleanly in just one line.

```{admonition} Tip
:class: tip

Use list comprehensions strictly for **building new lists**, not for printing or executing side effects.

```

---

## 4. Transforming values

### Changing values while building the list

The "expression" part at the front of the list comprehension doesn't just have to be the variable itself; it can be a mathematical transformation.

```{code-cell} python
values = [1, 2, 3]
doubled = [v * 2 for v in values]

```

### Example: Unit conversion

```{code-cell} python
temperatures_c = [0, 5, 10, 15]
temperatures_k = [t + 273.15 for t in temperatures_c]

```

This is a clean, Pythonic way to express a systematic transformation of spatial or environmental data.

---

## 5. If–else inside list comprehension

### Conditional transformation (Choosing between two values)

Sometimes you don't want to drop a value completely (filtering), but rather change it based on a condition.

If you need an `if-else` decision, the syntax changes. The entire `if-else` block must move to the **beginning** of the comprehension, before the `for` loop.

```{code-cell} python
[value_if_true if condition else value_if_false for item in collection]

```

:::{figure} images/11_list_comp_ifelse.png
:alt: Syntax breakdown of a list comprehension showing an if-else conditional expression placed at the beginning before the for loop.
:width: 700px
:align: center

*When transforming data conditionally, the entire `if-else` logic becomes the "output expression" and must be placed at the very beginning of the brackets.*
:::

Example:

```{code-cell} python
values = [3, -1, 5, -2]
labels = ["valid" if v >= 0 else "invalid" for v in values]
# Output: ['valid', 'invalid', 'valid', 'invalid']

```

Read this as:

> "Put 'valid' if `v` is >= 0, else put 'invalid'... do this for every `v` in `values`."

### Readability rule

The syntax for `if-else` inside a list comprehension can get visually messy very quickly.

```{admonition} Understanding matters
:class: attention

Shorter code is **not** better if it is harder to understand. If a list comprehension becomes too long or complex, rewrite it as a standard `for` loop!

```

---

## 6. When to use list comprehension

### Good use cases

List comprehensions work beautifully when:

* building a new list from an old one
* applying a simple mathematical transformation
* filtering values based on a single condition
* the logic fits comfortably and readably on one line

### When not to use it

Avoid list comprehension when:

* the logic involves complex nested loops
* you need multiple `elif` conditions
* you are updating external variables or printing
* readability suffers

In those cases, stick to a normal `for` loop.

---

## 7. Exercises

The following exercises help you practice **reading, writing, and deciding**
when list comprehension is appropriate.

Focus on **clarity first**, compactness second.

---

### Exercise 1: Rewrite a loop as list comprehension

You are given the following loop:

```{code-cell} python
rainfall = [0, 5, 12, 0, 8, 20]
non_zero = []

for r in rainfall:
    if r > 0:
        non_zero.append(r)
```

Rewrite this using **one list comprehension**.

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

```{code-cell} python
elevation_m = [450, 1200, 50, 3200]
```

Create a new list that converts these values to kilometres and rounds them to one decimal place. 
You can use Python's built-in `round()` function for this, which takes the number to round and the desired number of decimal places (e.g., `round(value, 1)`).



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

```{code-cell} python
temperatures = [-5, 3, 18, -12, 25]
```

Create a list of labels:

* `"cold"` for values below `0`
* `"warm"` for values `0` or above

Use **one list comprehension with if–else**.



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

* List comprehension is a **compact loop pattern** used strictly for building new lists.
* It combines looping, filtering, and transformation into one line.
* The `if` goes at the **end** when filtering data.
* The `if-else` goes at the **beginning** when transforming data conditionally.
* It improves clarity **only when used carefully**. If it is hard to read, use a standard loop.

---

### Choosing the right loop

```text
for loop           → “Repeat an action for each value.”
while loop         → “Repeat an action until a condition changes.”
list comprehension → “Build a new list from existing data.”

```

---

### What comes next

In the upcoming **practical exercises**, you will combine everything from this module to:

* process small environmental datasets using loops and conditions
* detect invalid values and thresholds
* write clean, Pythonic data structures for later analysis
