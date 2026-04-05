---
title: Practical L8 - Solutions

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Interactive Exploration and Data-Driven Cartography
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/10_L08_data-visualisation/07_practical_L8-solutions.ipynb)

---


```{admonition} A Note on Visualisation
:class: important

**Welcome to the art of spatial data science.** Up until now, our focus has been on data wrangling, topological queries, and statistical calculations. In this practical, you step into the role of a web cartographer and data artist. You will build an interactive web app to explore global hydrological basins, and then use your interactive map to select a region of interest to design a striking, high-resolution "dark mode" river map.
```

## Learning objectives

After completing this practical, you will be able to:

  * build multi-layered interactive web apps using GeoPandas `.explore()` and Folium.
  * utilize the `mask` parameter in GeoPandas to efficiently clip large vector datasets upon reading.
  * engineer visual variables by mathematically scaling raw attributes (catchment area) to visual properties (line thickness).
  * apply custom cartographic styling in Matplotlib to generate presentation-ready data art.

---

## Practical storyline

You have been hired as a geospatial visualization specialist for a major international water conservation NGO. They are preparing a flagship annual digital report on global freshwater ecosystems.

Your task is twofold. First, you must build an interactive "Basin Explorer" web app that allows the research team to view HydroSHEDS basins at varying levels of detail (Levels 1 to 3). Second, once the team uses your web app to select a specific basin of interest, you will run an automated cartography pipeline to generate a stunning, high-resolution "dark mode" atlas of that basin's river network, where the physical width of the rivers dynamically scales based on their upstream catchment area.

---

## Part 0 – The Data Intake Helper

