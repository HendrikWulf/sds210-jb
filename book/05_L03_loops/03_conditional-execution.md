---
title: Conditional Statements

site:
 outline_maxdepth: 1
 
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Choosing what happens
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/05_L03_loops/03_conditional-execution.ipynb)

```{admonition} Big idea
:class: tip

Loops repeat actions.  
Conditions decide **what happens** for each value.

Together, they allow code to dynamically react to data.


```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★★★ (A critical bottleneck; absolutely required for tracking the maximum distance in Part 5 and evaluating the even/odd median split in Part 7.)  
**Project Relevance:** ★★★ (Essential for filtering data arrays in project 3 and parsing specific categories or threshold indicators in projects 1 and 2.)  
**Foundation:** ★★★ (The fundamental logic structure for data-driven decision making.)  

**Time to Read:** 20 minutes  
**In a nutshell:** Conditions allow your loops to make decisions, transforming static repetition into dynamic, data-driven workflows like filtering and classification.  
**Skip this if:** You are fully comfortable with `if`, `elif`, and `else` statements, logical operators (`and`, `or`, `not`), and using them inside loops to filter and transform lists.

```

So far, every loop you have written executed the **same instructions** for every value.

Now we take the next step:

> We still repeat actions, but we allow the program's behaviour to change depending on the data it encounters.

---

## 1. Conditions as questions

### When repetition needs decisions

A condition is simply a question that the computer can answer with **yes or no**.

In Python, these answers are represented by the **{term}`Boolean values <Boolean>`**:

* `True`
* `False`

When conditions are used inside a loop, they allow the program to decide what to do for **each individual value**. The loop still steps through the data, but the behavior can change from one value to the next.

---

### Reading conditions in plain language

Conditions are easiest to write and understand when you read them as questions:

* Is this value greater than 10?
* Is this city contained in the list of capitals?
* Is this index equal to zero?

Each condition controls whether a specific block of code is allowed to execute.

```{admonition} Controlling flow
:class: note

Conditions do not stop loops. They control **what happens during** each repetition.


```

---

## 2. Operators for evaluating conditions

### Comparison operators

Comparison operators are used to compare two values against each other.

<!-- markdownlint-disable MD060-->
:::{table} Comparison operators in Python

| Operator | Description               | Comparison example     | Result |
|:--------:|:--------------------------:|:-----------------------:|:------:|
| `==`     | Equal to                  | `"apples" == "oranges"` | False |
| `!=`     | Not equal to              | `"apples" != "oranges"` | True |
| `<`      | Less than                 | `2 < 1`                | False |
| `>`      | Greater than              | `2 > 1`                | True |
| `<=`     | Less than or equal to     | `2 <= 2`               | True |
| `>=`     | Greater than or equal to  | `2 >= 4`               | False |

:::
<!-- markdownlint-enable MD060-->

Each comparison produces a Boolean result: either `True` or `False`. These operators are the most common way to express mathematical or textual conditions in code.

---

### Identity operators

Identity operators check whether two **{term}`variables <Variable>`** refer to the **exact same {term}`object <Object>` in memory**, not just whether they contain the same values.

```python
a is b
a is not b


```

Here is a conceptual example:

```{code-cell} python
a = [1, 2, 3]
b = a          # b points to the exact same list as a
c = [1, 2, 3]  # c is a brand new list with identical values


```

Now compare them:

```{code-cell} python
print(a is b)

```

Both `a` and `b` point to the **same {term}`list <List>`**.

```{code-cell} python
print(a is c)

```

Even though `a` and `c` contain the exact same numbers, they are **different objects** in the computer's memory.

```{admonition} Identity check
:class: note

Use `==` to check if two things have the same *value*.  
Use `is` to check if two names refer to the same *object*.


```

---

### Membership operators

Membership operators test whether a specific value exists inside a collection (like a list or a string).

```python
x in y
x not in y


```

For example:

```{code-cell} python
cities = ["Lima", "Quito", "Bogotá"]

print("Lima" in cities)

print("Santiago" in cities)


```

Membership operators also work seamlessly with **{term}`strings <String>`** to check for substrings:

```{code-cell} python
print("a" in "data")

```

```{admonition} Summary
:class: tip

