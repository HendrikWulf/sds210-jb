---
title: Practical L3 - Solutions

site:
  outline_maxdepth: 1

---

<div class="page-subtitle">
From structured data to automated spatial logic
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/5_L3_loops/08_practical-L3-solution.ipynb)

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

---

``````{admonition} Sample solution – Part 1
:class: dropdown

```{code-cell} python
# 2. Adding a new city
cities = ["Zurich", "Geneva", "Lugano", "Basel"]

coordinates = [
    [2682217, 1247945],   # Zurich
    [2499959, 1117840],   # Geneva
    [2720031, 1098728],   # Lugano
    [2611415, 1267104]    # Basel
]

# Standard looping method to build the dictionary
city_data = {}
for i in range(len(cities)):
    city_data[cities[i]] = coordinates[i]

# 1. Print Geneva's coordinates
print(f"Geneva coordinates: {city_data['Geneva']}")

# 3. Why dictionaries are useful:
# A dictionary links the human-readable city name (key) directly to its spatial 
# location (value). This allows us to look up data intuitively by name without 
# needing to memorize its exact index position in a list.
```

``````

---

## Part 2 – Looping over structured data

You now have a dictionary that links **city names** to **coordinates**. Your goal in this part is to **loop over that structure** and produce readable output **without hardcoding any city names**.

### Tasks

Write a loop that iterates over all cities in `city_data` and prints the city name together with its coordinates.

1. Use an **f-string** for formatting.
2. Modify the output to include coordinate units (e.g., km).
3. Add a comment explaining **what the loop variable `city` represents**.

---

``````{admonition} Sample solution – Part 2
:class: dropdown

```{code-cell} python
# The loop variable 'city' represents the current dictionary key (the city name)
# being processed in the current iteration of the loop.

# We use .items() to cleanly access both the key and the value at the same time
for city, coords in city_data.items():
    print(f"{city}: X = {coords[0]} m, Y = {coords[1]} m")
```

``````

---

## Part 3 – Generating city pairs

To calculate distances systematically, cities must be compared **pairwise**. Your task is to generate **all unique city pairs** from the dataset, avoiding duplicate and self-comparisons.

### Tasks

Write code that extracts all city names from `city_data` and uses **nested loops** to store each unique pair as a tuple in a list.

1. Explain in a comment why the inner loop starts at `i + 1`.
2. Verify that no city is paired with itself.
3. Count how many city pairs are generated and explain why this number makes sense.

---

``````{admonition} Sample solution – Part 3
:class: dropdown

```{code-cell} python
city_names = list(city_data.keys())
pairs = []

for i in range(len(city_names)):
    for j in range(i + 1, len(city_names)):
        pairs.append((city_names[i], city_names[j]))

print(pairs)

# 1. Why start at i + 1?
# If the inner loop started at 0, we would get self-pairs (Zurich, Zurich) and 
# reversed duplicates (Zurich, Geneva AND Geneva, Zurich). Starting at `i + 1` 
# ensures we only pair a city with cities that come *after* it in the list.

# 3. Pair count
print(f"\nTotal unique pairs generated: {len(pairs)}")
# With 4 cities, the combinations are:
# City 1 pairs with 3 others.
# City 2 pairs with 2 others.
# City 3 pairs with 1 other.
# City 4 is already paired with everyone.
# 3 + 2 + 1 = 6 pairs.
```

``````

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

---

``````{admonition} Sample solution – Part 4
:class: dropdown

```{code-cell} python
distances = {}

for city_a, city_b in pairs:
    xa, ya = city_data[city_a]
    xb, yb = city_data[city_b]

    dx = xa - xb
    dy = ya - yb

    euclidean = (dx**2 + dy**2) ** 0.5
    manhattan = (dx**2) ** 0.5 + (dy**2) ** 0.5

    # Store in dictionary
    distances[(city_a, city_b)] = {
        "euclidean": euclidean,
        "manhattan": manhattan
    }

    print(f"{city_a} – {city_b}: Euclidean={euclidean:.2f}, Manhattan={manhattan:.2f}")

# 1. Why inside the loop?
# The coordinates change with every iteration as we move to a new city pair. 
# If the calculation were outside the loop, it would only calculate the distance 
# once, using whatever variables happened to exist at the end.

# 2. GIS Attribute Table Comparison
# The 'distances' dictionary acts like an attribute table:
# - The dictionary keys (the city pair tuples) act as the unique Row IDs.
# - The inner dictionaries act as columns/attributes (euclidean, manhattan) 
#   storing specific feature data for that pair.
```

``````

---

## Part 5 – Tracking the maximum distance

Now you want to answer a question using your computed results:

> Which two cities are the **most distant** from each other?

### Tasks

Write code that iterates over the `distances` dictionary, checks the Euclidean distance for each pair, and updates a tracking variable to find the maximum distance.

1. Repeat the same logic using **Manhattan distance** instead of Euclidean.
2. Compare the results: Are the most distant city pairs the same? If not, why might that happen?
3. Explain why **tracking values during iteration** is more efficient than checking results afterwards.

---

``````{admonition} Sample solution – Part 5
:class: dropdown

```{code-cell} python
max_euclidean = 0
most_distant_euclidean = None

max_manhattan = 0
most_distant_manhattan = None

for pair, metrics in distances.items():
    # Track Euclidean
    d_euc = metrics["euclidean"]
    if d_euc > max_euclidean:
        max_euclidean = d_euc
        most_distant_euclidean = pair

    # Track Manhattan
    d_man = metrics["manhattan"]
    if d_man > max_manhattan:
        max_manhattan = d_man
        most_distant_manhattan = pair

print(f"Most distant cities (Euclidean): {most_distant_euclidean} ({max_euclidean:.2f})")
print(f"Most distant cities (Manhattan): {most_distant_manhattan} ({max_manhattan:.2f})")

# 2. Comparing Results
# They can differ! Two cities might be far apart diagonally (high Euclidean) 
# but another pair might have a massive difference strictly along the X or Y 
# axis (high Manhattan).

# 3. Why tracking is efficient
# Tracking the maximum value during the loop means we only have to read 
# through the data once. If we stored everything and then looped again to 
# find the maximum, we would be making the computer do extra work.
```

