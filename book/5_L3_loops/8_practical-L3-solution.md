---
title: Practical L3 - solutions

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

In the previous practical, you manually calculated distances between **pairs of cities**.

In this practical, you will **automate** this process.

You will work with a small spatial dataset and:

* replace repeated code with loops
* compute distances for *all* city pairs
* identify the **most distant** cities
* stop processing early when a condition is met

This mirrors a typical spatial data science workflow:
from **manual calculations** to **systematic processing**.

---

## Part 1 – Preparing the data

We start with a small dataset of cities and coordinates.

```python
cities = ["Zurich", "Geneva", "Lugano"]

coordinates = [
    [26, 12],   # Zurich
    [25, 11],   # Geneva
    [27, 10]    # Lugano
]
```

To work efficiently, we combine names and coordinates into a dictionary.

```python
city_data = {}

for i in range(len(cities)):
    city_data[cities[i]] = coordinates[i]

city_data
```

---

### Tasks

1. Print the coordinates of Geneva using the dictionary.
2. Add one more city with coordinates of your choice.
3. Explain in a comment why a dictionary is useful here.

---

## Part 2 – Looping over structured data

You now have a dictionary that links **city names** to **coordinates**.

Your goal in this part is to **loop over that structure** and produce readable output **without hardcoding any city names**.

Instead of printing individual values manually, you will let the loop handle *all* cities automatically.

---

### Task: inspect all cities and their coordinates

Write a loop that:

* iterates over all cities in `city_data`
* retrieves the coordinates for each city
* prints the city name together with its coordinates
* uses an **f-string** for formatting

Your output should clearly show:

* which city is being processed
* which values represent x and y

Do **not** hardcode any city names.

---

````{admonition} Get started with example code
:class: dropdown

Use this as a starting point if you are unsure how to begin.
Try to adapt and extend it rather than copying it unchanged.

```python
for city in city_data:
    coords = city_data[city]
    print(f"{city}: x={coords[0]}, y={coords[1]}")
```

````

---

### Follow-up tasks

Once your loop works:

1. Modify the output to include coordinate units.  
2. Change the wording or structure of the f-string to improve readability.  
3. Add a comment explaining **what the loop variable `city` represents**.

---

## Part 3 – Generating city pairs

To calculate distances, cities must be compared **pairwise**.

Your task is to generate **all unique city pairs** from the dataset, such that:

* every pair consists of **two different cities**
* no pair appears twice in reversed order
  (for example, `(Zurich, Geneva)` but not `(Geneva, Zurich)`)

This step prepares the data structure needed for systematic distance calculations.

---

### Task: build a list of unique city pairs

Write code that:

* extracts all city names from `city_data`
* uses **nested loops** to generate city pairs
* stores each pair as a tuple in a list
* avoids duplicate and self comparisons

At the end, print or display the list of pairs.

---

````{admonition} Get started with example code
:class: dropdown

Use this structure as a starting point.
Focus on understanding *why* it works.

```python
city_names = list(city_data.keys())

pairs = []

for i in range(len(city_names)):
    for j in range(i + 1, len(city_names)):
        pairs.append((city_names[i], city_names[j]))

pairs
```

````

---

### Follow-up tasks

After your code runs:

1. Explain in a comment why the inner loop starts at `i + 1`.  
2. Verify that no city is paired with itself.  
3. Count how many city pairs are generated and explain why this number makes sense.

---

## Part 4 – Computing distances for all pairs

You now have a list of **unique city pairs**.

The next step is to **compute distances automatically** for each pair and store the results in a structured way.

Your goal is to calculate **both**:

* Euclidean distance
* Manhattan distance

for **every city pair**, without repeating code manually.

---

### Task: compute and store distances

Write code that:

* loops over all city pairs
* retrieves coordinates for each city
* computes Euclidean and Manhattan distances
* stores the results in a dictionary
* prints a readable summary for each pair using an f-string

The result should allow you to **reuse distances later**, not just print them once.

---

````{admonition} Get started with example code
:class: dropdown

Use this structure as a starting point.
Focus on *where* each operation belongs.

