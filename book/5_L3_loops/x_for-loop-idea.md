---
title: The idea of a for loop

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
One value at a time
</div>

---

```{admonition} Big idea
:class: tip

A `for` loop lets the computer  
**repeat the same action**  
for **each value in a collection**.

The code adapts to the data,
not the other way around.
```

In the previous section, you saw **why** repetition matters.
Now we introduce the first tool that makes repetition practical:
the **for loop**.

A `for` loop allows you to apply the same operation
to every value in a collection,
without knowing in advance how many values there are.

---

## 1. From collections to repetition

Recall a simple list of city names:

```python
cities = ["Tokyo", "Delhi", "Shanghai", "Jakarta"]
```

You already know how to access individual values in this list.
What you want now is something more general:

> *Do the same thing for every city in the list.*

This is exactly what a `for` loop expresses.

---

## 2. A first loop

Here is a minimal example:

```python
for city in cities:
    print(city)
```

When this code runs, Python prints each city name on its own line.

This works no matter how long the list is.
If you add or remove cities,
the code does not need to change.

---

## 3. How to read a for loop

It helps to read the loop like a sentence:

> For each `city` in `cities`, print `city`.

Python follows this logic step by step:

1. Look at the collection `cities`
2. Take the first value and assign it to `city`
3. Run the indented code using that value
4. Move on to the next value
5. Stop when no values remain

At any moment, the loop variable holds **one value only**.

---

## 4. The loop variable

The name `city` is not special.
It is a variable created by the loop.

The variable can be any valid variable name you like:

```python
for name in cities:
    print(name)
```

Choosing meaningful names makes loops easier to read
and easier to understand later.

---

## 5. Indentation defines the loop body

Everything indented below the `for` statement
belongs to the loop.

```python
for city in cities:
    print(city)
    print("----")
```

Both print statements run once for each city.

When the indentation ends, the loop ends.
The recommended indentation is 4 spaces.
There is no additional special word needed to end the loop, you simply change the indentation back to normal.

---

## What we are not doing yet

At this stage, we focus only on the **core idea**.

We deliberately do not use:

* indices
* `range()`
* conditions inside the loop
* nested loops

These ideas build on the same foundation
and will be added step by step.

For now, the goal is simple:

> Use a `for` loop to process each value in a collection.

---

## Concept check

Before moving on, pause and think about the idea.

---

### Task

You are given a list of temperatures:

```python
temperatures = [12, 15, 9, 18]
```

Answer the following **without writing code**.

1. How many times would the loop body run?
2. What value does the loop variable hold in the first iteration?
3. Would the loop still work if another temperature were added?

Write down short answers in your own words.

---

```{admonition} Sample solution
:class: dropdown

1. Four times  
2. The value `12`  
3. Yes, the loop adapts automatically  

**Key insight:**  
The loop depends on the collection,
not on its current size.
```

---

### What comes next

Next, we will look more closely at:

* how Python knows what belongs to a loop
* how loops interact with conditions
* how repetition and decisions work together

Once this is clear,
you will be able to write programs that
react to data instead of just printing it.
