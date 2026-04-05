---

title: Going Interactive

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Web Maps with Folium and GeoPandas
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/10_L08_visualization/05_interactive_maps.ipynb)

---

```{admonition} Big idea
:class: tip

A beautifully designed static map is a powerful communication tool for reports and publications. However, a map that your audience can actively explore is even better. In this chapter, we transition from Matplotlib's static coordinates to modern, interactive web maps. You will learn how to create maps that users can pan, zoom, and click to reveal underlying data.
```

**Preparing the Data**

To follow along with this chapter, we are heading to Zurich, Switzerland. Please download the following datasets and place them in your `data` folder. They contain geographic information about the city's bicycle infrastructure and administrative boundaries.

```{admonition} Data Downloads
:class: note

* [Zurich Quarters (Zurich_quarters.gpkg)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/Zurich_quarters.gpkg)
* [PubliBike Stations (Zurich_PubliBike_stations.gpkg)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/Zurich_PubliBike_stations.gpkg)
* [Bike Parking (Zurich_bike_parking.gpkg)](https://gitlab.com/HendrikWulf/sds210/-/blob/main/L08/data/Zurich_bike_parking.gpkg)
```

---

## 1. Introduction to Folium

Interactive maps allow users to engage with spatial content directly. Instead of trying to cram every single data attribute onto a static legend, interactive maps let you hide complex information behind clickable markers and hover effects.

