---

title: L12 - Best Practices & Reproducibility

site:
outline_maxdepth: 1

---

```{div} page-subtitle
Writing spatial workflows that others can understand, rerun, and trust
```

---

By this point, you have learned Python fundamentals, geospatial data structures, data cubes, object-oriented programming, and practical workflows. You have the tools to analyze the environment as both discrete geometries and continuous surfaces. The last step is to connect all of that to professional habits.

In the computational sciences, a script that merely executes is not enough. Good code is not just code that works once. Good code is readable, maintainable, and easier to trust. As your spatial workflows grow in complexity, the way you structure, document, and share your projects becomes just as important as the analytical methods you apply.

This final lesson acts as a synthesis. We will transition from simply writing scripts that compute answers to building robust, transparent ecosystems where results can be independently verified.

---

## 1. Programming as communication

To master best practices, it helps to reframe programming. Programming is not just about giving instructions to a computer; it is also an act of communication.

When you write a spatial workflow, you are potentially communicating:

* with your future self
* with collaborators
* with instructors and reviewers
* with anyone who needs to rerun your work

Computers do not really care what your code looks like, but humans do. In the context of spatial data science, "good code" means prioritizing readability before cleverness. It means ensuring maintainability as projects grow, and treating coding best practices as a form of scientific integrity.

---

## 2. Why this matters for {abbr}`SDS (Spatial Data Science)`

In spatial data science, reproducibility is not an optional add on. It is part of doing spatial data science responsibly.

Geospatial workflows are complex. A final map or summary statistic is rarely the result of a single operation. They depend on a series of computational choices, such as reprojecting data, applying spatial thresholds and clipping rasters. If these intermediate steps cannot be repeated and verified by another researcher, it becomes difficult to trust the final result.

[*The Turing Way*](https://book.the-turing-way.org/reproducible-research/reproducible-research/) defines reproducibility in data research as making data and code available so the analysis can be fully rerun. Similarly, the *PLOS "[Ten Simple Rules](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285#s5)"* frames reproducibility as a practical minimum standard for computational research. By adopting these professional habits, you ensure that your spatial analyses can stand up to scientific scrutiny.

---

## 3. Learning objectives

After this lesson, you will be able to:

* **Write more readable code**  
Apply [PEP 8](https://peps.python.org/pep-0008/) principles to reduce errors, speed up debugging, and make spatial workflows easier to understand and maintain.
* **Organize spatial projects**  
Structure workflows so they do not collapse under their own complexity. Move beyond one giant notebook by utilizing robust relative paths and standard project layouts.
* **Code defensively**  
Write geospatial code that anticipates mistakes, explicitly checks assumptions, and fails clearly when something is wrong.
* **Capture software environments**  
Record exact dependencies to move beyond the "it works on my machine" problem, recognizing that reproducibility includes the software ecosystem.
* **Document for interpretability**  
Use READMEs, docstrings, and inline comments to ensure your project explains *why* things happen, not just *what* happens.
* **Practice reproducible research**  
Combine code, data, and environments so that another person, or you at a later time, can fully recover the exact same results.

---

## 4. Lesson structure

This lesson is structured as a synthesis lesson that connects coding habits to scientific workflow quality:

1. **Writing readable Python**: Code style as a tool for clarity, debugging, and scientific trust.
2. **Organizing code**: Moving from one large notebook to structured spatial workflows.
3. **Defensive coding**: Writing geospatial code that checks assumptions and fails clearly.
4. **Reproducible environments**: Moving beyond "It works on my machine".
5. **Documenting code**: Making spatial projects understandable, not just runnable.
6. **Reproducible research**: Bringing the pillars of reproducible spatial science together.

---

## 5. Looking ahead

Lesson 12 is about **scientific trustworthiness**.

You will learn not only *how to write scripts*, but how to:

* write code that is readable and maintainable
* organize projects so they do not collapse under their own complexity
* make analyses reproducible so that results can be rerun and verified later

If the previous lessons were about giving you the analytical power to map and measure the physical world, this lesson ensures those measurements have lasting value.

A good spatial analysis does not end with a final map. It ends with a transparent workflow that another person can understand, rerun, and trust.
