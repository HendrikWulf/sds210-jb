---
title: Assessment

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
How your programming project is evaluated
</div>

---

The assessment in SDS210 is based entirely on your **individual programming project**. This project brings together the concepts, methods, and coding practices developed throughout the course. It is your opportunity to demonstrate that you can design, implement, explain, and communicate a fully reproducible solution to a real-world spatial data problem using Python.

This section outlines how the project is graded, the specific criteria used, and what successful projects typically look like.

```{admonition} Big idea
:class: tip

This assessment is not just about getting your code to run without crashing. It is about building a complete, transparent solution that can be easily understood, explained, and reproduced by others.
```

---

## 1. Assessment Components

Your final project grade is divided equally between **two mandatory components**:

  * **Project Report & Code:** 50%
  * **Project Presentation:** 50%

Both components are critical. A project is only considered successful if you can document your workflow clearly *and* defend your analytical decisions convincingly in person.

### The Report & Code (50%)

This component evaluates the actual Python code you write and the written report that accompanies it. Your report must clearly document your approach, the workflow you designed, your final implementation, and your reflection on the results. It serves to connect your raw code, your GitHub/GitLab repository, and your final maps/charts into one coherent scientific summary.

### The Presentation (50%)

The presentation is a **10-minute** individual discussion held at the end of the semester. During this session, you will explain the core problem you tackled, demonstrate key parts of your code live, and justify your specific design choices. This component proves that you genuinely understand the logic behind your workflow and did not simply copy-paste a solution.

```{admonition} Important
:class: important

A beautifully formatted report cannot compensate for a weak, confused presentation where you cannot explain your own code. Conversely, a confident presentation cannot save a project that lacks a reproducible repository or a coherent written report. You must succeed in both arenas.
```

### Timing and Deadlines

  * **Report Submission Deadline:** Friday, 22 May 2026 at 18:00.
  * **Project Presentations:** Wednesday, 27 May 2026 – Monday, 01 June 2026.

*(Note: If the final project assessment is not passed, students have the opportunity to retake it once at the end of August).*

---

## 2. Assessment Criteria

Your project is evaluated using a strict 10-point rubric that reflects the core philosophies of spatial data science. We do not just grade technical correctness; we place massive value on code structure, clarity, reproducibility, and thoughtful problem-solving.

### The 10 Grading Dimensions

1.  **Project Presentation (50%):** You confidently justify your cartographic and coding choices and can demonstrate all functionality (interactive and static) flawlessly during the live presentation.
2.  **Report (10%):** You provide a highly professional written summary that clearly defines the spatial question, logically outlines the approach, interprets the results, and candidly reflects on challenges.
3.  **Reproducibility (10%):** Your project achieves perfect reproducibility. You use relative file paths exclusively, provide a clear `README.md` with setup instructions, and maintain a cleanly structured Git repository so a peer can effortlessly rerun your work.
4.  **Correctness (5%):** Your code executes flawlessly from top to bottom. All spatial operations and mathematical calculations produce accurate, expected results without errors.
5.  **Structure (5%):** Your project features a highly modular design. You make excellent use of custom functions to prevent repetition (the DRY principle) and clearly separate your logic (loading, cleaning, analysis, plotting).
6.  **Documentation (5%):** Comprehensive Markdown cells narrate your Jupyter Notebook workflow. Clear inline comments explain *why* specific code is written, and your custom functions have concise, accurate docstrings.
7.  **Readability (5%):** Your code is exceptionally easy to read. Variable and function names are highly descriptive, and your formatting and indentation are strictly consistent.
8.  **Robustness (4%):** Your code anticipates and gracefully handles edge cases (e.g., missing data/NaNs, invalid geometries), making it safe against unexpected inputs. 
9.  **Efficiency (3%):** You make perfect use of vectorized operations in Pandas/GeoPandas, avoiding unnecessary or slow `for` loops, and utilizing highly efficient spatial joins.
10. **Innovation (3%):** You utilize a highly creative approach, such as advanced thematic mapping, custom interactive elements, or unique data combinations that go well beyond basic course expectations.

### How to Interpret the Criteria

Do not fall into the trap of assuming you need a highly advanced, machine-learning-driven project to score well. As you can see from the weightings above, **Innovation** is only worth 1%. The vast majority of your grade depends on the **clarity, reproducibility, and explanation** of your work.

```{admonition} A useful mindset
:class: note

A simple, tightly scoped project that features readable code, a perfectly structured repository, and a flawless live explanation will always score higher than a massively ambitious project that is messy, crashes frequently, and cannot be easily explained.
```

---

## 3. What Good Projects Typically Show

While strong projects can explore vastly different topics, they almost always share a specific set of professional qualities.

### A Focused Workflow

Good projects do not feel like a random collection of code snippets. They start with a highly specific question, and every single step of the workflow—from data cleaning to final visualization—is logically designed to answer that specific question.

### Understandable Code

You are not expected to write production-grade software, but your code must show care. Good project code is divided into logical sections, utilizes highly descriptive variable names (e.g., `zurich_neighborhoods` instead of `data_2`), relies on custom functions to eliminate repetitive copying and pasting, and includes helpful comments.

### Meaningful Outputs

Strong projects produce outputs (maps, charts, summary tables) that directly support the project's core question. The goal is not to generate 20 random plots to prove you know how to use Matplotlib; the goal is to produce 3 or 4 highly polished, interpretable visualizations that actually explain the spatial phenomenon you are studying.

### Absolute Reproducibility

A good project repository guarantees that another student can rerun the work. This means your GitHub/GitLab repository contains a clear `README.md`, your notebooks use relative file paths, and your environment setup is explicitly documented. Reproducibility is the clearest indicator that a project was developed carefully and professionally.

### Honest Reflection

Finally, strong projects prove that the student can critically reflect on their own process. During the report and presentation, you must be able to explain exactly *why* you chose a specific colormap, *what* specific coding challenges you encountered, *how* you solved them, and *where* your analytical workflow has statistical or spatial limitations.

```{admonition} What assessors are looking for
:class: dropdown

When evaluating your project, your instructors are essentially asking themselves:

1. Did the student design a workflow that actually makes logical sense?
2. Does the code run smoothly and produce mathematically correct outputs?
3. Is the repository organized cleanly enough for a stranger to use?
4. Can the student clearly explain *what* their code does and *why* they designed it that way?
5. Could I download this right now and reproduce their exact results?
```

---

```{admonition} In summary
:class: note

The programming project is assessed through a written report/codebase (50%) and a live presentation (50%). To succeed, you must combine correct, readable code with a clear workflow, meaningful visual outputs, a perfectly reproducible Git repository, and a confident, well-reasoned defense of your design choices.
```