---
title: Practical L6

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Mastering Environmental Data with Pandas
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/08_L06_data-frames/08_practical_L6.ipynb)

---

## Learning objectives

After completing this practical, you will be able to:

* ingest and inspect raw, multi-decade tabular data using `read_csv` and `.info()`
* sanitize datasets by renaming columns, fixing data types, and safely interpolating missing `NaN` values
* leverage vectorization to calculate new environmental indicators without `for` loops
* apply Boolean indexing to slice and filter data based on multiple logical conditions
* harness the DatetimeIndex to resample high-frequency data and calculate moving averages
* quantify long-term climate change by extracting the slope of a linear trendline using NumPy

---

## Practical storyline

You have been hired as an environmental data consultant for a historic ski resort in the Swiss Alps. The resort management is deeply worried about long-term climate trends threatening their winter snowpack and bringing extreme summer heatwaves. They have handed you a raw, multi-decade dataset from their local weather station spanning from 1972 to the present day (`magic_mountain_weather.csv`).

Unfortunately, the historic sensor data is messy. The column names are cryptic, the system occasionally recorded precipitation as text instead of numbers, and power outages left gaps in the readings. Your job is to ingest this file, sanitize it, calculate derived extreme indicators, plot a smoothed historical trend, and mathematically prove exactly how much the climate has warmed since 1972.

---

## Part 1 – The Intake Workflow

Before we can analyze anything, we need to load the data, understand its shape, and set up our temporal index. 

```{admonition} Download the Dataset
:class: note
Please download this file to your local working directory:
* [magic_mountain_weather.csv](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L06/data/magic_mountain_weather.csv)

```

*(Note: For this practical, assume the file `magic_mountain_weather.csv` is in your working directory. The raw file contains a header row and columns for Date, maximum temperature, minimum temperature, and daily precipitation).*

### Tasks

1. Load the dataset into a variable called `climate_data`. Use the `parse_dates` parameter to instantly convert the `"TIMESTAMP"` column into datetime objects.
2. Set the newly parsed `"TIMESTAMP"` column as the DataFrame's index.
3. Run the critical "first 30 seconds" check: Print the `.shape` of the DataFrame, and then use the `.info()` method to inspect the data types and look for missing values.

```{code-cell} python
import pandas as pd

# Write your code here

```

---

## Part 2 – Cleaning the Mess

Based on your `.info()` output, you should have noticed a few glaring issues. The column names are ugly, there are missing values, and one of the numeric columns is hiding as an `object` (text) type!

### Tasks

1. **Rename columns:** Use a dictionary to rename the following cryptic columns to standard, lowercase names:
    * `"T_MAX_C"` $\rightarrow$ `"temp_max"`
    * `"T_MIN_C"` $\rightarrow$ `"temp_min"`
    * `"PRECIP_MM"` $\rightarrow$ `"precip"`
2. **Fix data types:** The `precip` column is stored as an `object` because the sensor occasionally wrote the word `"Trace"` instead of `0.0` for light snow/rain. First, replace the word `"Trace"` with `"0.0"`, and then convert the entire column to a `float` using `.astype()`.
3. **Handle NaNs:** You noticed gaps in the `temp_max` column. Because this is daily time-series data, dropping them or filling them with a static average is scientifically dangerous. Use `.interpolate()` to estimate the missing temperatures by connecting the dots between the surrounding days.


```{code-cell} python
# Write your code here

```

---

## Part 3 – Vectorization and Slicing

The data is finally clean. Now, the resort management wants to know about "Extreme Temperature Swings"—days where the temperature fluctuated wildly between freezing nights and hot days. We will calculate this instantly using vectorization, and then filter the dataset to find the most extreme days over the last 5 decades.

### Tasks

