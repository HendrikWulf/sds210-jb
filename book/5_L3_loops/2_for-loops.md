---
title: The for Loop

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Doing the same thing many times
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/2_for-loops.ipynb)

```{admonition} Big idea
:class: tip

Loops allow the computer to  
**repeat actions for us**.

We write the instruction once.  
The computer does the repetition.
```

Programs become powerful when they can repeat work automatically.
Loops are the main tool for expressing repetition in Python.

This section focuses only on **repetition**, not on decisions.
Every example does the same thing each time the loop runs.

## 1. The idea of a loop

### One value at a time

A loop processes values **one after another**.

Instead of writing the same instruction many times, we describe a pattern:

> Take one value, do something, move on to the next value.

This idea applies to many situations, such as:

* printing all values in a list
* performing the same calculation repeatedly
* stepping through a sequence in order

The number of repetitions is controlled by the data, not by you.

Consider a simple list of values:

```python
values = [3, 7, 12]
```

When a loop runs over this list, it does **not** see the list all at once.

Instead, it works like this:

* first, it sees `3`
* then, it sees `7`
* finally, it sees `12`

At each step, the same instructions are executed again.

---

### The loop variable

Each loop introduces a **temporary variable**.

This variable:

* holds exactly one value at a time
* changes automatically on each repetition
* exists while the loop is running

The name of the loop variable is chosen by you and should be meaningful.

---

### How loops run

Conceptually, a loop always follows the same steps:

1. Take the next value from the sequence
2. Assign it to the loop variable
3. Execute the loop body
4. Repeat until no values remain

Understanding this execution model is more important than memorising syntax.

---

## 2. The for loop

### Iterating over collections

The most common loop in Python is the `for` loop.

It is used to iterate over collections such as lists.

```python
for item in collection:
    do_something(item)
```

This line tells Python to take one value from the collection at a time
and run the same instructions for each value.

Read it like a sentence:

> For each `item` in the `collection`, do something with it.

The loop continues until the collection has no values left.

---

### A concrete example

Consider a simple list of city names:

```python
cities = ["Tokyo", "Delhi", "Shanghai", "Jakarta"]
```

Now run the following loop:

```python
for city in cities:
    print(city)
```

**What you will see as output:**

```text
Tokyo
Delhi
Shanghai
Jakarta
```

Python executes the same `print(city)` instruction four times.
Each time, `city` refers to a different value from the list.

The code itself does not change.
Only the value of `city` changes.

---

### How Python executes this loop

Internally, Python proceeds step by step:

1. Assigns `"Tokyo"` to `city` and runs the loop body
2. Assigns `"Delhi"` to `city` and runs the loop body
3. Assigns `"Shanghai"` to `city` and runs the loop body
4. Assigns `"Jakarta"` to `city` and runs the loop body
5. Stops because no values remain

At any moment, the loop variable holds **exactly one value**.

---

### Loop body and indentation

Everything indented below the `for` statement
belongs to the loop.

```python
for city in cities:
    print(city)
    print("----")
```

Both `print` statements are part of the loop body,
so both run once for each city.

When the indentation ends, the loop ends.

Python does not use an explicit “end loop” keyword.
Structure is defined entirely by indentation.

---

### Loop variable lifetime

The loop variable is a **normal variable**.

It is assigned a new value on each repetition.

After the loop finishes:

* the variable still exists
* it contains the **last value** from the collection

You can verify this directly:

```python
print(city)
```

This behaviour can be surprising at first, so it is important to be aware of it.

---

```{admonition} Note
:class: note

The loop variable does not disappear  
when the loop ends.
```
---

## 3. Looping with range

### Repeating a fixed number of times

Sometimes you do not want to loop over a list.
You simply want to repeat an action a **known number of times**.

This is what `range()` is for.

```python
for i in range(5):
    print(i)
```

When this code runs, you will see:

```text
0
1
2
3
4
```

The loop runs five times.
On each repetition, the loop variable takes on the next number in the sequence.

---

### How range works

