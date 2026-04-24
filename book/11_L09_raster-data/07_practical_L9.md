---
title: Practical L9

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Tracking Surface Changes with Satellite Data
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/11_L09_raster-data/07_practical_L9.ipynb)

---

```{admonition} A Note on Raster Workflows
:class: important
**Welcome to the matrix.** Up until now, you have relied heavily on GeoPandas to manage discrete vector shapes. In this practical, you will drop down to the core of spatial data science: multidimensional arrays. You will use `rasterio` to read raw satellite imagery and `numpy` to build custom spectral change detection algorithms from scratch. 
Do not be intimidated by the math. At its core, raster analysis is just adding, subtracting, and multiplying pixels with each other.
```

## Learning objectives

After completing this practical, you will be able to:

* read, inspect, and extract multi-band raster data using `rasterio`.
* manipulate array dimensions to properly visualize False Color Composites in `matplotlib`.
* apply mathematical scaling and normalization across specific array axes using `numpy`.
* calculate advanced spectral change metrics (Euclidean Distance and Cosine Similarity).
* derive statistical Z-scores and apply boolean masking to isolate areas of significant land-cover change.

---

## Practical storyline

You have been tasked with monitoring the massive expansion of the Urtmorin [Solar Park](https://en.wikipedia.org/wiki/List_of_photovoltaic_power_stations) in China. The project is a critical piece of the global energy transition.

To bypass the complexities of cloud-masking raw data on your local machine, a data engineer has already pre-processed the Sentinel-2 data in Google Earth Engine. They have provided you with two clean, median composites representing the summer seasons of **2017** (before major expansion) and **2025** ('current' state). Both images contain six spectral bands (B2, B3, B4, B8, B11, B12).

Your task is to write a Python pipeline that compares these two massive arrays, calculates the spectral distance between them, and isolates the pixels where new solar panels were installed, and calculates their total area.

---

## Part 0 – The Data Intake Helper

We will use the `gdown` library to download the two pre-processed Sentinel-2 `.tif` files. Alterantively you will find these files also on [GitLab](https://gitlab.com/HendrikWulf/sds210/-/tree/0bd25613a7742fde5d8e37a4a31ae5cde1d9d5cc/L09/data).

### Tasks

1.  Run the cell below to download the required datasets to your local `data` folder.

```{code-cell} python
import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Install packages (if needed in Colab)
# !pip install gdown

import gdown

# Create data directory
data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

# Dictionary of file IDs and their output names
datasets = {
    's2_composite_2017.tif': '1nKuXp1pk2nWx7pXsSHegDYoJflkBhVuw',
    's2_composite_2025.tif': '1OOcFk_UG_rBbiSDRXfHGKXmnMkANGUlU'
}

for filename, file_id in datasets.items():
    filepath = os.path.join(data_folder, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, filepath, quiet=False)
    else:
        print(f"{filename} already exists.")

s2_2017_fp = os.path.join(data_folder, 's2_composite_2017.tif')
s2_2025_fp = os.path.join(data_folder, 's2_composite_2025.tif')
```

---

## Part 1 – Reading & Visualizing

To understand what has changed, we must first look at the data. Sentinel-2 data is often stored as 16-bit integers with values roughly ranging from 0 to 10,000. 

The 6 bands in our file correspond to the following NumPy indices (0-based):
* `Index 0`: Blue (B2)
* `Index 1`: Green (B3)
* `Index 2`: Red (B4)
* `Index 3`: Near-Infrared / NIR (B8)
* `Index 4`: SWIR-1 (B11)
* `Index 5`: SWIR-2 (B12)

### Tasks
1. **Load the Data:** Use `rasterio.open()` to read the entire 2017 and 2025 images into NumPy arrays called `img_2017` and `img_2025`. Check their `.shape` to confirm they have 6 bands.
2. **Define a Normalization Function:** Just like you did with Landsat, define a `normalize(array, vmin=0, vmax=3500)` function that [clips](https://numpy.org/devdocs/reference/generated/numpy.clip.html#numpy.clip) the array to those bounds and scales it to a `0-1` range for display. *(Note: We use `3500` instead of `0.4` here because Sentinel-2 reflectance is scaled up to ~10,000).*
3. **Extract and Normalize Bands:** For both 2017 and 2025, extract the 2D arrays for SWIR-2 (`Index 5`), NIR (`Index 3`), and Red (`Index 2`). Pass each of these 2D arrays through your `normalize` function.
4. **Stack and Plot:** Use [`np.dstack()`](https://numpy.org/devdocs/reference/generated/numpy.dstack.html#numpy-dstack) to stack your three normalized bands into False Color Composites (`fcc_2017` and `fcc_2025`). Plot both composites side-by-side using `plt.subplots(1, 2)`.

```{code-cell} python
# Write your code here
```

---

## Part 2 – Scaling & Normalization

To perform robust spectral change detection, especially when using metrics like Cosine Similarity, we need to mathematically transform our raw data. 

The goal is twofold: first, scale the reflectance values from their original range `[0, 10000]` down to `[-1, 1]`; second, normalize each pixel's 6-band spectral signature into a **unit vector** (a vector with a length of exactly 1 in 6-dimensional space).

```{admonition} Why Cosine Similarity and [-1, 1] Scaling?
:class: note

Cosine similarity evaluates the angle between two vectors, making it highly robust against overall brightness changes (like shadows or slight illumination differences). Scaling data to `[-1, 1]` and computing cosine similarity is a standard technique used with AI Foundation Models, such as **Alpha Earth embeddings**. In this practical, we are mimicking that exact preprocessing workflow to test the suitability and performance of the cosine similarity on raw Sentinel-2 spectral bands.
```

### Tasks

1.  **Handle NaNs and Scale the Arrays:** Satellite imagery often contains "NoData" pixels around the edges represented as `NaN` (Not a Number). If left unchecked, these NaNs will propagate through our equations and potentially break the analysis. First, wrap your raw arrays in `np.nan_to_num()` to safely convert missing values to `0`. Then, create `scaled_2017` and `scaled_2025` using the following formula:
    $x_{scaled} = \frac{x}{5000.0} - 1.0$
    *(Note: We are using the original `(Bands, Rows, Cols)` arrays so the math broadcasts correctly across the entire matrix!)*
2.  **Calculate Vector Lengths (Norm):** To normalize a vector, we first need its length (magnitude). Calculate the Euclidean norm by squaring the scaled array, summing it across the bands (`axis=0`), and taking the square root. Save these as `norm_2017` and `norm_2025`.
    $||v|| = \sqrt{\sum_{i=1}^{n} v_i^2}$ *(where $n=6$ bands)*
3.  **Normalize to Unit Length:** Divide the scaled arrays by their respective norms to create unit vectors. Save these as `unit_2017` and `unit_2025`.
    $\hat{v} = \frac{v}{||v||}$

```{code-cell} python
# Write your code here
```

---

## Part 3 – Detecting Changes

We are now ready to quantify change. We will calculate two different metrics to evaluate how the landscape has evolved.

* **Euclidean Distance:** Measures how far apart the pixels are in 6D space. This is highly sensitive to overall brightness (magnitude). A shadow falling on the exact same patch of dirt will result in a large Euclidean distance.
* **Cosine Similarity:** Measures the angle between their spectral signatures. This evaluates the *shape* of the spectrum (the actual material/color), making it highly robust against shadows or illumination differences.

*For an interactive vector visualizer highlighting the difference between the Euclidean Distance and the Cosine Similarity, follow this [link](https://hendrikwulf.github.io/sds210_assets_L09_ch07_sam_ed_visualizer/).*

### Tasks
1. **Euclidean Distance:** Subtract `img_2017` from `img_2025`, square the result, sum it across the bands (`axis=0`), and take the square root. Save as `change_ed`.
2. **Cosine Similarity:** Multiply `unit_2017` by `unit_2025` element-wise, and sum the result across the bands (`axis=0`). Save as `cosine_sim`.
3. **Change Cosine:** A similarity of `1` means no change. To convert this into a "Change Score", calculate `1.0 - cosine_sim` and save it as `change_cosine`.
4. **Plot the Metrics:** Plot `change_ed` and `change_cosine` side-by-side using `plt.subplots`. Choose a suitable colorbar and vmin/vmax values.

```{admonition} The Dot Product
:class: note

In linear algebra, the formula for the cosine of the angle $\theta$ between two vectors is their dot product divided by the product of their lengths (magnitudes):

$$\cos(\theta) = \frac{A \cdot B}{||A|| \times ||B||}$$

Because you spent Part 2 normalizing your arrays so that their lengths ($||A||$ and $||B||$) are exactly $1$, the bottom half of that equation just becomes $1 \times 1$. The denominator disappears. 

Therefore, when dealing with unit vectors, the **Cosine Similarity is mathematically identical to the Dot Product**. You can calculate it simply by multiplying the two vectors element-wise and summing the result!
```

```{code-cell} python
# Write your code here
```

---

## Part 4 – Masking & Quantifying

We have a continuous map of change, but to deliver actionable intelligence to stakeholders, we need to classify it. Is a change score of `0.2` significant? What about `0.8`?

Instead of guessing, we will use statistics. We will calculate the mean and standard deviation of the landscape, and convert our map into a **Z-Score** (which tells us exactly how many standard deviations away from the mean a pixel is). Finally, we will apply a threshold to isolate the solar panels and calculate their total physical area.

### Tasks

1.  **Calculate Stats:** Calculate the `mean_val` and `std_val` of your `change_cosine` array using `np.nanmean()` and `np.nanstd()`.
2.  **Calculate Z-Score:** Subtract the mean from `change_cosine`, and divide by the standard deviation. Save as `z_score`.
3.  **Boolean Mask:** Define a variable `threshold = 0.5`. Create a mask called `strong_change` that is `True` wherever the `z_score` is strictly greater than this threshold.
4.  **Calculate Area:** Sentinel-2 pixels have a spatial resolution of 10m x 10m (100 m² per pixel). Use `np.sum()` on your boolean mask to count the number of changed pixels. Multiply this count by the pixel area to get total square meters, convert it to square kilometers (divide by 1,000,000), and print the result.
5.  **Visualize the Final Product:** Create a 1x2 side-by-side plot (`plt.subplots(1, 2)`). 
    * **Plot 1 (Left):** Plot the continuous `z_score` array along with a colorbar.
    * **Plot 2 (Right):** Plot the `fcc_2025` image as a background. Then, overlay your `strong_change` mask using `cmap='winter'` and `alpha=0.8`. *(Hint: To make the `False` values invisible, use `np.where(strong_change, 1, np.nan)` before plotting the mask, see: [where](https://numpy.org/devdocs/reference/generated/numpy.where.html#)).*

```{code-cell} python
# Write your code here
```

---

## Reflection

Take a step back and review what you have built. You translated a complex, cloud-based Earth Engine algorithm into raw, localized Python math using multidimensional arrays.

Please answer the following questions briefly:

1.  **Euclidean vs. Cosine:** In Part 3, we calculated both Euclidean Distance and Cosine Similarity. Euclidean distance measures raw magnitude, while Cosine similarity measures the *angle* (the shape) of the spectral signature. Why might Cosine Similarity be more robust against shadows or slight differences in sunlight between 2017 and 2025?
2.  **The Power of NumPy:** In Part 2, you normalized the vectors by running `np.sum(scaled_2017**2, axis=0)`. If this image has 2 million pixels, how many `for` loops did you explicitly write in Python to do that math? What makes NumPy so much faster?
3.  **Statistical Thresholding:** In Part 4, we used a statistically derived Z-score threshold instead of just hardcoding a raw change score limit like `0.15`. Why is a Z-score more adaptable if you were asked to run this exact same script on a different solar park in a completely different climate zone (like a snowy region or a dense forest)?

```{code-cell} python
# Write your reflections here (as python comments or in a markdown cell)
```

```{admonition} Sample Answers
:class: dropdown
1. **Euclidean vs. Cosine:** Euclidean distance is highly sensitive to overall brightness. A pixel in a shadow in 2025 will have a large Euclidean distance from a sunlit pixel in 2017, even if it is the exact same material (like bare soil). Cosine similarity measures the *shape* of the spectral signature regardless of brightness. A shadow reduces the magnitude of all bands proportionally, but the angle of the vector remains nearly identical, preventing false positives.
2. **The Power of NumPy:** You wrote exactly **zero** `for` loops. NumPy utilizes "vectorization." Instead of passing each of the 2 million pixels through the slow Python interpreter one by one, it pushes the entire matrix operation down to highly optimized, pre-compiled C code that executes simultaneously.
3. **Statistical Thresholding:** A hardcoded threshold of `0.15` might isolate solar panels perfectly in a stable, arid desert where nothing else changes. However, if you run that in a forest that experiences massive seasonal leaf-drop, the entire forest might register a change of `0.2`. The Z-score is locally adaptive. It normalizes the change relative to the *baseline variability* of that specific landscape, ensuring you only flag the statistically extreme anomalies for that specific region.
```