```python
distances = {}

for city_a, city_b in pairs:
    xa, ya = city_data[city_a]
    xb, yb = city_data[city_b]

    dx = xa - xb
    dy = ya - yb

    euclidean = (dx**2 + dy**2) ** 0.5
    manhattan = (dx**2) ** 0.5 + (dy**2) ** 0.5

    distances[(city_a, city_b)] = {
        "euclidean": euclidean,
        "manhattan": manhattan
    }

    print(
        f"{city_a} – {city_b}: "
        f"Euclidean={euclidean:.2f}, "
        f"Manhattan={manhattan:.2f}"
    )
```

````

---

### Follow-up tasks

After running your code:

1. Explain in a comment why the distance calculation must happen **inside the loop**.  
2. Inspect the structure of the `distances` dictionary.  
3. Explain how this structure resembles an **attribute table** in GIS  
   (rows, columns, and attributes).

---

## Part 5 – Tracking the maximum distance

So far, you have computed distances for **all city pairs**.

Now you want to **answer a question** using those results:

> Which two cities are the **most distant** from each other?

To do this, you need to:

* loop over computed distances
* compare values step by step
* keep track of the current maximum
* remember *which pair* produced it

This is a classic pattern in data analysis.

---

### Task: find the most distant city pair

Write code that:

* iterates over the `distances` dictionary
* checks the Euclidean distance for each pair
* updates the current maximum when a larger value is found
* stores both the distance **and** the corresponding city pair
* prints a message whenever a new maximum is detected
* prints the final result after the loop finishes

---

````{admonition} Get started with example code
:class: dropdown

Use this structure as a guide.
Focus on *why* each variable exists.

```python
max_distance = 0
most_distant_pair = None

for pair in distances:
    d = distances[pair]["euclidean"]

    if d > max_distance:
        max_distance = d
        most_distant_pair = pair
        print(
            f"New maximum found: {pair} "
            f"with distance {d:.2f}"
        )

print(
    f"\nMost distant cities: {most_distant_pair} "
    f"({max_distance:.2f})"
)
```

````

---

### Follow-up tasks

After running your code:

1. Repeat the same logic using **Manhattan distance** instead of Euclidean.  
2. Compare the results:  
   - Are the most distant city pairs the same?
   - If not, why might that happen?  
3. Explain in your own words why **tracking values during iteration**
   is more efficient than checking results afterwards.

---

## Part 6 – Stopping early with `break`

So far, your loops have processed **all city pairs**.

Sometimes, however, you already have your answer
**before the loop reaches the end**.

For example:

> Stop as soon as a distance exceeds a critical threshold.

In such cases, continuing the loop would waste time
and make the logic harder to follow.

This is where `break` becomes useful.

---

### Task: stop when a distance exceeds a threshold

Write code that:

* loops over all city pairs
* computes the Euclidean distance
* checks whether the distance exceeds a given threshold
* prints a warning message when this happens
* **stops the loop immediately**

---

````{admonition} Get started with example code
:class: dropdown

Use this structure as a starting point.
Focus on the role of `break`.

```python
threshold = 2.5

for city_a, city_b in pairs:
    xa, ya = city_data[city_a]
    xb, yb = city_data[city_b]

    distance = ((xa - xb)**2 + (ya - yb)**2) ** 0.5

    if distance > threshold:
        print(
            f"Threshold exceeded by {city_a} and {city_b}: "
            f"{distance:.2f}"
        )
        break
```

````

---

### Follow-up tasks

After running your code:

1. Explain what happens **immediately after** `break` is executed.  
2. Change the threshold value and observe:
   - when the loop stops  
   - which city pair triggers the stop  
3. Discuss situations in spatial data science where:
   - early stopping saves time  
   - continuing to loop would not add new information  

---

## Part 7 – Median and ordering

Loops are often used to **prepare data for analysis**.

Here, you will work with a numeric sequence and discover
why **data ordering matters** for statistical calculations.

---

### Task 1: create a numeric sequence

Write code that:

* creates an empty list
* fills it with `size` values using a `for` loop
* stores the values in **increasing order**

For example, the values could follow a simple pattern
such as doubling the loop index.

---

````{admonition} Get started with code
:class: dropdown

Use this structure as a starting point.

```python
numbers = []
size = 10

for i in range(size):
    numbers.append(i * 2)

numbers
```

````

---

### Task 2: compute the median

Now compute the **median** of the list.

Recall:

- if the list length is odd: take the middle value  
- if the list length is even: average the two middle values  

Write code that:

- checks whether the list length is even or odd
- selects the correct index or indices
- prints the median using an f-string

---

````{admonition} Get started with code
:class: dropdown

Use this logic as a guide.

```python
numbers_len = len(numbers)
median = None

if numbers_len % 2 == 0:
    j = numbers_len // 2
    median = (numbers[j - 1] + numbers[j]) / 2
else:
    j = numbers_len // 2
    median = numbers[j]

print(f"Median: {median}")
```

````

---

### Follow-up questions

After running the code:

1. Change `size` to an odd number and rerun the cell.  
2. Explain why integer division (`//`) is used for the index.  
3. Explain why the median logic works **in this case**.

---

### Task 3: break the assumption

Now replace the ordered list with an **unordered one**:

```python
numbers = [12, 3, 19, 7, 5, 10]
```

Reuse **exactly the same median code** as before.

---

### Questions

1. What median value do you get?
2. Why is this result incorrect?
3. What hidden assumption does the median calculation rely on?

---

### Task 4: fix the problem

Fix the median calculation by adding **one single line of code**
*before* computing the median.

---

````{admonition} Sample solution
:class: dropdown

```python
numbers.sort()
```

**Explanation:**

The median definition assumes **ordered data**.
Sorting restores that assumption before the calculation.

````

---

## Part 8 – Optional – Fibonacci sequence

This challenge brings together everything you have learned about:

* lists
* indexing
* `for` and `while` loops
* stopping conditions
* tracking values during iteration

The **Fibonacci sequence** starts with:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Each new value is the **sum of the two previous values**.

---

### Task A: generate a fixed number of values

Write code that:

* starts with a list containing the first two Fibonacci values
* uses a `for` loop to generate the next values
* stops after a fixed number of elements
* stores all values in a list

Think carefully about:

* where the loop starts
* which indices are needed to compute the next value

---

````{admonition} Get started with code
:class: dropdown

Use this structure as a starting point.

```python
n = 10
fibonacci = [0, 1]

for i in range(2, n):
    next_value = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_value)

fibonacci
```

````

---

### Questions

1. Why does the loop start at index `2`?  
2. Which values are used to compute each new number?  
3. What would happen if you changed `n`?

---

### Task B: stop based on a condition

Now solve the **same problem differently**.

Instead of stopping after a fixed number of steps,
stop when the sequence **exceeds a threshold value**.

Write code that:

- keeps generating Fibonacci numbers  
- stops as soon as a value exceeds a given threshold  
- prints  
  - the index of the value that exceeds the threshold  
  - the previous value and its index  

Here, you do **not** know in advance how many values are needed.

---

````{admonition} Get started with code
:class: dropdown

Use this pattern as guidance.

```python
threshold = 100
fibonacci = [0, 1]
index = 2

while True:
    next_value = fibonacci[index - 1] + fibonacci[index - 2]
    fibonacci.append(next_value)

    if next_value > threshold:
        print(f"Threshold exceeded at index {index}: {next_value}")
        print(
            f"Previous value at index {index - 1}: "
            f"{fibonacci[index - 1]}"
        )
        break

    index += 1
```

````

---

## Reflection

Answer briefly in comments or markdown:

1. What did loops automate for you in this practical?
2. Where did conditions change program behaviour?
3. When would you use `for` instead of `while`?

---

## What comes next

Next, you will learn how to *package logic into functions* and reuse the same logic without copying code.
Functions are the next step from *working code* to **well-structured code**.
They allow you to turn patterns you used in this practical
(for example distance calculation or median logic)
into reusable building blocks.