When `range()` is given a single number, it produces a sequence of integers:

```python
range(5)
```

Conceptually, this corresponds to:

```text
0, 1, 2, 3, 4
```

Important details:

* the sequence starts at `0`
* the final value is **not included**
* the length of the sequence matches the number you provide

This start at zero, stop before the end behaviour is very common in programming.

---

### Start, stop, step

The `range()` function can take one, two, or three arguments.

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

For example:

```python
for i in range(2, 9, 3):
    print(i)
```

This produces:

```text
2
5
8
```

Read this as:

> Start at 2, increase by 3 each time, stop before reaching 9.


```{admonition} What would be the output of range(4, 15, 3)?
:class: dropdown

4
7
10
13
```


Using these arguments gives you precise control over how many repetitions occur.

You can learn a bit more about range by typing `help(range)`.

```python
help(range)
```

---

### Typical use cases

Loops with `range()` are often used for:

* counters
* repeated actions
* controlled sequences of numbers

---

## 4. Looping with index values

### When values are not enough

So far, you have looped directly over the values in a list.
In many cases, this is exactly what you want.

Sometimes, however, you also need to know **where** a value appears in a list.

This is where **index values** become useful.

---

### Accessing values by index

Recall that list elements are accessed using an index.
The first element has index `0`.

We can combine this idea with `range()` and `len()`.

```python
cities = ["Buenos Aires", "São Paulo", "Lima", "Bogotá", "Santiago"]

for i in range(len(cities)):
    print(f"{cities[i]} is at index {i}")
```

**Output:**

```text
Buenos Aires is at index 0
São Paulo is at index 1
Lima is at index 2
Bogotá is at index 3
Santiago is at index 4
```

Here is what happens:

* `len(cities)` gives the number of elements in the list
* `range(len(cities))` produces the indices `0, 1, 2, ...`
* `i` takes on each index value
* `cities[i]` accesses the corresponding city

---

### Why the loop starts at zero

Because Python lists start at index `0`,
the first value in the list is accessed as `cities[0]`.

Using `range(len(cities))` ensures that:

* every valid index is used
* no index goes out of bounds

This pattern is common and worth recognising.

---

### Using indices with related lists

Index-based loops are especially useful
when you have **multiple lists that belong together**.

Consider the following example:

```python
cities = ["Buenos Aires", "Brasília", "Lima", "Bogotá", "Santiago"]
countries = ["Argentina", "Brazil", "Peru", "Colombia", "Chile"]
```

Each city corresponds to a country at the same index.

```python
for i in range(len(cities)):
    print(cities[i], "is the capital of", countries[i])
```

**Output:**

```text
Buenos Aires is the capital of Argentina
Brasília is the capital of Brazil
Lima is the capital of Peru
Bogotá is the capital of Colombia
Santiago is the capital of Chile
```

The index `i` allows access to matching elements
from both lists at the same time.

---

### When index-based loops are needed

Using indices is useful when:

* you need to update values in a list
* you want to refer to the position of an element
* you need to access multiple related lists together

In many other cases, looping directly over values
is simpler and clearer.

---

```{admonition} Note
:class: note

If you only need the values,  
loop over the values.

If you need positions or coordination  
between lists, use indices.
```

---

## 5. Nested loops

### Repetition inside repetition

A loop can be placed **inside another loop**.
This is called a **nested loop**.

```python
for a in first_list:
    for b in second_list:
        print(a, b)
````

In this structure:

* the **outer loop** controls the larger repetition
* the **inner loop** runs fully for each outer value

---

### A concrete example

Consider two small lists:

```python
colors = ["red", "blue"]
shapes = ["circle", "square"]
```

Now run the nested loop:

```python
for color in colors:
    for shape in shapes:
        print(color, shape)
