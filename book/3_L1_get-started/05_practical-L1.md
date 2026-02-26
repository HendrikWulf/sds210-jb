---
title: Practical L1
site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
Understanding and execution notebooks
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/3_L1_get-started/05_practical-L1.ipynb)


## Learning objectives

After completing this practical, you will be able to:

* distinguish between **Markdown cells** and **Code cells**
* execute notebook cells in the correct order
* explain why execution order and kernel state matter
* restart a kernel and run a notebook from top to bottom safely
* avoid common mistakes caused by hidden state

---

## Practical storyline

In this practical, you will build a **safe and reliable workflow** for working with notebooks.

You will learn:

1. how notebooks are structured
2. how code is executed
3. how variables are stored in memory
4. why execution order matters

This practical establishes habits that are essential for reproducible scientific work.

---

## Part 1 – Understanding notebooks

Notebooks are divided into **cells**.

There are two main types:

* **Markdown cells** → text and explanation
* **Code cells** → executable Python

---

### Editing Markdown cells

This cell is written in Markdown.

```{admonition} Important
:class: important
Markdown cells contain text and formatting only.  
They do not execute Python code.
```

### Tasks

1. Double-click this cell.
2. Change some of the words in this sentence: "This is really very important."
3. Make one word _italic_ and another **bold** using `*` and `_` signs.
4. Run the cell again (`Ctrl + Enter`).
5. Using the Markdown guide below, figure out how to render a third word __bold__ and *italic*. 
   
Markdown reference:
[https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)

---

## Part 2 – Executing code cells

Code cells contain Python instructions.  
The example below contains **Python code**.  
When you click on it, notice how the cell type changes from Markdown to Code in the dropdown above.


To run a code cell:

* Click ▶ Run
* or press **Shift + Enter**

---

### Example

```python
# The line below prints text to the screen
# Change it so that it prints something more meaningful.

print("Wo sind die Schnapspralinen?")
```

### Tasks

1. Modify the printed text.
2. Add a comment explaining what the code does.
3. Run the cell.

---

## Part 3 – Expressions and output

The next example works with numbers.  
Before running the cell, predict what will be displayed.

```python
x = 3
y = 4

x - y
x + y
```

### Tasks

1. Predict what will be displayed.
2. Run the cell.
3. Change `x` and `y`.
4. Run it again.

---

```{admonition} Concept check
:class: note

Why is only one result displayed?

(A) Python ignores earlier lines  
(B) Only the final expression is automatically returned  
(C) The first calculation failed  

Discuss with a neighbour before answering.
```

---

## Part 4 – Making output explicit

To display multiple results, use `print()`.

```python
print(x - y)
print(x + y)
```

### Tasks

1. Modify the numbers.
2. Add a third print statement.
3. Observe how explicit output improves clarity.

```{admonition} Notice
:class: note

* Calculations happen inside `print()`
* All printed lines are displayed
* The cell depends on variables from previous cells

The **order** in which you run cells matters.
```

---

## Part 5 – Variables and memory

A common programming pattern is:

1. compute something  
2. store it in variables
3. reuse it 

```python
a = x - y
b = x + y

print("The answers to the two calculations are", a, "and", b)
```

You have now created variables that exist in the notebook’s memory.

---

### Kernel experiment

Restart the {term}`kernel` of the notebook:

**Kernel → Restart** (in Colab: Runtime → Restart Session)

Then run **only the last cell**.

````{admonition} What happens?
:class: dropdown

You should see an error such as:

```
NameError: name 'x' is not defined
```
````

```{admonition} Why?
:class: dropdown

Because:

* The notebook memory was cleared.
* `x` and `y` were not defined again.

This is called {term}`hidden state`.

```

Good scientific practice requires:

1. Restarting the kernel.
2. Running all cells from top to bottom.
3. Checking that the notebook works without manual reordering.

### Task

Restart the kernel again.

Then choose:

**Kernel → Restart & Run All**  
or Click ⏩ (Restart the kernel and run all cells) in the taskbar

Confirm that everything works.

---

## Part 6 – Useful notebook actions

Practice the following:

* Insert new cells via **Insert → Cell Above / Below**
* Add a simple calculation.
* Add a Markdown explanation.
* Run cells step by step
* Save your notebook locally

Remember: execution order matters.

---

## Exercises

1. Modify the first code cell so that it prints **something**
2. Change the values of `x` and `y` and observe the results
3. Add a new code cell with a simple calculation
4. Restart the kernel and run only one later cell.
5. Add a Markdown cell describing what you did in form of a bullet point list
6. Save your notebook locally and open it in JupyterLab


````{admonition} Sample solution (click to expand)
:class: dropdown

### 1. Printing something

You could modify the first code cell like this:

```{code-cell} python
print("Es jibt eben sone und solche, und dann jibt es noch janz andre, aba dit sind die Schlimmstn, wa?")
```

(Use your own words instead.)

---

### 2. Changing `x` and `y`

Example:

```{code-cell} python
x = 10
y = 2

x - y
x + y
```

Output:

```
12
```

Only the **last expression** (`x + y`) is shown automatically.

---

### 3. Adding a new calculation

Example:

```{code-cell} python
z = 6
result = z * 3

print("z times 3 is", result)
```

This creates a new variable and prints the result explicitly.

---

### 4. Restarting the kernel and running only one later cell

If you restart the kernel and run only:

```{code-cell} python
a = x - y
print(a)
```

You will likely get an error like:

```
NameError: name 'x' is not defined
```

**Reason:**

* Restarting the kernel clears all variables from memory.
* Since `x` and `y` were defined in earlier cells, they no longer exist.

This demonstrates how notebooks depend on execution order.

---

### 5. Adding a Markdown explanation

Example Markdown cell:

```markdown
### What I did

- Modified the first code cell to print my name.
- Changed the values of `x` and `y` and observed different outputs.
- Added a new calculation using a new variable.
- Restarted the kernel and noticed that variables were no longer defined.
- Learned that execution order matters in notebooks.
```

---

### 6. Saving and opening in JupyterLab

If running locally:

1. Click **File → Save Notebook**.
2. Open a terminal and navigate to your saved notebook
3. [Activate your environment](https://hendrikwulf.github.io/sds210-jb/book/setup/conda/#id-5-working-with-conda):

```bash
conda activate sds210
```

4. [Start JupyterLab](https://hendrikwulf.github.io/sds210-jb/book/setup/jupyterlab/#id-3-getting-started):

```bash
jupyter lab
```

5. Navigate to your saved notebook file and open it.

---

```{admonition} Takeaway
:class: tip

A notebook should work after:

1. Restarting the kernel  
2. Running all cells from top to bottom  

If it does not, it likely depends on {term}`hidden state`.
```
````

## Summary

You have learned to:

- distinguish Markdown and Code cells  
- execute cells interactively  
- understand why execution order matters  
- store and reuse values  

These mechanics may seem simple, but they are foundational.
Reliable execution is the basis for trustworthy analysis.

### What comes next

So far, you have learned **how notebooks run**.
In the next lessson, you will focus on variables and data structures.