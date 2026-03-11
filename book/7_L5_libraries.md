---

title: L5 - Libraries & Web APIs

site:
    outline_maxdepth: 1

---

<div class="page-subtitle">
Connecting Python to the wider world
</div>

---

In the previous lesson, you learned how to package your code into reusable **functions**.

That was an essential step for building your own tools, but it raises an important realization:

> Do you really have to write every complex spatial algorithm yourself? And what happens when the data you need isn't saved on your hard drive?

So far, you have been working in a closed environment, writing custom logic for local data. This lesson introduces a massive expansion of your toolkit. Instead of reinventing the wheel, you will learn how to tap into the global Python community and connect your code directly to the live internet.

---

## 1. From local logic to global ecosystems

Programming in the real world is rarely done in isolation.

The transition from a beginner to an advanced programmer involves realizing that most common problems have already been solved by someone else. Python is famous for its "batteries included" philosophy and its massive open-source community.

Furthermore, modern spatial data is dynamic. Weather changes, traffic updates, and satellite imagery is continuously captured. To analyze this data, your code needs to break out of your local computer and securely ask remote servers for the exact information it needs.

---

## 2. Why this matters for {abbr}`SDS (Spatial Data Science)`

Spatial Data Science is inherently connected to the real world, which makes it computationally complex and highly dependent on fresh data.

Writing your own mathematical formula to calculate the distance between two coordinates on an oblate spheroid is error-prone. Instead, you can import a community-tested library that does it flawlessly in one line. Need to analyze traffic accidents? You cannot map "Main Street, Athens", you need a tool to automatically translate that text into exact geometric coordinates.

By learning how to import libraries and query web servers, you transform Python from a simple calculator into a powerful, automated data-gathering engine.

---

## 3. Learning objectives

After this lesson, you will be able to:

* **Organize code externally**
Move complex functions out of notebooks and into dedicated Python script files to build your own importable modules.
* **Leverage community tools**
Import built-in modules from the Standard Library and safely install third-party packages to perform complex mathematical and spatial operations.
* **Communicate with the web**
Query external servers using Web APIs, parse the resulting JSON data, and automate live data retrieval while respecting rate limits.

---

## 4. Lesson structure

This lesson is structured to incrementally expand your code's reach:

1. **Writing script files**: Moving your custom functions out of the Jupyter Notebook sandbox into clean, reusable `.py` files.
2. **The Python Standard Library**: Unlocking the powerful, pre-installed tools bundled directly with Python (like `math` and `json`).
3. **Third Party Modules**: Using package managers to install specialized, community-built tools (like `geopy` and `tqdm`) to abstract away complex tasks.
4. **Using Web APIs**: Fetching live data (like weather and routing) and historical datasets directly from web servers using the `requests` module.
5. **Geocoding**: Applying Web APIs practically to translate human addresses into geographic geometry.

---

## 5. Looking ahead

Lesson 5 is about **breaking out of the sandbox**.

You will learn not only *how to download tools*, but how to:

* navigate the modern open-source Python ecosystem securely
* read and extract data from deeply nested web responses
* build automated pipelines that talk to the rest of the world

If Lesson 4 was about *thinking in structure and reuse*, Lesson 5 is about **thinking globally**.

The skills you learn here—importing packages and fetching data—are the absolute prerequisites for the next major phase of the course. In the upcoming lesson 7, we will introduce Pandas and GeoPandas, the ultimate third-party libraries that will change how you handle spatial data in bulk. However, before that you need to know how to manage it locally. In the next lesson, we will cover how to read and write files, parse CSVs and JSONs, and clean messy text data.

