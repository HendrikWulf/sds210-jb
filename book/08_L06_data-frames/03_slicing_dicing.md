---
site:
 outline_maxdepth: 1
---

# Slicing and Dicing

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Selecting and filtering data in Pandas
</div>
<!-- markdownlint-enable MD033-->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/08_L06_data-frames/03_slicing_dicing.ipynb)

---

```{admonition} Big idea
:class: tip

Now that your data is loaded into a two dimensional grid, you need to know how to navigate it. Pandas allows you to instantly extract specific columns, filter rows based on logical conditions, and sort your information without writing complex loops.

```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★★★ (A critical bottleneck; you must know how to use `&` operators for boolean indexing and `.sort_values()` to pass Part 3: Vectorization and Slicing.)  
**Project Relevance:** ★★★ (Mandatory for isolating relevant subsets of data in any analytical pipeline, such as filtering for specific neighborhoods in project 1 or biomes in project 2.)  
**Foundation:** ★★★ (Core Pandas mechanics that replace standard, slow Python loops and `if` statements.)  

**Time to Read:** 20 minutes  
**In a nutshell:** Master the core Pandas operations to select columns, filter rows with logical conditions, and safely modify data without triggering the notorious view vs. copy trap.  
**Skip this if:** You already know how to use boolean masks, `&`/`|` operators, `.sort_values()`, `.loc`/`.iloc`, and fully understand Copy-on-Write and when to use `.copy()`.

```

In the previous chapter, we successfully loaded the [kloten_summer_2022.txt](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L06/data/kloten_summer_2022.txt) weather dataset. Let us quickly reload it to your local working directory so we have a fresh **{term}`DataFrame`** to work with.

```{code-cell} python
import pandas as pd

# Load the Kloten summer weather data, skipping metadata
data = pd.read_csv('data/kloten_summer_2022.txt', skiprows=10)

```

---

## 1. Selecting Columns

When performing data analysis, you rarely need every variable in your dataset. You can extract specific columns by placing the column name inside square brackets next to your DataFrame variable.

To extract a single column, pass the name as a string. This returns a one dimensional **{term}`Series`**.

```{code-cell} python
# Extract a single column
max_temps = data["MAX"]

# Prove it is a Series
print(type(max_temps))

# Look at the first 3 rows
max_temps.head(3)

```


```{admonition} The Dot Notation Alternative
:class: warning
You might see tutorials online selecting columns using dot notation, like `data.MAX`. While this sometimes works, it can crash your code if your column name contains spaces (e.g., `data.Max Temp`) or shares a name with a built in Pandas method (like `data.count`). **Better use bracket notation `data["MAX"]`** to avoid these hidden bugs!

```

To extract multiple columns, you must pass a **{term}`list <List>`** of column names inside the square brackets. This means you will see double brackets `[[ ]]`.

* The **outer brackets** tell Pandas you are making a selection: `data[ ... ]`
* The **inner brackets** define the Python list of strings: `["YEARMODA", "MAX", "MIN"]`

Extracting multiple columns returns a smaller DataFrame, rather than a Series.

```{code-cell} python
# Extract multiple columns
subset = data[["YEARMODA", "MAX", "MIN"]]

# Prove it is a DataFrame
print(type(subset))

display(subset.head(3))

```

*"Note: We use the `display()` function here to explicitly print the DataFrame as a cleanly formatted HTML table in our notebook."*

---

## 2. Filtering Rows

Selecting columns is easy, but how do we select specific rows? In pure Python, you would use an `if` statement to check each row one by one. In Pandas, we use a concept called **{term}`Boolean indexing`** to ask the entire dataset a True or False question simultaneously.

:::{figure} images/05_boolean_indexing_mask.png
:alt: A conceptual diagram showing a source table on the left, a vertical True/False boolean mask in the middle, and the resulting filtered table on the right. Arrows illustrate that only rows corresponding to 'True' pass through the filter.
:width: 700px
:align: center

*Boolean indexing conceptually acts as a filter. The mask of True/False values determines exactly which rows from the original DataFrame are allowed to pass through into your new subset.*
:::

First, we ask the question. Let us find out which days had a maximum temperature greater than 30 degrees Celsius:

```{code-cell} python
# Ask the question (creates a boolean mask)
data["MAX"] > 30

