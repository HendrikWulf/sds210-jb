---
title: The while Loop

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Repeat while a condition is true
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/05_L03_loops/04_while-loops.ipynb)

```{admonition} Big idea
:class: tip

A `while` loop allows code to **repeat as long as a condition is true**.

The loop continues while the condition holds and stops the moment it becomes `False`.

```

So far, your programs have repeated actions over lists or fixed ranges.

Now we introduce a different idea:

> Repetition can continue **until a condition changes**, not just until a collection runs out.

This makes `while` loops especially useful when you do not know in advance how many times something needs to repeat. They complement `for` loops by shifting the programming focus from *what to loop over* to *when to stop looping*.

---

## 1. When a for loop is not enough

Up to now, loops have repeated over:

* a list with a known number of values
* a fixed range of numbers

In these cases, the exact number of repetitions is known **before the loop even starts**.

Sometimes, however, this is not possible. You may not know in advance **how many times** an action needs to be repeated. Common situations include:

* waiting until a user enters a valid input
* processing data until a specific threshold is reached
* searching through a dataset until a specific condition becomes true

In these cases, repetition must be controlled by a **condition**, not by a fixed collection of values. This is exactly where a `while` loop is needed.

---

## 2. The idea of a while loop

A `while` loop repeats a block of code **as long as a condition evaluates to `True`**.

```{code-cell} python
while condition:
    do_something()

```

Read this line as a plain English sentence:

> "While the condition remains true, keep doing this."

:::{figure} images/06_infinite_loop_comparison.png
:alt: Diagram contrasting a healthy loop that updates its control variable to reach a stop condition versus an infinite loop that never updates its variable and runs forever.
:width: 600px
:align: center

*If the loop body does not actively change the state of the program (like updating a counter or a flag), the condition will never evaluate to False, trapping your program in an infinite loop.*
:::

The key difference from a `for` loop is **when and how the condition is checked**. Before **every single repetition**, Python follows this process:

1. Check the condition.
2. If the condition is `True`, run the loop body.
3. If the condition is `False`, skip the loop body and move on.

If the condition is already false at the very beginning, the loop body does not run at all.

The condition is not just a gate at the start; it is checked **again and again** to decide whether another repetition should happen. It is the central control mechanism for the loop's lifespan.

---

## 3. Control variables and termination

### The control variable

Most `while` loops rely on a **control variable** to make progress toward stopping.

This variable:

* is created *before* the loop starts
* appears *inside* the loop condition
* is updated *inside* the loop body

It represents the part of the program state that determines whether the condition stays true or becomes false.

Example:

```{code-cell} python
counter = 1

while counter <= 5:
    print(counter)
    counter += 1  # This is the update step!

```

Here, Python repeatedly performs the same cycle:

1. Check if `counter <= 5`
2. Run the loop body (`print`)
3. Update `counter` (`+= 1`)
4. Cycle back and check the condition again

The update step is essential. It changes the program's state so that the condition will eventually become false. Without this change, the loop would never progress.

---

### Termination matters

Every `while` loop must have a clear path to **termination**.

If nothing inside the loop affects the condition, the condition will never change. The loop will then run forever. This is called an **infinite loop**.

:::{figure} images/07_infinite_loop_comparison.png
:alt: Diagram contrasting a healthy loop that updates its control variable to reach a stop condition versus an infinite loop that never updates its variable and runs forever.
:width: 700px
:align: center

*If the loop body does not actively change the state of the program (like updating a counter or a flag), the condition will never evaluate to False, trapping your program in an infinite loop.*
:::

Infinite loops usually happen when:

* the control variable is completely forgotten and not updated
* the update does not actually affect the condition being checked
* the condition logic is written incorrectly (e.g., checking `counter > 0` while adding `1` to it)

When writing `while` loops, always ask yourself:

> *Which exact line inside this loop moves the condition toward `False`?*

Being explicit about this step is the difference between a correct `while` loop and a program that freezes.

```{admonition} Escaping an infinite loop
:class: danger

If you accidentally run an infinite loop, your notebook will freeze and the cell will show a `[*]` (or a spinning loading icon) indicating it is stuck running forever. **Do not panic!** You do not need to close your browser. You can force the code to stop:

* **JupyterLab:** Click the **Stop** button (the black square) in the top toolbar, or go to the menu and select **Kernel > Interrupt Kernel**.
* **Google Colab:** Click the rotating stop button directly on the left side of the running cell.
* **VS Code:** Click the Interrupt button (the square stop icon) to the left of the running cell, or click Interrupt in the notebook toolbar at the top of the screen.

```

---

## 4. While loops with decisions

### Combining while and if

