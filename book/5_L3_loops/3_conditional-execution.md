---
title: Conditional Statements

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Choosing what happens
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/3_conditional-execution.ipynb)

```{admonition} Big idea
:class: tip

Loops repeat actions.  
Conditions decide **what happens** for each value.

Together, they allow code to react to data.
```

So far, every loop has executed the **same instructions** for every value.

Now we take the next step:

> We still repeat actions,
> but we allow different behaviour depending on the value.

---

## 1. Conditions as questions

### When repetition needs decisions

A condition is a question that can be answered with **yes or no**.

In Python, these answers are represented by the Boolean values:

* `True`
* `False`

When conditions are used inside a loop,
they allow the program to decide
what to do for **each individual value**.

The loop still repeats,
but the behaviour can change from one value to the next.

---

### Reading conditions in plain language

Conditions are easiest to understand
when you read them as questions:

* Is this value greater than 10?
* Is this city contained in the list of capitals?
* Is this index equal to zero?

Each condition controls whether
a specific block of code is executed.

---

```{admonition} Note
:class: note

Conditions do not stop loops.  
They control **what happens during** each repetition.
```

---

## 2. Operators for evaluating conditions

### Comparison operators

Comparison operators are used to compare two values.

:::{table} Comparison operators in Python
| Operator | Description               | Comparison example     | Result |
|:--------:|---------------------------|------------------------|:------:|
| `==`     | Equal to                  | `"apples" == "oranges"`| False  |
| `!=`     | Not equal to              | `"apples" != "oranges"`| True   |
| `<`      | Less than                 | `2 < 1`                | False  |
| `>`      | Greater than              | `2 > 1`                | True   |
| `<=`     | Less than or equal to     | `2 <= 2`               | True   |
| `>=`     | Greater than or equal to  | `2 >= 4`               | False  |
:::

Each comparison produces a Boolean result:
either `True` or `False`.

These operators are the most common way
to express conditions in code.

---

### Identity operators

Identity operators check whether two variables refer to the **same object**,
not just whether they contain the same value.

```python
a is b
a is not b
```

Here is a conceptual example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
```

Now compare them:

```python
a is b
```

Result:

```text
True
```

Both `a` and `b` point to the **same list**.

```python
a is c
```

Result:

```text
False
```

Even though `a` and `c` contain the same values,
they are **different objects**.

---

```{admonition} Note
:class: note

Use `==` to compare values.  
Use `is` to check whether two names refer to the same object.
```

---

### Membership operators

Membership operators test whether a value exists
inside a collection.

```python
x in y
x not in y
```

These operators are especially useful
when working with lists and strings,
for example to check whether a value is part of a group.

---

Here is another example:

```python
cities = ["Lima", "Quito", "Bogotá"]
```

Check membership:

```python
"Lima" in cities
```

Result:

```text
True
```

```python
"Santiago" in cities
```

Result:

```text
False
```

Membership operators also work with strings:

```python
"a" in "data"
```

Result:

```text
True
```

---

```{admonition} Tip
:class: tip

Comparison checks values.  
Identity checks objects.  
Membership checks collections.
```

---

## 3. Logical operators (and, or, not)

### Combining conditions

Logical operators allow you to combine
**multiple conditions into a single decision**.

The three logical operators in Python are:

```python
and
or
not
```

They are often used inside loops
to make more precise decisions.

---

### Simple examples

Consider a numeric value:

```python
value = 42
```

```python
value > 0 and value < 100
```

Result:

```text
True
```

Both conditions must be true for the whole expression to be true.

---

Now consider membership:

```python
cities = ["Lima", "Quito", "Bogotá"]
capitals = ["Lima", "Buenos Aires"]
```

```python
"Quito" in cities or "Quito" in capitals
```

Result:

```text
True
```

Only one of the conditions needs to be true.

---

Using `not` reverses a condition:

```python
value = 0
not value == 0
```

Result:

```text
False
```

---

### Reading logic in words

It helps to read logical expressions aloud:

* `and` means **both conditions must be true**
* `or` means **at least one condition must be true**
* `not` means **the opposite of the condition**

For example:

> “The value is greater than zero **and** less than one hundred.”

---

### Parentheses and clarity

When combining several conditions,
use parentheses to make the logic clear.

```python
(a < b and b < c) or (a > b)
```

Parentheses:

* improve readability
* prevent mistakes
* make evaluation order explicit

They are recommended even when not strictly required.

---

```{admonition} Note
:class: note

If you have to pause to understand a condition,  
add parentheses or split it into simpler parts.
```

---

### Concept check

Predict the result without running the code:

```python
x = 5

(x > 3 and x < 10) or x == 0
```

---

```{admonition} True or False?
:class: dropdown

The result is `True`.

`x > 3` and `x < 10` are both true,
so the entire expression is true.
```

---

## 4. Conditional execution (if, elif, else)

### Choosing what happens

So far, conditions have been used as **questions**.
Now we use them to **choose between actions**.

Python provides three related keywords:

* `if` for a single decision
* `if … else …` for two alternative paths
* `if … elif … else …` for multiple paths

Only one path is executed.

---

### A single decision with if

Use `if` when you want code to run **only if a condition is true**.

```python
temperature = 5

if temperature > 0:
    print("Above freezing")
```

If the condition is false, nothing happens.
The program simply continues.

---

### Two paths with if and else

Use `else` when there are **exactly two outcomes**.

```python
temperature = -2

if temperature > 0:
    print("Above freezing")
else:
    print("Freezing or below")