The gold standard for interactive web mapping is a JavaScript library called **[Leaflet.js](https://leafletjs.com/)**. However, learning JavaScript just to make a map can be a daunting detour for a data scientist.

This is where **[Folium](https://python-visualization.github.io/folium/latest/)** comes in. Folium is a fantastic Python library that acts as a bridge to Leaflet. It allows you to write standard Python code, which Folium then seamlessly translates into the HTML and JavaScript required to render a fully interactive Leaflet map in your browser or Jupyter Notebook.

Because the output is standard HTML, you can easily save these maps as standalone files to share with colleagues or embed in websites. Even better, modern versions of GeoPandas have built-in support for Folium, allowing you to generate these interactive web maps directly from your GeoDataFrames!

---

## 2. Initializing a Web Map

Creating an interactive canvas with Folium is incredibly straightforward. You initialize a map object using the `folium.Map()` class.

```{code-cell} python
# Import the folium library
import folium

# Create a new Folium map object. By default, it's centered globally.
m = folium.Map()
# Display the map object. This will render the map.
m
```

You can customise it by providing a starting `location` (passed as a list containing `[latitude, longitude]`) and an initial zoom level via the `zoom_start` parameter. Higher numbers zoom in closer to the street level, while lower numbers zoom out toward a global view. You can also define a basemap using `tiles` to change the `OpenStreetMap` default.

```{code-cell} python
# Install folium if you haven't already:
# !pip install folium

import folium

# Initialize the map centered on Zurich
# Coordinates are [Latitude, Longitude]
zurich_map = folium.Map(
    location=[47.3769, 8.5417], 
    zoom_start=13,
    tiles="CartoDB Positron" # A clean, light basemap
)

# Display the map in the notebook
zurich_map
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_01_zurich_map/"
    width="100%"
    title="An interactive web map centered on Zurich using a light grey basemap."
    frameborder="0"
    style="border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
    allowfullscreen>
</iframe>

*A fully interactive canvas. You can click and drag to pan around, and use your scroll wheel to zoom in and out of the city. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_01_zurich_map/).* 

### Changing the Basemap

The background style of your map is controlled via the `tiles` argument. Folium includes several built-in background map tiles (such as `"OpenStreetMap"`, `"CartoDB Positron"`, or `"CartoDB DarkMatter"`). When using these built-in options, Folium automatically adds the required attribution to the bottom right corner of the map.

There is a vast ecosystem of tile providers available online. You can explore the various styles using the interactive Leaflet Providers Preview below:

<iframe
src="https://leaflet-extras.github.io/leaflet-providers/preview/"
width="100%"
title="Leaflet Providers Preview"
frameborder="0"
style="border: none; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 10px;"
allowfullscreen>
</iframe>

*Explore different map styles by selecting providers on the right. For improved visibility of the explorer, follow this [link](https://leaflet-extras.github.io/leaflet-providers/preview/).* 

If you find a style you like that is not built into Folium, you can use it by passing a custom URL directly to the `tiles` argument. **Important:** When using a custom URL, Folium cannot automatically guess the attribution. You must explicitly provide the copyright and map credits using the `attr` parameter.

Because we will be overlaying a lot of dense bicycle infrastructure data in this chapter, standard basemaps with heavy text labels can make the final visualization look cluttered and confusing. To maximize mapping clarity, let us create a clean, minimalist map using a specialized basemap called **CartoDB Positron (No Labels)**:

```{code-cell} python
# Define the custom URL and attribution for CartoDB Positron (No Labels)
# Note: We omit the optional {r} (retina) tag for standard Folium compatibility
custom_tile_url = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

custom_attribution = (
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap - yeah</a> contributors '
    '&copy; <a href="https://carto.com/attributions">CARTOoooo</a>'
)

# Initialize the map with the custom tiles
clean_map = folium.Map(
    location=[47.3769, 8.5417],
    zoom_start=13,
    tiles=custom_tile_url,
    attr=custom_attribution
)

clean_map
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_02_clean_map/"
    width="100%"
    title="An interactive web map centered on Zurich using a light grey basemap and custom attribution."
    allowfullscreen>
</iframe>

*Example of a clean map with custom attribution. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_02_clean_map/).*

---

## 3. Building a Map Layer by Layer

Now that we have a blank interactive canvas, it is time to add our spatial data. Building a production-ready web map often requires fine-grained control over individual elements like markers, popups, and styling. To achieve this, we will construct our Folium map layer by layer from scratch.

In this walkthrough, we will take the dataset of bicycle parking spots in Zurich (`Zurich_bike_parking.gpkg`) and incrementally transform it from a basic plot into an interactive, data-driven web-map.

**A Quick Note on Projections:**  Web map tiles are served in Web Mercator (`EPSG:3857`), but libraries like Folium expect input coordinates in geographic latitude and longitude (`EPSG:4326`). If your data is stored in a projected coordinate system (e.g., `EPSG:2056` or `EPSG:3857`), you must convert it to `EPSG:4326` before passing it to Folium. Internally, Leaflet will then reproject these coordinates to align with the Web Mercator tile grid.


### Step 1: Adding a Basic Layer
The simplest way to add a GeoDataFrame to a Folium map is by passing it to the `folium.GeoJson()` class. 

```{code-cell} python
import folium
import geopandas as gpd

# 1. Load the bicycle parking data and reproject to standard Lat/Lon (EPSG:4326)
bike_parking = gpd.read_file('data/Zurich_bike_parking.gpkg').to_crs(epsg=4326)

# 2. Initialize the basemap centered on Zurich
m1 = folium.Map(
    location=[47.3769, 8.5417], 
    zoom_start=13, 
    tiles='CartoDB Positron'
)

# 3. Add the raw GeoDataFrame to the map as a GeoJSON layer
folium.GeoJson(bike_parking).add_to(m1)                         # <- THIS IS NEW

# 4. Display the map
m1
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m1/"
    width="100%"
    title="A basic Folium map showing default blue markers for every bike parking location in Zurich."
    allowfullscreen>
</iframe>

*Output Step 1: The raw data is added to the map. By default, Folium renders point geometries as standard blue clickable markers. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m1/).*

### Step 2: Giving the User Control
If you plan to add multiple datasets (like bike lanes and pumping stations) to a single map, the user needs a way to toggle them on and off. We can achieve this by giving our layer a explicit `name` and appending a `LayerControl` object to the map.

```{code-cell} python
# Initialize the basemap centered on Zurich
m2 = folium.Map(location=[47.3769, 8.5417], zoom_start=13, tiles='CartoDB Positron')

# Add the layer and assign it a clean, readable name for the menu
folium.GeoJson(
    bike_parking,
    name='Bike Parking'                                         # <- THIS IS NEW
).add_to(m2)

# Add the interactive layer control menu to the top right corner
folium.LayerControl().add_to(m2)                                # <- THIS IS NEW

m2
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m2/"
    width="100%"
    title="The same map as before, but now with a layer control box in the top right corner allowing the user to toggle 'Bike Parking' on and off."
    allowfullscreen>
</iframe>

*Output Step 2: The LayerControl widget appears in the top right, allowing users to interactively filter which datasets are currently visible. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m2/).*

### Step 3: Adding Tooltips
Right now, our markers are blind. To make the map informative, we need to reveal the underlying data. Our dataset contains a column named `anzahl_pp`, which represents the number of parking spaces at each location. We can attach a `GeoJsonTooltip` to display this information on hover.

