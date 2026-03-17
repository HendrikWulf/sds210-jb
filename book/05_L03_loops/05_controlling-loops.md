---
title: Controlling Loops

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Stopping early and skipping work
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/05_L03_loops/05_controlling-loops.ipynb)

```{admonition} Big idea
:class: tip

Loops do not always need to run to the end.

Python provides small keywords that let you  
**stop a loop early**, **skip an iteration**,  
or **leave a placeholder while drafting code**.

```

So far, loops have followed a strict and predictable pattern: start, repeat, and stop only when the main loop condition is met or the data runs out.

Now we add a powerful new capability:

> You can control the loop's flow **from inside the loop body**.

This is incredibly useful for data checking, quality control, and making your processing more efficient.

---

## 1. Placeholders with `pass`

### Why pass exists

Sometimes you want to sketch out the structure of your code before you actually know what the logic should be.

However, Python relies on indentation. If you create a `for` loop or an `if` statement and leave the indented block completely empty, Python will throw an error.

`pass` is a placeholder statement that literally does nothing. It simply tells Python, *"I know a block of code belongs here, just ignore it for now."*

```{code-cell} python
for i in range(5):
    pass  # Keeps the code valid while you are drafting

```

This loop runs perfectly, but performs no action.

### When to use pass

Use `pass` when you:

* sketch out a loop you will complete later
* create a temporary placeholder while debugging
* need a code block that is syntactically required but intentionally empty

```{admonition} Doing nothing
:class: note

`pass` does nothing on purpose. It is **not** the same as “skip this iteration”. It just prevents an indentation error.

```

---

## 2. Exiting a loop with `break`

### Stopping early

The `break` statement is an emergency exit. It ends the loop **immediately**. Execution jumps completely out of the loop and continues with the first line of code *after* the loop block.

This is useful when your goal has been reached and continuing the loop would just be wasted work.

### Example: Stop when an outlier is found

```{admonition} Tracking positions with enumerate()
:class: info
In this example, we want to print a warning that includes both the temperature **and** the specific day it was recorded. 

Instead of dealing with `range(len())`, Python provides a highly readable tool called `enumerate()`. It automatically counts items as it loops, giving you two variables at once: the count (which we call `day`) and the value (`temp`). By adding `start=1`, we tell Python to start counting at Day 1 instead of 0!
```

```{code-cell} python
temperatures = [3, 5, 7, 6, 8, 9, 10, 111, 11]
min_temp = -20
max_temp = 40

for day, temp in enumerate(temperatures, start=1):
    print(f"Day {day}: {temp} °C")
    
    if temp < min_temp or temp > max_temp:
        print(f"⚠️ Outlier detected on day {day}: {temp} °C. Stopping analysis!")
        break

print("Finished checking the record.")

```

As soon as the `break` statement is triggered on the 111 °C outlier, the loop is abandoned. The remaining temperature (11 °C) is never checked.

### Why use break?

Without `break`, the loop would uselessly keep checking values even after the problem was found. With `break`, the loop stops early, saving time and processing power.

This is a common pattern when:

* searching for the very first occurrence of a feature
* detecting the onset of an environmental event
* safely stopping a process when an error condition is met

---

## 3. Skipping an iteration with `continue`

### Skip the rest of this round

While `break` stops the entire loop, `continue` only stops the **current iteration**. It skips the remaining code in the loop body and immediately jumps back to the top to start the **next iteration**.

This is perfect when some values should be **ignored**, but you still want to process the rest of the dataset.

:::{figure} images/08_break_vs_continue.png
:alt: Side-by-side flowcharts showing 'break' completely exiting a loop boundary, while 'continue' skips the rest of the current block and loops back to the top.
:width: 700px
:align: center

*Notice the difference in the escape paths: `break` shatters the loop entirely and moves on. `continue` acts like a reset button for the current iteration, sending Python straight back to the top to grab the next value.*
:::

### Example: Ignore missing values

```{code-cell} python
temperatures = [3, None, 7, 6, None, 9]

for temp in temperatures:
    if temp is None:
        continue  # Skip to the next temperature
        
    print(f"Valid value: {temp} °C")

```

Here, the loop skips the `None` entries without breaking the loop, ensuring the valid temperatures (`7`, `6`, `9`) are still printed.

### What is `None`?

In Python, `None` represents the **absence of a value**. It is commonly used to indicate:

* missing data
* unavailable measurements
* placeholders where no valid value exists

`None` is **not** zero, not an empty string, and not `False`. It is a distinct data type with a special meaning. Because of this, it is usually checked explicitly using the `is` operator.

### A common coding pattern

Often, `continue` is used as a "guard" at the very top of a loop:

```{code-cell} python
for value in dataset:
    if value is None:
        continue
        
    # main, complex processing happens down here

```

This acts as a filter, keeping the main logic less indented and much easier to read.

---

## 4. `continue` and `while` loops