```

Exactly one of the two blocks runs.

---

### Multiple paths with if, elif, and else

When more than two cases are possible,
use `elif` (else if).

Python checks conditions **from top to bottom**.
As soon as one condition is true, the rest are skipped.

```python
temperature = -3

if temperature > 0:
    print(f"{temperature} degrees Celsius is above freezing")
elif temperature == 0:
    print(f"{temperature} degrees Celsius is at the freezing point")
else:
    print(f"{temperature} degrees Celsius is below freezing")
```

Output:

```text
-3 degrees Celsius is below freezing
```

---

```{admonition} Note
:class: note

Only one branch of an if–elif–else chain runs.  
Order matters.
```

---

### Reading conditional chains

It helps to read the logic like a checklist:

1. Is the first condition true
2. If not, try the next one
3. If none match, use the fallback (`else`)

This makes conditional execution predictable and easy to debug.

---

### Concept check

Predict the output **before running the code**:

```python
yesterday = 14
today = 10
tomorrow = 13

if yesterday <= today:
    print("A")
elif today != tomorrow:
    print("B")
elif yesterday > tomorrow:
    print("C")
elif today == today:
    print("D")
```

---

````{admonition} Sample solution
:class: dropdown

The output is:

```

B

```

**Explanation:**

- `yesterday <= today` → False  
- `today != tomorrow` → True  

Python stops checking as soon as a condition is true.
The remaining conditions are ignored.
````

---

```{admonition} Tip
:class: tip

Write conditions in the order  
you want them to be checked.
```

---

## 5. Decisions inside loops

### Using if inside a loop

Conditions become most useful
when they are placed **inside loops**.

```python
values = [3, 12, 7, 25]

for v in values:
    if v > 10:
        print(v)
```

This loop still processes **every value** in the list.
However, only values that satisfy the condition are printed.

The loop controls *how often* the code runs.
The condition controls *what happens* for each value.

---

### Filtering values

**Filtering** means selecting some values
and ignoring the rest.

In the previous example, values greater than 10 are printed,
while smaller values are skipped.

Filtering is useful when you want to:

* select values above or below a threshold
* remove invalid or unwanted entries
* focus on a specific subset of data

---

### Transforming values

**Transforming** means changing values
depending on a condition.

```python
for v in values:
    if v > 10:
        print(v * 2)
    else:
        print(v)
```

Here:

* values greater than 10 are doubled
* other values are printed unchanged

Every value produces output,
but the output depends on the condition.

---

```{admonition} Note
:class: note

Filtering decides **which values** are used.  
Transforming decides **how values change**.
```

---

### A small prediction check

Before running the code, predict the output:

```python
values = [5, 15, 8]

for v in values:
    if v > 10:
        print(v + 1)
    else:
        print(v - 1)
```

---

````{admonition} Sample solution
:class: dropdown

```

4
16
7

```

**Explanation:**

- `5` becomes `4`  
- `15` becomes `16`  
- `8` becomes `7`  
````

---

```{admonition} Tip
:class: tip

Readable patterns matter more than short code.  
Write code that explains its intent.
```

---

## 6. Exercises

The following exercises help you practise how **conditions and loops work together**.

Focus on understanding *when a condition is checked* and *what effect it has inside the loop*.

---

### Exercise 1: Filtering values

You are given a list of temperatures:

```python
temperatures = [5, 12, 18, 3, 25]
```

Write a loop that prints **only temperatures above 10**.

1. Write the loop.
2. Predict which values will be printed before running it.


````{admonition} Sample solution
:class: dropdown

```{code-cell} python
for t in temperatures:
    if t > 10:
        print(t)
```

Printed values:

```
12
18
25
```

**Key idea:**
The loop runs for all values,
the condition controls which values produce output.

````

---

### Exercise 2: Transforming values

You are given a list of distances (in kilometres):

```python
distances = [2, 10, 4, 5]
```

Write a loop that:

* doubles distances greater than or equal to 5
* leaves smaller distances unchanged

Print the result for each value.

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
for d in distances:
    if d >= 5:
        print(d * 2)
    else:
        print(d)
```

Output:

```
2
20
4
10
```

**Key idea:**
Transforming changes values,
but still processes every item.

````

---

### Exercise 3: Using membership inside a loop

You are given a list of cities and a list of capitals:

```python
cities = ["Lima", "Quito", "Santiago", "Bogotá"]
capitals = ["Lima", "Bogotá"]
```

Write a loop that prints only the cities
that are also capitals.

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
for city in cities:
    if city in capitals:
        print(city)
```

Output:

```
Lima
Bogotá
```

**Key idea:**
Membership operators work naturally inside loops.

````

---

### Exercise 4: Predict before you run

Without running the code, predict the output:

```python
values = [1, 4, 7, 13, 18]

for v in values:
    if v % 2 == 0:
        print("even")
    else:
        print("odd")
```

Write down the expected output line by line.

````{admonition} Sample solution
:class: dropdown

```

odd
even
odd
odd
even

```

**Key idea:**  
Conditions are evaluated separately for each loop iteration.
````

---

## 7. Summary

In this section, you learned how **repetition and decisions work together**.

---

### Key ideas

* Loops control **how often** code runs
* Conditions control **what happens** for each value
* Conditions evaluate to `True` or `False`
* Operators allow values, objects, and collections to be tested
* Logical operators combine conditions
* Placing `if` inside a loop enables filtering and transforming data

---

### Mental models to keep

```{admonition} Tip
:class: tip

A loop answers:  
“How many times should this run?”

A condition answers:  
“What should happen this time?”
```

Readable code makes both questions clear.

---

### What comes next

...