```{code-cell} python
# Initialize the basemap centered on Zurich
m3 = folium.Map(location=[47.3769, 8.5417], zoom_start=13, tiles='CartoDB Positron')

# Add the layer with a configured tooltip
folium.GeoJson(
    bike_parking,
    name='Bike Parking',
    # Link the tooltip to the 'anzahl_pp' column and give it a readable English alias
    tooltip=folium.GeoJsonTooltip(                              # <- THIS IS NEW
        fields=['anzahl_pp'], 
        aliases=['Spaces:']
    )
).add_to(m3)

# Add the interactive layer control menu
folium.LayerControl().add_to(m3)

m3
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m3/"
    width="100%"
    title="The map now shows a small white tooltip box reading 'Spaces: 12' hovering next to the mouse cursor over a marker."
    allowfullscreen>
</iframe>

*Output Step 3: Hovering over any marker now instantly queries the GeoDataFrame and displays the exact number of parking spaces available. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m3/).*

### Step 4: Custom Icons
Standard blue teardrop markers are generic. We can customize the aesthetics by passing a `folium.Marker` object equipped with a specific icon. Folium supports the [FontAwesome](https://fontawesome.com/v4/icons/) (`fa`) icon library, giving us access to hundreds of intuitive symbols.

```{code-cell} python
# Initialize the basemap centered on Zurich
m4 = folium.Map(location=[47.3769, 8.5417], zoom_start=13, tiles='CartoDB Positron')

# Add the layer with a custom marker parameter
folium.GeoJson(
    bike_parking,
    name='Bike Parking',
    tooltip=folium.GeoJsonTooltip(fields=['anzahl_pp'], aliases=['Spaces:']),
    # Override the default teardrop with a blue bicycle icon
    marker=folium.Marker(                                       # <- THIS IS NEW
        icon=folium.Icon(color='blue', icon='bicycle', prefix='fa')
    )
).add_to(m4)

# Add the interactive layer control menu
folium.LayerControl().add_to(m4)
m4
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m4/"
    width="100%"
    title="The generic markers have been replaced by blue markers containing a white bicycle icon."
    allowfullscreen>
</iframe>

*Output Step 4: Thematic icons drastically improve the immediate readability of the map, instantly communicating that these points relate to bicycles. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m4/).*

### Step 5: Managing Clutter with Marker Clusters
We have a problem: Zurich has thousands of bike parking locations. Drawing them all at once creates a messy, overlapping visualization that is difficult to read and slow to load in the browser. 

We can solve this using the `MarkerCluster` plugin. 

*A critical warning:* When you wrap a `folium.GeoJson` object directly inside a `MarkerCluster`, the complex clustering logic often intercepts "mouse over" events, causing your carefully crafted tooltips to break. The most reliable, production-ready way to cluster interactive data is to iterate through your GeoDataFrame row by row, creating individual markers and assigning them directly to the cluster.

```{code-cell} python
from folium.plugins import MarkerCluster

# Initialize the basemap centered on Zurich
m5 = folium.Map(location=[47.3769, 8.5417], zoom_start=13, tiles='CartoDB Positron')

# Create an empty MarkerCluster group and add it to the map
marker_cluster = MarkerCluster(name='Bike Parking Clusters').add_to(m5) # <- THIS IS NEW

# Iterate manually through the GeoDataFrame to ensure tooltips survive clustering
for idx, row in bike_parking.iterrows():                          # <- THIS IS DIFFERENT
    # Extract coordinates
    lat = row.geometry.y
    lon = row.geometry.x
    
    # Format the tooltip text explicitly
    tooltip_text = f"Spaces: {int(row['anzahl_pp'])}"
    
    # Create the individual marker and add it to the cluster (NOT directly to the map)
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color='blue', icon='bicycle', prefix='fa'),
        tooltip=tooltip_text
    ).add_to(marker_cluster)

# Add the interactive layer control menu
folium.LayerControl().add_to(m5)

m5
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m5/"
    width="100%"
    title="The map now shows clustered circles with numbers indicating how many parking spots are in a given area. Clicking them expands into the bicycle icons."
    allowfullscreen>
</iframe>

*Output Step 5: By iterating through the data, we create a clean, performant clustered map where the interactive tooltips remain fully functional upon zooming in. The map now shows clustered circles with numbers indicating how many parking spots are in a given area. Clicking them expands into the bicycle icons. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m5/).*

### Step 6: Scaling Symbols (advanced)
Our map is looking highly professional, but we can push it one step further. Right now, a parking rack with 2 spaces looks identical to a massive parking garage with 500 spaces. 

Instead of using a generic icon, we can dynamically scale the size of our custom icon based on the actual `anzahl_pp` data value. To do this, we use `folium.DivIcon` to inject raw HTML and CSS styling directly into the map marker, calculating the size on the fly using a square-root mathematical scaling (which correctly scales the visual *area* of the circle).

```{code-cell} python
import numpy as np