```

This returns a Series of `True` and `False` values, often called a **mask**.

To actually filter the data, we place this conditional mask *inside* the selection brackets. Pandas will keep every row that evaluates to `True` and hide every row that evaluates to `False`.

For absolute clarity, here is how you do it in two steps:

```{code-cell} python
# Step 1: Save the mask to a variable
is_hot = data["MAX"] > 30

# Step 2: Pass the mask variable into the brackets
hot_days = data[is_hot]

```

However, experienced programmers usually combine this into a single line of code by placing the condition directly inside the brackets. Notice how the word `data` appears twice:

```{code-cell} python
# The standard one-line approach
hot_days = data[data["MAX"] > 30]

display(hot_days.head(3))

```

Notice the **{term}`Index`** on the far left. It jumped from 15 to 18 to 19, preserving the original row labels of the days that met our criteria.

---

## 3. Multiple Conditions

Often, you need to filter data using multiple criteria simultaneously. You can combine logical conditions using special operators. Standard Python keywords `and` and `or` will not work here, as Pandas needs bitwise operators that perform vectorized logical comparisons on entire Series at once.

Pandas uses these operators:

* **`&`** (AND): Both conditions must be True.
* **`|`** (OR): At least one condition must be True.

```{admonition} The Parentheses Rule
:class: warning
When combining conditions in Pandas, you **must** wrap each individual condition in parentheses `()`. Otherwise, Python's order of operations will evaluate the statement incorrectly and throw an error.

```

### AND Condition Example

Let us find "extreme" summer days that were both very hot (`MAX > 30`) but also had surprisingly cool mornings (`MIN < 14`).

```{code-cell} python
# Using & (AND) for logical conditions
extreme_days = data[(data["MAX"] > 30) & (data["MIN"] < 14)]
display(extreme_days)

```

### OR Condition Example

Next, let us find days that were either extremely hot (`MAX > 33`) OR had very cold mornings (`MIN < 10`). This query will include days meeting either criteria, or both.

```{code-cell} python
# Using | (OR) logic for extreme temperatures
either_extreme_days = data[(data["MAX"] > 33) | (data["MIN"] < 10)]
display(either_extreme_days)

```

---

## 4. Sorting Data (sort_values)

Once you have isolated your data, you frequently want to order it. The `.sort_values()` method allows you to sort your DataFrame by one or more columns.

By default, Pandas sorts in ascending order (smallest to largest). To find the absolute hottest days of the summer at the top of our table, we need to set the `ascending` parameter to `False`.

```{code-cell} python
# Sort by MAX temperature, descending
sorted_data = data.sort_values(by="MAX", ascending=False)
display(sorted_data.head(3))

```

---

## 5. Copy-on-Write: Why Subsets Behave Safely

When you filter a DataFrame, pandas tries to be efficient with your computer's memory. In older versions of pandas, this created a confusing situation: sometimes a subset behaved like a **{term}`view <View (Pandas)>`** into the original data, and sometimes it behaved like a fully independent copy.

Starting with pandas 3.0, pandas uses **Copy-on-Write** by default. This means that a subset behaves like an independent object when you modify it. Behind the scenes, pandas may still share memory to save resources, but if you write to the subset, pandas protects the original DataFrame by copying the data when needed.

```{admonition} The Notebook Analogy
:class: tip

Imagine your original DataFrame as the official class notebook.

When you create a subset, pandas may first give you a lightweight working page that still shares information with the original notebook. As long as you only read from it, this is efficient.

But as soon as you start writing on that working page, pandas makes sure your changes stay on your page and do not accidentally overwrite the official notebook.
```

This makes pandas more predictable than older versions. You can create a filtered subset and add a new column to that subset without worrying that the original DataFrame will silently change.

Let us filter the data for early June and add a new column:

```{code-cell} python
# Create a subset for early June
early_june = data[data["YEARMODA"] < 20220610]

# Add a new column to the subset
early_june["IS_HOT"] = early_june["MAX"] > 25

display(early_june.head())
```

The new column is added to `early_june`. The original `data` DataFrame remains unchanged.

```{code-cell} python
# The new column exists in the subset
print("Columns in early_june:")
print(early_june.columns)

