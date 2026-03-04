---
title: Why Loops Matter

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
From manual work to automation
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/01_why-is-this-relevant.ipynb)

```{admonition} Big idea
:class: tip

Computers are powerful because they can  
**repeat the same action** and  
**make decisions based on data**.

Without repetition and decisions, code does not scale.

```

So far, you have learned how to store values and collections of values. You can define variables, work with lists, and access individual elements.

However, writing useful spatial programs requires more than just storing data. It requires **processing data systematically**.

This section explains **why** automation is necessary before you learn **how** to implement it.

---

## 1. The Limits of Manual Code

Programming becomes powerful when code can **scale beyond a single value**.

To understand why, let's ask a new kind of question:

> *What if the same operation must be applied to many values?*

Consider a simple list of major cities:

```{code-cell} python
cities = ["Lagos", "Nairobi", "Dhaka", "São Paulo"]

```

Suppose you want to display each city. One option is to access each element manually using its index:

```{code-cell} python
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

```

This works, but only as long as the list stays exactly the same.

---

### Why this approach does not scale

Manual repetition quickly becomes a problem. Issues appear when:

* the list grows longer (imagine 500 cities!)
* the order of cities changes
* a city is added or removed

For example, if you add one more city to the data:

```{code-cell} python
cities.append("Kinshasa")

```

Your code will still only print the first four cities. You would have to manually type `print(cities[4])` to fix it. The real issue here is not indexing; the issue is **manual repetition**.

```{admonition} Avoid manual work
:class: note

If changing your underlying data forces you to rewrite your code,  
your code is doing too much manual work.

```

:::{figure} images/01_loop_vs_sequential_flowchart.png
:alt: A side-by-side flowchart comparing linear code execution with a cyclical loop structure.
:width: 700px
:align: center

*Sequential execution requires writing a new line for every step. A loop reuses the same line of code by cycling through the data until it reaches the end.*
:::

---

## 2. The Solution: Looping

What we really want to express to the computer is not:

> “Print city 0, then print city 1, then print city 2…”

but rather:

> “For **each city** in this collection, print its name.”

This idea is called **iteration** (or looping). Instead of repeating code yourself, you write the instruction once and let the computer repeat the work for you.

Here is a sneak peek of what that looks like in Python:

```{code-cell} python
for city in cities:
    print(city)

```

```{admonition} The Power of Structure
:class: tip

Good code depends on **structure**, not on the current size of the data. 
Whether your list has 4 cities or 4,000 cities, those two lines of code above will process all of them without needing a single change.

```

---

## 3. Making Loops Smarter with Decisions

Repetition alone is incredibly useful, but in real-world spatial data science, you rarely want to treat every single value exactly the same way.

Imagine you want to loop through a massive list of cities, but you only want to:

* print the city if its population is over 1 million
* classify it differently if it is coastal vs. inland
* skip the entry entirely if its coordinates are missing

Now the program must not only repeat actions,
but also **decide** what to do for each value.
This is where **conditions** become important.

---

### From Values to Logic

Every decision has the same basic shape:

* check a condition
* choose what happens next

This introduces another core idea:

> Code can **branch** based on conditions.

This is how programs react to data instead of just processing it blindly.

---

## 4. Repetition & Decisions Go Together

In real workflows, repetition and decisions are often combined.

Typical patterns include:

* go through many values
* decide something about each one

Examples from geospatial and environmental work include:

* checking each coordinate for validity
* classifying cities by region
* filtering measurements based on thresholds

Repetition handles **how many times**.
Decisions handle **what to do**.

---

```{admonition} What is what
:class: note

Repetition answers:  
“How do I do this for many values?”

Decisions answer:  
“How do I react to differences in data?”
```

## 5. Concept Check

Before learning the actual Python syntax for loops, pause and reflect on the concept.

### Task

You are given a list of river names:

```{code-cell} python
rivers = ["Nile", "Congo", "Zambezi", "Niger"]

```

Answer the following **without writing code**.

1. If you used **manual indexing**, how many `print()` statements would you need?
2. What would happen to that manual code if one more river were added to the list?
3. If you used a **loop**, would the code need to change if the list grows?

Write down short answers in your own words.

---

```{admonition} Sample solution
:class: dropdown

1. Four `print()` statements, one for each river.
2. The new river would be ignored unless you manually typed a fifth `print()` statement.
3. No, the exact same loop would automatically process the new river.

**Key insight:** A loop adapts to the size of the data. Manual code does not.

```

---

### What Comes Next

Next, we will:

* express repetition using `for` loops
* understand how indentation defines what gets repeated inside the loop
* see how loop variables change step by step
* connect loops to lists, indices, and simple spatial data

Once this mental model of repetition is in place, we will add **conditions** so your loops can behave dynamically!
