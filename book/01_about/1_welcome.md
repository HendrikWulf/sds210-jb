# Welcome

Welcome to *Programming with Spatial Data* (SDS210).
This course introduces **computational thinking and Python programming for geospatial applications**. In an increasingly data-driven and automated world, the ability to design, write, and organise code for spatial analysis has become an essential skill for addressing environmental, social, and urban challenges.

Rather than focusing on isolated tools or button-clicking workflows, this course emphasises **thinking with code**. You will learn how to translate spatial questions into structured, reproducible workflows and how to implement these workflows using Python. Over the semester, you will build a solid foundation in core programming concepts and progressively apply them with widely used geospatial libraries such as GeoPandas, RasterIO, and Matplotlib. Throughout the course, strong emphasis is placed on writing **clear, structured, and well-documented code**, supported by Jupyter Notebooks and Git to enable transparent and reproducible work.

The course concludes with an individual programming project in which you design and implement your own solution to a spatial data problem. By the end of the course, you will be well prepared to take on more advanced challenges in spatial data science, both in research and in applied contexts.

---

## Why Learn to Program?

You might be wondering why you should even bother learning to program at all. After all, you are probably not a computer scientist, and neither are we. Yet all authors of this course use programming regularly as part of their scientific and applied work. Often, the programs we write are short, simple, and highly practical but they make a real difference.

The reason is simple: **geography and geoscience have become increasingly quantitative**. We now work with larger datasets, repeated observations, numerical models, and automated analyses. Many of these tasks quickly become inefficient, error-prone, or impossible when done manually. Even basic programming skills allow you to explore data more flexibly, apply analyses consistently, and document exactly what you did.

Programming does not replace GIS software, but it **extends it**. Many tools you already know, such as QGIS, are built around Python and allow you to automate workflows, inspect data programmatically, or develop custom tools. Understanding a bit of code helps you move beyond button-clicking and better understand what happens behind the scenes.

:::{figure} images/01_QGIS-python.png
:alt: Via the Python console you can interact with GIS data in QGIS.
:width: 700px

