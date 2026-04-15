---
title: Project Report

site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
How to document, submit, and reflect on your programming project
</div>

---

The project report is the written component of your final assessment, accounting for **50%** of your total project grade. It is your opportunity to explain what spatial problem you tackled, how you designed your workflow, what you actually implemented, and what you learned along the way.

The report does not replace your Jupyter Notebook or your GitHub repository; instead, it acts as the bridge connecting them. It guides the reader through the purpose of your project, the logic behind your code, your main results, and the key challenges you overcame.

```{admonition} Big idea
:class: tip

A good report does not try to explain every single line of code. It selects the most important parts of your project and explains the *why* behind your technical decisions.
```

---

## 1. The Purpose of the Report

Programming in spatial data science is not just about making code run; it is about making your workflow understandable to others. Your code might execute perfectly, but if your report fails to explain the core problem and your methodology, a massive part of the project is missing. Conversely, a beautifully written report cannot mask a broken, unreproducible workflow. The report, notebook, and repository must work together.

A strong report tells the story of your project in a compact, focused way. It should help an informed reader understand exactly what spatial problem you addressed and why it matters. It must clearly outline how you designed your workflow, highlight your most important implementation steps, present your final results, and candidly discuss the challenges you faced and how you resolved them.

Think of the report as an executive summary for a peer who has access to your repository but needs a high-level overview of your approach before diving into the code.

```{admonition} Keep the focus clear
:class: note

Your report is not a lab journal and certainly not a line-by-line code tutorial. Focus strictly on the core question, the overarching workflow, key implementation strategies, and your most significant roadblocks.
```

---

## 2. Required Contents and Structure

According to the syllabus, the written report is strictly limited to **two pages** in PDF format. Because space is limited, you must be selective. You do not have room to include long code snippets, massive tables, or explanations of minor parameter tweaks. The report must highlight the absolute most important parts of your project without duplicating what is already visible in the notebook.

### A Practical Report Structure

To ensure you hit all the required grading criteria, we recommend structuring your two-page report as follows:

  * **Introduction:** Briefly explain your chosen project topic, the specific spatial question you are answering, and the ultimate aim of the analysis.
  * **Workflow and Implementation:** Summarize the logical steps of your workflow. Focus on your overarching approach to data cleaning, spatial analysis, and visualization rather than minute technical details.
  * **Results:** Present your main findings, outputs, and spatial observations clearly.
  * **Challenges and Reflection:** Discuss at least one meaningful technical or analytical challenge you encountered. Describe how you dealt with it and what you learned from the debugging or redesign process.
  * **Repository Link & AI Statement:** You *must* include the URL to your public GitHub/GitLab repository. If you utilized AI tools, you must also include a short disclosure statement (see Section 4).

<!-- end list -->

```{admonition} A useful writing question
:class: dropdown

When editing your report, ask yourself:
1. Does this paragraph directly help explain the problem, the workflow, the result, or a challenge?
2. Am I wasting space repeating technical details that are already obvious in the notebook?
3. Would a fellow student understand the logic of my project after reading this?

If not, simplify and refocus.
```

---

## 3. Submission Format Requirements

Your final submission must be uploaded as a **single PDF document** via the MS Teams assignment. However, this single PDF must actually contain two distinct parts merged together:

1.  **The Written Report:** Your concise, two-page project summary.
2.  **The Notebook Export:** A PDF export (via Markdown/HTML print) of your fully executed Jupyter Notebook.

This combined format allows the assessors to read your high-level summary and immediately scroll down to verify the documented code and visual outputs that support it.

### Repository Expectations

Your written report must include a clickable link to your **public GitHub or GitLab repository**. This repository is where your reproducibility is tested. It must include clear setup instructions in the `README.md`, rely entirely on relative file paths, and contain a notebook that executes cleanly from top to bottom.

### Notebook Expectations

Your exported Jupyter Notebook is not just a script; it is part of your documentation. The syllabus requires your notebook to feature logically structured code, well-defined functions, meaningful variable names, and concise comments explaining complex operations.

```{admonition} Submission Checklist
:class: important

Before submitting to MS Teams, verify that you have:
1. A written report (maximum 2 pages).
2. A PDF export of your fully executed notebook attached to the end of the report.
3. A working link to your public GitHub/GitLab repository included in the text.
4. A clear `README.md` with setup instructions inside your repository.
5. Confirmed that your notebook runs from top to bottom without crashing.
```

---

## 4. AI Use Disclosure

In SDS210, the use of AI tools (like ChatGPT or GitHub Copilot) is permitted, provided it is purposeful, transparent, and reflective. AI is an excellent tool to support learning, but it must never replace your own understanding, judgment, or decision-making.

**If you used AI tools at any point during the project, you must state this clearly at the end of your report.**

### What is Expected

You are strictly responsible for all content submitted in your project. Any AI-assisted text or code must be critically reviewed, edited, validated, and fully understood by you. Copying AI-generated text or code without revision, understanding, or acknowledgment is considered plagiarism and will be sanctioned according to University of Zurich guidelines.

### Acceptable vs. Unacceptable Use

AI is great for explaining complex spatial concepts, improving your grammar, reviewing code for syntax errors, or exploring alternative analytical approaches. However, it is unacceptable to submit material that you cannot explain or justify yourself. If you use AI to write a complex spatial function, you must be able to defend exactly how that function works during your live presentation.

### Example Disclosure Statement

The syllabus provides the following example of an appropriate disclosure statement, which you can adapt and place at the bottom of your report:

> *I used a large language model as an assistance tool during the preparation of this project to check grammar and spelling, improve linguistic clarity, and help debug code for data processing. Apart from the uses listed above, no AI tools were used in the preparation of this submission, and all final logic and writing was verified by me.*

```{admonition} Transparency matters
:class: caution

Using AI is not a problem. Failing to acknowledge it, or submitting AI-generated work that you do not actually understand, is a serious academic offense. When in doubt, ask the course instructors.
```

---

## 5. Deadlines and Final Advice

The deadline for the report submission is **Friday, 22 May 2026 at 18:00**. You must submit the combined PDF via the **MS Teams assignment**.

### Why Timing Matters

Do not treat the report as an afterthought to be written in the final 48 hours. Because the report directly references your repository structure, notebook logic, and final maps, it is significantly easier to write if you draft it alongside your code.

Finish the technical coding early enough that you actually have time to revise the written report for clarity. Clear, concise scientific writing is almost always the result of heavy revision, not last-minute assembly.

---

```{admonition} In summary
:class: note

The project report is a two-page written explanation that connects your spatial question, workflow, implementation, results, and reflection. It must be merged with a PDF export of your executed notebook and submitted as a single file via MS Teams by Friday, 22 May 2026 at 18:00. It must include a link to your reproducible public repository and explicitly disclose any AI assistance.
```