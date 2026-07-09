---

site:
    outline_maxdepth: 1

---

# Vectorization

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Math Without Loops
</div>
<!-- markdownlint-enable MD033-->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/08_L06_data-frames/05_vectorization.ipynb)

---

```{admonition} Big Idea
:class: tip

The core superpower of Pandas is **{term}`Vectorization`**. You no longer need to write tedious `for` loops to modify or calculate data. Pandas allows you to apply mathematical operations across entire datasets instantly, saving you time and massively speeding up your code.

```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★★☆ (Highly useful for calculating the `temp_swing` cleanly in Part 3, though it is an intuitive calculation.)  
**Project Relevance:** ★★★ (Essential for calculating derived indicators across massive datasets efficiently, particularly spectral indices in projects 3 and 4.)  
**Foundation:** ★★★ (A fundamental shift from slow Python loops to lightning-fast array-based mathematical programming.)  

**Time to Read:** 15 minutes  
**In a nutshell:** Master the art of replacing slow Python loops with lightning-fast vectorized math, and learn how to apply custom logic across entire datasets.  
**Skip this if:** You already intuitively use vectorized operators for Pandas columns and know exactly when to use `.apply(axis=1)` for custom row-by-row logic.

```

Before we explore this superpower, we need some fresh data. For this chapter, we will use an extended dataset from the Kloten weather station (`kloten_summer_2022_extended.txt`). This file contains additional environmental variables like relative humidity, wind speed, and solar radiation.

```{admonition} Data Preparation
:class: dropdown

To follow along with this chapter, place the following dataset in a `data` folder next to your notebook:

* [kloten_summer_2022_extended.txt](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L06/data/kloten_summer_2022_extended.txt)

```

We can actually perform some data cleaning right at the moment we read the file! By using advanced parameters in the `read_csv()` function, we can handle varying spaces, skip specific rows of dashes, and convert missing data markers all in one step.

```{code-cell} python
import pandas as pd

# Define relative path to the file
fp = "data/kloten_summer_2022_extended.txt"

# Read data using advanced cleaning parameters
data = pd.read_csv(
    fp,
    sep=r"\s+",             # Handle varying amounts of spaces between columns
    skiprows=[1],           # Skip the second row (usually a line of dashes)
    na_values=["-9999"],    # Convert -9999 placeholders directly to NaN
    usecols=["DATE", "tmin", "tmax", "tmean", "rh", "wind_speed", "radiation"]
)

# Inspect the first few rows
display(data.head(3))

```

Notice that our `tmean` column has a missing value (**{term}`NaN`**) on the third day. We will use this to our advantage later.

---

## 1. The Concept of Vectorization

If you were asked to calculate the temperature range (maximum minus minimum) for every single day in pure Python, you would have to write a `for` loop. You would instruct the computer to look at row 0, subtract the numbers, save the result, move to row 1, subtract the numbers, and so on.

Here is what that clunky code looks like:

```{code-cell} python
# The slow, pure Python way (DO NOT DO THIS)
temp_ranges = []
for i in range(len(data)):
    diff = data.loc[i, "tmax"] - data.loc[i, "tmin"]
    temp_ranges.append(diff)

```

For a dataset with millions of records, this row-by-row looping is rather slow and requires more typing.

Pandas uses a concept called **Vectorization**. Under the hood, Pandas pushes your data into highly optimized C-language arrays. When you ask Pandas to perform a calculation, it does not loop in Python; instead, it aligns the entire columns and pushes the math operation through the optimized C backend almost simultaneously.

:::{figure} images/09_vectorization_concept.png
:alt: Diagram comparing a slow row-by-row for-loop execution to a lightning-fast simultaneous vectorized column operation.
:width: 700px
:align: center

*A `for` loop (left) must process every single row sequentially, which takes time. Vectorization (right) aligns the data arrays in memory and calculates the entire column in a single, simultaneous operation.*
:::

```{admonition} The Golden Rule of Pandas
:class: warning
If you ever find yourself writing a `for` loop to modify or calculate data in a **{term}`DataFrame`**, **stop**. There is almost certainly a vectorized Pandas **{term}`method <Method>`** that can do it in a single line of code, many times faster.

```

---

## 2. Column-wise Math

Vectorized math in Pandas is as simple as writing basic algebra. You just use the standard mathematical operators (`+`, `-`, `*`, `/`) directly on the **{term}`Series`** objects.

When you do this, Pandas performs an **element-wise** operation. It looks at the index, matches row 0 of the first column with row 0 of the second column, performs the math, and instantly moves down the line.

Let us calculate the temperature range (the difference between the maximum and minimum temperatures) for every day in our dataset.

```{code-cell} python
# Calculate the difference between two columns simultaneously
temp_difference = data["tmax"] - data["tmin"]