# Initialize the basemap centered on Zurich
m6 = folium.Map(location=[47.3769, 8.5417], zoom_start=13, tiles='CartoDB Positron')
marker_cluster = MarkerCluster(name='Scaled Bike Parking Clusters').add_to(m6)

for idx, row in bike_parking.iterrows():
    lat = row.geometry.y
    lon = row.geometry.x
    count = int(row['anzahl_pp'])
    tooltip_text = f"Spaces: {count}"

    # Mathematical Scaling Logic: 
    # Base size of 14px, plus an increase based on the square root of the parking count
    icon_size = 14 + (np.sqrt(count) * 3)                      # <- THIS IS NEW

    # Injecting custom CSS to draw a perfect circle with our dynamic size (NEW)
    icon_html = f'''
        <div style="
            font-size: {icon_size}px;
            color: #1f77b4;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 50%;
            width: {icon_size}px;
            height: {icon_size}px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #1f77b4;">
            <i class="fa fa-bicycle"></i>
        </div>'''

    # Apply the custom HTML using DivIcon
    folium.Marker(
        location=[lat, lon],
        icon=folium.DivIcon(                                    # <- THIS IS NEW
            html=icon_html,
            icon_size=(icon_size, icon_size),
            icon_anchor=(icon_size/2, icon_size/2) # Centers the icon perfectly
        ),
        tooltip=tooltip_text
    ).add_to(marker_cluster)

# Add the interactive layer control menu
folium.LayerControl().add_to(m6)

m6
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m6/"
    width="100%"
    title="The map shows clustered data, but when expanded, individual bicycle icons vary wildly in size, clearly indicating major parking hubs versus small racks."
    allowfullscreen>
</iframe>

*Output Step 6: Data-driven visual scaling. By injecting custom HTML/CSS and scaling by the square root of the capacity, the map now instantly communicates both the location and the magnitude of the bicycle infrastructure. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_03_m6/).*

---

## 4. Interactive Thematic Maps

In previous chapters, you learned how to create static choropleth maps using GeoPandas and Matplotlib. Now, we will bring those thematic maps to life using Folium. 

Folium provides a dedicated `Choropleth` class that binds your tabular data (like Pandas DataFrames or Series) to your spatial geometries. Just like the `GeoJson` class, you can pass a GeoDataFrame directly to it to generate a thematic map.

### Step 1: The Basic Choropleth

Let us start by creating a simple choropleth map that visualizes the geographic area of each administrative quarter in Zurich.

The most critical parameter to understand here is `key_on`. Folium needs to know exactly how to match the rows in your data table to the polygons in your spatial geometry. By default, GeoPandas stores your column data inside a nested JSON structure under `feature.properties`. If your matching column is named `name`, you must tell Folium to look for `feature.properties.name`.

