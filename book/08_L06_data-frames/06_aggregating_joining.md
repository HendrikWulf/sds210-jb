---
title: Summarizing, Aggregating, and Joining

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Extracting Insights from Relational Data
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/08_L06_data-frames/06_aggregating_joining.ipynb)

---


```{admonition} Big idea
:class: tip

Raw data is just a collection of numbers. To create actual knowledge, you need to zoom out. In this section, you will learn how to extract high level insights using summary statistics, combine multiple datasets using shared keys, and group data into meaningful categories.
```

Before we begin, make sure you have downloaded the necessary datasets for this section. We will be using our familiar Kloten datasets, plus a new extended dataset from Lugano.

```{admonition} Download the Datasets
:class: note
Please download these files to your local working directory:
* [kloten_summer_2022_rain_sun.csv](https://gitlab.com/HendrikWulf/sds210/-/blob/main/data/kloten_summer_2022_rain_sun.csv)
* [kloten_summer_2022_extended.txt](https://gitlab.com/HendrikWulf/sds210/-/blob/main/data/kloten_summer_2022_extended.txt)
* [Lugano_summer_2022_extended.txt](https://gitlab.com/HendrikWulf/sds210/-/blob/main/data/Lugano_summer_2022_extended.txt)
```

Let us load our primary extended Kloten dataset. We will also extract the month from the date string right away, as we will need it for grouping later.

```{code-cell} python
import pandas as pd

# Load the extended Kloten dataset
fp = "kloten_summer_2022_extended.txt"
data = pd.read_csv(
    fp,
    sep=r"\s+",
    skiprows=[1],
    na_values=["-9999"]
)

# Extract the month (characters 4 and 5 from the YYYYMMDD string)
data["month"] = data["DATE"].astype(str).str.slice(4, 6)

display(data.head(3))
```

:::{table} Extended Kloten Dataset (with month)
:align: center

|   | DATE     | tmin | tmax | tmean | rh   | wind_speed | radiation | month |
|---|----------|------|------|-------|------|------------|-----------|-------|
| 0 | 20220601 | 11.1 | 19.6 | 14.8  | 83.1 | 1.8        | 126.7     | 06    |
| 1 | 20220602 | 12.3 | 21.8 | 17.0  | 81.4 | 2.3        | 231.3     | 06    |
| 2 | 20220603 | 12.7 | 24.8 | NaN   | 82.2 | 2.4        | 198.1     | 06    |

:::

---

## 1. Unique Values and Counts

Sometimes you want to know exactly what distinct categories exist within a specific column. Pandas provides two simple methods for this: `.unique()` to list the distinct values, and `.nunique()` to count them.

For example, let us confirm exactly which months are represented in our dataset.

```{code-cell} python
# See the actual unique values
print("Unique months:", data["month"].unique())

# Count the number of unique values
print("Number of unique months:", data["month"].nunique())
```

``````{admonition} Expected Output
:class: note
```text
Unique months: ['06' '07' '08']
Number of unique months: 3
```
*(Note: Notice the lack of commas in the `Unique months` list? That is because `.unique()` returns a highly optimized NumPy array, not a standard Python list!)*
``````

### Counting Category Frequencies

Knowing the unique categories is helpful, but usually, we also want to know how many rows belong to each category. 

To answer "how many of each?", Pandas provides the incredibly useful `.value_counts()` method. It instantly calculates the frequency of every unique value in a column and sorts them from most to least common.

```{code-cell} python
# Count how many days of data we have for each specific month
display(data["month"].value_counts())
```

``````{admonition} Expected Output
:class: note
```text
07    31
08    31
06    30
Name: month, dtype: int64
```
``````

These three methods (`unique`, `nunique`, and `value_counts`) form your standard toolkit for exploring categorical data. This is incredibly useful for tasks like checking how many unique weather stations are present in a massive global dataset, or finding out which station recorded the most data points!

---

## 2. Basic Statistics

The DataFrame and Series objects contain built-in methods for generating rapid summary statistics. Rather than writing complex math, you can simply call `.mean()`, `.median()`, `.min()`, `.max()`, and `.std()` (standard deviation).

If you call these on a single column, you get a single number:

```{code-cell} python
# Find the absolute maximum temperature of the entire summer
hottest_temp = data["tmax"].max()
print(f"The highest temperature was {hottest_temp}°C")
```

``````{admonition} Expected Output
:class: note
```text
The highest temperature was 36.0°C
```
``````

If you want a comprehensive overview of your entire dataset, the `.describe()` method is your best friend. It generates a statistical summary for all numeric columns at once, automatically ignoring missing NaN values.

```{code-cell} python
# Generate summary statistics for specific columns
columns_to_check = ["tmax", "tmin", "wind_speed"]
display(data[columns_to_check].describe())
```

