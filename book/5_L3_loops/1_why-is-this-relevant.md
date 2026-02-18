---
title: Why Loops Matters

site:
 outline_maxdepth: 1
 
---

<div class="page-subtitle">
From manual work to automation
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/1_why-is-this-relevant.ipynb)

```{admonition} Big idea
:class: tip

Computers are powerful because they can  
**repeat the same action** and  
**make decisions based on data**.

Without repetition and decisions, code does not scale.
```

So far, you have learned how to store values and collections of values.
You can define variables, work with lists, and access individual elements.

However, writing useful programs requires more than storing data.
It requires **processing data systematically**.

This section explains **why** repetition and decisions are necessary
before you learn **how** to implement them.

---

## 1. The Limits of Manual Code

Programming becomes powerful when code can **scale beyond a single value**.

So far, you have learned how to store values and collections.
Now we ask a new kind of question:

> *What if the same operation must be applied to many values,  
> and not all of them should be treated in the same way?*

This is where **repetition** and **decisions** become essential.

---

### From manual work to automation

Consider a simple list of major cities in the Global South:

```python
cities = ["Lagos", "Nairobi", "Dhaka", "São Paulo"]
```

Suppose you want to display each city.

One option is to access each element manually:

```python
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
```

This works, but only as long as the list stays exactly the same.

---

### Why this approach does not scale

Manual repetition quickly becomes a problem.

Issues appear when:

* the list grows longer
* the order of cities changes
* a city is added or removed

For example, adding one more city changes the data:

```python
cities.append("Kinshasa")
```

But the output code still prints only four cities.
You now need to update the code again.
The real issue is not indexing.
The issue is **manual repetition**.

---

```{admonition} Note
:class: note

If changing the data forces you to rewrite the code,  
the code is doing too much manual work.
```

---

## 2. Same Action, Many Values

What we really want to express is not:

> “Print city 0, then city 1, then city 2…”

but rather:

> “For **each city** in this collection, do the same thing.”

This idea is called **repetition**.

Instead of repeating code yourself, you want the *computer* to repeat the work for you.

---

```{admonition}
:class: tip

Good code depends on **structure**,  
not on the current size of the data.
```

Whether there are 3 cities or 300,
the code should behave the same way.

---

## 3. When decisions enter the picture

Repetition alone is not enough.
In many situations, you want to treat values **differently** depending on their properties.

Imagine you want to:

* handle cities differently based on population
* treat coastal and inland cities differently
* skip missing or invalid entries

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

```{admonition} Note
:class: note

Repetition answers:  
“How do I do this for many values?”

Decisions answer:  
“How do I react to differences in data?”
```

## 5. Concept Check

Before learning more syntax, pause and reflect on the idea.

---

### Task

You are given a list of river names:

```python
rivers = ["Nile", "Congo", "Zambezi", "Niger"]
```

Answer the following **without writing code**.

1. If you used **manual indexing**, how many `print()` statements would you need?
2. What would happen to that code if one more river were added?
3. With a loop, would the code need to change if the list grows?


Write down short answers in your own words.

---

```{admonition} Sample solution
:class: dropdown

1. Four `print()` statements, one for each river  
2. You would need to add another line manually  
3. No, the same loop would still work  


**Key insight:**  
The loop adapts to the data.  
Manual code does not.
```

---

### What Comes Next

Next, we will:

* express repetition using `for` loops  
* understand how indentation defines what is repeated  
* see how loop variables change step by step  
* connect loops to lists, indices, and simple grids  

Once this mental model of repetition is in place,
we will add **conditions** so loops can behave differently
for different values.