display(temp_difference.head(4))

```

In just one line of code, Pandas matched the indices and calculated the precise difference for every single row in the dataset!

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L06_ch05_01_vectorization_vs_loop/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: Vectorization vs. For-Loop.</b><br>
    Click the buttons to simulate exactly how Python processes data row-by-row versus how Pandas executes math simultaneously across entire arrays. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L06_ch05_01_vectorization_vs_loop/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

---

## 3. Creating New Columns

Once you perform a calculation, you usually want to save it as a brand new feature in your dataset. You can attach a newly calculated Series back onto the main DataFrame by defining a new column name in brackets and assigning the calculation to it.

```{code-cell} python
# Create a new column named 'temp_range' and store the results
data["temp_range"] = data["tmax"] - data["tmin"]

# Check the DataFrame to see the new column attached at the end
display(data[["DATE", "tmax", "tmin", "temp_range"]].head(3))

```

```{admonition} The Overwrite Pitfall
:class: warning
If you assign data to a column name that *already exists* in your DataFrame, Pandas will silently overwrite the old data without warning you (because updating and creating use the exact same syntax!). Always double-check your spelling when creating new columns!

```

### Static Default Values

You do not always need a mathematical calculation to create a new column. You can also initialize a new column with a static default value.

For example, if you wanted to create a blank column to store future quality-control notes, you could simply assign a single string. Pandas will automatically copy that single value down to fill every single row:

```{code-cell} python
# Create a column filled with a static string
data["qc_notes"] = "Not checked"

display(data[["DATE", "qc_notes"]].head(3))

```

---

## 4. Plotting the Math

Staring at a table of numbers is a terrible way to spot trends. Humans are visual creatures—we process shapes and colors much faster than raw text.

Now that we have successfully calculated our new `temp_range` column, let us visualize it alongside our daily extremes. Pandas makes this incredibly easy with the built-in `.plot()` method, which acts as a wrapper around Python's powerful Matplotlib library (which we will get to know later).

### A Note on Dates

You might have noticed that our `DATE` column looks like a number (`20220601`). Because we have not explicitly told Pandas that this is a calendar date yet (we will cover that in a future session!), plotting it on the x-axis right now would look very strange.

Luckily, since our data starts exactly on June 1st and records one row per day, the standard Pandas row index (`0, 1, 2...`) perfectly represents **"Days after June 1st"**. We can just let Pandas use the default index for the bottom axis!

### Stage 1: The Quick Plot

Let us plot our maximum temperature (red), minimum temperature (blue), and our new temperature range (green).

```{code-cell} python
# 1. Define exactly which columns we want to draw
columns_to_plot = ["tmax", "tmin", "temp_range"]

# 2. Create a basic plot with custom colors
data[columns_to_plot].plot(color=["red", "blue", "green"]);

```

<!-- markdownlint-disable MD033-->
<div class="figure-caption-like">
    A basic Pandas plot is fast to generate, but it lacks essential context like axis labels, legends, and a readable canvas size.
</div>
<!-- markdownlint-enable MD033 -->

This quick plot is helpful for a fast visual check, but it is not something you would want to put in a scientific report. It is small, there are no axis labels, and all the lines look identical.

### Stage 2: The Professional Plot

Good data scientists do not just make plots; they design visualizations that tell a clear data story. By passing a few extra parameters into the `.plot()` method, we can dramatically upgrade our chart's readability and style without writing complex code.

Let us add labels, adjust the canvas size, and change the line styles to differentiate our calculated range from the actual sensor readings.

```{code-cell} python
# Create a customized, styled plot
data[columns_to_plot].plot(
    figsize=(10, 5),                 # Make the canvas wide (10) and tall (5)
    color=["red", "blue", "green"],  # Assign specific colors
    style=["-", "-", "*"],           # Solid lines for temps, stars for range
    linewidth=2,                     # Make the lines slightly thicker
    title="Daily Temperatures and Range (Kloten, Summer 2022)",
    ylabel="Temperature (°C)",       # Always label your axes!
    xlabel="Days after June 1st",    # Clarify what the bottom numbers mean
    grid=True,                       # Add a faint grid for readability
    # subplots=True                    # each column in its own subplot
);

