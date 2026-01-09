# Welcome

## Target Audience & Learning Objectives

### Target Audience

The *Programming with Spatial Data* module (ESS341, GEO876, SDS210) is designed for students who want to learn how to work with spatial data using Python and who are at an early stage in their programming journey.

The course is particularly well suited for:
- students with little or no prior experience in programming,
- students who have encountered some code before but lack confidence or routine,
- students from geography, environmental sciences, or related fields who want to move beyond graphical user interfaces and understand what happens “under the hood”.

No advanced programming background is assumed. The course starts from first principles and gradually builds up complexity. At the same time, it takes the learning process seriously: you will not only learn *how* to write code, but also *why* certain approaches work and how to structure solutions in a clear and reproducible way.

Programming with Spatial Data is not about pushing buttons. It is about using logic, programming, and your growing analytical skills to tackle real-world problems in a creative, reproducible, and open manner. The emphasis is on understanding, reasoning, and communicating with code rather than memorising syntax.

---

### Learning Objectives

This course aims to build a solid foundation in Python programming for spatial data analysis. Rather than focusing on isolated tools or short-term solutions, the emphasis is on developing transferable skills that help you plan, implement, and communicate code-based solutions in a structured and reproducible way.

By the end of the course, you should be able to work independently on small to medium-sized spatial programming tasks and understand how individual coding decisions fit into a larger analytical workflow.

On completion of this course, you will be able to:

- Apply core Python programming concepts, including variables, loops, functions, and data structures.
- Develop a conceptual outline and workflow before implementing a coding solution.
- Write well-documented, modular, and reproducible Python code following best practices.
- Design and implement object-oriented programming solutions that can read, store, manipulate, visualize, and export spatial data.

---

## Flipped Classroom and Expectations

This course follows a flipped classroom approach that combines self-paced learning with interactive, in-person lab sessions. Each week, you are expected to engage with the lecture videos and the accompanying written material before attending the lab. These resources introduce the core programming concepts and spatial data techniques that form the basis for the practical work.

The lab sessions are then used to apply what you have learned, clarify open questions, and work collaboratively on coding exercises. Instructors will be present to discuss your code, help you reason through problems, and support you when you encounter difficulties while implementing your solutions.

This structure allows you to:
- learn new concepts at your own pace through focused videos and readings,
- deepen your understanding during labs through hands-on coding and peer exchange,
- receive targeted support when and where you need it.

Because the classroom is flipped, preparation is essential. Except for the first week, you are expected to come to each lab having already watched the assigned videos and completed the required readings. The labs are not designed for first exposure to new material, but for applying, testing, and discussing it.

Being present and engaged in the lab sessions is therefore crucial. Make sure you attend the labs, actively work on the exercises, and use the opportunity to ask questions and reflect on your understanding.

---

### Workload and Commitment

This module is demanding, and making the most of it requires consistent effort. Success does not come from last-minute preparation, but from regular practice between lab sessions, careful reading of the materials, and repeated experimentation with code.

According to UZH guidelines, a 5 ECTS module corresponds to approximately 150 hours of total workload. With about two hours of timetabled lab activity per week, this leaves up to seven hours per week for self-study. In practice, you should expect to spend on average one hour per day learning, coding, and, most importantly, practicing.

---

### Why the Effort Is Worthwhile

There is a strong and growing demand for analysts, planners, and geographers who can think computationally and work confidently with data and code. Across public administration, research, business, and non-profit organisations, there is a clear skills gap in spatial data analysis and programming.

By investing the time and effort required in this course, you are developing skills that are widely applicable and highly valued. The ability to make sense of data through programming and analytical thinking opens up significant opportunities across many sectors.

---

## Why Is Programming (Still) Important?

With recent advances in AI, it is reasonable to ask whether learning to program is still worth the effort. If machines can write code for us, why spend time learning Python yourself?

In this short video the speaker argues that programming remains a high-impact skill not because of syntax, but because it teaches problem solving, systems thinking, and the ability to turn ideas into working solutions. These are precisely the skills this course aims to develop.

The video is not about learning a specific language or tool. Instead, it provides a broader perspective on why programming knowledge continues to matter, even in a world where AI can generate code.

### Video

The video is about eight minutes long. For this course, focus on first three minutes, which explain why learning to code remains valuable, with emphasis on problem solving, reasoning, and the limits of automation.

As you watch, reflect on how the arguments relate to learning Python for spatial data analysis, not just to software development in general.

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

Many students start this course wondering whether programming is simply too difficult, whether they need advanced mathematics, or whether they are “the right type of person” to learn how to code.

In this short video, the speaker addresses these concerns directly. The message is honest: learning to program is not effortless, but it is far more accessible than many people assume. What matters most is not prior knowledge, but persistence, curiosity, and having a meaningful reason to keep going when things become challenging.

### Video

The video is about three minutes long. It is meant as reassurance at the beginning, not as technical instruction.

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

Python is the programming language used throughout this course. It is widely adopted across science, data analysis, and many applied domains because it combines expressive power with readability and a rich ecosystem of libraries. Python allows you to focus on problem solving, data workflows, and reproducibility rather than on technical overhead.

### Video

In this video, the speaker highlights Python’s accessibility for beginners, its usefulness beyond traditional software development, and the reasons why it is often chosen for data driven work.

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

Geospatial data is complex by nature. It is large, structured in multiple dimensions, linked to coordinate reference systems, and often collected repeatedly over time. While graphical tools are useful for exploration and visualization, they quickly reach their limits when analyses become more complex, repetitive, or need to be reproduced.

Programming allows you to work with geospatial data in a transparent and controlled way. Instead of manually repeating the same steps, you can describe an entire workflow explicitly and apply it consistently to different datasets, regions, or time periods. This is essential when working with real-world spatial data, which is rarely clean, complete, or static.

Many common geospatial tasks benefit directly from programming, such as:
- processing large numbers of files or time steps,
- applying the same analysis to many spatial units,
- combining vector and raster data in systematic ways,
- ensuring that results can be reproduced and reviewed.

Programming also makes your analytical decisions visible. Code documents not only *what* you did, but *how* and *why* you did it. This supports reproducibility, collaboration, and critical evaluation of results, all of which are central to responsible spatial data science.

In this course, programming is used as a tool to think clearly about spatial problems and to build workflows that scale beyond a single dataset or map. The focus is not on replacing GIS software, but on complementing it with methods that provide flexibility, transparency, and analytical depth.