```

**Observed output:**

```text
red circle
red square
blue circle
blue square
```

Each color is combined with **every** shape.
The same pattern repeats until all combinations are produced.

---

### Execution order

Nested loops always follow the same order:

1. The outer loop takes its first value
2. The inner loop runs through all its values
3. The outer loop moves to the next value
4. The inner loop runs again from the beginning

This creates a grid-like pattern of repetition.

---

### Visualising the pattern

You can think of nested loops as filling a table:

* rows correspond to the outer loop
* columns correspond to the inner loop

Every cell represents one execution of the inner loop body.

---

### When nested loops are useful

Nested loops are useful when:

* combining values from two collections
* working with two dimensions
* generating all possible pairs

At this stage, examples stay simple
and deliberately avoid conditions.

---

```{admonition} Caution
:class: caution

Nested loops can grow quickly.  
Each extra loop multiplies the number of repetitions.
```

---

## 6. Exercises

These exercises help you practise the core idea of repetition using loops.  
Focus on **understanding what happens**, not on writing the shortest code.

---

### Exercise 1: Looping over values

You are given a list of elevations (in meters):

```python
elevations = [450, 1200, 890, 2300]
```

1. Write a `for` loop that prints each elevation.
2. Run the code and observe the output.
3. How many times does the loop body execute?

````{admonition} Sample solution
:class: dropdown

```python
for elevation in elevations:
    print(elevation)
```

The loop runs **four times**, once for each value in the list.

**Key idea:**
The loop adapts automatically to the number of values.

````

---

### Exercise 2: Repeating with `range()`

Write a loop that prints the numbers 1 to 5. Use `range()` to control the number of repetitions.

1. Write the loop.
2. Explain why the stop value is not printed.


````{admonition} Sample solution
:class: dropdown

```python
for i in range(1, 6):
    print(i)
```

The loop stops before reaching `6`.

**Key idea:**
`range(start, stop)` includes the start value but excludes the stop value.

````

---

### Exercise 3: Looping with index values

You are given two related lists:

```python
cities = ["Quito", "La Paz", "Asunción"]
countries = ["Ecuador", "Bolivia", "Paraguay"]
```

1. Use an index-based loop to print each city together with its country.
2. Why does looping directly over `cities` not work in this case?


````{admonition} Sample solution
:class: dropdown

```python
for i in range(len(cities)):
    print(cities[i], "is in", countries[i])
```

Looping directly over `cities` gives you the city names,
but not the matching position in the `countries` list.

**Key idea:**
Indices allow coordination between multiple lists.

````

---

### Exercise 4: Nested loops and grids

You are given x and y coordinates:

```python
x_coords = [3, 4, 5]
y_coords = [8, 9]
```

1. Write a nested loop that prints all `(x, y)` coordinate pairs.
2. How many times does the inner loop run in total?



````{admonition} Sample solution
:class: dropdown

```python
for x in x_coords:
    for y in y_coords:
        print(x, y)
```

The inner loop runs **six times** in total.

**Key idea:**
The total number of repetitions is
`len(x_coords) × len(y_coords)`.

````

---

### Exercise 5: Predict before you run

Without running the code, predict the output:

```python
values = [10, 20, 30]

for v in values:
    print(v)
print(v)
```

1. What is printed by the loop?
2. What is printed by the final `print(v)`?


````{admonition} Sample solution
:class: dropdown

The loop prints:

```
10
20
30
```

The final `print(v)` prints:

```
30
```

**Key idea:**  
The loop variable still exists after the loop and holds the last value.
````

---

## 7. Summary

In this section, you learned how Python expresses **repetition** using loops.

---

### Key ideas

* A loop processes values **one at a time**
* The loop variable holds **one value per iteration**
* `for` loops are used to iterate over collections
* `range()` controls repetition when no list is involved
* Index-based loops allow access to positions and related lists
* Nested loops combine repetition across multiple dimensions

---

```{admonition} Mental models to remember
:class: tip

A loop answers the question:  
“How do I do the same thing many times?”
```

* The code inside the loop stays the same
* Only the loop variable changes
* Indentation defines what is repeated

---

### What comes next

So far, all loops have repeated the **same action**.

Next, we will introduce **conditions**,
which allow loops to behave differently
for different values. 
So, repetition becomes **decision-aware**.