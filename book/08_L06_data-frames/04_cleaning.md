---

title: Cleaning the Mess

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Handling Real-World Data with Pandas
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/08_L06_data-frames/04_cleaning.ipynb)

---

```{admonition} Big idea
:class: tip

Real-world spatial and environmental data is often messy. Before performing calculations or plotting, you must "sanitize" your dataset. This section teaches you how to standardize column headers, convert data types, clean text strings, and safely handle missing values (NaNs).
```

Real-world data is rarely ready for immediate analysis. Files from environmental sensors, satellites, or crowdsourced databases often contain irregular formatting, missing observations, or incorrect data types. Skipping the data cleaning stage is dangerous, as it leads to errors in calculations and misleading visualizations.

In this section, we will learn standard techniques to programmatically clean a dataset using Pandas. We will return to our `kloten_summer_2022.txt` dataset, applying the skipping logic learned in previous sections to load a fresh DataFrame.

```{code-cell} python
import pandas as pd
from IPython.display import display

# Define relative path to the file
fp = "kloten_summer_2022.txt"

# Read data, skipping the top 10 rows of metadata
data = pd.read_csv(fp, skiprows=10)

# Inspect the first few rows of the uncleaned data
display(data.head())
```

:::{table} Uncleaned Kloten DataFrame
:align: center

|   | YEARMODA | MAX  | MIN  | TEMP1 | TEMP2 |
|---|----------|------|------|-------|-------|
| 0 | 20220601 | 19.6 | 11.1 | 19.5  | 15.6  |
| 1 | 20220602 | 21.8 | 12.3 | 18.4  | 21.0  |
| 2 | 20220603 | NaN  | 12.7 | 23.1  | 20.7  |
| 3 | 20220604 | 24.3 | 12.8 | 21.6  | 22.8  |
| 4 | 20220605 | 24.3 | 14.8 | 20.7  | 23.5  |

:::

Take a close look at the table above. What is wrong with it? 
1. The column names are uppercase and cryptic (`YEARMODA`, `TEMP1`).
2. There is a missing value (`NaN`) sitting right in the middle of our `MAX` temperature column. 
3. (Hidden from view) The `YEARMODA` column is currently stored as a number, not a date or a string!

Let's clean this mess up step-by-step.

---

## 1. Renaming Columns

The first step in data cleaning is often standardizing the column headers. Messy, cryptic, or inconsistently capitalized names (like `YEARMODA` or `TEMP1`) make code harder to write and read. Standardizing headers to lowercase, descriptive names without spaces is best practice.

We can rename columns using the `.rename()` method. To tell Pandas exactly what to change, we use a Python **dictionary** passed to the `columns` parameter. A dictionary stores key-value pairs mapping the *old* name (the key) to the *new* name (the value).

Let's define descriptive, lowercase names for our Kloten data.

```{code-cell} python
# Define the dictionary mapping old names to new names
new_names = {
    "YEARMODA": "date",
    "MAX": "temp_max",
    "MIN": "temp_min",
    "TEMP1": "temp_10am",
    "TEMP2": "temp_2pm",
}

# Apply the rename operation using the 'columns' parameter
data = data.rename(columns=new_names)

# View the clean headers
print(data.columns)
```

**Output:**

```text
Index(['date', 'temp_max', 'temp_min', 'temp_10am', 'temp_2pm'], dtype='object')
```

```{admonition} Reassignment vs. Inplace
:class: tip
You might see tutorials online that write the code like this: `data.rename(columns=new_names, inplace=True)`. 

By default, Pandas operations return a *new* modified DataFrame and leave the original alone. To make the changes stick to your original `data` variable, you either have to overwrite it (`data = data.rename(...)`) OR use `inplace=True`. We recommend the overwrite method (`data = ...`), as the Pandas development team is gradually phasing out the `inplace` parameter in future updates.
```

---

## 2. Data Type Conversions

Pandas makes an educated guess about data types when reading a file, but it doesn't always get it right. Sometimes, numbers are imported as text, or integers are imported as floats. Incorrect data types will break mathematical operations and plotting functions.

The key method for changing data types in Pandas is `.astype()`.

Let's check the current types of our DataFrame using `.dtypes`.

```{code-cell} python
data.dtypes
```

**Output:**