### Why continue can be risky

In a `for` loop, Python automatically fetches the next value from the list when `continue` is called. So, `continue` is very safe to use.

In a `while` loop, **you** are responsible for updating the control variable (like `index += 1`). If `continue` skips the line of code that updates your variable, the loop will evaluate the exact same condition again and again, freezing your program.

### Example of the risk (Do not run this!)

```{code-cell} python
values = [3, None, 7]
index = 0

while index < len(values):
    value = values[index]

    if value is None:
        continue  # DANGER: We skip the index update!

    print(value)
    index += 1    # This line is never reached for None

```

This code prints `3`, and then gets permanently stuck on the `None` value because `index` remains `1` forever.

### The safe pattern

If you use `continue` in a `while` loop, make sure your control variable is updated **before** the `continue` statement is reached.

```{code-cell} python
values = [3, None, 7]
index = 0

while index < len(values):
    value = values[index]
    index += 1  # Update happens FIRST

    if value is None:
        continue

    print(value)

```

Now the loop safely progresses to the end of the list.

```{admonition} Safety check
:class: caution

In a `while` loop, always trace your logic to ensure the loop can still make progress after a `continue` statement is triggered.

```

---

## 5. Exercises

### Exercise 1: Drafting a data check with pass

You are planning to write a quality check for a dataset,
but you are not yet sure what the check should do.

Create a loop that iterates over the indices of a dataset
and prints the index number.

Leave the body of the loop empty for now using `pass`.

```{code-cell} python
data = [12, 15, 18, 21, 24]
```

*Why might this be useful while developing code?*

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
data = [12, 15, 18, 21, 24]

for i in range(len(data)):
    pass
```

**Explanation:**

- the loop structure is correct  
- the body is intentionally empty  
- logic can be filled in later without breaking the code  
````

---

### Exercise 2: Stop at the first invalid measurement

You are checking daily temperature measurements.
Values below −20 °C or above 40 °C are invalid.

```{code-cell} python
temperatures = [5, 7, 9, 11, 13, 45, 14, 16]
```

Write a loop that:

1. Iterates over the list using an index
2. Prints each day and temperature
3. Stops immediately when an invalid value is found
4. Prints a clear warning using an `f`-string

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
temperatures = [5, 7, 9, 11, 13, 45, 14, 16]
min_temp = -20
max_temp = 40

for i in range(len(temperatures)):
    temp = temperatures[i]
    print(f"Day {i + 1}: {temp} °C")

    if temp < min_temp or temp > max_temp:
        print(f"⚠️ Invalid measurement on day {i + 1}")
        break
```

**Explanation:**

- indexing makes the day number explicit  
- `break` stops the loop as soon as the decision is made  
- the loop’s intent is  detecting the first error  
````

---

### Exercise 3: Skip missing values but keep counting

You are processing sensor data where some measurements are missing (`None`).

```{code-cell} python
temperatures = [3, None, 6, 7, None, 9]
```

Write a loop that:

1. Iterates over the list
2. Skips missing values
3. Prints only valid temperatures
4. Includes the position in the output

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
temperatures = [3, None, 6, 7, None, 9]

for i in range(len(temperatures)):
    temp = temperatures[i]

    if temp is None:
        continue

    print(f"Valid value at position {i}: {temp} °C")
```

**Explanation:**

- `continue` ignores invalid entries  
- indexing preserves positional information  
- output stays readable and informative  
````

---

### Exercise 4: Decide whether to break or continue

Consider the following dataset:

```{code-cell} python
values = [10, 12, None, 15, -999, 18]
```

Assume:

* `None` means *missing* and should be skipped
* `-999` means *corrupted* and should stop processing

Write a loop that:

* skips `None` values
* stops entirely when `-999` is encountered
* prints all valid values before stopping

Think carefully about **where** to use `continue`
and **where** to use `break`.

---

````{admonition} Sample solution
:class: dropdown

```{code-cell} python
values = [10, 12, None, 15, -999, 18]

for i in range(len(values)):
    value = values[i]

    if value is None:
        continue

    if value == -999:
        print(f"⚠️ Corrupted value at position {i}")
        break

    print(f"Value at position {i}: {value}")
```

**Explanation:**

- `continue` skips missing values  
- `break` stops processing when data is corrupted  
- different control statements express different intent  
````

---

## 6. Summary

* `pass` is a placeholder that does nothing.
* `break` exits a loop entirely and immediately.
* `continue` skips the remainder of the current iteration and moves to the next one.

`break` and `continue` are most useful when processing real-world data, because they allow your program to react dynamically to missing, corrupted, or target values.

---

### What comes next

Next, you will combine everything you have learned:

* repetition with `for` and `while`
* decisions with `if`, `elif`, `else`
* loop control with `pass`, `break`, and `continue`

This gives you a complete toolkit for writing programs that can automate spatial logic and react to real data in a controlled, intelligent way.