1. **Vectorize:** Create a new column called `temp_swing` by subtracting `temp_min` from `temp_max`. 
2. **Filter (Boolean Indexing):** Create a new DataFrame called `extreme_days` that only contains rows where the `temp_swing` was greater than **18.0** °C AND the `precip` was exactly **0.0** (dry days). 
    * *Crucial constraint:* Remember to wrap your conditions in parentheses `()` and append `.copy()` to avoid the `SettingWithCopyWarning`!
3. **Sort and Peek:** Sort your `extreme_days` DataFrame by `temp_swing` in descending order (highest swing at the top). Display the top 5 rows using `.head()`.

```{code-cell} python
# Write your code here

```

---

## Part 4 – Temporal Superpowers

Management doesn't just want to see extreme individual days; they want to see the big picture. Daily weather data over 50 years is just a solid wall of noise. We need to use Pandas' time-travel tools to smooth the data out and reveal the underlying climate trajectory.

### Tasks

1. **Resample:** Create a new DataFrame called `monthly_climate` by resampling the original `climate_data` into monthly averages (`"MS"`). Calculate the `.mean()` for these monthly buckets.
2. **Rolling Window:** Create a new column inside `monthly_climate` called `10_year_trend`. Calculate this using a `.rolling(120)` window (120 months = 10 years) on the `temp_max` column, taking the `.mean()`. This will smooth out the yearly seasons and expose the true climate shift!
3. **Plot:** Generate a professional visualization from your `monthly_climate` DataFrame. 
    * Plot both the raw monthly `temp_max` and your smoothed `10_year_trend`.
    * Use `figsize=(12, 6)`.
    * Apply distinct colors (e.g., light gray for the monthly data, a thick crimson line for the trend).
    * Add a descriptive `title`, a `ylabel` ("Temperature (°C)"), and enable the `grid`.

```{code-cell} python
# Write your code here

```

---

## Part 5 – Quantifying the Warming Trend

Visualizing the red line going up in your plot is powerful, but management needs a hard number to justify their climate adaptation budget. Exactly how much has the average temperature risen per year since 1972?

To find out, we will calculate a linear trendline (the slope) using NumPy.

### Tasks

1. **Import:** Import the `numpy` library.
2. **Resample to Annual:** Take the `temp_max` column from your cleaned `climate_data` and `.resample("YE")` it to get annual (Year-End) averages. Make sure to apply `.mean()` and then chain `.dropna()` to the end of it to ensure no missing years mess up the math. Save this to a variable called `annual_temps`.
3. **Create the Time Array:** Create a simple numerical array representing the passing years (0, 1, 2, 3...) using `years_passed = np.arange(len(annual_temps))`.
4. **Calculate the Trend:** Use `coefficients = np.polyfit(years_passed, annual_temps, 1)` to fit a straight line to your data. Then, use `np.polyval(coefficients, years_passed)` to generate the actual Y-values for your `trend_line`.
5. **Print the Verdict:** Extract the `slope` and `intercept` from your coefficients. Print the warming trend in °C per year, and calculate the *total* warming over the entire dataset (`slope * len(years_passed)`).
6. **Visualize the Warming:** Convert your `trend_line` array back into a Pandas Series (making sure to use `annual_temps.index` so the years match). Combine the actual annual temperatures and your new trend line into a single DataFrame, and `.plot()` them together to visually prove the warming trend!

```{code-cell} python
# Write your code here

```

---

## Reflection

Take a moment to review what you have built and analyzed. Answer briefly in comments or markdown:

1. In Part 2, why was using `.interpolate()` a better scientific choice for cleaning missing daily temperatures compared to using `.fillna()` with the overall 50-year average?
2. Look at your final plot in Part 4. Explain the visual difference between the monthly resampled data and the 10-year rolling trend. Why was the rolling trend necessary to answer the management's question?
3. In Part 5, you mathematically quantified the warming trend. Look at the total warming over the dataset. How might this specific number impact a ski resort's business model (e.g., snowmaking requirements or summer tourism)?

```{code-cell} python
# Write your reflections here.

```