```

<!-- markdownlint-disable MD033-->
<div class="figure-caption-like">
    A styled plot effectively communicates the data story by using clear labels, descriptive line styles, and an expanded canvas size.
</div>
<!-- markdownlint-enable MD033 -->

### The Elements of Good Style

Notice how much easier the second chart is to read. Here is what we changed:

* **`figsize=(10, 5)`:** Expanding the figure size ensures the data isn't crammed together, making daily spikes much easier to see.
* **`style=["-", "-", "*"]`:** We used standard solid lines (`"-"`) for the physical temperature measurements, but a star marker (`"*"`) for our calculated range. This visual distinction helps the reader immediately separate raw data from derived math!
* **`ylabel` and `xlabel`:** A chart without context is just a drawing. Always include a title and clearly label the units on your axes.

```{admonition} Experiment with Styling!
:class: tip
The best way to learn plotting is to break it and fix it. Try changing the parameters in the code block above and re-running the cell:

1. **Change the `style`:** * Try `"--"` for dashed lines.
   * Try `":"` for dotted lines.
   * Try `"-."` for a dash-dot line.
   * Try other markers like `"o"` (circles) or `"."` (tiny dots).
2. **Change the `color`:** Swap "red" for `"orange"`, `"purple"`, or even a hex code like `"#FF5733"`.
3. **Change the `linewidth`:** What happens if you change it to `1` or `5`?
4. **Toggle the `grid`:** Change `grid=True` to `grid=False` to see how it affects readability.

```

---

## 5. Applying Functions (apply)

Sometimes simple algebra is not enough. You might have a complex spatial formula, a block of `if/else` statements, or a custom Python function that requires logic beyond basic addition and subtraction. For these situations, Pandas provides the `.apply()` method.

The `.apply()` method takes a custom function and runs it efficiently across your data.

To learn the syntax, let us start by defining a standard Python function that converts temperatures from Celsius to Kelvin, and then apply it to our `tmax` column. *(Note: While we could easily do this with simple vectorized math like `data["tmax"] + 273.15`, using a simple formula helps us focus purely on how `.apply()` works!)*

```{code-cell} python
# Define a standard Python function
def celsius_to_kelvin(temp_celsius):
    """Converts Celsius to Kelvin."""
    return temp_celsius + 273.15

# Apply the function to the entire column
data["tmax_kelvin"] = data["tmax"].apply(celsius_to_kelvin)

display(data[["tmax", "tmax_kelvin"]].head(3))

```

```{admonition} No Parentheses!
:class: warning
Notice that when we used `.apply(celsius_to_kelvin)`, we did **not** put parentheses `()` after the function name. If you include parentheses, Python tries to run the function immediately before passing it to Pandas, which will cause an error. You are just handing the *name* of the function to Pandas so it can use it later.

```

### Applying Across Multiple Columns (axis=1)

The example above applied a function to a *single column* (`data["tmax"]`). But what if your custom function needs to look at *multiple* columns at the same time to make a decision?

To do this, we apply our function to the entire DataFrame (`data.apply(...)`) instead of just one column. When we do this, we must include the **`axis=1`** parameter.

In Pandas, `axis=0` (the default) means moving vertically down columns. `axis=1` tells Pandas to pass the data into your function **horizontally, row by row**.

Let us write a function that uses an `if/else` block to check both the `tmax` and `rh` (humidity) columns to categorize if a day was "Muggy" (hot and humid):

```{code-cell} python
# 1. Define a function that accepts an entire row of data
def check_muggy(row):
    """Categorizes a day as Muggy if temp > 24C AND humidity > 70%."""
    # We extract the specific values we need from the row
    if row["tmax"] > 24.0 and row["rh"] > 70.0:
        return "Yes"
    else:
        return "No"

# 2. Apply the function to the entire DataFrame using axis=1
data["is_muggy"] = data.apply(check_muggy, axis=1)

# 3. View the results
columns_to_show = ["DATE", "tmax", "rh", "is_muggy"]
display(data[columns_to_show].head(3))

```

#### Concept Check: The Axis of Action

You wrote a custom function `calculate_risk(row)` that needs to read both the `elevation` and `slope` columns in your dataset to assign a flood risk category to each location. You attempt to apply it by writing the following code:

`data["risk"] = data.apply(calculate_risk)`

What happens when you run this?

A) It crashes because you forgot `axis=1`. Pandas tries to pass entire columns into the function instead of row-by-row data.

B) It works perfectly and calculates the risk for each row.

C) It crashes because you forgot the parentheses on the function: `calculate_risk()`.

```{admonition} Check your understanding
:class: dropdown

**Answer: A**
By default, `.apply()` uses `axis=0`, which attempts to pass the entire vertical column into your function at once. Because your function was designed to read multiple data points horizontally across a single row, you must explicitly use `axis=1` to tell Pandas to feed the data through row by row. (And regarding C, omitting the parentheses on the function name inside `.apply()` is actually the correct syntax!).

