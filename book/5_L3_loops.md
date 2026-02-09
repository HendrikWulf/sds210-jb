---
title: L3 - Loops

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Controlling program flow
</div>

---

In the previous lesson, you learned how to **store and organise data** using variables, lists, and dictionaries.

That was an essential step, but it raises an obvious next question:

> What if we want to apply the **same operation** to many values?

So far, every calculation you wrote was **explicit**:
you told Python exactly which values to use and exactly what to do with them.

This lesson introduces a shift in how you think about code.

Instead of writing *more lines*, you will learn how to write **rules** that Python can apply automatically.

---

## From data to behaviour

Once data is stored in collections, such as lists or dictionaries, the real power of programming comes from being able to:

* repeat operations
* react to different values
* stop or change behaviour based on conditions

This is where **loops** and **conditional logic** come in.

Loops control **repetition**.
Conditions control **decisions**.

Together, they define the **flow of a program**:
what runs, how often, and under which circumstances.

---

## Why loops matter

Without loops, programs do not scale.

Imagine spatial analysis without repetition:

* calculating distances for each city pair manually
* checking every measurement one by one
* writing the same formula dozens of times

Loops allow you to express intent instead of repetition:

> “Do this for every value.”
> “Keep going until a condition is met.”
> “Stop as soon as something important happens.”

This lesson teaches you how to express these ideas clearly and safely.

---

## Why this matters for SDS

In spatial data science, repetition is unavoidable:

* features are processed one by one
* attributes are checked for validity
* distances, areas, and statistics are computed repeatedly
* workflows must scale from small examples to large datasets

Loops are the bridge between:

* **structured data** (what you learned in Lesson 2)
* **automated analysis** (what you will do throughout the course)

They turn static data into **dynamic processes**.

---

## Learning objectives

After this lesson, you will be able to:

* **Control program flow with conditions**
  Use `if`, `elif`, and `else` statements to compare values and make decisions based on logical conditions.

* **Repeat operations using loops**
  Apply `for` and `while` loops to iterate over sequences and repeat code in a controlled and readable way.

* **Process collections programmatically**
  Combine loops and conditional statements to filter, transform, and analyse values stored in lists and dictionaries.

---

## Looking ahead

Lesson 3 is about **making code do more work for you**.

You learn not only *how loops work*, but how to:

* reason about program execution step by step
* avoid common logical and flow errors
* write loops that are clear, safe, and purposeful

These skills are essential whenever your code must process more than a single value.

In the next lesson, you will take this one step further by learning how to **package repeated logic into functions**.
Functions allow you to turn loops and conditions into **named, reusable units**, making your code easier to read, test, and extend.

If Lesson 2 was about *thinking in data*,
Lesson 3 is about **thinking in processes**—
and Lesson 4 will be about **thinking in structure and reuse**.