**Comparison** (`==`, `>`) checks values.  
**Identity** (`is`) checks objects.  
**Membership** (`in`) checks collections.

```

---

## 3. Logical operators (and, or, not)

### Combining conditions

Logical operators allow you to combine **multiple conditions into a single decision**.

The three logical operators in Python are:

* `and` (both conditions must be true)
* `or` (at least one condition must be true)
* `not` (reverses the condition)

They are often used to make highly precise decisions.

### Simple examples

Consider a numeric value:

```{code-cell} python
value = 42

print(value > 0 and value < 100)

```

Both conditions are true, so the whole expression is true.

Now consider membership:

```{code-cell} python
cities = ["Lima", "Quito", "Bogotá"]
capitals = ["Lima", "Buenos Aires"]

print("Quito" in cities or "Quito" in capitals)

```

Only one of the conditions needs to be true for an `or` statement to evaluate to `True`.

Using `not` simply flips the Boolean result:

```{code-cell} python
value = 0
print(not value == 0)

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

When combining several conditions, it is best practice to use parentheses to make the logic clear.

```{code-cell} python
(a < b and b < c) or (a > b)


```

Parentheses:

* improve readability
* prevent logic mistakes
* make the order of evaluation explicit

```{admonition} Guideline
:class: note

If you have to pause and squint to understand a condition, add parentheses or split it into simpler variables.


```

---

#### Concept Check: Evaluating Logic

Predict the Boolean result without running the code:

```python
x = 5
result = (x > 3 and x < 10) or x == 0

```

Is `result` `True` or `False`?

```{admonition} Check your understanding
:class: dropdown

**Answer: True**
The first part `(x > 3 and x < 10)` evaluates to `True` because 5 is between 3 and 10. Because the logical operator linking the two sides is `or`, the fact that the first half is `True` makes the entire expression `True`, completely regardless of whether the `x == 0` part is true or false.

```

---

## 4. Conditional execution (if, elif, else)

### Choosing what happens

So far, conditions have been used purely as **questions**. Now we will use them to **choose between actions**.

Python provides three related keywords for control flow:

* `if` for a single decision
* `if … else` for a two-way split
* `if … elif … else` for multiple paths

### A single decision with if

Use `if` when you want code to run **only if a condition is true**.

```{code-cell} python
temperature = 5

if temperature > 0:
    print("Above freezing")

```

If the condition is false, nothing happens. The program skips the indented block and continues.

---

### Two paths with if and else

Use `else` when there are **exactly two outcomes**. It acts as a catch-all for when the `if` condition is false.

```{code-cell} python
temperature = -2

if temperature > 0:
    print("Above freezing")
else:
    print("Freezing or below")

```

Exactly one of the two blocks will run. Never both.

---

### Multiple paths with if, elif, and else

When more than two cases are possible, use `elif` (short for "else if").

Python checks conditions **from top to bottom**. As soon as one condition evaluates to `True`, it runs that block and **skips the rest of the chain**.

```{code-cell} python
temperature = -3

if temperature > 0:
    print(f"{temperature} degrees is above freezing")
elif temperature == 0:
    print(f"{temperature} degrees is at the freezing point")
else:
    print(f"{temperature} degrees is below freezing")

```

:::{figure} images/04_if_elif_else_flowchart.png
:alt: Flowchart illustrating sequential evaluation in an if-elif-else chain, showing Python stopping after the first True condition.
:width: 500px
:align: center

*An `if-elif-else` chain acts like a filter. Python checks conditions sequentially; once it finds a match (True), it executes that code block and immediately exits the chain, ignoring all remaining conditions.*
:::

```{admonition} Order matters
:class: note

Only one branch of an `if-elif-else` chain will ever run. Because Python stops checking as soon as it finds a `True` statement, **order matters**. Always put your most specific conditions at the top!

```

---

### Reading conditional chains

It helps to read the logic like a checklist:

1. Is the first condition true
2. If not, try the next one
3. If none match, use the fallback (`else`)

This makes conditional execution predictable and easy to debug.

---

#### Concept Check: The Execution Order

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

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
1. `yesterday <= today` (14 <= 10) → False. Python moves to the next.
2. `today != tomorrow` (10 != 13) → True. Python prints "B".
3. Because a `True` condition was found, Python **skips the rest of the block entirely**. It never even looks at "C" or "D", even though `yesterday > tomorrow` and `today == today` are both technically True. Only the *first* True block in an `if-elif` chain executes.