```{code-cell} python
import folium
import geopandas as gpd

# 1. Prepare the data
quarters = gpd.read_file("data/Zurich_quarters.gpkg")

# Calculate the area in square kilometers
quarters['area'] = (quarters.geometry.area / 1000000).round(3)

# 2. Initialize the Folium Map
m = folium.Map(location=[47.3769, 8.5417], zoom_start=12, tiles="CartoDB Positron No Labels")

# 3. Add the Choropleth layer
folium.Choropleth(
    geo_data=quarters,             # The spatial geometries
    name="Quarter Area",           # Name for the LayerControl
    data=quarters,                 # The tabular data source containing the values
    columns=["name", "area"],      # [The Key column to match, The Value column to color by]
    key_on="feature.properties.name", # The exact path to the key inside the GeoJSON structure
    fill_color="viridis",          # The color palette
    fill_opacity=0.6,              # Transparency of the polygons
    line_opacity=0.2,              # Transparency of the borders
    legend_name="Area in km2"      # Title for the automatically generated legend
).add_to(m)

# 4. Add layer control to toggle the map on and off
folium.LayerControl().add_to(m)

m
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_04_map1/"
    width="100%"
    title="A map of Zurich divided into quarters, colored from dark purple to bright yellow based on their geographic area, with a legend in the top right."
    allowfullscreen>
</iframe>

*Output Step 1: A basic interactive choropleth. Folium automatically generates and places a color scale legend in the top right corner. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_04_map1/).*

### Step 2: Spatial Joins and Density

Visualizing raw area is a good start, but spatial data science is about uncovering hidden patterns. A much more interesting question is: **Which Zurich quarter has the highest density of bicycle parking?**

To answer this, we must first perform a spatial join to count how many parking spots fall within each quarter, and then divide that count by the quarter's area. 

Because area calculations and spatial joins require location accuracy, we should perform these mathematical operations in the accurate Swiss projected coordinate system (`EPSG:2056`). Once the math is done, we will project the final results back to standard latitude and longitude (`EPSG:4326`) so Folium can render it on the web map.

```{code-cell} python
# 1. Prepare the data and ensure correct projected CRS for Swiss spatial math
bike_parking = gpd.read_file("data/Zurich_bike_parking.gpkg")

if quarters.crs is None:
    quarters.set_crs(epsg=2056, inplace=True)
if bike_parking.crs is None:
    bike_parking.set_crs(epsg=2056, inplace=True)

quarters['area_km²'] = (quarters.geometry.area / 1000000).round(3)

# 2. Spatial Join: Count parking locations within each quarter
joined = gpd.sjoin(bike_parking, quarters, how="inner", predicate="within")

# Handle potential naming conflicts from the join
name_col = 'name_right' if 'name_right' in joined.columns else 'name'

# Group by the quarter name and count the occurrences
counts = joined.groupby(name_col).size().reset_index(name='anzahl_pp')
counts.rename(columns={name_col: 'name'}, inplace=True)

# Merge the counts back into the main quarters GeoDataFrame
quarters = quarters.merge(counts, on='name', how='left').fillna({'anzahl_pp': 0})

# Calculate the density (parking locations per square kilometer)
quarters['parking_density'] = (quarters['anzahl_pp'] / quarters['area_km2']).round(2)

# 3. Reproject back to Web standard for Folium
quarters_4326 = quarters.to_crs(epsg=4326)
```

### Step 3: Multi-Layer Choropleths with Tooltips

Now we will map our new density data. We will actually add *two* choropleth layers to our map: one for Area, and one for Density. 

To prevent the map from looking messy when it first loads, we can disable the Area layer from showing on the initial load by passing the `show=False` parameter directly to the Choropleth object. Users can still turn it on via the LayerControl menu.

Finally, we encounter a quirk of Folium. The `folium.Choropleth` class does not natively support hover tooltips as easily as standard point markers do. To solve this, we use a cartographic hack: we add a completely invisible `GeoJson` layer directly on top of our map. This invisible layer handles all the mouse hover interactions, triggering our helpful tooltips!

```{code-cell} python
# Initialize the map
m2 = folium.Map(location=[47.3769, 8.5417], zoom_start=12, tiles="CartoDB Positron No Labels")

# 1. Area Choropleth (Hidden by default using show=False)
folium.Choropleth(
    geo_data=quarters_4326,
    name="Quarter Area (km2)",
    data=quarters_4326,
    columns=["name", "area_km2"],
    key_on="feature.properties.name",
    fill_color="YlGn",
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name="Area in km2",
    show=False # Keeps the map clean on initial load
).add_to(m2)

# 2. Density Choropleth (Visible by default)
folium.Choropleth(
    geo_data=quarters_4326,
    name="Parking Density (locations/km2)",
    data=quarters_4326,
    columns=["name", "parking_density"],
    key_on="feature.properties.name",
    fill_color="viridis",
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name="Bike Parking Locations per km2",
).add_to(m2)

# 3. Add Interactive Tooltips via an Invisible GeoJson Layer
folium.GeoJson(
    quarters_4326,
    name="Interactive Tooltips",
    # Make the polygons completely transparent so they do not hide the choropleth colors
    style_function=lambda x: {'fillColor': '#ffffff00', 'color': '#ffffff00'},
    tooltip=folium.GeoJsonTooltip(
        fields=['name', 'parking_density'],
        aliases=['Quarter:', 'Density:'],
        localize=True
    )
).add_to(m2)

