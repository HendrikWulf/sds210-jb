---
title: Practical L3

site:
  outline_maxdepth: 1

---

<div class="page-subtitle">
From structured data to automated spatial logic
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/07_practical-L3.ipynb)

---

## Learning objectives

After completing this practical, you will be able to:

* iterate over lists and dictionaries using `for` loops
* combine loops with conditional logic
* automate distance calculations between multiple cities
* store and analyse results during iteration
* stop loops early when a condition is met
* choose between `for` and `while` loops based on the task

---

## Practical storyline

In the previous practical, you manually calculated distances between **pairs of cities**. In this practical, you will **automate** this process.

You will work with a small spatial dataset and:
* replace repeated code with loops
* compute distances for *all* city pairs
* identify the **most distant** cities
* calculate the **median distance** across the network
* stop processing early when a condition is met

This mirrors a typical spatial data science workflow: from **manual calculations** to **systematic processing**.

---

## Part 1 – Preparing the data

We start with a small dataset of cities and coordinates. To work efficiently, we combine names and coordinates into a dictionary.

### Code

```{code-cell} python
cities = ["Zurich", "Geneva", "Lugano"]

coordinates = [
    [2682217, 1247945],   # Zurich
    [2499959, 1117840],   # Geneva
    [2720031, 1098728]    # Lugano
]

city_data = {}

for i in range(len(cities)):
    city_data[cities[i]] = coordinates[i]

print(city_data)

```

### Tasks

1. Print the coordinates of Geneva using the dictionary.
2. Add one more city with coordinates of your choice to the original lists.
3. Explain in a comment why a dictionary is useful here.

```{code-cell} python

```

---

## Part 2 – Looping over structured data

You now have a dictionary that links **city names** to **coordinates**. Your goal in this part is to **loop over that structure** and produce readable output **without hardcoding any city names**.

### Tasks

Write a loop that iterates over all cities in `city_data` and prints the city name together with its coordinates.

1. Use an **f-string** for formatting.
2. Modify the output to include coordinate units (e.g., km).
3. Add a comment explaining **what the loop variable `city` represents**.

```{code-cell} python

```

---

## Part 3 – Generating city pairs

To calculate distances systematically, cities must be compared **pairwise**. Your task is to generate **all unique city pairs** from the dataset, avoiding duplicate and self-comparisons.

### Tasks

Write code that extracts all city names from `city_data` and uses **nested loops** to store each unique pair as a tuple in a list.

1. Explain in a comment why the inner loop starts at `i + 1`.
2. Verify that no city is paired with itself.
3. Count how many city pairs are generated and explain why this number makes sense.

```{code-cell} python

```

---

## Part 4 – Computing distances for all pairs

You now have a list of unique city pairs. The next step is to compute distances automatically for each pair and store the results.

For reference, the mathematical formulas are:

**Euclidean distance:**


$$d_{euclidean}=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

**Manhattan distance:**


$$d_{manhattan}=|x_2-x_1|+|y_2-y_1|$$

### Tasks

Write code that loops over all city pairs, computes both Euclidean and Manhattan distances, and stores the results in a nested dictionary. Print a readable summary for each pair.

1. Explain in a comment why the distance calculation must happen **inside the loop**.
2. Inspect the structure of the `distances` dictionary and explain how it resembles an **attribute table** in GIS.

```{code-cell} python

```

---

## Part 5 – Tracking the maximum distance

Now you want to answer a question using your computed results:

> Which two cities are the **most distant** from each other?

### Tasks

Write code that iterates over the `distances` dictionary, checks the Euclidean distance for each pair, and updates a tracking variable to find the maximum distance.

1. Repeat the same logic using **Manhattan distance** instead of Euclidean.
2. Compare the results: Are the most distant city pairs the same? If not, why might that happen?
3. Explain why **tracking values during iteration** is more efficient than checking results afterwards.

```{code-cell} python

```

---

## Part 6 – Stopping early with `break`

Sometimes you already have your answer before the loop reaches the end. For example, stopping as soon as a distance exceeds a critical threshold.

### Tasks

Write code that loops over all city pairs, computes the Euclidean distance, and uses `break` to stop the loop immediately if the distance exceeds `200000`.

1. Explain what happens **immediately after** `break` is executed.
2. Discuss situations in spatial data science where early stopping saves time.

```{code-cell} python

```

---

## Part 7 – Median and ordering

Loops are often used to **prepare data for analysis**. Here, you will extract the Euclidean distances you computed earlier and discover why **data ordering matters** for statistical calculations.

### Tasks

1. Create an empty list called `euclidean_list`. Loop through the `distances` dictionary from Part 4, extract the Euclidean distance for each pair, and append it to the list.
2. Compute the **median** of `euclidean_list` using index logic (`// 2`).
3. **The Problem:** If you run your median calculation on the list exactly as it was extracted from the dictionary, your result is likely incorrect. Why? What hidden assumption does the median rely on?
4. **The Fix:** Fix the calculation by sorting the data *before* computing the median.

```{code-cell} python

```

---

## Part 8 – Optional – Fibonacci sequence

### Tasks

1. Generate a Fibonacci sequence of exactly 10 values using a `for` loop. Why does the loop start at index `2`?
2. Generate a Fibonacci sequence using a `while` loop that stops only when a value exceeds `100`.

```{code-cell} python

```

---

## Reflection

Answer briefly in comments or markdown:

1. What did loops automate for you in this practical?
2. Where did conditions change program behaviour?
3. When would you use `for` instead of `while`?

```{code-cell} python

```

---

## What comes next

Next, you will learn how to *package logic into functions* and reuse the same logic without copying code. Functions are the next step from *working code* to **well-structured code**. They allow you to turn patterns you used in this practical (for example distance calculation or median logic) into reusable building blocks.