```text
date           int64
temp_max     float64
temp_min     float64
temp_10am    float64
temp_2pm     float64
dtype: object
```

We see that `date` is currently stored as an integer (`int64`). Since we intend to perform string slicing on the date in the next subsection, we must first convert it to a string.

```{code-cell} python
# Convert the 'date' column to string
data["date"] = data["date"].astype(str)

# Verify the change
data.dtypes
```

**Output:**

```text
date          object
temp_max     float64
temp_min     float64
temp_10am    float64
temp_2pm     float64
dtype: object
```

```{admonition} Why does it say "object"?
:class: note
You might be wondering why Pandas says the `date` column is an `object` instead of a `string`. In Pandas, `object` is simply the default data type used to store text strings (or columns that contain a mix of different data types). If you see `object`, you can safely assume it is acting as text!
```

### The Integer Truncation Trap

You might also want to convert floating-point numbers into integers to save memory. However, you must be careful. When converting from `float` to `int`, Pandas does not round the numbers; it simply drops everything after the decimal point (truncation).

Look at what happens to the first value of our `temp_max` column (originally `19.6`):

```{code-cell} python
# Look at the first value
original_val = data["temp_max"].iloc[0]

# Truncation (Drops the decimal)
truncated_val = data["temp_max"].astype(int).iloc[0]

# Mathematically correct rounding
rounded_val = data["temp_max"].round(0).astype(int).iloc[0]

print(f"Original: {original_val}")
print(f"astype(int): {truncated_val} <-- Truncated!")
print(f"round().astype(int): {rounded_val} <-- Correctly rounded!")
```

**Output:**
```text
Original: 19.6
astype(int): 19 <-- Truncated!
round().astype(int): 20 <-- Correctly rounded!
```

---

## 3. String Slicing and Cleaning

Spatial datasets often contain important information embedded within text strings. For example, a single "timestamp" column might contain the year, month, and day combined. We need tools to "cut" or clean these strings.

### String slicing

The `date` column now has the structure `yyyyMMdd` as a string (e.g., `"20220601"`). We can use the `.str.slice()` method to extract specific parts of this string to create new categorical columns.

Let's extract the month information. Remember that Python indexing starts at 0, and the `stop` parameter is **exclusive** (meaning it stops *before* that index). 

Here is a visual map of our string:
```text
String:   2  0  2  2  0  6  0  1
Index:    0  1  2  3  4  5  6  7
```
To get the month (`06`), we need to start at index `4` and stop before index `6`.

```{code-cell} python
# Extract months (characters at position 4 and 5)
data["month"] = data["date"].str.slice(start=4, stop=6)

display(data.head())
```

:::{table} DataFrame after date slicing
:align: center

|   | date     | temp_max | temp_min | temp_10am | temp_2pm | month |
|---|----------|----------|----------|-----------|----------|-------|
| 0 | 20220601 | 19.6     | 11.1     | 19.5      | 15.6     | 06    |
| 1 | 20220602 | 21.8     | 12.3     | 18.4      | 21.0     | 06    |
| 2 | 20220603 | NaN      | 12.7     | 23.1      | 20.7     | 06    |
| 3 | 20220604 | 24.3     | 12.8     | 21.6      | 22.8     | 06    |
| 4 | 20220605 | 24.3     | 14.8     | 20.7      | 23.5     | 06    |

:::

#### Concept Check: Slicing the Year

Based on the visual map above, how would you write the code to extract just the **year** (the first four characters) into a new column called `year`?

```{admonition} Check your understanding
:class: dropdown

```python
data["year"] = data["date"].str.slice(start=0, stop=4)
```
You start at index 0, and stop at 4 (which grabs indices 0, 1, 2, and 3). 
```

