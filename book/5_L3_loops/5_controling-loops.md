---
title: Controlling Loops

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
Stopping early and skipping work
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/5_controling-loops.ipynb)

```{admonition} Big idea
:class: tip

Loops do not always need to run to the end.

Python provides small keywords that let you  
**stop a loop early**, **skip an iteration**,  
or **leave a placeholder while drafting code**.
```

So far, loops have followed a simple pattern:
start, repeat, and stop when the loop condition is done.

Now we add a new capability:

> You can control loop flow **from inside the loop body**.

This is useful for data checking, quality control, and efficient processing.

---

## 1. Placeholders with pass

### Why pass exists

Sometimes you want to write the structure of a loop
before you know what should happen inside it.

`pass` is a placeholder statement that does nothing.
It keeps the code valid while you are drafting.

```python
for i in range(5):
    pass
```

This loop runs, but performs no action.

---

### When to use pass

Use `pass` when you:

* sketch out a loop you will complete later
* create a temporary placeholder while debugging
* want a block that is syntactically required but intentionally empty

---

```{admonition} Note
:class: note

`pass` does nothing on purpose.  
It is not the same as “skip this iteration”.
```

---

## 2. Exiting a loop with break

### Stopping early

`break` ends the loop immediately.
Execution continues with the first line **after** the loop.

This is useful when the goal has been reached
and continuing would be wasted work.

---

### Example: stop when an outlier is found

```python
temperatures = [3, 5, 7, 6, 8, 9, 10, 111, 11]
min_temp = -20
max_temp = 40

for day, temp in enumerate(temperatures, start=1):
    print(f"Day {day}: {temp} °C")
    if temp < min_temp or temp > max_temp:
        print(f"⚠️ Outlier detected on day {day}: {temp} °C")
        break

print("Finished checking the record.")
```

Here, `break` makes the loop stop as soon as a problem is found.

---

### What break changes

Without `break`, the loop would keep checking values.
With `break`, the loop stops early and saves time.

This is a common pattern when:

* searching for the first occurrence of a feature
* detecting the onset of an event
* stopping when a condition is met

---

## 3. Skipping an iteration with continue

### Skip the rest of this round

`continue` skips the remaining code in the loop body
and immediately starts the **next iteration**.

This is useful when some values should be **ignored**
without stopping the loop entirely.

---

### Example: ignore missing values

```python
temperatures = [3, None, 7, 6, None, 9]

for temp in temperatures:
    if temp is None:
        continue
    print(f"Valid value: {temp} °C")
```

Here, the loop simply skips missing entries.

---

### What is None

In Python, `None` represents the **absence of a value**.

It is commonly used to indicate:

* missing data  
* unavailable measurements  
* placeholders where no valid value exists  

`None` is **not** zero, not an empty string, and not `False`.
It is a distinct value with a special meaning.

Because of this, `None` is usually checked explicitly.

---

### A common pattern

Often, `continue` is used as a guard at the top of a loop:

```python
for value in dataset:
    if value is None:
        continue
    # main processing happens below
```

This keeps the main logic less indented and easier to read.

---

## 4. Continue and while loops

### Why continue can be risky

In a `for` loop, the next value is always provided automatically.
So `continue` is usually safe.

In a `while` loop, you often update a control variable yourself.
If `continue` skips that update, the loop may never progress.

---

### Example of the risk

```python
values = [3, None, 7]
index = 0

while index < len(values):
    value = values[index]

    if value is None:
        continue  # index is not updated

    print(value)
    index += 1
```

This code will get stuck on the `None` value because `index` never changes.

---

### Safe pattern

If you use `continue` in a `while` loop,
make sure the control variable is updated first.

```python
values = [3, None, 7]
index = 0

while index < len(values):
    value = values[index]
    index += 1

    if value is None:
        continue

    print(value)
```

Now the loop always progresses.

---

```{admonition} Caution
:class: caution

In a `while` loop, always make sure  
the loop can still progress after `continue`.
```

---

## 5. Exercises

### Exercise 1: Drafting a data check with pass

You are planning to write a quality check for a dataset,
but you are not yet sure what the check should do.

Create a loop that iterates over the indices of a dataset
and prints the index number.

Leave the body of the loop empty for now using `pass`.

```python
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

```python
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

```python
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

```python
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

* `pass` is a placeholder that does nothing  
* `break` exits a loop immediately  
* `continue` skips the rest of the current iteration  

`break` and `continue` are most useful when processing data,
because they let you react immediately to special cases.

---

### What comes next

Next, you will combine everything you have learned:

* repetition with `for` and `while`
* decisions with `if`, `elif`, `else`
* loop control with `pass`, `break`, and `continue`

This gives you a complete toolkit
for writing programs that react to real data in a controlled way.