```

---

## 5. Decisions inside loops

### Using if inside a loop

Conditions become very powerful when placed **inside loops**.

```{code-cell} python
values = [3, 12, 7, 25]

for v in values:
    if v > 10:
        print(v)

```

The loop still processes **every value** in the list. However, only values that satisfy the condition (`v > 10`) are printed.

* The loop controls *how often* the code runs.
* The condition controls *what happens* for each specific value.

:::{figure} images/05_filtering_vs_transforming.png
:alt: Conceptual diagram showing an input list being processed on the left via 'filtering' (reducing list size) and on the right via 'transforming' (maintaining list size but changing values).
:width: 600px
:align: center

*Filtering creates a smaller subset of data based on a rule. Transforming alters the content of the data while maintaining the overall structure and size.*
:::

---

### Filtering values

**Filtering** means selecting some values and ignoring the rest.

In the previous example, values greater than 10 are printed, while smaller values are skipped. Filtering is a core data science pattern used to:

* select spatial data above or below an elevation threshold
* remove invalid or missing coordinate entries
* focus analysis on a specific country or region

---

### Transforming values

**Transforming** means changing values depending on a condition.

```{code-cell} python
for v in values:
    if v > 10:
        print(v * 2)
    else:
        print(v)


```

Here:

* values greater than 10 are doubled
* other values are printed unchanged

Unlike filtering, transforming generally produces an output for *every* value, but the output itself depends on the condition.

```{admonition} Filtering vs. Transforming
:class: note

**Filtering** decides *which values* are kept.  
**Transforming** decides *how values change*.

```

---

<!-- markdownlint-disable MD033 -->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L03_ch3_01_filtering_vs_transforming/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Filtering vs. Transforming.</b><br>
    Click the action buttons to watch the values flow through the loop. Notice how "Filtering" ignores elements that fail the condition resulting in a shorter final list, while "Transforming" evaluates every element and creates an altered list of the exact same length. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L03_ch3_01_filtering_vs_transforming/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

#### Concept Check: Identify the Operation

Before running the code below, look at the logic structure:

```python
values = [5, 15, 8]

for v in values:
    if v > 10:
        print(v + 1)
    else:
        print(v - 1)

```

Is this an example of filtering or transforming? What will the printed output be?

```{admonition} Check your understanding
:class: dropdown

**Answer: Transforming (Output: 4, 16, 7)**
This is transforming because every single value from the input list produces a modified output value (the list length is maintained). 
- `5` is not > 10, so it hits `else` and becomes `4`.
- `15` is > 10, so it hits `if` and becomes `16`.
- `8` is not > 10, so it hits `else` and becomes `7`.

```

---

## 6. Exercises

The following exercises help you practise how **conditions and loops work together**.

Focus on understanding *when a condition is checked* and *what effect it has inside the loop*.

---

### Exercise 1: Filtering values

You are given a list of temperatures:

```{code-cell} python
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

```{code-cell} python
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

```text
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

```{code-cell} python
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

```{code-cell} python
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

```text
odd
even
odd
odd
even
```

**Key idea:** Conditions are evaluated separately for each loop iteration.

````

---

## 7. Summary

In this chapter, you learned how **repetition and decisions work together**.

### Key ideas

* Loops control **how often** code runs.
* Conditions control **what happens** for each value.
* Conditions evaluate to `True` or `False`.
* Operators allow values (`==`), objects (`is`), and collections (`in`) to be tested.
* Logical operators (`and`, `or`, `not`) combine conditions.
* Placing `if` inside a loop enables core data workflows like **filtering** and **transforming**.

```{admonition} Mental models to keep
:class: tip

A loop answers:  
“How many times should this run?”

A condition answers:  
“What should happen this time?”

Readable code makes both answers instantly obvious to whoever is reading it.

```

---

### What comes next

So far, your decisions have happened inside a loop that already knows **how long it will run**.
Next, you will learn a new kind of repetition: a loop that continues **until a condition changes**.
You will meet the while loop, which is useful when you do not know in advance how many repetitions are needed.
The key shift is this:

* for loops focus on **what to loop over**
* while loops focus on **when to stop**