### Other String Cleaning Methods
Now we have a clean `month` column we can use for grouping later. The `.str` accessor offers many other useful cleaning methods that you will use frequently with messy text data:
* `.str.upper()` or `.str.lower()` to standardize capitalization.
* `.str.strip()` to remove accidental invisible white spaces from the beginning or end of words.
* `.str.contains("keyword")` to search for specific substrings.
```

---

## 4. The Infamous NaN

Some datasets have gaps where observations were not recorded (perhaps a sensor lost power or a file was corrupted by the course instructor). Pandas represents these missing values using the marker **NaN**, which stands for **Not a Number**.

If we look back at our Kloten DataFrame above, we can clearly see a `NaN` at index 2 in the `temp_max` column. These markers behave differently than standard numbers. Most dangerously, they are "infectious": any mathematical operation involving a `NaN` usually results in a `NaN` (e.g., `5 + NaN = NaN`). 

Pandas provides handy tools to detect missing values. Every Series has a `.hasnans` attribute which quickly tells you if the column contains any missing data:

```{code-cell} python
# Check if a column has NaNs
print(data["temp_max"].hasnans)
```

**Output:**
```text
True
```

### Finding the Missing Data

Knowing that NaNs exist is good, but usually, we want to know exactly *where* they are and *how many* there are. We can use the `.isna()` method to do this.

By itself, `.isna()` generates a True/False mask. If we chain the `.sum()` method to it, Pandas will count up all the `True` values, telling us exactly how many NaNs are in the column:

```{code-cell} python
# Count exactly how many NaNs are in the column
missing_count = data["temp_max"].isna().sum()
print(f"There are {missing_count} missing values in temp_max.")
```

**Output:**
```text
There are 4 missing values in temp_max.
```

Even better, we can use `.isna()` as a boolean filter inside our selection brackets to isolate and view only the rows that are missing data!

```{code-cell} python
# Filter the DataFrame to show ONLY rows where temp_max is NaN
missing_data_rows = data[data["temp_max"].isna()]

display(missing_data_rows.head(3))
```

:::{table} Output of missing_data_rows
:align: center

|    | date     | temp_max | temp_min | temp_10am | temp_2pm | month |
|----|----------|----------|----------|-----------|----------|-------|
| 2  | 20220603 | NaN      | 12.7     | 23.1      | 20.7     | 06    |
| 26 | 20220627 | NaN      | 15.3     | 22.9      | 26.9     | 06    |
| 56 | 20220727 | NaN      | 15.0     | 22.7      | 24.8     | 07    |

:::

---

## 5. Dropping and Filling Missing Data

Having missing data in your dataset is common, and you must decide how to handle it. The two primary strategies are to either **remove (drop)** the rows containing missing values or **replace (fill)** them with another value.

### Dropping NaNs

We can remove missing data using the `.dropna()` function.

```{admonition} Always use the subset parameter
:class: warning
It is highly recommended to use the `subset` parameter to specify exactly which columns Pandas should check for NaNs. Using `.dropna()` without a subset will drop any row that has a NaN in *any* column, which can accidentally delete valuable data you wanted to keep.
```

Let's drop rows where `temp_max` is missing. We had 92 rows initially.

```{code-cell} python
# Define crucial columns to check
cols_to_check = ["temp_max"]

# Drop rows where NaNs are found in 'temp_max'
kloten_clean = data.dropna(subset=cols_to_check)

# Check the new size
print(f"Original rows: {len(data)}")
print(f"Cleaned rows: {len(kloten_clean)}")
```

**Output:**

```text
Original rows: 92
Cleaned rows: 88
```

4 rows were dropped.

### Filling NaNs

Dropping data might not be optimal, as you lose other valuable information in those rows (like the `temp_min` or `temp_10am` recordings that might still be perfectly fine). Pandas allows us to fill missing values using the `.fillna()` function.

For mathematical data like temperatures, you must be extremely cautious about what you fill. While filling with a constant like `0` or `-9999` might save the file without errors, it will dramatically alter your statistical analyses (e.g., making your average summer temperature artificially freezing!).

A better approach is often to fill NaNs with a representative statistic, like the average (mean) value of the rest of the column.

```{code-cell} python
# 1. Make a safe copy first
data_filled = data.copy() 

# 2. Calculate the average max temp (Pandas automatically ignores NaNs here)
avg_max = data_filled["temp_max"].mean()

# 3. Safely fill NaNs in the copied dataset with the calculated average
data_filled["temp_max"] = data_filled["temp_max"].fillna(avg_max)

