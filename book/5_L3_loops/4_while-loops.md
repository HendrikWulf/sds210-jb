---
title: The while Loop

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Repeat while a condition is true
</div>

---


```{admonition} Big idea
:class: tip

A `while` loop allows code to **repeat as long as a condition is true**.

The loop continues while the condition holds and stops as soon as it becomes `False`.
```

So far, your programs have repeated actions over lists or fixed ranges.

Now we introduce a different idea:

> Repetition can continue **until a condition changes**,
> not until a collection runs out.

This makes `while` loops especially useful when you do not know in advance how many times something needs to repeat.
They complement `for` loops by shifting the focus from *what to loop over* to *when to stop looping*.

---

## 1. When a for loop is not enough

Up to now, loops have repeated over:

* a list with a known number of values  
* a fixed range of numbers  

In these cases, the number of repetitions is known **before the loop starts**.

Sometimes, however, this is not possible.

You may not know in advance **how many times** an action needs to be repeated.

Common situations include:

* waiting until the user enters a valid input  
* processing values until a threshold is reached  
* searching until a condition becomes true  

In these cases, repetition is controlled by a **condition**,
not by a collection of values.

This is exactly the situation where a `while` loop is needed.

---

## 2. The idea of a while loop

A `while` loop repeats a block of code  
**as long as a condition evaluates to `True`**.

```python
while condition:
    do_something()
```

Read this line as a sentence:

> While the condition is true, keep doing this.

The key difference to a `for` loop is **when the condition is checked**.

Before **every repetition**, Python follows this process:

1. Check the condition
2. If the condition is `True`, run the loop body
3. If the condition is `False`, stop the loop

If the condition is already false at the beginning,
the loop does not run at all.

This means the condition is not just a gate at the start.
It is checked **again and again** to decide
whether another repetition should happen.

The condition is therefore the central control mechanism
for how long the loop continues.

---

## 3. Control variables and termination

### The control variable

Most `while` loops rely on a **control variable**
to make progress toward stopping.

This variable:

* is created before the loop starts
* appears in the loop condition
* is updated inside the loop body

It represents the part of the program state
that determines whether the condition stays true or becomes false.

Example:

```python
counter = 1

while counter <= 5:
    print(counter)
    counter += 1
```

Here, Python repeatedly performs the same cycle:

1. Check `counter <= 5`
2. Run the loop body
3. Update `counter`
4. Check the condition again

The update step is essential.
It changes the program state so that the condition
will eventually become false.

Without this change, the loop would never progress.

---

### Termination matters

Every `while` loop must have a clear path to **termination**.

If nothing inside the loop affects the condition,
the condition will never change.

The loop will then run forever.
This is called an **infinite loop**.

Infinite loops usually happen when:

* the control variable is not updated
* the update does not affect the condition
* the condition is written incorrectly

When working with `while` loops,
always ask yourself:

> Which line inside this loop moves the condition toward `False`?

Being explicit about this step is the key difference
between a correct `while` loop
and one that never stops.

---

## 4. While loops with decisions

### Combining while and if

A `while` loop can also be combined with an `if` statement
to control **when repetition should stop**.

This pattern is common whenever repetition depends on user input
or on a condition that changes over time.

Consider the following example:

```python
values = [3, 7, 12, 0, 9]
index = 0
keep_running = True

while keep_running:
    current_value = values[index]
    print(current_value)

    if current_value == 0:
        keep_running = False

    index += 1
```

Here, two different roles are clearly separated:

* the `while` loop controls **whether repetition continues**
* the `if` statement decides **when the loop should stop**

---

### How this loop works

This loop processes values **one by one** from the list.

The program logic is:

1. Take the next value from the list
2. Print the value
3. Check whether it equals `0`
4. Stop the loop if the condition is met
5. Otherwise, move to the next value

As soon as the value `0` is encountered,
the condition becomes false and the loop ends.

---

## 5. A practical example

At some point in your analysis you may want to process data **until a quality criterion is satisfied**,
not until a list simply ends.

A common example is working with **time series or profiles** where you want to stop
once a threshold is reached.

Here is a simple **example**. Imagine you have elevation values sampled along a transect.
You want to find the **first point above 2500 m**.

```python
elevations = [1800, 1950, 2100, 2350, 2600, 2750]
threshold = 2500

index = 0
found = False

while not found:
    elevation = elevations[index]
    print(f"Checking elevation: {elevation} m")

    if elevation >= threshold:
        found = True
        print("Threshold reached")

    index += 1
```

Conceptually, this loop:

* moves step by step through ordered data
* checks a physical threshold
* stops as soon as the condition is satisfied

You do **not** know in advance *where* the threshold will be crossed.
You only know **when to stop**.

---

## 6. Exercise

You are given a time-ordered record of daily mean temperatures (in °C).
Some values may be **unrealistic** due to sensor errors.

```python
temperatures = [3, 5, 7, 6, -42, 8, 9, 58, 10]
```

Assume the following plausible range:

* minimum realistic temperature: **−20 °C**
* maximum realistic temperature: **40 °C**

Your task is to:

1. Check the temperatures **one by one**
2. Stop as soon as an **outlier** is found to fix it
3. Print each checked value using a readable message
4. Print a **clear warning** when an outlier is detected

Use:

* a `while` loop
* conditional logic
* an f-string for clear output

Before coding, think about:

* What condition keeps the loop running?
* What condition signals an outlier?
* Which line causes the loop to stop?

---

````{admonition} Sample solution
:class: dropdown

```python
temperatures = [3, 5, 7, 6, -42, 8, 9, 58, 10]
min_temp = -20
max_temp = 40

index = 0
outlier_found = False

while not outlier_found and index < len(temperatures):
    temp = temperatures[index]
    print(f"Checking day {index + 1}: {temp} °C")

    if temp < min_temp or temp > max_temp:
        print(
            f"Outlier detected on day {index + 1}: "
            f"{temp} °C is outside the valid range"
        )
        outlier_found = True

    index += 1
```

**What this code does:**

- processes the record in time order  
- reports each checked value clearly  
- reacts immediately to invalid data  
- stops as soon as a problem is found  

````
---

## 7. Summary

In this section, you learned how to use the `while` loop
to control repetition based on **conditions**, not collections.

### Key ideas

- a `while` loop repeats **as long as a condition is true**  
- the condition is checked before every repetition  
- control variables move the loop toward termination  
- every `while` loop must have a clear stopping condition  
- `while` loops are ideal when the number of repetitions is unknown  

---

### For vs while loops

```md
for loop   → “Repeat for each value”
while loop → “Repeat until a condition changes”
```

Typical guidance:

* use `for` when iterating over data  
* use `while` when waiting for a condition  

Neither loop is better. They just solve different problems.  
Choosing the right loop makes your code
clearer, safer, and easier to understand.

---

### What comes next

So far, loops have always run to completion
once they start.

Next, you will learn how to **control loop execution**:

- stopping a loop early  
- skipping individual iterations  
- reacting immediately to special cases  

These tools give you fine-grained control
over how and when repetition happens.

````