```

---

## 6. Exercise: Transform the Dataset

Let us put your new vectorized math and plotting skills to the test. We will use the extended Kloten dataset to test a scientific approximation and build a derived environmental indicator.

### Task 1: Approximating the Daily Mean

The `tmean` column in our dataset is highly accurate because the modern Kloten sensor calculates it by averaging 24 separate hourly measurements. However, many historical weather stations only recorded the daily maximum (`tmax`) and minimum (`tmin`).

Can we accurately guess the true daily mean by just averaging the min and max? Let's find out!

1. Calculate a new column called `tmean_approx` by averaging `tmax` and `tmin`. *(Hint: Add them together first, then divide by 2. Do not forget your algebraic parentheses!)*
2. Calculate a new column called `tmean_error` by subtracting your `tmean_approx` from the true `tmean`.
3. **Plot the results:** Create a line plot of your `tmean_error` column. Does this simple min/max method usually overestimate or underestimate the true daily temperature?

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
# TASK 1: Testing an Approximation
# 1. Calculate the min/max approximation
data["tmean_approx"] = (data["tmax"] + data["tmin"]) / 2

# 2. Find the error between the true 24h mean and our approximation
data["tmean_error"] = data["tmean"] - data["tmean_approx"]

# 3. Plot the error
data["tmean_error"].plot(
    title="Approximation Error (True Mean vs. Min/Max Mean)", 
    ylabel="Difference (°C)",
    figsize=(10, 4)
);
```
*Observation: If the plot mostly dips below 0, it means the (max+min)/2 method consistently overestimates the true 24-hour average!*

``````

### Task 2: "Feels like" Proxy

Temperature alone does not dictate human comfort. High humidity makes the air feel warmer, while wind makes it feel cooler. Let us combine multiple variables to build a derived indicator.

While we *could* do this with basic vectorized math, let us practice using `.apply()` for situations where formulas are too complex for simple operators. When a function needs data from multiple columns at once, we use `.apply(..., axis=1)` to pass the data row-by-row.

1. **Write the function:** Define a Python function called `calc_feels_like(row)` that calculates and returns the index using this formula:
`row["tmean"] + (0.1 * row["rh"]) - (0.7 * row["wind_speed"])`
2. **Apply the function:** Create a new column called `feels_like_index` by applying your function to the `data` DataFrame. *(Crucial: You must include `axis=1` inside the apply parentheses so Pandas knows to send rows, not columns!)*
3. **Plot the results:** Plot both the original `tmean` and your new `feels_like_index` on the same graph to visually compare how the wind and humidity altered the baseline temperature across the summer.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution
:class: dropdown

```{code-cell} python
# TASK 2: Environmental Indicator

# 1. Define the custom logic
def calc_feels_like(row):
    """Calculates a rough comfort index using temp, humidity, and wind."""
    feels_like = row["tmean"] + (0.1 * row["rh"]) - (0.7 * row["wind_speed"])
    return feels_like

# 2. Apply the function row-by-row (axis=1)
data["feels_like_index"] = data.apply(calc_feels_like, axis=1)

# 3. Plot both columns together
columns_to_plot = ["tmean", "feels_like_index"]
data[columns_to_plot].plot(
    title="True Mean vs. 'Feels Like' Temperature", 
    ylabel="Temperature (°C)",
    xlabel="Days after June 1st",
    figsize=(10, 4)
);
```

``````

---

## 7. Summary: The Power of Loopless Math

Vectorization is the core engine that makes data science in Python viable. By treating entire columns as single mathematical entities, you can process millions of rows of environmental data in fractions of a second.

### Key takeaways

* **Vectorization:** Pandas aligns data arrays and performs operations on all rows simultaneously, entirely eliminating the need for slow `for` loops.
* **Column Operations:** You can use standard mathematical operators (`+`, `-`, `*`, `/`) directly on Series objects to perform rapid, element-wise calculations.
* **New Columns:** You can save calculations permanently by assigning them to a new column name using brackets: `df["new_col"] = ...`
* **Visualization:** Doing math is only half the job. The `.plot()` method allows you to instantly verify your calculations, and parameters like `figsize`, `color`, and `style` turn raw data into readable scientific stories.
* **The Apply Method:** For logic too complex for simple algebra (like `if/else` conditions), you can write a custom Python function and map it across your data using `.apply()`. **Remember:** Use `axis=1` if your function needs to read multiple columns row-by-row!

### What comes next?

You now know how to clean your data, compute new variables, and plot the daily values. But what if you want to zoom out and look at the big picture?

How do we find the absolute highest temperature of the entire summer? What is the average rainfall for the month of June specifically? How would we combine this Kloten dataset with sensor data from Geneva?

In the next chapter, **Summarizing, Aggregating, and Joining**, we will learn how to extract high-level statistical insights from thousands of rows of raw data, group our information into manageable categories, and merge separate tables together.