print("\nColumns in original data:")
print(data.columns)
```

```{admonition} Key idea
:class: note

A filtered subset can be used as a separate working object. If you modify that subset, pandas 3.0 protects the original DataFrame through Copy-on-Write.
```

### Do We Still Need `.copy()`?

You can still use `.copy()` when you want to make your intention extra clear:

```{code-cell} python
early_june_copy = data[data["YEARMODA"] < 20220610].copy()
early_june_copy["IS_HOT"] = early_june_copy["MAX"] > 25

display(early_june_copy.head())
```

This is not wrong. It tells readers of your code: “I want this to be an independent object.”

However, in pandas 3.0, `.copy()` is no longer needed just to avoid the old `SettingWithCopyWarning`. The old warning existed because pandas could not always clearly tell whether you were modifying a view or a copy. Copy-on-Write removes this ambiguity for everyday use.

### The Important Question: What Are You Trying to Change?

When writing pandas code, the most important question is not simply “Do I need a copy?” Instead, ask:

```{admonition} A better question
:class: important

Am I creating a new object for separate analysis, or am I trying to change the original DataFrame?
```

If you create a new object, use a new variable name:

```{code-cell} python
hot_days = data[data["MAX"] > 30]
```

If you want to continue working with this subset, you can modify it:

```{code-cell} python
hot_days["VERY_HOT"] = hot_days["MAX"] > 33

display(hot_days.head())
```

This changes `hot_days`, not the original `data`.

If your actual goal is to change the original `data` DataFrame, we need a more precise selection tool. That tool is introduced in the next section: `.loc[]`.

#### Concept Check: Separate object or original data?

Imagine you are writing a script to analyze weather patterns.

**Scenario A:** You filter the dataset to find all days where the maximum temperature exceeded 30°C, just so you can inspect them.

**Scenario B:** You filter the dataset to create a separate `hot_days` table and add a new column only to that table.

**Scenario C:** You want to add a new column to the original `data` DataFrame marking which days were hot.

Which scenario requires a more precise assignment method introduced in the next section?

A) Scenario A

B) Scenario B

C) Scenario C

```{admonition} Check your understanding
:class: dropdown

**Answer: C**

In Scenario A, you are only reading a subset.

In Scenario B, you are creating and modifying a separate object. With pandas 3.0, Copy-on-Write protects the original DataFrame.

In Scenario C, your goal is to modify the original DataFrame itself. For this, you need a more precise assignment method. That method is introduced in the next section with `.loc[]`.
```

---

## 6. Index based Selection (loc vs iloc)

In the previous section, we saw that filtered subsets can safely be used as separate working objects. But sometimes you do not want to create a separate object. Sometimes you want to select exact rows and columns in the original DataFrame and modify them directly.

For this, pandas provides two powerful indexers: `.loc[]` and `.iloc[]`.

* **`.loc[]`** (Label-based): Selects data based on its exact label (the name of the index row or the name of the column).
* **`.iloc[]`** (Integer position-based): Selects data based on its strict numerical position (0, 1, 2...), exactly like a standard Python list.

:::{figure} images/06_loc_vs_iloc_indexing.png
:alt: A conceptual diagram showing a Pandas DataFrame with a sorted, non-sequential index. An arrow for .loc[0] points to the specific row labeled '0', while an arrow for .iloc[0] points to the physical top row of the table.
:width: 700px
:align: center

*Understanding the difference between label-based (.loc) and position-based (.iloc) indexing. When data is sorted, the physical position (0) no longer matches the original row label (0).*
:::

Let us look at the difference. Imagine we sort our data so the hottest day (originally Index 18) is at the very top of the table.

```{code-cell} python
# 1. .iloc looks for the row currently sitting in the very first position (position 0)
print("Result of .iloc[0]:")
print(sorted_data.iloc[0])

print("\n-------------------\n")

# 2. .loc looks for the row literally labeled '0' (which is now deep in the middle of the sorted data)
print("Result of .loc[0]:")
print(sorted_data.loc[0])