Via the Python console you can interact with GIS data in the [QGIS](https://www.qgis.org/) program.
:::

Programming can also be **surprisingly enjoyable**. Once you learn the basics, complex problems can be broken down into smaller, logical steps. You can test ideas immediately, adjust your approach, and see whether your solution works. This problem-solving mindset is one reason why programming is increasingly introduced early in education. The aim is not to train programmers, but to train **thinkers**.

Finally, programming supports **[good scientific practice](https://microsite.geo.uzh.ch/olwa/olwa/en/html/index.html)**. The [scientific method](https://en.wikipedia.org/wiki/Scientific_method) relies on transparency, testing, and reproducibility. Writing code forces you to be explicit about your assumptions, your steps, and your decisions. Data processing, analysis, and visualisation become repeatable rather than ad-hoc. Throughout this course, you will learn programming practices that help make your work reproducible, communicable, and reusable, which are key principles of modern, [open science](https://book.the-turing-way.org/reproducible-research/open/).

---

## Is This the Right Course for You?

### Target Audience

*Programming with Spatial Data* is designed for students who want to learn how to work with spatial data using Python and who are at an early stage in their programming journey.

The course is particularly well suited for:

* students with little or no prior programming experience,
* students who have encountered code before but lack confidence or routine,
* students from geography, environmental sciences, or related fields who want to move beyond graphical user interfaces and better understand what happens behind the scenes.

No advanced programming background is assumed. The course starts from first principles and gradually builds up complexity. At the same time, it takes the learning process seriously: you will not only learn *how* to write code, but also *why* certain approaches work, how to structure solutions clearly, and how individual decisions affect reproducibility and maintainability.

This is not a course about pushing buttons. It is about using logic, programming, and analytical thinking to tackle real-world spatial problems in a transparent, reproducible, and communicable way.

### Learning Objectives

This course aims to build a solid foundation in Python programming for spatial data analysis. Rather than focusing on short-term solutions or isolated tools, the emphasis is on developing transferable skills that help you plan, implement, and explain code-based workflows.

By the end of the course, you should be able to work independently on small to medium-sized spatial programming tasks and understand how individual coding decisions fit into a larger analytical process.

On successful completion of the course, you will be able to:

* apply core Python programming concepts such as variables, loops, functions, and data structures,
* design a conceptual workflow before implementing a coding solution,
* write clear, modular, and reproducible Python code with appropriate documentation,
* read, understand, and debug existing Python code for spatial analysis,
* design and implement object-oriented solutions to read, manipulate, visualise, and export spatial data.
  
---

## How to Approach This Course?

This course follows a flipped classroom approach that combines self-paced learning with interactive, in-person lab sessions. Each week, you are expected to engage with the lecture videos and the accompanying written material before attending the lab. These resources introduce the programming concepts and spatial data techniques that form the basis for the practical work.

The lab sessions are used to apply what you have learned, clarify open questions, and work collaboratively on coding exercises. Instructors are present to discuss your code, help you reason through problems, and support you when you encounter difficulties during implementation.

This structure allows you to:

* learn new concepts at your own pace through videos and readings,
* deepen your understanding during labs through hands-on coding and peer exchange,
* receive targeted support where and when you need it.

Because the classroom is flipped, preparation is essential. Except for the first week, you are expected to come to each lab having already engaged with the assigned materials. The labs are designed for applying, testing, and discussing ideas, not for first exposure to new content.

### Workload and Commitment

This module is demanding and requires consistent effort throughout the semester. Success does not come from last-minute preparation, but from regular practice, careful reading, and repeated experimentation with code.

According to UZH guidelines, a 5 ECTS module corresponds to approximately 150 hours of total workload. With about two hours of timetabled lab activity per week, this leaves several hours per week for self-study. In practice, you should expect to spend time almost every day reading, coding, and practicing.

### Why the Effort Is Worthwhile

There is a growing demand for analysts, planners, and geographers who can think computationally and work confidently with data and code. Across research, public administration, industry, and non-profit organisations, spatial data skills combined with programming literacy are increasingly sought after.

By investing the time and effort required in this course, you are developing skills that are widely applicable and highly valued. Learning to reason with code opens up opportunities across many domains and allows you to engage more critically and creatively with spatial data.

---

## How to Read This Course Book?

Becoming proficient in spatial programming cannot be accomplished just by passively reading; it requires structure, strategy, and hundreds of hours of hands-on practice. We have designed this book to put you in the driving seat of your own learning.

While you can (and generally should) read this book from start to finish, as each lesson logically builds upon the last, we have organized the content so you can safely budget your time and focus on what matters most to your progress.

### The Structure of a Lesson

The book is divided into thematic **Lessons** (e.g., L3 - Loops, L7 - Vector Data). Each lesson follows a predictable structure:

* **The Lesson Introduction:** Sets the stage, explains the motivation behind the tools, and outlines the big-picture learning objectives.
* **The Chapters:** Each lesson is broken down into several chapters with numbered sections. These pages tackle specific concepts, syntax, and workflows, culminating in short exercises to test your immediate understanding.
* **The Practical Lab:** At the end of every lesson, a comprehensive lab brings all the individual chapter concepts together. Here, you will apply what you have learned to a complex, real-world spatial storyline.

### The Triage Tool: "Chapter Relevance"

We know your time is valuable. To help you evaluate how deeply you need to study a specific topic, every chapter begins with a dropdown box titled **Chapter Relevance**. Think of this as your personal signpost. It evaluates the chapter across three criteria using a 0-to-3 star rating system:

* **Lab Relevance:** How critical is this exact chapter for managing this week's Practical Lab?
* **Project Relevance:** How useful is this methodology for a Final Student Project?
* **Foundation:** How important is this concept for your general growth as a GeoPython programmer?

Additionally, this block provides a **"Time to Read"** estimate, a one-sentence **"In a nutshell"** summary, and a specific **"Skip this if"** condition. If you already possess the prior knowledge listed in the "Skip" condition, you can confidently skim or bypass the chapter without falling behind.

### Practice and Productive Struggle

The short exercises at the end of the chapters and the weekly Practical Labs are based on real-world environmental and geographical data, making them interesting and challenging. It is entirely normal to feel stuck at first. When you hit a wall, take a break, read the Python error messages carefully, and try breaking the problem down into smaller steps. Although we provide sample solutions in dropdown boxes, we strongly encourage you to attempt the code yourself first. The learning happens during the struggle, not when reading the answer.

### The Final Project

Everything in this book (every chapter and every lab) is designed to prepare you for the **Final Project**. This project is where the training wheels come off. It is your opportunity to synthesize the different skills you have learned (data intake, cleaning, spatial analysis, and visualization) and demonstrate that you can work independently to solve a real-world spatial problem from start to finish.

---

## Why Programming Still Matters

With recent advances in AI, it is reasonable to ask whether learning to program is still worth the effort. If machines can generate code, why spend time learning Python yourself?

In the following short video, the speaker argues that programming remains a high-impact skill not because of syntax, but because it teaches problem solving, systems thinking, and the ability to turn ideas into working solutions. These are precisely the skills this course aims to develop.

The video is not about mastering a specific language or tool. Instead, it provides a broader perspective on why programming knowledge continues to matter, even in an increasingly automated world. Focus on first three minutes to get this point.

<iframe
  width="100%"
  height="450"
  src="https://www.youtube.com/embed/zSySYY8c32E"
  title="Why learning to code still matters"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

## Is Programming Hard?

Many students begin this course wondering whether programming is too difficult, whether advanced mathematics are required, or whether they are “the right type of person” to learn how to code.

In the following short video, these concerns are addressed directly. Learning to program is not effortless, but it is far more accessible than many people assume. What matters most is persistence, curiosity, and having a meaningful reason to continue when things become challenging.

<iframe
  width="100%"
  height="450"
  src="https://www.youtube.com/embed/k7Txbdvzx90"
  title="Is learning to code hard?"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

## Why Python?

Python is the programming language used throughout this course. It is widely adopted across science, data analysis, and applied domains because it combines expressive power with readability and a rich ecosystem of libraries. Python allows you to focus on problem solving, data workflows, and reproducibility rather than on technical overhead. For this course, Python provides the best balance between ease of entry and long-term relevance for spatial data science workflows.

:::{figure} images/stackoverflow-trends-chart.svg
:alt: The popularity of programming languages as indicated by the number of questions on Stack Overflow.
:width: 700px

The popularity of programming languages as indicated by the number of questions on Stack Overflow.
:::

In the following video, the speaker highlights why Python is often chosen for data-driven work and why it is particularly suitable for beginners who want to build practical, transferable skills.

<iframe
  width="100%"
  height="450"
  src="https://www.youtube.com/embed/Y8Tko2YC5hA"
  title="Why Python is so popular"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>

---

## Why Programming with Geospatial Data?

Geospatial data is complex by nature. It is often large, multi-dimensional, linked to coordinate reference systems, and collected repeatedly over time. While graphical tools are useful for exploration and visualisation, they quickly reach their limits when analyses become complex, repetitive, or need to be reproduced.

Programming allows you to work with geospatial data in a transparent and controlled way. Instead of manually repeating the same steps, you can describe entire workflows explicitly and apply them consistently across datasets, regions, or time periods. Code documents not only what you did, but also how and why you did it, supporting reproducibility, collaboration, and critical evaluation.

In this course, programming is used as a complement to GIS software. The goal is not to replace graphical tools, but to extend them with methods that provide flexibility, transparency, and analytical depth when working with real-world spatial data.