# Add Layer Control and display
folium.LayerControl().add_to(m2)

m2
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_04_map2/"
    width="100%"
    title="A multi-layer interactive map of Zurich. The visible choropleth shows parking density, with a tooltip revealing the exact density value when hovering over a specific quarter. The layer control menu shows three toggleable layers."
    allowfullscreen>
</iframe>

*Output Step 3: A multi-layered thematic map. The invisible GeoJson layer captures mouse movements to display tooltip data, while `show=False` ensures the initial view is not cluttered with overlapping colors. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_04_map2/).*

---

## 5. The Magic of `.explore()`

In the previous section, we built a multi-layered choropleth map from scratch. While building maps layer by layer provides more control over every single element, you probably noticed that it requires a substantial amount of code. Creating an invisible GeoJSON layer just to get tooltips working can feel like a tedious workaround.

For rapid spatial data exploration, we need a faster way to visualize data interactively. 

Enter the magic of `.explore()`. Just as GeoPandas uses `.plot()` to instantly generate static Matplotlib figures, it provides the `.explore()` method to instantly generate fully interactive Folium web maps. GeoPandas handles all the complex JavaScript translation, GeoJSON conversion, and tooltip linking behind the scenes.

Let us recreate our parking density map using the `quarters_4326` GeoDataFrame we prepared in the previous section, but this time, we will use `.explore()`.

```{code-cell} python
# Assuming quarters_4326 is still in memory from our previous spatial join

# Generate an interactive choropleth in a single command
interactive_map = quarters_4326.explore(
    column="parking_density",   # The column dictating the color
    cmap="viridis",             # The colormap
    alpha=0.6,                  # Transparency of the polygons
    tiles="CartoDB Positron No Labels", # A clean basemap
    legend_kwds={'caption': 'Parking locations / km²'} # Set legend title
)

# Display the map
interactive_map
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_05_explore/"
    width="100%"
    title="An interactive choropleth map of Zurich showing parking density. A large tooltip box is visible, automatically listing every single data column for the hovered quarter."
    allowfullscreen>
</iframe>

*An interactive thematic map generated in one line of code. Notice that by default, the tooltip automatically displays every single attribute column available in the GeoDataFrame. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_05_explore/).*

### `.explore()`, Pure Folium, and the Hybrid Approach

If `.explore()` is so much faster, why would we ever write pure Folium code? The answer comes down to the classic programming tradeoff: **Convenience vs. Control**. 

However, as you will see, these two tools are not mutually exclusive. Here is a quick guide on how to approach interactive mapping depending on your needs:

**1. Standalone GeoPandas `.explore()`:**
* **Exploratory Data Analysis (EDA):** Best when you are actively analyzing data and need to quickly check if a spatial join worked, spot outliers, or view the distribution of a single dataset.
* **Speed:** When you need a functional, interactive map with an automatic legend and comprehensive tooltips in exactly one line of code.

**2. Pure Folium (`folium.Map`, `folium.GeoJson`, `folium.Choropleth`):**
* **Pixel-Perfect Control:** When you are building a final product for a client and need absolute control over the aesthetics, missing values (`NaN`), and legend placement.
* **Custom Interactivity:** When you need to utilize advanced Leaflet plugins (like our dynamically scaled `MarkerCluster` icons), inject custom CSS/HTML into popups, or use specialized clustering logic that `.explore()` cannot natively handle.

**3. The Hybrid Approach (The Best of Both Worlds):**
You do not have to choose just one! You can actually combine the speed of `.explore()` with the structural control of Folium. By initializing a blank `folium.Map()` first, you can pass it to the `m` parameter inside `.explore()`. 

This is the perfect approach for building **Multi-Layer Dashboards**. It allows you to rapidly add multiple GeoDataFrames to the exact same canvas and easily append a `LayerControl` menu:

```{code-cell} python
import folium

# 1. Initialize the Folium map (The Control)
my_map = folium.Map(location=[47.37, 8.54], zoom_start=12)

# 2. Add multiple datasets using GeoPandas (The Convenience)
bike_lanes.explore(m=my_map, color="blue", name="Bike Lanes")
parks.explore(m=my_map, color="green", name="Parks")

# 3. Add Folium plugins back on top
folium.LayerControl().add_to(my_map)

