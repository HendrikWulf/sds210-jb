---
title: L7 - Vector Data

site: 
    outline_maxdepth: 1

---

<div class="page-subtitle">
Mastering geographic shapes and spatial analysis
</div>

---

In the previous lesson, you learned how to wield **Pandas** to sanitize, filter, and mathematically manipulate large tabular datasets and time series.

That was an essential step for taming real-world information, but it raises an obvious next question:

> What happens when your data isn't just numbers and text, but represents physical locations on the surface of the Earth?

So far, your data has been blind to space. You could calculate the average temperature of a weather station, but you could not calculate how far it is from a lake, or whether it sits inside a specific canton.

This lesson introduces a massive expansion of your analytical capabilities. Instead of just analyzing *what* happened, you will learn how to analyze *where* it happened using **GeoPandas**.

---

## 1. From tables to geometries

Programming data analysis can be fundamentally broken down into different mindsets. Up until now, your mental model of data has been a flat spreadsheet.

GeoPandas extends this model by fusing the data manipulation power of Pandas with a powerful geometric engine called Shapely. By adding a special `geometry` column to your DataFrames, your rows suddenly represent mathematical shapes: Points (locations), LineStrings (paths), and Polygons (areas).

Your data becomes geographically aware. A table is no longer just a passive container of text and numbers; it becomes a dynamic spatial object that can measure its own distances, check for intersections, and project 3D coordinates onto a flat 2D map.

---

## 2. Why this matters for {abbr}`SDS (Spatial Data Science)`

In spatial data science, location is the ultimate connecting variable.

Often, you will have datasets that share no common IDs or text columns. How do you link a table of patient locations to a table of hospital zones? You use geography.

Mastering vector data allows you to answer inherently spatial questions: How many people live within a 50-kilometer radius of a nuclear power plant? Which roads intersect this newly flooded area? Which weather stations fall strictly within the borders of Zurich?

GeoPandas provides the tools to read industry-standard GIS files, perform these topological queries instantly, and classify the results into presentation-ready thematic maps. It is the bridge between raw coordinates and actionable geographic insights.

---

## 3. Learning objectives

After this lesson, you will be able to:

  * **Manage spatial data structures**
    Transition from standard Pandas to GeoPandas, loading professional GIS files and manipulating Points, Lines, and Polygons.
  * **Navigate Coordinate Reference Systems (CRS)**
    Safely flatten the 3D Earth onto a 2D metric grid to ensure your area and distance calculations are mathematically accurate.
  * **Generate spatial metrics and shapes**
    Engineer new geometries like proximity buffers and centroids, and calculate intrinsic properties like border length and surface area.
  * **Perform topological queries and spatial joins**
    Filter data based on physical relationships (like `within` or `intersects`) and fuse distinct datasets together using geography as the key.
  * **Classify and map data**
    Bridge the gap between raw spatial analysis and human readability by normalizing counts and applying statistical classification schemes to create choropleth maps.

---

## 4. Lesson structure

This lesson is structured to take you from basic spatial shapes to complete geographic assessments:

1.  **The Spatial Mental Model**: Adding the "Geo" to your data structures.
2.  **Reading, Writing & Peeking**: Loading, visualizing, and saving professional geographic files.
3.  **Coordinate Reference Systems (CRS)**: The "Where" of spatial data and safely flattening the Earth.
4.  **Measuring & Modifying**: Generating new geospatial metrics and shapes.
5.  **Spatial Relationships**: Asking spatial questions to filter data based on topology.
6.  **Vector Analysis**: Combining and aggregating datasets using spatial joins and overlays.
7.  **Data Classification**: Categorizing continuous data to create readable thematic maps.
8.  **Practical L7**: Applying these skills to assess the climate crisis across Swiss cantons using live weather APIs.

---

## 5. Looking ahead

Lesson 7 is about **thinking in space**.

You will learn not only *how to map data*, but how to:

  * seamlessly blend tabular data processing with geometric mathematics
  * solve complex proximity and intersection problems
  * design statistically sound, visually clear geographic visualizations

If Lesson 6 was about *taming data*, Lesson 7 is about **grounding it in the real world**.

The vector operations you master here form the foundation of modern Geographic Information Systems (GIS). Eventually, we will explore the other half of the spatial coin: **Raster Data**, which will allow you to process continuous surfaces like satellite imagery and digital elevation models. But before we tackle that, our immediate next step is a dedicated lesson on **Data Visualization**. After all, the most sophisticated spatial analysis in the world isn't much fun until you can translate those numbers into compelling maps that people can easily understand.