display(data_filled.head(3))
```

:::{table} kloten DataFrame with filled NaNs
:align: center

|   | date     | temp_max   | temp_min | temp_10am | temp_2pm | month |
|---|----------|------------|----------|-----------|----------|-------|
| 0 | 20220601 | 19.600000  | 11.1     | 19.5      | 15.6     | 06    |
| 1 | 20220602 | 21.800000  | 12.3     | 18.4      | 21.0     | 06    |
| 2 | 20220603 | 25.845455  | 12.7     | 23.1      | 20.7     | 06    |

:::

Notice index 2 is now successfully filled with the calculated average (`25.845`).

### Interpolation: A Better Way for Time-Series

While filling with the overall average is okay for some datasets, it is actually quite dangerous for weather data. 

Think about it: if a sensor breaks during a massive 35°C heatwave, filling that missing day with the overall summer average of 25°C will completely distort your heatwave analysis!

For time-series data (where the order of the rows matters), the best approach is to guess the missing value based on the day immediately before and the day immediately after. In Pandas, this is called **linear interpolation**, and we use the `.interpolate()` method.

Let's look at the original data around our missing value at Index 2:
* Index 1 (June 2): `21.8`
* Index 2 (June 3): `NaN`
* Index 3 (June 4): `24.3`

```{code-cell} python
# 1. Make a safe copy 
data_interp = data.copy() 

# 2. Use interpolate() to connect the dots between the day before and day after
data_interp["temp_max"] = data_interp["temp_max"].interpolate()

display(data_interp.head(4))
```

:::{table} kloten DataFrame with Interpolated NaNs
:align: center

|   | date     | temp_max   | temp_min | temp_10am | temp_2pm | month |
|---|----------|------------|----------|-----------|----------|-------|
| 0 | 20220601 | 19.600     | 11.1     | 19.5      | 15.6     | 06    |
| 1 | 20220602 | 21.800     | 12.3     | 18.4      | 21.0     | 06    |
| 2 | 20220603 | 23.050     | 12.7     | 23.1      | 20.7     | 06    |
| 3 | 20220604 | 24.300     | 12.8     | 21.6      | 22.8     | 06    |

:::

> Notice how clever Pandas is! It looked at the day before (`21.8`) and the day after (`24.3`), drew a straight line between them, and calculated the exact midpoint: `(21.8 + 24.3) / 2 = 23.05`. This is a much safer and more accurate way to clean environmental data than using the overall summer average.

```{admonition} Forward and Backward Filling
:class: note
If you only want to carry the previous day's temperature forward (without looking at the next day), Pandas also offers `.ffill()` (forward fill) and `.bfill()` (backward fill).
```

#### Concept Check: To Drop or To Fill?

Imagine you are analyzing a dataset of 1,000 houses to see how the number of bedrooms affects the house price. 

* **Scenario A:** 5 houses are missing their "Price" data.
* **Scenario B:** 200 houses are missing their "Year Built" data, but you really want to include age in your analysis.

Which strategy makes the most sense for each scenario?

```{admonition} Check your understanding
:class: dropdown

**Scenario A: Drop.** Since "Price" is the core target of your analysis, trying to guess or fill the price of a house would invalidate your results. Since it's only 5 out of 1,000 rows (0.5%), dropping them is extremely safe.

