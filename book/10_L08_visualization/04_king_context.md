---
title: Context is King

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Adding Basemaps
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/10_L08_visualization/04_king_context.ipynb)

---

```{admonition} Big idea
:class: tip

A beautifully styled thematic map is excellent, but polygons floating in a blank white space often lack real world grounding. In this chapter, you will learn how to add geographical context behind your data using the contextily library. We will explore how to fetch standard web map tiles like satellite imagery or street maps and place them seamlessly beneath your Matplotlib plots.
```

**Preparing the Data**

To follow along with this chapter and complete the exercises, please download the following dataset and place it in a `data` folder next to your notebook. This package contains the predicted spatial data for the total solar eclipse occurring over Europe on September 3 2081.

```{admonition} Data Downloads
:class: note

* [Total Solar Eclipse 2081 - core shadow (total_solar_eclipse_03-09-2081_core_shadow.gpkg)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/total_solar_eclipse_03-09-2081_core_shadow.gpkg)
* [Total Solar Eclipse 2081 - center line (total_solar_eclipse_03-09-2081_center_line.gpkg)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/total_solar_eclipse_03-09-2081_center_line.gpkg)
* [World Cities (worldcities.csv)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/worldcities.csv)
```

---

## 1. What is Contextily?

By now you familiar with the power of GeoPandas and Matplotlib to draw shapes and choropleths. However, creating geospatial visualizations often requires overlaying your data on a background map so the reader understands exactly where in the world the data is located. Until recently, adding these basemaps directly within a Python environment was not a simple task.