my_map
```

---

## 6. Exercise: The EV Charging Web Map

It is time to bring all these interactive concepts together. For this exercise, you will step out of Zurich and map infrastructure for the entire country. As a spatial data scientist, you have been tasked with visualizing Switzerland's electric vehicle (EV) charging network. 

Because charging stations are numerous, you must use clustering to prevent visual clutter. Furthermore, to make the map visually striking, you will use a dark-themed basemap and specialized icons.

**Your Tasks:**

1.  Load the `EV_charging_stations.gpkg` dataset. Remember to project it to the standard web coordinate system (`EPSG:4326`) before passing it to Folium.
2.  Initialize a Folium map centered on Switzerland (roughly `[46.8, 8.2]`) with a `zoom_start` of 8. To make the markers stand out, use the `"CartoDB DarkMatter"` tileset.
3.  Initialize a `MarkerCluster` object, give it a logical name, and add it to your map.
4.  Iterate over the rows in your GeoDataFrame. For each row:
    * Extract the latitude (`geometry.y`) and longitude (`geometry.x`).
    * Create a `folium.Marker`.
    * Set the `tooltip` to show a string containing the station's power output (e.g., `"Power: 50 kW"` using the `"power"` column).
    * Customize the marker using `folium.Icon`. Set the color to `"green"` and use an appropriate FontAwesome icon (e.g., `icon="bolt"` or `icon="plug"`, with `prefix="fa"`).
    * Add this marker directly to your `MarkerCluster`.
5.  Add a `LayerControl` to the map and display your final interactive map.

```{code-cell} python
# Write your code here

```

````{admonition} Sample Solution
:class: dropdown

```{code-cell} python
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster

# 1. Load and reproject the data to Lat/Lon (EPSG:4326)
ev_stations = gpd.read_file("data/EV_charging_stations.gpkg").to_crs(epsg=4326)

# 2. Initialize the map centered on Switzerland
map = folium.Map(
    location=[46.8, 8.2], 
    zoom_start=8, 
    tiles="CartoDB DarkMatter" # Dark basemap for contrast
)

# 3. Create the cluster and add it to the map
cluster = MarkerCluster(name="EV Charging Stations").add_to(map)

# 4. Iterate through the data and build the markers
for idx, row in ev_stations.iterrows():
    lat = row.geometry.y
    lon = row.geometry.x
    
    # Format the tooltip
    power_output = f"Power: {row['power']} kW"
    
    # Create marker with a green lightning bolt icon and add to cluster
    folium.Marker(
        location=[lat, lon],
        tooltip=power_output,
        icon=folium.Icon(color="green", icon="bolt", prefix="fa") 
    ).add_to(cluster)

# 5. Add Layer Control and display the map
folium.LayerControl().add_to(map)
map
```

<iframe 
    src="https://hendrikwulf.github.io/sds210_assets_L08_ch05_06_exercise/"
    width="100%"
    title="A dark-themed interactive map of Switzerland showing clustered circles. When expanded, individual green markers with lightning bolt icons appear, showing tooltips like 'Power: 50 kW'."
    allowfullscreen>
</iframe>

*A stylized, interactive web map. The dark basemap provides contrast for the bright green lightning bolt markers, and clustering ensures smooth performance across the entire country. For improved visibility of the map, follow this [link](https://hendrikwulf.github.io/sds210_assets_L08_ch05_06_exercise/).*

````

---

## 7. Summary: Web Mapping

In this chapter, you bridged the gap between static data science outputs and modern web development. You transitioned from plotting unmoving pixels in Matplotlib to generating dynamic, interactive HTML canvases that users can explore.

* **Folium:** You learned that Folium acts as a Python wrapper for the powerful Leaflet.js library, allowing you to build web maps layer by layer without writing a single line of JavaScript.
* **Thematic Maps:** You built complex, multi-layered choropleths that combine spatial geometries with tabular data, using clever cartographic techniques (like invisible layers) to trigger detailed tooltips.
* **The Magic of `.explore()`:** You used GeoPandas to instantly render interactive choropleths and point maps with a single command, ideal for rapid exploratory data analysis.
* **UX Design (Tooltips and Icons):** You improved the user experience by replacing generic teardrops with data-driven thematic icons, and by hiding complex attribute data behind interactive hovers and clicks to keep the visual layout clean.
* **Managing Scale:** You utilized the `MarkerCluster` plugin to intelligently group thousands of geometries together. This ensures your maps remain performant, legible, and visually appealing, regardless of how far the user zooms out.