:::{table} Output of describe()
:align: center

|       | tmax  | tmin  | wind_speed |
|-------|-------|-------|------------|
| count | 92.00 | 92.00 | 92.00      |
| mean  | 27.07 | 13.95 | 2.53       |
| std   | 4.01  | 2.37  | 0.68       |
| min   | 18.60 | 7.30  | 1.10       |
| 25%   | 24.33 | 12.70 | 2.10       |
| 50%   | 27.25 | 13.60 | 2.40       |
| 75%   | 29.50 | 15.38 | 3.00       |
| max   | 36.00 | 19.40 | 4.20       |

:::

```{admonition} Where is the median?
:class: tip
If you are looking for the median value in the `.describe()` table, look at the **50%** row! The 50th percentile means exactly half the data is above this number and half is below—which is the exact definition of a median.
```

---

## 3. Grouping Data

Calculating the average temperature for the entire summer is interesting, but what if we want to know the average temperature for *each specific month*?

Pandas uses a powerful concept called **Split-Apply-Combine**, accessible via the `.groupby()` method. This allows us to:

1.  **Split** the dataset into groups based on a category (like our `month` column).
2.  **Apply** a mathematical function (like mean or sum) to each group independently.
3.  **Combine** the results back into a neat summary table.

Let us group our data by month and calculate the average temperatures and wind speed. To understand the mechanics, we will write it out step-by-step first:

```{code-cell} python
# 1. SPLIT: Group the data by the 'month' column
grouped_data = data.groupby("month")

# 2. SELECT: Isolate the columns we want to calculate
columns_to_aggregate = ["tmax", "tmin", "wind_speed"]

# 3. APPLY & COMBINE: Apply the mean() function
monthly_averages = grouped_data[columns_to_aggregate].mean()

display(monthly_averages)
```

### The Chained Approach

Once you understand the Split-Apply-Combine logic, you do not need to write three separate lines of code. Pandas is designed to "chain" these commands together. 

We can also add one crucial extra command at the end: `.reset_index()`. By default, `.groupby()` turns your grouping category (`month`) into the index. Resetting the index turns `month` back into a normal, usable column!

```{code-cell} python
# The elegant, one-line Pandas way:
monthly_averages = data.groupby("month")[["tmax", "tmin", "wind_speed"]].mean().reset_index()

# Round the results to 2 decimal places for readability
display(monthly_averages.round(2))
```

:::{table} Output of groupby and mean
:align: center

|   | month | tmax  | tmin  | wind_speed |
|---|-------|-------|-------|------------|
| 0 | 06    | 25.87 | 13.10 | 2.40       |
| 1 | 07    | 28.21 | 14.60 | 2.62       |
| 2 | 08    | 27.09 | 14.14 | 2.55       |

:::

With a single line of chained code, we extracted a high-level insight: July (`07`) was noticeably hotter and slightly windier on average than June or August!

---

## 4. Table Joins

In real-world projects, your data is rarely contained in just one file. You might have one table with daily temperature data and another table with complementary measurements like rainfall. To analyze them together, you must join them.

Pandas uses the `.merge()` method to combine two DataFrames. It looks for a common column (the "key") in both tables and aligns the rows where the keys match.

Let us load a new supplementary dataset (`kloten_summer_2022_rain_sun.csv`) that contains daily `precipitation` and `sunshine_duration`, and merge it with our extended temperature dataset. We will use the date as our shared key.

```{code-cell} python
# Load the supplementary dataset 
# (Since it is a standard CSV, we don't need sep or skiprows!)
supp_fp = "kloten_summer_2022_rain_sun.csv"
supp_data = pd.read_csv(supp_fp)

# Merge the two DataFrames.
# Since the date columns have different names ('DATE' vs 'YEARMODA'),
# we use left_on and right_on to tell Pandas which keys to match!
combined_data = pd.merge(
    data, 
    supp_data, 
    left_on="DATE", 
    right_on="YEARMODA"
)

# Remove duplicate key column
combined_data = combined_data.drop(columns=["YEARMODA"])

# Display a few columns from the newly merged massive dataset
columns_to_show = ["DATE", "tmax", "rh", "precipitation", "sunshine_duration"]
display(combined_data[columns_to_show].head(3))
```

:::{table} Output of merged DataFrames
:align: center

|   | DATE     | tmax | rh   | precipitation | sunshine_duration |
|---|----------|------|------|---------------|-------------------|
| 0 | 20220601 | 19.6 | 83.1 | 2.2           | 74                |
| 1 | 20220602 | 21.8 | 81.4 | 0.0           | 281               |
| 2 | 20220603 | 24.8 | 82.2 | 0.3           | 333               |