For this practical, we are using the **HydroRIVERS** dataset (filtered) [831 MB] and the **HydroSHEDS** basin boundaries (Levels 1 [27 MB], 2 [36 MB], and 3 [47 MB]). As these datasets are larger than usual, they have been stored outside GitLab. For convenience, they are hosted on Google Drive, where we can use the `gdown` library to download them directly into our local environment. Alternatively, you can download the datasets manually using this [link](https://drive.google.com/drive/folders/1FiMjQdKq4xt31cYXSCHPhi5-0jriD3If?usp=sharing). The data can also be found on the university course server under the `course/sds210/data/L08/`.

### Tasks

1.  Run the cell below to download the required datasets to your local `data` folder.

```{code-cell} python
import os
import geopandas as gpd
import matplotlib.pyplot as plt
import folium

# Install packages (if needed)
# !pip install gdown
import gdown

# !pip install cmcrameri
import cmcrameri.cm as cmc

# Create data directory
data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

# Dictionary of file IDs and their output names
datasets = {
    'hydrorivers_100.gpkg': '1fbJewilJnHkEQjNxEbhid0EGVH1X2Evi',
    'hydrosheds_basins_level_01.gpkg': '1wReA_w83eO8sR-4Ma_j-JvtjoSeCU5Z0',
    'hydrosheds_basins_level_02.gpkg': '1uA4qvCIv0egR7698WkI8oUIidjmPLt_n',
    'hydrosheds_basins_level_03.gpkg': '1mJcFlzCEt-K60DoVX8BE1gmEFhfTDux3'
}

for filename, file_id in datasets.items():
    filepath = os.path.join(data_folder, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, filepath, quiet=False)
    else:
        print(f"{filename} already exists.")

rivers_fp = os.path.join(data_folder, 'hydrorivers_100.gpkg')
basins_l1_fp = os.path.join(data_folder, 'hydrosheds_basins_level_01.gpkg')
basins_l2_fp = os.path.join(data_folder, 'hydrosheds_basins_level_02.gpkg')
basins_l3_fp = os.path.join(data_folder, 'hydrosheds_basins_level_03.gpkg')
```

---

## Part 1 – The Basin Explorer Web App

Before we load the massive river dataset, we need to decide which basin to map. We will build an interactive map featuring the three HydroSHEDS basin layers. We will format the tooltips so the researchers can easily read the catchment areas and retrieve the unique Basin ID.

### Tasks

1.  **Load the Basins:** Read the Level 1, 2, and 3 basin GeoPackages into GeoDataFrames (`l1`, `l2`, `l3`). Ensure they are all in `EPSG:4326`.
2.  **Format the Tooltip:** The `UP_AREA` column contains the upstream area in square kilometers. Create a new column in each GeoDataFrame called `Tooltip_Area` that formats this number for human readability (e.g., `Area: 4'256'308 km²`).
3.  **Initialize the Web App:** Create a `folium.Map` centered globally (e.g., `location=[20, 0]`) with a `zoom_start` of 3. Use a dark basemap like `"CartoDB DarkMatter"`.
4.  **Add the Layers:** Use the [`.explore()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html#geopandas.GeoDataFrame.explore) method on each GeoDataFrame to add them to your map.
      * Color the polygons based on `UP_AREA`. Choose suitable colormaps from [matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html) and [crameri](https://www.fabiocrameri.ch/colourmaps/).
      * Set the fill transparency high enough to see the basemap (e.g. `alpha=0.4`).
      * Set the tooltips to show the `HYBAS_ID` and your newly formatted `Tooltip_Area`.
      * Turn `show=False` for Levels 2 and 3 so the map isn't cluttered on load.
5.  **Layer Control:** Add a `folium.LayerControl()` and display your app. Explore the map and pick a basin you find interesting! Write down its `HYBAS_ID`.

<!-- end list -->

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
# 1. Load the basins and ensure standard projection
l1 = gpd.read_file(basins_l1_fp).to_crs(epsg=4326)
l2 = gpd.read_file(basins_l2_fp).to_crs(epsg=4326)
l3 = gpd.read_file(basins_l3_fp).to_crs(epsg=4326)

# 2. Format the tooltip strings using a lambda function
format_area = lambda x: f"Area: {x:,.0f} km²".replace(',', "'")

l1['Tooltip_Area'] = l1['UP_AREA'].apply(format_area)
l2['Tooltip_Area'] = l2['UP_AREA'].apply(format_area)
l3['Tooltip_Area'] = l3['UP_AREA'].apply(format_area)

# 3. Initialize the Web App
basin_app = folium.Map(location=[20, 0], zoom_start=3, tiles="CartoDB DarkMatter")

# 4. Add the Layers using .explore()
# Note: We use style_kwds to control the outline (color) and fill transparency
l1.explore(
    m=basin_app, 
    column='UP_AREA', 
    name='Level 1 Basins',
    tooltip=['HYBAS_ID', 'Tooltip_Area'], 
    cmap='cmc.batlow',
    style_kwds={'fillOpacity': 0.4, 'color': 'white', 'weight': 1},
    show=True
)

l2.explore(
    m=basin_app, 
    column='UP_AREA', 
    name='Level 2 Basins',
    tooltip=['HYBAS_ID', 'Tooltip_Area'], 
    cmap='inferno',
    style_kwds={'fillOpacity': 0.4, 'color': 'white', 'weight': 0.5},
    show=False # Hidden by default
)

l3.explore(
    m=basin_app, 
    column='UP_AREA', 
    name='Level 3 Basins',
    tooltip=['HYBAS_ID', 'Tooltip_Area'], 
    cmap='viridis',
    style_kwds={'fillOpacity': 0.4, 'color': 'white', 'weight': 0.2},
    show=False # Hidden by default
)

# 5. Add Layer Control and display
folium.LayerControl().add_to(basin_app)
basin_app
```
````

---

## Part 2 – Extracting the River Network

Now that you have explored the basins, it is time to load the actual river data. Instead of loading the entire world (which would crash your computer), we will use your chosen basin as a spatial `mask`.

### Tasks

1.  **Define Your Basin:** Create a variable `target_basin_id` and assign it the `HYBAS_ID` of the basin you selected in Part 1 (e.g., the Amazon basin in South America, or the Congo basin in Africa).
2.  **Filter the Boundary:** Filter the appropriate basin GeoDataFrame (L1, L2, or L3 depending on where you got your ID) to keep only the row matching your `target_basin_id`. Save this as `selected_basin`.
3.  **Mask and Load:** Use [`gpd.read_file()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html#geopandas.read_file) to load the `rivers_fp`. Pass your `selected_basin` GeoDataFrame to the `mask` parameter. Save the result as `river_gdf`.

<!-- end list -->

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
# 1. Define the target basin (Example: A large Level 2 basin in South America)
target_basin_id = 4020024190 

# 2. Filter the boundary polygon
selected_basin = l2[l2['HYBAS_ID'] == target_basin_id]

# 3. Load the rivers, masking them to only our chosen basin
print(f"Loading rivers for Basin ID: {target_basin_id}...")
river_gdf = gpd.read_file(rivers_fp, mask=selected_basin)
print(f"Loaded {len(river_gdf)} river segments.")
```
````

---

## Part 3 – Engineering Visual Variables

If we plot the rivers now, they will all be exactly the same thickness. A tiny upstream tributary will look identical to the massive main river channel.

To fix this, we need to map the data to a visual variable. We will scale the upstream catchment area (`UPLAND_SKM`) into a visual line width ranging between 0.2 and 2.0.

### Tasks

1.  **Define Bounds:** Create variables: `original_min = 300`, `original_max = 50000` (adjust this upper limit depending on how massive your chosen basin is!), `target_min = 0.2`, and `target_max = 2.0`.
2.  **Scale the Data:** Calculate the scaled fraction: `(river_gdf['UPLAND_SKM'] - original_min) / (original_max - original_min)`.
3.  **Calculate the Width:** Create a new column `river_gdf['width']`. Apply [`.clip(0, 1)`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.clip.html#geopandas.GeoSeries.clip) to your scaled fraction to prevent massive outliers from breaking the map, then multiply it by `(target_max - target_min)` and add `target_min`.
4.  **Sort the Data:** Sort your dataframe by `UPLAND_SKM` (ascending). This guarantees that the thickest, largest rivers are drawn *last* (on top of the smaller streams) so they stand out boldly.

<!-- end list -->

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
# 1. Define bounds
original_min = 300
original_max = 50000
target_min = 0.2
target_max = 2.0

# 2 & 3. Scale the upland area to our target visual width
scaled = (river_gdf['UPLAND_SKM'] - original_min) / (original_max - original_min)
river_gdf['width'] = scaled.clip(0, 1) * (target_max - target_min) + target_min

# 4. Sort the dataframe so thick rivers are drawn last (on top)
river_gdf = river_gdf.sort_values(by=['UPLAND_SKM'])
```
````

---

## Part 4 – The Dark Canvas (Data Art)

It is time to generate the final, high-resolution static map for the NGO's report. We will use a dark cartographic theme to simulate a glowing, neon river network.

### Tasks

1.  **Setup Canvas:** Create a `fig, ax` subplot with `figsize=(12, 12)`.
2.  **Paint it Black:** Set the background color of the overall figure using `fig.patch.set_facecolor('black')` and the plot area using `ax.set_facecolor('black')`.
3.  **Plot the Rivers:** Call [`.plot()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.plot.html) on your `river_gdf`.
      * Color each distinct sub-basin by setting `column='MAIN_RIV'` and `categorical=True`.
      * Use a vibrant colormap like `cmap='hsv'` or `cmap='magma'`.
      * **Crucial:** Set `linewidth=river_gdf['width']` so every river segment is drawn with its custom calculated thickness!
4.  **Final Polish:** Add a white title (e.g., "Basin Hydrology") and turn the axis off.

<!-- end list -->

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
# 1. Setup Canvas
fig, ax = plt.subplots(figsize=(12, 12))

# 2. Paint it Black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# 3. Plot the Rivers
river_gdf.plot(
    ax=ax,
    column='MAIN_RIV',            # Distinct ID for each main river network
    categorical=True,             # Treat the ID as a category
    cmap='hsv',                   # A vibrant, neon color map
    linewidth=river_gdf['width'], # Use our engineered visual variable!
    alpha=0.9
)

# 4. Final Polish
ax.set_title(f"Hydrological Network (Basin {target_basin_id})", color="white", fontsize=20, pad=20)
ax.axis("off")

plt.tight_layout()
plt.show()
```

**Key idea:**
By using `linewidth=river_gdf['width']`, you are feeding an entire column of dynamic, pre-calculated values directly into the Matplotlib rendering engine. This allows tens of thousands of distinct geometries to have their own unique styling in a single line of code!


:::{figure} images/13_rivermap.png
:alt: A striking, dark-themed map of a hydrological basin. The river network glows in vibrant, neon colors against a solid black background. The main river channels are drawn with thick lines, while the network branches out into thousands of progressively thinner, delicate tributaries.
:width: 600px
:align: center

*The final result: A presentation-ready piece of data art. By mathematically scaling the line widths based on upstream catchment area and utilizing a high-contrast dark theme, the complex hierarchical structure of the basin is vividly brought to life.*
:::

````

---

## Reflection

Take a step back and review your workflow. You built a web app to navigate the globe, isolated a massive dataset using spatial masks, and mapped raw statistics into data art. Please answer the following questions briefly:

1.  **Web vs. Static:** Why was it a good idea to use an interactive Folium map to explore the basin *polygons*, but a static Matplotlib map to render the highly detailed river *lines*?
2.  **The Mask Parameter:** Why is passing the `mask` parameter directly into `gpd.read_file()` so much more efficient than loading the entire global river dataset and then clipping it afterward?
3.  **Visual Hierarchy:** In Part 3, why was it mathematically necessary to use `.clip(0, 1)` on our scaled fraction before calculating the final width? What would happen visually to the main river channel if we didn't clip the upper limit?

<!-- end list -->

```{code-cell} python
# Write your reflections here (as python comments or in a markdown cell)

```

```{admonition} Sample Answers
:class: dropdown

1. **Web vs. Static:** Web maps (Folium/Leaflet) render every geometry as an interactive browser element. While browsers easily handle hundreds of basin polygons, trying to render hundreds of thousands of complex river lines would instantly crash the webpage. Matplotlib, however, flattens everything into a single, high-resolution static image (PNG), making it perfect for incredibly dense visual data.
2. **The Mask Parameter:** Loading the entire global dataset reads gigabytes of coordinate data into your computer's memory. The `mask` parameter acts as a filter at the hard drive level—it checks the spatial index of the file and only permits the geometries inside your specific basin polygon to enter your computer's RAM.
3. **Visual Hierarchy:** Without `.clip(0, 1)`, a massive river segment with an upland area of 2,000,000 sq km would generate a scaled multiplier of 40x. The resulting line thickness would be so wide it would completely obliterate and cover the entire basin on the plot, ruining the map.
```