**Scenario B: Fill (or investigate further).** Dropping 200 rows means throwing away 20% of your entire dataset! That is too much valuable data to lose. You should try to fill these (perhaps with the median "Year Built" of houses in the same neighborhood) or figure out why they are missing in the first place.
```

### Saving the Cleaned Data

Now that we have successfully sanitized our dataset by standardizing headers, fixing data types, and safely interpolating missing values, we need to save our hard work! This allows us to load the pristine data in the next lesson without having to rewrite all our cleaning code.

As you learned in the [Getting Data In and Out](https://hendrikwulf.github.io/sds210-jb/book/l06-data-frames/data_in_out/) section, we use the `.to_csv()` method for this. 

```{code-cell} python
# Save the fully cleaned dataset to a new CSV file
data_interp.to_csv("kloten_summer_2022_clean.csv", index=False)
print("Cleaned dataset saved successfully!")
```

---

## 6. Exercise: Sanitize the City Data

Real-world spatial and demographic data is rarely perfect. Let's apply our cleaning skills to the global `worldcities.csv` dataset you downloaded in the previous section. 

Because this specific CSV happens to be quite clean already, we are going to intentionally simulate a "messy" state in Step 3 so you can practice fixing it.

**Tasks:**

1.  Load `worldcities.csv` into a DataFrame.
2.  Select only these columns: `city`, `country`, `population`. **(Crucial: Append `.copy()` to this selection so you don't trigger a `SettingWithCopyWarning` later!)**
3.  Check the datatypes. Notice `population` is a float. Convert `population` to a string (`astype(str)`) to simulate a messy real-world file where numbers are accidentally stored as text.
4.  Use `.str.upper()` to standardize all the `city` names to uppercase.
5.  Use `.str.strip()` to remove any accidental leading or trailing white spaces from the `city` names.
6.  Convert the `population` column (currently a simulated string) back into a float so we can do math on it later.
7.  Crucial Check: Use `.dropna()` (using the `subset` parameter) to remove any cities where the `population` is missing (NaN).
8.  Display the first 5 rows of the cleaned DataFrame, and print the total number of rows left to verify your drop worked.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
import pandas as pd

# 1. Load the data
cities_df = pd.read_csv("worldcities.csv")

# 2. Select columns AND create a safe independent copy
cities_subset = cities_df[["city", "country", "population"]].copy()

# 3. Check types and simulate messy object state for population
cities_subset["population"] = cities_subset["population"].astype(str)

# 4. Standardize text (uppercase)
cities_subset["city"] = cities_subset["city"].str.upper()

# 5. Clean whitespace (strip)
cities_subset["city"] = cities_subset["city"].str.strip()

# 6. Convert messy object back to float for math
cities_subset["population"] = cities_subset["population"].astype(float)

# 7. Crucial check: Drop rows where critical population data is missing
cols_needed = ["population"]
cities_final = cities_subset.dropna(subset=cols_needed)

# 8. Display result
display(cities_final.head())
print(f"Remaining rows after cleaning: {len(cities_final)}")
```

**Expected Output:**

|   | city       | country | population |
|---|------------|---------|------------|
| 0 | TOKYO      | Japan   | 37785000.0 |
| 1 | JAKARTA    | Indonesia| 33756000.0 |
| 2 | DELHI      | India   | 32226000.0 |
| 3 | GUANGZHOU  | China   | 26940000.0 |
| 4 | MUMBAI     | India   | 24973000.0 |

`Remaining rows after cleaning: 47808`

```{admonition} The "nan" String Trap
:class: tip
Did you know you navigated a hidden trap in this exercise? In Step 3, when you converted the column to a string using `.astype(str)`, Pandas converted the missing `NaN` values into the literal word `"nan"`. 

If you had tried to run `.dropna()` in Step 5 while it was still a string, it wouldn't have dropped anything! To Pandas, the word `"nan"` is just text. Thankfully, converting it back to a float in Step 6 translated that word back into a true mathematical missing value, allowing `.dropna()` to do its job.
```

``````

---

## 7. Summary: Data Cleaning Practices

Sanitizing your dataset is a critical best practice before any analysis. Real environmental and spatial data is almost always heterogeneous and messy. If you skip this step, your future calculations will fail!

### Key takeaways

* **Columns:** Renaming columns using dictionaries standardizes cryptic sensor headers into descriptive lowercase names.
* **Types:** Always verify `.dtypes`. Use `.astype()` to correct numbers incorrectly stored as text, but beware of integer truncation!
* **Strings:** The `.str` accessor allows you to programmatically slice strings (like extracting a month from a timestamp) or clean text by changing case and stripping whitespace.
* **Missing Data (NaNs):** Gaps are common and infectious.
    * **Detect:** Find them using `.hasnans` or `.isna().sum()`.
    * **Drop:** Use `.dropna(subset=[...])` to safely remove rows missing crucial target data.
    * **Fill:** Use `.fillna()` cautiously. For time-series data (like daily temperatures), use `.interpolate()` to draw a line between the day before and the day after rather than filling with a static average.

### What comes next?

Now that your dataset is clean, properly formatted, and free of missing values, you are finally ready to do some actual data analysis!

But wait, if you want to divide a column of populations by a column of areas to find the density for 48,000 cities, how do you do it? In pure Python, you would have to write a massive, slow `for` loop to calculate each row one by one. 

In Pandas, we have a superpower called **Vectorization**. In the next section, **Math Without Loops**, we will learn how to apply instant arithmetic across entire datasets and create brand new columns of data in a single line of code.