A `while` loop can also be combined with an `if` statement to control **when repetition should stop**. This is often called using a "flag variable."

This pattern is common whenever repetition depends on a condition that changes dynamically over time.

Consider the following example:

```{code-cell} python
values = [3, 7, 12, 0, 9]
index = 0
keep_running = True  # This is our flag

while keep_running:
    current_value = values[index]
    print(current_value)

    if current_value == 0:
        keep_running = False  # Lower the flag to stop the loop!

    index += 1

```

Here, two different roles are clearly separated:

* the `while` loop condition (`keep_running`) dictates **whether repetition continues**
* the `if` statement inside the loop decides **when to trigger the stop**

---

### How this loop works

This loop processes values **one by one** from the list. The logic is:

1. Take the next value from the list using the index.
2. Print the value.
3. Check whether it equals `0`.
4. If it does equal `0`, change the flag to `False`.
5. Update the index to move to the next value.

As soon as the value `0` is encountered, `keep_running` becomes false. The loop finishes its current cycle, checks the condition again, sees `False`, and ends.

---

## 5. A practical example

In spatial data science, you rarely process data just for the sake of it. You often process data **until a physical or quality criterion is satisfied**.

A common example is working with **elevation profiles**. Imagine you have elevation values sampled along a transect. You want to walk along this transect and stop at the **first point above 2500 m**.

```{code-cell} python
elevations = [1800, 1950, 2100, 2350, 2600, 2750]
threshold = 2500

index = 0
found = False

while not found:
    elevation = elevations[index]
    print(f"Checking elevation: {elevation} m")

    if elevation >= threshold:
        found = True
        print(f"--> Threshold reached at index {index}!")

    index += 1

```

Conceptually, this loop:

* moves step-by-step through spatially ordered data
* checks a physical threshold at every step
* stops exactly when the condition is satisfied

You do **not** know in advance *where* the threshold will be crossed. You only know the rule for **when to stop**.

---

## 6. Exercise

You are given a time-ordered record of daily mean temperatures (in °C). Some values may be **unrealistic** due to sensor errors.

```{code-cell} python
temperatures = [3, 5, 7, 6, -42, 8, 9, 58, 10]

```

Assume the following plausible range for this environment:

* minimum realistic temperature: **−20 °C**
* maximum realistic temperature: **40 °C**

Your task is to:

1. Check the temperatures **one by one**.
2. Stop as soon as an **outlier** is found so it can be fixed.
3. Print each checked value using a readable message.
4. Print a **clear warning** when an outlier is detected.

Use:

* a `while` loop
* conditional logic (`if`)
* an f-string for clear output

Before coding, think about:

* *What condition keeps the loop running?*
* *What condition signals an outlier?*
* *Which line will cause the loop to eventually stop?*

---

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
temperatures = [3, 5, 7, 6, -42, 8, 9, 58, 10]
min_temp = -20
max_temp = 40

index = 0
outlier_found = False

# We add 'index < len(temperatures)' as a safety net in case 
# the list has no outliers, preventing an IndexError!
while not outlier_found and index < len(temperatures):
    temp = temperatures[index]
    print(f"Checking day {index + 1}: {temp} °C")

    if temp < min_temp or temp > max_temp:
        print(f"--> Outlier detected on day {index + 1}: {temp} °C is outside the valid range.")
        outlier_found = True

    index += 1
```

**What this code does:**
- processes the environmental record in time order  
- reports each checked value clearly  
- reacts immediately to invalid data  
- stops safely as soon as the first problem is found  

``````

---

## 7. Summary

In this section, you learned how to use the `while` loop to control repetition based on **conditions**, rather than fixed collections.

### Key ideas

* a `while` loop repeats **as long as a condition evaluates to True** - the condition is checked as a gatekeeper before *every* repetition
* **control variables** are required to move the loop toward termination
* every `while` loop must have a clear stopping condition to avoid **infinite loops**
* `while` loops are the ideal tool when the total number of required repetitions is unknown

---

### For vs. While loops

```md
for loop   → “Repeat for every single value in this collection.”
while loop → “Repeat until this specific condition changes.”

```

**Typical guidance:**

* use `for` when iterating over a known dataset or fixed range.
* use `while` when waiting for a condition to be met (like a threshold or user input).

Neither loop is "better" than the other. They just solve different structural problems. Choosing the right loop makes your code cleaner, safer, and much easier to read.

---

### What comes next

So far, loops have always run to completion once they start.

Next, you will learn how to **control loop execution manually**:

* stopping a loop early from the inside (`break`)
* skipping individual iterations without stopping the whole loop (`continue`)
* reacting immediately to special edge cases

These tools will give you fine-grained control over exactly how and when your spatial data processing happens.
