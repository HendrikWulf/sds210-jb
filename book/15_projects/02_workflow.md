---
title: Project Workflow

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
From a first idea to a working and reproducible project
</div>

---

A good programming project rarely starts with perfect code. It usually begins with a question, takes shape through a rough plan, and improves step by step through testing, revision, and reflection.

This section outlines how to approach your project in a structured way. The goal is not to force you into one rigid process, but to help you build a workflow that is manageable, transparent, and effective.

```{admonition} Big idea
:class: tip

Strong projects are built iteratively. First, make something simple work. Then, improve it.
```

---

## 1. From question to workflow

Every project begins with a question, but initial ideas are often too broad. A good workflow turns an abstract theme into a sequence of actionable steps.

For example, a broad topic like *urban heat* is not yet a workflow. It becomes one only when you decide exactly which area you want to study, what data you need, which variables to analyze, and how you will summarize and visualize the results. Your first task is to narrow your focus.

### Start with a focused question

A highly focused question is specific enough that you can immediately imagine what your first few code cells should do.

Compare these two examples:

**Too broad:** How has Zurich changed over time?

**More focused:** How have summer land surface temperatures and NDVI changed in Zurich between 1985 and 2024?

The second version is much easier to tackle because it explicitly defines the geography, the timeline, and the exact variables required.

### Turn the question into steps

Once your question is clear, break it down into a logical sequence. While every project is unique, most successful workflows move through a similar progression: defining the study area, accessing the data, inspecting and cleaning it, calculating relevant summaries, visualizing the results, interpreting the outcome, and documenting the process.

```{admonition} The Workflow Test
:class: note

Ask yourself: *Can I explain my project workflow as a sequence of five to seven clear steps?* If you can sketch it out as a simple flowchart, you are ready to code.
```

---

## 2. Planning your analysis

A few minutes of planning saves hours of debugging. Planning prevents you from writing massive blocks of code before you even know what your workflow is supposed to achieve.

A plan does not need to be a formal document; a short outline is perfectly fine.

### What to plan first

Before writing substantial code, clarify your direction. Ask yourself: What are my exact questions, and what data will I use? What does a successful output look like? Identify which steps seem straightforward and which might be tricky, and figure out how to build the simplest useful version first. You do not need to solve every detail in advance, but you should have a rough roadmap.

### Sketch the workflow

A helpful approach is to write a "mini-workflow" in plain English (pseudocode) before writing any Python. For example:

1.  Load the wildfire records.
2.  Keep only the relevant columns.
3.  Convert the raw coordinates into a geometry.
4.  Count the fires by month.
5.  Map the selected events and add interactive popups.

This kind of outline makes it incredibly easy to translate your ideas into specific functions, notebook sections, or individual code cells.

### Think about outputs early

Many students focus entirely on the code and forget about the final deliverable. Projects are about producing meaningful insights. Your expected output might be a thematic map, a comparative chart, a summary table, or a clear written interpretation in your report. Knowing exactly what output you are aiming for helps you write code that is targeted and efficient.

---

## 3. Building an incremental solution

One of the most valuable habits in programming is building your project incrementally. Do not try to solve the entire problem in one massive script. Start with a small, functioning core and scale up. This is faster, safer, and much easier to debug.

### Start simple

Your first draft should handle only the absolute core task. For instance, try loading just one file before combining a dozen, or map a single variable before building a complex interactive visualization. Testing your logic on a small data sample helps verify that your approach works before you apply it to the entire dataset.

### Improve in layers

Once your baseline version works, enhance it step by step. You can refine your code by choosing better variable names, grouping repeated logic into reusable functions, polishing your plots, and adding safety checks for missing values or errors. This layered approach keeps the project manageable and helps you catch problems early.

### Separate core tasks

As your project grows, logically separate your tasks. Keep data loading, data cleaning, spatial analysis, and visualization in distinct sections of your notebook. This modular approach makes your code much easier to read and adapt.

```{admonition} A common mistake
:class: important

Do not wait until the very end to "clean up" your code. Small organizational improvements made throughout the project are much easier to manage than a massive rewrite the day before the deadline.
```

---

## 4. Testing, debugging, and refining

Programming projects never work perfectly on the first try. Errors, unexpected outputs, and messy intermediate results are entirely normal. Debugging is not a sign of failure; it is the fundamental feedback loop of programming.

### Test small parts first

When a script breaks, it is much easier to find the root cause if you test small, isolated pieces. Check your assumptions cell by cell: verify if a file loaded correctly, if a function returned the expected data type, or if your coordinate column actually contains valid numbers.

### Read errors carefully

Tracebacks can look intimidating, but they almost always point directly to the solution. Slow down and read the actual error message. Ask yourself: Which specific line caused the crash? What data type did Python expect versus what it actually received? Did you misspell a column name or provide an invalid file path? Very often, the cause is a simple typo rather than a fundamental flaw in your logic.

### Refine after it works

Once your code runs, the project is not necessarily finished. A working solution can always be improved. Ask yourself if the workflow is easy to follow, if your variable names are clear, and if the outputs are readable. Could another student understand exactly what your code is doing? Refining means moving from code that merely executes to code that is clear, robust, and easy to explain.

```{admonition} The Debugging Mindset
:class: tip

When your code fails, do not just ask, "How do I fix this?" Ask, "What is this error teaching me about my data's structure?"
```

---

## 5. Working reproducibly

Reproducibility is a core expectation of this project. Another student or instructor should be able to download your repository and run your workflow on their own machine without the code crashing.

Working reproducibly means organizing your project so that the logic, structure, and required environment are completely transparent.

### What reproducibility means in practice

In practice, a reproducible project features a clear file structure, readable notebook sections, and relative file paths. It also requires clear setup instructions in your README, a consistent Python environment, and code that executes smoothly from top to bottom. It doesn't mean your project has to be massive; it simply means it must be understandable and re-runnable.

### Make your future self a user

A great way to test reproducibility is to imagine returning to this project in three months. Would you still understand how to run it? If the answer is no, someone else definitely won't. Leave clear signposts: explain what the project does, where the data comes from, how to install required packages, and how to interpret the final outputs.

### Reproducibility supports better thinking

Reproducibility isn't an extra chore added at the end for grading purposes; it is a professional standard that improves your own workflow. When your project is structured clearly, it becomes much easier to test, revise, explain, and present your work.

```{admonition} Reproducibility checklist
:class: dropdown

Before you submit your project, verify the following:

1. Does the notebook run successfully from top to bottom?
2. Are all data files referenced using relative paths?
3. Is the repository structure logical and clean?
4. Does the `README` clearly explain the setup and execution?
5. Could another student reproduce your main result based on your instructions?

If you cannot answer "yes" to all of these, your project needs a bit more refinement.
```

-----

```{admonition} In summary
:class: note

A successful project workflow moves from a highly focused question to a structured plan, from a simple baseline to a refined solution, and from functional code to fully reproducible science. Start small, test frequently, improve iteratively, and ensure your workflow is transparent enough for anyone to follow.
```