:::

Because both tables shared the exact same dates, Pandas neatly attached the rain and sun columns from the new table right next to the corresponding temperatures in our main table!

```{admonition} Duplicate Keys
:class: tip
Notice that we added `.drop(columns=["YEARMODA"])` to our code above. When you use `left_on` and `right_on` to merge, the resulting DataFrame actually contains *both* key columns (so it will have both a `DATE` and a `YEARMODA` column containing the exact same numbers). Dropping one immediately keeps your table perfectly clean!
```

---
## 5. Exercise: Combine and Extract Insights

It is time to put your relational data skills to the test. You have been asked to compare the summer weather of Kloten (near Zurich) with Lugano (in southern Switzerland).

**Tasks:**

1.  Load the `Lugano_summer_2022_extended.txt` file into a new DataFrame. Remember to use the same `sep`, `skiprows`, and `na_values` parameters.
2.  Use `pd.merge()` to combine your newly merged Kloten `combined_data` DataFrame with the Lugano DataFrame using the `DATE` column as the key.
    *(Hint: Because both tables have columns named `tmean` and `precipitation`, Pandas will automatically add `_x` and `_y` to the names to tell them apart. You can control this using the `suffixes` parameter in your [merge function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html), like `suffixes=("_kloten", "_lugano")`)*
3.  Group the newly merged DataFrame by `month`. *(If your merged DataFrame lost the month column, recreate it by slicing the DATE string!)*
4.  Calculate the `.mean()` for `tmean` and `precipitation` for both cities.
5.  Display the final aggregated table (round your results to 1 decimal place). Which city was hotter on average in July?

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
# 1. Load Lugano data
lugano_data = pd.read_csv(
    "Lugano_summer_2022_extended.txt", 
    sep=r"\s+", 
    skiprows=[1], 
    na_values=["-9999"]
)

# 2. Merge Kloten and Lugano side by side using the DATE key
# We apply suffixes so we know which columns belong to which city
cities_merged = pd.merge(
    combined_data, 
    lugano_data, 
    on="DATE", 
    suffixes=("_kloten", "_lugano")
)

# 3. Ensure we have a month column for grouping
cities_merged["month"] = cities_merged["DATE"].astype(str).str.slice(4, 6)

# 4. Group by month and calculate averages
target_cols = [
    "tmean_kloten", "tmean_lugano", 
    "precipitation_kloten", "precipitation_lugano"
]

monthly_comparison = cities_merged.groupby("month")[target_cols].mean()

# 5. Display the result rounded to 1 decimal place
display(monthly_comparison.round(1))
```

:::{table} Output of monthly comparison
:align: center

| month | tmean_kloten | tmean_lugano | precipitation_kloten | precipitation_lugano |
|-------|--------------|--------------|----------------------|----------------------|
| 06    | 19.7         | 22.5         | 2.5                  | 5.0                  |
| 07    | 21.6         | 25.4         | 1.2                  | 3.3                  |
| 08    | 20.7         | 24.0         | 2.6                  | 2.8                  |

:::

*Observation: Lugano's average temperature in July was significantly higher than Kloten's (25.4°C vs 21.6°C), highlighting the climatic differences between northern and southern Switzerland! Interestingly, Lugano also saw higher average daily precipitation during these months.*
``````

---

## 6. Summary: Relational Data and Knowledge

You have officially transitioned from just manipulating rows of data to generating actionable knowledge and insights.

### Key takeaways

* **Unique Values:** Use `.unique()`, `.nunique()`, and `.value_counts()` to quickly understand the distinct categories and their frequencies in your dataset.
* **Summary Statistics:** Methods like `.mean()`, `.max()`, and `.describe()` provide an instant mathematical overview of your columns.
* **Grouping:** The `.groupby()` method is essential for aggregating data. It splits your data by a category (like a specific month), applies a calculation, and builds a neat summary table.
* **Joining Tables:** The `pd.merge()` function allows you to stitch separate datasets together horizontally by matching rows based on a shared key column (like a specific date).

### What comes next?

Throughout this chapter, we relied on a bit of a hack: we used string slicing (`.str.slice()`) to chop up text and extract the month from our dates. But what if we wanted to calculate the exact number of days between two measurements? Or what if our dates were formatted messily like "Jan 1st, 2022" instead of "20220101"?

Dates are not just strings of text; they are measurable, plottable dimensions. 

In the next section, **Working with Temporal Data**, we will learn how to convert clunky text into intelligent Pandas `datetime` objects. You will learn how to effortlessly extract years, months, and days using the special `.dt` accessor, and how to automatically resample time-series data (like converting hourly sensor readings into daily averages) without writing complex code.