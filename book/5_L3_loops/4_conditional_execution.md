---
title: Conditions as decision logic

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
When code must decide
</div>

---

```{admonition} Big idea
:class: tip

Conditions allow code to  
**ask questions about data**  
and **choose what happens next**.

Every condition evaluates to either  
`True` or `False`.
```

So far, your programs have executed line by line.
Now we introduce a new capability:

> Code can behave **differently** depending on the data.

This is the foundation of decision making in programming.

---

## 1. Conditions and Boolean logic

### Conditions as questions

A condition is an expression that can be answered with **yes or no**.

Examples of questions code can ask:

* Is the temperature above freezing?
* Is this value equal to zero?
* Is this item contained in a list?

In Python, the answers are the Boolean values `True` and `False`.

---

### Boolean values

Python has a dedicated data type for Boolean logic:

* `True`
* `False`

These values are not strings.
They represent logical truth.

```python
temperature = 17
temperature > 25
```

This expression evaluates to `False`.

---

## 2. Operators for evaluating conditions

### Comparison operators

Comparison operators compare two values.

```python
a == b
a != b
a < b
a > b
a <= b
a >= b
```

Each comparison evaluates to `True` or `False`.

---

### Identity operators

Identity operators check whether two variables refer to the **same object**.

```python
a is b
a is not b
```

At this stage, identity checks are rare.
They become more important later when working with complex objects.

---

### Membership operators

Membership operators test whether a value exists inside a collection.

```python
x in y
x not in y
```

This is especially useful when working with lists, strings, and dictionaries.

---

```{admonition}
:class: note

Comparison checks values.  
Identity checks objects.  
Membership checks collections.
```

---

## 3. Logical operators

### Combining conditions

Logical operators allow you to combine multiple conditions into one.

```python
and
or
not
```

Examples:

```python
temperature > 0 and temperature < 30
city in cities or city in capitals
not temperature < 0
```

---

### Reading logic in words

It helps to read logical expressions aloud:

* `and` means both conditions must be true
* `or` means at least one condition must be true
* `not` reverses the condition

---

### Parentheses and readability

When combining several conditions, use parentheses.

```python
(a < b and b < c) or (a > b and b < a)
```

Parentheses make the logic clearer and avoid mistakes.
Some libraries require them explicitly.

---

## 4. Conditional execution

### The if statement

The `if` statement runs code only when a condition is true.

```python
if temperature > 25:
    print("It is hot")
```

If the condition is false, nothing happens.

---

### Two possible paths

Use `else` when there are two alternatives.

```python
if temperature > 25:
    print("It is hot")
else:
    print("It is not hot")
```

Exactly one of the two blocks will run.

---

### Multiple decisions

Use `elif` when there are several mutually exclusive cases.

```python
if temperature > 0:
    print("Above freezing")
elif temperature == 0:
    print("At freezing point")
else:
    print("Below freezing")
```

Python checks conditions from top to bottom
and stops at the first true one.

---

```{admonition}
:class: tip

Only one branch of an  
`if – elif – else` chain  
is executed.
```

---

## 5. Short Exercises

### Task

Consider the following code:

```python
a = 5
b = 10

if a < b and b < 20:
    print("A")
elif a == b:
    print("B")
else:
    print("C")
```

Answer without running the code:

1. Which conditions are evaluated?
2. Which line is printed?
3. Why are parentheses not required here?

Write down your reasoning in one or two sentences.

---

```{admonition} Sample solution
:class: dropdown

1. `a < b` and `b < 20`  
2. `A` is printed  
3. The logic is simple and unambiguous, but parentheses would still improve readability
```

---

### What comes next

You now know how code can **decide**.

Next, we will introduce **repetition**:
how the same decisions can be applied
to many values using loops.

Conditions will then move *inside* loops,
where their real power becomes visible.