``````

---

## Part 6 – Stopping early with `break`

Sometimes you already have your answer before the loop reaches the end. For example, stopping as soon as a distance exceeds a critical threshold.

### Tasks

Write code that loops over all city pairs, computes the Euclidean distance, and uses `break` to stop the loop immediately if the distance exceeds `200000`.

1. Explain what happens **immediately after** `break` is executed.
2. Discuss situations in spatial data science where early stopping saves time.

---

``````{admonition} Sample solution – Part 6
:class: dropdown

```{code-cell} python
threshold = 200000

for city_a, city_b in pairs:
    xa, ya = city_data[city_a]
    xb, yb = city_data[city_b]

    distance = ((xa - xb)**2 + (ya - yb)**2) ** 0.5

    if distance > threshold:
        print(f"Threshold exceeded by {city_a} and {city_b}: {distance:.2f}")
        break

# 1. What happens after 'break'?
# The loop completely terminates. The program skips any remaining 
# iterations and moves on to the first line of code outside the loop.

# 2. Spatial Data Science Use Cases
# In proximity searches (e.g., "Find ANY hospital within 5km of a crash"), 
# once you find the first hospital that meets the criteria, you can 'break'. 
# Continuing to check the other 500 hospitals would waste processing power.
```

``````

---

## Part 7 – Median and ordering

Loops are often used to **prepare data for analysis**. Here, you will extract the Euclidean distances you computed earlier and discover why **data ordering matters** for statistical calculations.

### Tasks

1. Create an empty list called `euclidean_list`. Loop through the `distances` dictionary from Part 4, extract the Euclidean distance for each pair, and append it to the list.
2. Compute the **median** of `euclidean_list` using index logic (`// 2`).
3. **The Problem:** If you run your median calculation on the list exactly as it was extracted from the dictionary, your result is likely incorrect. Why? What hidden assumption does the median rely on?
4. **The Fix:** Fix the calculation by sorting the data *before* computing the median using `sort()` (`list_sorted = list.sort()`).

---

``````{admonition} Sample solution – Part 7
:class: dropdown

```{code-cell} python
# Task 1: Extract distances
euclidean_list = []
for metrics in distances.values():
    euclidean_list.append(metrics["euclidean"])

# Task 3 & 4: The hidden assumption is that median requires ORDERED data.
# Dictionaries (and lists derived from them) are not guaranteed to be ordered.
euclidean_list.sort() # <--- This line fixes the problem!

# Task 2: Compute median
list_len = len(euclidean_list)

if list_len % 2 == 0:
    # Even number of elements (average the two middle ones)
    j = list_len // 2
    median = (euclidean_list[j - 1] + euclidean_list[j]) / 2
else:
    # Odd number of elements
    j = list_len // 2
    median = euclidean_list[j]

print(f"Sorted distances: {[round(d, 2) for d in euclidean_list]}")
print(f"Median network distance: {median:.2f}")
```

``````

---

## Part 8 – Optional – Fibonacci sequence

### Tasks

1. Generate a Fibonacci sequence of exactly 10 values using a `for` loop. Why does the loop start at index `2`?
2. Generate a Fibonacci sequence using a `while` loop that stops only when a value exceeds `100`.

---

``````{admonition} Sample solution – Part 8
:class: dropdown

```{code-cell} python
# Task 1: Fixed length (for loop)
n = 10
fib_fixed = [0, 1]

# We start at index 2 because indices 0 and 1 are already defined!
for i in range(2, n):
    next_value = fib_fixed[i - 1] + fib_fixed[i - 2]
    fib_fixed.append(next_value)

print(f"Fixed length sequence: {fib_fixed}")

# Task 2: Threshold condition (while loop)
threshold = 100
fib_cond = [0, 1]
index = 2

while True:
    next_value = fib_cond[index - 1] + fib_cond[index - 2]
    fib_cond.append(next_value)

    if next_value > threshold:
        print(f"\nThreshold exceeded at index {index}: {next_value}")
        print(f"Previous value at index {index - 1}: {fib_cond[index - 1]}")
        break

    index += 1
```

``````

---

## Reflection

Answer briefly in comments or markdown:

1. What did loops automate for you in this practical?
2. Where did conditions change program behaviour?
3. When would you use `for` instead of `while`?

---

```{admonition} Sample solution – Reflection
:class: dropdown

1. Loops automated the repetitive task of comparing multiple geographical points. Instead of writing separate math equations for Zurich-Geneva, Geneva-Lugano, etc., we wrote the math once and let the loop apply it to all possible pairs.
2. Conditions (`if` statements) allowed the program to dynamically track the maximum value, handle even vs. odd list lengths for the median, and trigger the `break` command to stop processing early.
3. You use a `for` loop when you know exactly how many times you need to iterate (e.g., looping over all items in a finite list). You use a `while` loop when you do not know the number of iterations in advance, and instead need the loop to run until a specific logical condition is met (like surpassing a threshold).

```

---

## What comes next

Next, you will learn how to *package logic into functions* and reuse the same logic without copying code. Functions are the next step from *working code* to **well-structured code**. They allow you to turn patterns you used in this practical (for example distance calculation or median logic) into reusable building blocks.