**[Contextily](https://contextily.readthedocs.io/en/latest/index.html)** is a lightweight Python package designed specifically to solve this problem. It retrieves map tiles from the internet and adds them to your Matplotlib figures as static background images.

By acting as a bridge between your local Python environment and online map providers, contextily allows you to dynamically fetch exactly the right image tiles for the specific bounding box of your plot. The library integrates seamlessly with the `xyzservices` package, granting you access to popular tile providers like OpenStreetMap, Stamen Design, and CartoDB. Because contextily operates directly on Matplotlib axes objects (`ax`), it effortlessly integrates with your existing GeoPandas workflow.

---

## 2. The Web Mercator Default

Before we can pull tiles from the internet, we must address a crucial spatial requirement. Almost all major online map providers, including Google Maps, OpenStreetMap, and Mapbox, serve their image tiles in a specific coordinate reference system called **[Web Mercator](https://en.wikipedia.org/wiki/Web_Mercator_projection)**.

In the EPSG registry, the official identifier for Web Mercator is **[EPSG:3857](https://epsg.io/3857)**.

### Why Web Mercator?
You might wonder why the entire internet relies on a projection infamous for drastically inflating the size of polar regions (famously making Greenland look as large as Africa). The answer comes down to local navigation and computational speed. 

Web Mercator preserves local angles and shapes perfectly. This means a 90-degree right turn on the map is a true 90-degree turn in reality, and North is always perfectly up—exactly what you need for a street-level navigation app. Furthermore, the spherical math required to render these tiles on the fly is much simpler and faster for servers to compute than highly accurate ellipsoidal models. Because of these traits, Google Maps adopted it in 2005, and the rest of the web simply followed suit.

### The Coordinate Clash
Because it is the de facto standard for web mapping, `contextily` expects to pull and place tiles using this exact projection. However, most raw spatial data (like GPS tracks) is recorded in standard WGS84 latitude and longitude (`EPSG:4326`).

If your spatial data uses a different projection than the basemap, `contextily` will not know how to align the internet tiles with your polygons. Plotting unprojected data over Web Mercator tiles will result in alignment errors, distortion, or a blank map. 

To solve this coordinate clash, spatial data scientists have two options depending on the size of their dataset:

* **Option A: Reproject the Data (The Standard Approach)**
  For most datasets, the easiest and fastest solution is to reproject your GeoDataFrame to match the web tiles before plotting. You can do this effortlessly by appending `.to_crs(epsg=3857)` to your data.
* **Option B: Warp the Tiles (The Advanced Approach)**
  If you are working with a massive, highly detailed dataset (e.g., millions of high-resolution polygons), reprojecting the vector data can be rather slow and computationally expensive. In these cases, it is actually more efficient to leave your data in its native CRS and let `contextily` mathematically "warp" the incoming image tiles to match your data instead. 

For the purposes of this chapter and most standard workflows, we will rely on **Option A** and reproject our GeoDataFrames to Web Mercator prior to mapping.


---

## 3. Adding the Basemap

For those of us based here in the Zurich area, astronomical events like total [solar eclipses](https://en.wikipedia.org/wiki/Solar_eclipse) are exceedingly rare. In fact, the next total solar eclipse visible from Switzerland will not occur until Wednesday, September 3, 2081. If you are lucky, you just might live to see it!

But will our exact location actually be plunged into total darkness, or will we need to travel to see the full effect? To find out, we need to map the predicted path of totality and overlay it onto a real-world basemap.

Let us load the [umbral path polygon](http://xjubier.free.fr/en/site_pages/SolarEclipsesGoogleEarth.html) (the exact zone of total darkness) for the 2081 solar eclipse. We will immediately reproject this data to Web Mercator (`EPSG:3857`) to avoid the coordinate clash trap we discussed in the previous section.

Once the data is plotted on our axes, we use the `ctx.add_basemap(ax)` function. This tool looks at the current spatial boundaries of your axes, connects to the internet to download the corresponding OpenStreetMap tiles, and seamlessly draws them underneath your data.

```{code-cell} python
# Install the contextily package if you haven't already:

# Colab:
# !pip install contextily

# Conda environment (VS Code / JupyterLab):
# conda install -c conda-forge contextily

import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Load the umbral path polygon and instantly reproject to Web Mercator (EPSG:3857)
eclipse_path = gpd.read_file("total_solar_eclipse_03-09-2081_core_shadow.gpkg").to_crs(epsg=3857)

# Set up the Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the eclipse path with transparency so the basemap shows through
eclipse_path.plot(
    ax=ax, 
    facecolor="black", 
    alpha=0.4, 
    edgecolor="none"
)

# Add the default OpenStreetMap basemap
ctx.add_basemap(ax)

ax.set_title("Path of Totality: Solar Eclipse Sept 3rd, 2081", fontsize=16)

plt.show()
```

:::{figure} images/11_basemap_step1.png
:alt: A map showing the dark transparent path of the 2081 solar eclipse sweeping across Europe, overlaid on a standard OpenStreetMap background.
:width: 700px
:align: center

*Output: By ensuring our data is in EPSG:3857, contextily successfully fetches the matching background tiles to provide real-world location context. It looks like Zurich is right in the path of totality!*
:::

---

## 4. Exploring and Customizing Basemaps

Adding a default background map is a great start, but true cartographic design requires making intentional choices about the style, resolution, and framing of your map. `contextily` offers incredible flexibility to customize all of these aspects.

### The Map Provider Library
There is no single "best" basemap. Sometimes you need detailed satellite imagery; other times, a minimalist grey street map is better to make your colorful data pop. `contextily` includes over 200 basemap styles from various online providers. 

You can view the main providers by printing the `ctx.providers` dictionary. On top, you can filter for open-access providers only:

```{code-cell} python
import contextily as ctx

print(list(ctx.providers.filter(requires_token=False)))

```

```text
['OpenStreetMap', 'OpenSeaMap', 'OPNVKarte', 'OpenTopoMap', 'OpenRailwayMap', 'OpenFireMap', 'SafeCast', 'Stadia', 'BaseMapDE', 'CyclOSM', 'Esri', 'FreeMapSK', 'MtbMap', 'CartoDB', 'HikeBike', 'BasemapAT', 'nlmaps', 'NASAGIBS', 'JusticeMap', 'GeoportailFrance', 'OneMapSG', 'USGS', 'WaymarkedTrails', 'OpenAIP', 'OpenSnowMap', 'SwissFederalGeoportal', 'TopPlusOpen', 'Gaode', 'Strava', 'UN']
```

:::{figure} images/11_basemaps_tiles.webp
:alt: A comparison of different web map tile styles including OpenStreetMap, OpenTopoMap, Stamen Toner, Stamen Terrain, CartoDB Positron, and others, all showing the same geographic region with different visual designs.
:width: 700px
:align: center

*Comparison of common web map tile styles. Each basemap represents the same geographic area but emphasizes different features through color, contrast, and level of detail. Choosing an appropriate basemap is a key cartographic decision, as it strongly influences readability and the interpretation of overlaid data.*
:::

Furthermore, each provider offers multiple unique styles. For example, we can inspect the specific basemaps offered by OpenStreetMap:

```{code-cell} python
# Print the names of different basemap styles
print(ctx.providers.OpenStreetMap.keys())
```

```text
dict_keys(['Mapnik', 'DE', 'CH', 'France', 'HOT', 'BZH', 'CAT'])
```

Test different providers and styles by changing the source flag and adding different providers and styles-
```{code-cell} python
# Set up the Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the eclipse path with transparency so the basemap shows through
eclipse_path.plot(
    ax=ax, 
    facecolor="black", 
    alpha=0.4, 
    edgecolor="none"
)

# Replace the default OpenStreetMap with another basemap
ctx.add_basemap(ax, source=ctx.providers.OpenTopoMap.url)

ax.set_title("Path of Totality: Solar Eclipse Sept 3rd, 2081", fontsize=16)
plt.show()
```

:::{figure} images/11_basemap_step2.png
:alt: A map showing the dark transparent path of the 2081 solar eclipse sweeping across Europe, overlaid on a standard OpenTopoMap background.
:width: 700px
:align: center

*The map is now showing the dark transparent path of the 2081 solar eclipse sweeping across Europe, overlaid on the new OpenTopoMap basemap.*
:::

### Controlling Zoom and Resolution
Web map tiles are structured in a [pyramid](https://docs.maptiler.com/google-maps-coordinates-tile-bounds-projection/). At [zoom level](https://docs.maptiler.com/guides/how-maps-work/map-resolution/#zoom-levels-explained) 0, the entire world is rendered in a single image tile. As you zoom in (levels 1, 2, 3... up to 19), the map is divided into exponentially more tiles, revealing greater detail but requiring more data to download.

:::{figure} images/12_web_map_tile_pyramid.png
:alt: A 3D pyramid of web map tiles showing how one tile at zoom level 0 expands into multiple tiles at higher zoom levels, with the same geographic area becoming more detailed at each level.
:width: 500px
:align: center

*Web map tile pyramid. Each zoom level subdivides the same geographic area into more tiles, increasing spatial resolution. The base shows many high-resolution tiles, while the top represents a single low-resolution global tile.*
:::

When you call `ctx.add_basemap()`, contextily automatically calculates a reasonable zoom level based on the current bounding box of your plot. However, you can manually request higher or lower resolution tiles using the `zoom` parameter. 

If you aren't sure what zoom level to use, contextily provides handy utility functions to calculate it based on your data's spatial bounds:

```{code-cell} python
# Calculate the optimal zoom level for the entire eclipse path
zoom_level = ctx.tile._calculate_zoom(*eclipse_path.total_bounds)
print(f"Optimal auto-zoom level: {zoom_level}")

# Check how many tiles a specific zoom level would download
tile_count = ctx.howmany(*eclipse_path.total_bounds, zoom=4, ll=False)
print(f"Tiles required at zoom level 4: {tile_count}")
```

### Polishing the Map: Axes, Extents, and Attribution
Let us put all of this together to create a polished, localized map. 

Since we want to know if Zurich will experience totality, we don't need to look at the entire continent. We can "zoom in" spatially by limiting our axes' view area using `ax.set_xlim()` and `ax.set_ylim()`. 

Finally, we must clean up the visual clutter. The Web Mercator coordinate numbers on the X and Y axes are mathematically accurate (representing meters), but they are entirely useless to a human reader. We will remove them using `ax.set_axis_off()`. Because we are publishing this, we will also use the `attribution` parameter to properly credit both our data source and the map provider.

```{code-cell} python
# Set up the Figure and Axes
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the eclipse path
eclipse_path.plot(
    ax=ax, 
    facecolor="#2c1932", # A dark purple from the twilight palette
    alpha=0.6, 
    edgecolor="none"
)

# 1. Spatial Zoom: Focus on the Alps/Switzerland region 
# (Coordinates are in EPSG:3857 Web Mercator meters)
ax.set_xlim(600000, 1500000)
ax.set_ylim(5700000, 6300000)

# 2. Custom Attribution
custom_credits = "Eclipse Data: NASA | Map Tiles © CartoDB"

# 3. Add Basemap: Use CartoDB Positron for a clean look, set a specific zoom, and apply credits
ctx.add_basemap(
    ax, 
    source=ctx.providers.CartoDB.Positron, 
    zoom=7,
    attribution=custom_credits
)

# 4. Polish: Remove the mathematical axis borders and ticks
ax.set_axis_off()

ax.set_title("Will Zurich see the 2081 Solar Eclipse?", fontsize=16)

plt.show()
```

:::{figure} images/11_basemap_step3.png
:alt: A clean, zoomed-in map of Switzerland and the Alps showing the eclipse path over a light grey CartoDB basemap, with custom attribution text and no mathematical coordinate borders.
:width: 700px
:align: center

*Output: By explicitly controlling the map provider, the zoom level, the spatial extents, and turning off the axes, we have transformed a basic plot into a polished cartographic layout.*
:::

---

## 5. Exercises: Contextualize the Data

Now it is your turn to practice adding real-world context to spatial data and answering geographical questions. 

### Exercise 5.1: The Center Line and Istanbul
We already established that Zurich will be in the path of totality. But what about other major cities? 

**Your Tasks:**
1. Load the `core_shadow` and `center_line` layers, and immediately reproject both to Web Mercator (`epsg=3857`).
2. Create a Figure and Axes setup.
3. Plot the core shadow (e.g., in black with `alpha=0.4`) and the center line (e.g., in orange or red so it stands out).
4. Use contextily to add a new basemap. Try exploring the providers list and pick a different style than before (e.g., `ctx.providers.CartoDB.Voyager` or `ctx.providers.Esri.WorldTerrain`).
5. Remove the axis borders and add a title.
6. Look at your final map: **Will Istanbul experience the total solar eclipse?**

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution 5.1
:class: dropdown

```{code-cell} python
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# 1. Load and reproject to Web Mercator
shadow = gpd.read_file("data/total_solar_eclipse_03-09-2081_core_shadow.gpkg").to_crs(epsg=3857)
center = gpd.read_file("data/total_solar_eclipse_03-09-2081_center_line.gpkg").to_crs(epsg=3857)

# 2. Setup
fig, ax = plt.subplots(figsize=(12, 8))

# 3. Plot the geometris
shadow.plot(ax=ax, facecolor="black", alpha=0.4, edgecolor="none")
center.plot(ax=ax, color="orange", linewidth=2)

# Zoom in on Istanbul region (estimated coordinates)
ax.set_xlim(3130000, 3330000)
ax.set_ylim(4950000, 5150000)

# 4. Add a new basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Voyager, zoom=8)

# 5. Formatting
ax.set_axis_off()
ax.set_title("2081 Total Solar Eclipse: Shadow & Center Line (Istanbul)", fontsize=16)

plt.show()

# 6. Answer:
# Yes! If you look at the map, the dark path of the core shadow passes over the Bosphorus Strait. Istanbul will experience totality!
```

:::{figure} images/11_basemap_exercise_1.png
:alt: A map showing the dark transparent path and orange center line of the 2081 solar eclipse sweeping across Europe and the Middle East, passing clearly over Istanbul.
:width: 700px
:align: center

*Exercise 5.1 Result: A beautifully mapped eclipse path using a new basemap. Istanbul sits comfortably inside the core shadow.*
:::
````

### Exercise 5.2: Calculating Potential Viewers
How many people actually live directly in the path of the eclipse? 

To find out, we need to perform a spatial filter (a point-in-polygon overlay). We will use the `worldcities.csv` dataset, convert it into spatial points, and figure out how many people reside in the cities that fall exactly inside the core shadow.

**Your Tasks:**
1. Load the core shadow and reproject it to `epsg=3857`.
2. Load the `worldcities.csv` dataset using pandas.
3. Use the provided starter code below to convert the CSV into a GeoDataFrame, but be sure to fix the projection to `epsg=3857` so it matches the shadow.
4. Perform a spatial join (`gpd.sjoin`) to filter only the cities that fall `within` the core shadow.
5. Sum the `population` column of the filtered cities and print the result. *(Optional: plot the filtered cities on top of the shadow!)*

**Starter Code:**
```python
import pandas as pd

# Load CSV
df = pd.read_csv("data/worldcities.csv")

# Convert to GeoDataFrame and reproject to Web Mercator
cities = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df.lng, df.lat), 
    crs="EPSG:4326"
).to_crs(epsg=3857) # Replaced 4326 with 3857 to match our basemap projection!
```

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution 5.2
:class: dropdown

```{code-cell} python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# 1. Load shadow
shadow = gpd.read_file("data/total_solar_eclipse_03-09-2081_core_shadow.gpkg").to_crs(epsg=3857)

# 2 & 3. Load CSV, convert to GeoDataFrame, and project to EPSG:3857
df = pd.read_csv("data/worldcities.csv")
cities = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df.lng, df.lat), 
    crs="EPSG:4326"
).to_crs(epsg=3857)

# 4. Spatial join: Keep only cities within the shadow
cities_in_path = gpd.sjoin(cities, shadow, predicate="within")

# 5. Calculate the total population
total_population = cities_in_path["population"].sum()
print(f"Potential viewers in major cities (assuming no clouds!): {total_population:,.0f}")

# Optional: Plotting the result
fig, ax = plt.subplots(figsize=(12, 8))
shadow.plot(ax=ax, facecolor="black", alpha=0.4, edgecolor="none")

# Plot only the filtered cities
cities_in_path.plot(ax=ax, color="yellow", markersize=15, edgecolor="black", linewidth=0.5)

ctx.add_basemap(ax, source=ctx.providers.CartoDB.DarkMatter)
ax.set_axis_off()
ax.set_title("Major Cities in the Path of Totality", fontsize=16)

plt.show()
```

:::{figure} images/11_basemap_exercise_2.png
:alt: A dark-themed map displaying the eclipse shadow. Cities that fall inside the shadow are highlighted as bright yellow points.
:width: 700px
:align: center

*Exercise 5.2 Result: A spatial join perfectly integrates our point data with our polygons, revealing that tens of millions of city-dwellers lie in the path of the 2081 eclipse.*
:::
````

---

## 6. Summary: Web Tiles in Static Plots

Adding a basemap is one of the most effective ways to instantly elevate the quality and readability of your spatial visualizations. 

In this chapter, you learned how to use the **contextily** library to fetch standard web map tiles directly from the internet and render them behind your Matplotlib plots. This process relies on a very strict workflow:

* **Reproject:** You must always reproject your GeoDataFrames to the Web Mercator projection (`EPSG:3857`) before plotting. Failing to do so triggers the coordinate clash, resulting in severe misalignment.
* **Customize:** Do not just settle for the default! Explore `ctx.providers` to select a basemap style (like `OpenTopoMap`, `CartoDB.Positron`, or `Esri.WorldImagery`) that perfectly complements your data.
* **Fetch and Frame:** Use `ctx.add_basemap(ax)` to automatically download the correct background tiles. Use `ax.set_xlim()` and `ax.set_ylim()` to focus the reader's attention on specific geographic extents, and manage resolution with the `zoom` parameter.
* **Polish:** Always call `ax.set_axis_off()` to hide the meaningless mathematical coordinate ticks, and use the `attribution` parameter to properly credit your data sources. 

---

### What comes next: Going Interactive

A beautifully designed static map is powerful, but an interactive one is even better. In the next chapter, we will transition to modern web maps that users can pan, zoom, and click. You will learn how to:

* **Bridge Python and JavaScript:** Use **Folium** to tap into the Leaflet web mapping engine.
* **Unlock `.explore()`:** Generate interactive GeoPandas choropleths with a single line of code.
* **Add Popups and Tooltips:** Reveal underlying data when a user hovers over or clicks on spatial features.
* **Manage Visual Clutter:** Use `MarkerCluster` to intelligently group thousands of data points for clean, readable dashboards.