```

Notice how `.iloc[0]` returned the data for the hottest day (labeled 18), while `.loc[0]` hunted down the specific row labeled 0 (June 1st).

### Selecting Rows AND Columns

The true power of these indexers is that you can select rows and columns at the same time by separating them with a comma: `[rows, columns]`.

```{code-cell} python
# Use .loc to get rows labeled 0 through 3, and specifically the "MAX" and "MIN" columns
subset_loc = data.loc[0:3, ["MAX", "MIN"]]
display(subset_loc)

```

:::{table} Output of .loc[0:3, ["MAX", "MIN"]]
:align: center

|  | MAX | MIN |
| --- | --- | --- |
| 0 | 19.6 | 11.1 |
| 1 | 21.8 | 12.3 |
| 2 | NaN | 12.7 |
| 3 | 27.4 | 12.8 |

:::

```{admonition} The Slicing Gotcha
:class: warning
Did you notice something strange in the table above? 

In standard Python list **{term}`slicing <Slicing>`** (and when using `.iloc[0:3]`), the end number is **exclusive**, meaning it would only return rows 0, 1, and 2. 

However, because `.loc[]` searches for specific labels, it is **inclusive**. `data.loc[0:3]` includes the row labeled '3'!

```

---

## 7. Exercise: Isolate the Target Data

Let us bring all these skills together using the global cities dataset you downloaded in the previous chapter.

Imagine you are doing an analysis focused solely on major urban centers in Japan. You need to load the data, extract exactly what you need, and secure it in memory.

**Tasks:**

1. Load `worldcities.csv` into a DataFrame.
2. Filter the data to include only rows where the `country` column is exactly `"Japan"`.
3. *Crucial:* Make sure to append `.copy()` to create an independent dataset!
4. Sort this new Japan DataFrame by the `population` column in descending order (largest to smallest).
5. Display the top 5 rows, but *only* show the `city` and `population` columns.

*(Hint for Step 5: Remember that selecting multiple columns requires a list inside the selection brackets, which looks like double brackets `[[ ]]`)*.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
import pandas as pd

# 1. Load the data
cities_df = pd.read_csv("data/worldcities.csv")

# 2 & 3. Filter for Japan AND create a safe copy
japan_cities = cities_df[cities_df["country"] == "Japan"].copy()

# 4. Sort by population descending
japan_sorted = japan_cities.sort_values(by="population", ascending=False)

# 5. Extract specific columns and show the top 5
top_japan_cities = japan_sorted[["city", "population"]]
display(top_japan_cities.head(5))
```

**Expected Output:**
|     | city     | population |
| --- | -------- | ---------- |
| 0   | Tokyo    | 37785000.0 |
| 23  | Ōsaka    | 15126000.0 |
| 45  | Nagoya   | 9197000.0  |
| 197 | Yokohama | 3757630.0  |
| 366 | Fukuoka  | 2286000.0  |


*(Note: The exact index numbers on the left might differ slightly depending on the version of the dataset, but the top 5 cities and populations should match!)*

``````

---

## 8. Summary: Navigating the 2D Grid

In this chapter, you learned how to slice and dice your data to extract exactly the information you need. You now have the tools to surgically navigate large datasets without relying on manual `for` loops.

### Key takeaways

* **Columns:** Extract a single Series using `df["col"]` or a smaller DataFrame using a list `df[["col1", "col2"]]`.
* **Rows:** Use Boolean Indexing (`df[df["col"] == value]`) to act as a filter, keeping only rows that meet logical conditions.
* **Conditions:** Combine multiple filters using `&` (AND) or `|` (OR), always wrapping each individual condition in parentheses `()`.
* **Sorting:** Use `.sort_values(by="col", ascending=False)` to order your DataFrame.
* **Safety:** With pandas 3.0, filtered subsets behave safely through Copy-on-Write.
* **Index Selection:** Use `.iloc[]` to select rows based on their strict numerical position, and `.loc[]` to select based on exact row/column labels.

### What comes next?

Now that you can navigate, slice, and filter your data, you might notice a glaring issue: real-world data is rarely perfect.

If you try to do math on a column where numbers are accidentally stored as text, or if a sensor went offline and left blank gaps in your dataset, your code will crash. In the next chapter, **Cleaning the Mess**, we will learn how to standardize messy column headers, fix text strings, and handle the infamous `NaN` (Not a Number) so your data is pristine and ready for analysis!
