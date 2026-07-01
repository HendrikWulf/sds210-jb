---
title: Writing script files

site:
   outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Moving code out of the notebook
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/07_L05_libraries/01_script_files.ipynb)

---

```{admonition} Big idea
:class: tip

Don't copy and paste the same code into every notebook.

By moving your custom functions into a dedicated Python script file (`.py`), you can **import** them into any project. This keeps your notebooks clean, makes your code reusable, and creates a single, reliable source of truth for your tools.


```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★☆☆ (Helpful context for organizing code, but not directly required to complete the Jupyter Notebook tasks in Practical L5)  
**Project Relevance:** ★★☆ (Essential for building a modular codebase and achieving high marks on the Structure criteria [5] across projects 1, 2, 3, and 4)  
**Foundation:** ★★☆ (A vital structural concept for moving beyond basic notebook scripting into professional software development)  

**Time to Read:** 10 minutes  
**In a nutshell:** Learn how to move custom functions out of messy notebooks and into structured `.py` files that act as reusable toolkits.  
**Skip this if:** You already know how to create `.py` scripts, import them locally into Jupyter, and fully understand why updating a file requires an IPython kernel restart.

```

Up to this point, you have been keeping your Python code and Markdown comments in a single Jupyter notebook document. This is great for exploration and learning. However, there are cases where you want to have Python code in a separate document. When you have long Python code blocks or a set of **{term}`functions <Function>`** used across many different notebooks, moving them out makes your notebook much easier to read and use.

An alternative to typing all your commands directly into cells is to list them in a Python **{term}`script <Script>`** file. A Python script file is simply a plain text file containing a list of the commands you want to run, formatted exactly as if you were to type them into a cell. Python script files traditionally use the `.py` file extension.

---

## 1. Creating a script file

Because a Python script file is simply a list of commands, we can easily create a basic one and test things out right inside **{term}`JupyterLab`**.

First, create a new text file by clicking on **File > New > Python File** in the JupyterLab menu bar. You can do the same in **{term}`VS Code <Visual Studio Code>`** (File > New File > Python File) or **{term}`Colab <Google Colab>`** (File > Download > Download .py).

:::{figure} images/01_python-file.png
:alt: Creating a new Python file in JupyterLab.
:width: 500px
:align: center

*Creating a new Python file in JupyterLab.*
:::

This creates a new tab in your window with a blank slate. By default, new Python files will have the name `untitled.py`. You can rename the file by right clicking on it in the file browser and renaming it to `spatial_tools.py`.

:::{figure} images/02_rename.png
:alt: Renaming the new file in JupyterLab.
:width: 700px
:align: center

*Renaming the new file in JupyterLab.*
:::

Start by copying and pasting the text below into your new editor panel. This is a function that calculates the straight line **{term}`Euclidean distance`** between two projected coordinates using the basic math operators you learned in Lesson 2:

```{code-cell} python
def euclidean_distance(x1, y1, x2, y2):
    """
    Calculates the straight line distance between two projected coordinates.
    Assumes inputs are in the same unit (e.g., meters) and returns that unit.
    """
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate the hypotenuse using ** 0.5 for the square root
    distance = (dx**2 + dy**2) ** 0.5
    
    return distance

```

Be sure to save your `spatial_tools.py` file after making your changes. You have just created your first custom Python **{term}`module <Module>`**!

---

## 2. The working directory

To use the function you just saved, your new Jupyter notebook needs to know where to find the script file. Python looks for imported files in your current **{term}`working directory <Working directory>`**.

Hopefully you saved your `spatial_tools.py` file in the exact same folder as the new notebook you are currently working in. We can verify this running an [IPython](https://en.wikipedia.org/wiki/IPython) magic command called `%ls` in a code cell. The `%` symbol is a special built-in shortcut used to perform helpful tasks that are outside of standard Python code.

```{code-cell} python
%ls

```

The `%ls` command lists all the files located in the directory where you are currently working. If you see `spatial_tools.py` in the output list, you are all set to proceed.

```{admonition} Troubleshooting your directory
:class: caution
If you do not see your script file in the list, you have two options:
1. Use the JupyterLab file browser to move or copy `spatial_tools.py` into the same folder as your current notebook.
2. Use the `%cd` command (change directory) to navigate your notebook into the folder where the script is saved.

```

#### Concept Check: The Hidden Directory

Imagine your file browser looks like this:

```text
project_folder/
├── analysis.ipynb      <-- You are working here
└── scripts/
    └── my_code.py

```

If you run `%ls` in `analysis.ipynb`, will you see `my_code.py` in the output list, and will a standard `import my_code` work?

A) Yes, Python scans all subfolders automatically.

B) No, `%ls` only shows the current directory, and Python cannot automatically see inside the `scripts` subfolder.

C) Yes, but only if you use `import scripts.my_code`.

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
The `%ls` command lists files in the *current* directory (`project_folder`). It will show the `scripts/` folder, but not the contents *inside* it. Because Python cannot automatically see the `.py` file sitting inside the subfolder, a standard `import my_code` will fail. You would need to move `my_code.py` up into `project_folder`.

```

---

## 3. Importing script functions

Now that your notebook and your script are in the same folder, you can access your custom functions using an `import` statement.

:::{figure} images/03_import_directory_structure.png
:alt: A diagram showing a notebook and a python script sitting in the same folder, with an import arrow connecting them.
:width: 500px
:align: center

*Python looks for the imported script file in the same working directory as your active notebook.*
:::

Let us import our `euclidean_distance()` function from the script file:

```{code-cell} python
from spatial_tools import euclidean_distance

```

Now we can use the function to see that it is working. Let us calculate the distance between Zurich and Bern using their Swiss Grid (LV95) coordinates in meters:

```{code-cell} python
# Zurich: 2683000, 1248000 | Bern: 2600000, 1200000
dist_meters = euclidean_distance(2683000, 1248000, 2600000, 1200000)
dist_km = dist_meters / 1000

print(f"The straight line distance is {dist_km:.1f} km")

```

### Other ways to import

It is often useful to import the whole script and all of its functions at once. This can be done by importing the file and giving it a short alias.

```{code-cell} python
import spatial_tools as st

dist_meters = st.euclidean_distance(2683000, 1248000, 2600000, 1200000)

```

#### Concept Check: Dot Notation Mystery

Look at these two different ways to import the same function:

**Scenario A:**

```python
from spatial_tools import euclidean_distance

```

**Scenario B:**

```python
import spatial_tools as st

```

If you are using **Scenario B**, how must you correctly call the function in your notebook?

A) `euclidean_distance(...)`

B) `st.euclidean_distance(...)`

C) `spatial_tools.euclidean_distance(...)`

```{admonition} Check your understanding
:class: dropdown

**Answer: B**
In Scenario B, you imported the *entire module* as an object named `st`. Therefore, you must use "dot notation" to dive into that object and access the function inside it (`st.euclidean_distance(...)`). Scenario A brings the function directly into your notebook's **{term}`namespace <Namespace>`**, allowing you to use it without a prefix.

```

---

## 4. Building a modular tool

Let us add a slightly more complex tool to our script. We will create a wrapper function that accepts coordinate pairs grouped in lists, rather than forcing the user to type out four separate numbers.

Go back to your `spatial_tools.py` tab, leave two blank lines below your first function, and add the following code:

```{code-cell} python
def calculate_distance(pt1, pt2, method="euclidean"):
    """
    Wrapper function to calculate distance between two points.

    Parameters
    ----------
    pt1: <list>
        A list containing [x, y] coordinates
    pt2: <list>
        A list containing [x, y] coordinates
    method: <str>
        The calculation method. Supported values: 'euclidean'

    Returns
    -------
    <float>
        Computed distance.
    """
    if method == "euclidean":
        # Extract coordinates from the lists and pass to our dedicated function
        dist = euclidean_distance(pt1[0], pt1[1], pt2[0], pt2[1])
    else:
        print("Method not supported yet.")
        dist = None

    return dist

```

Save the file once more. Your custom module now contains two functions.

---

## 5. The notebook kernel trap

Now that we have updated our script, we want to test the new `calculate_distance` function in our notebook. However, when working in a Jupyter Notebook, reloading updated modules can be tricky.

To save memory, Python only imports a script **once** per session. If you change a script file and save it, simply running the `import` cell again will not load your new changes. Python thinks it already has the file and ignores the command entirely!

:::{figure} images/04_kernel_memory_trap.png
:alt: A diagram showing the disconnect between a saved file on a hard drive and the cached version in the Jupyter Kernel memory.
:width: 700px
:align: center

*When a script is first imported, it is loaded into the Kernel's active memory. Updating the text file on your hard drive does not update the memory until the Kernel is explicitly restarted.*
:::

1. Go to **Kernel > Restart kernel...** in the menu bar.
2. Wait a moment for the memory to clear.
3. Re-run your import cell.

```{admonition} Watch your memory
:class: warning
Restarting the kernel deletes all **{term}`variables <Variable>`** currently stored in memory. You will need to re-run any cells that defined your data before you can continue analyzing it.

```

After restarting the kernel, you can safely import your updated script and use your new tool:

```{code-cell} python
import spatial_tools as st

zurich = [2683000, 1248000]
bern = [2600000, 1200000]

distance_m = st.calculate_distance(zurich, bern, method="euclidean")
print(f"Distance: {distance_m / 1000:.1f} km")

```

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L05_ch01_01_kernel_memory/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: The Kernel Memory Trap.</b><br>
    Follow the sequence of buttons to observe how the Jupyter Kernel (active RAM) interacts with your Hard Drive. Notice how updating a file on your disk does not automatically push it into memory, and why restarting the kernel is the only way to load your changes. For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L05_ch01_01_kernel_memory/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

---

## 6. Exercises

To practice working with script files, complete the following tasks using your `spatial_tools.py` script.
Focus on **understanding the workflow** between your script and your notebook.

---

### Exercise 1: Add a Manhattan distance function

Open your `spatial_tools.py` file in the text editor.

1. Write a new function called `manhattan_distance(x1, y1, x2, y2)` that calculates the grid-based **{term}`Manhattan distance`** between two coordinates.
2. Remember from Lesson 2 that you can get the absolute (positive) difference by squaring it and taking the square root: `((x2 - x1)**2)**0.5`.
3. Save the file.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution (spatial_tools.py)
:class: dropdown

```{code-cell} python
def manhattan_distance(x1, y1, x2, y2):
    """Calculates the grid-based distance between two projected coordinates."""
    dx = ((x2 - x1)**2)**0.5
    dy = ((y2 - y1)**2)**0.5
    
    distance = dx + dy
    
    return distance
```

**Key idea:**
You are defining a new, isolated tool in your script. It takes the exact same four inputs as the Euclidean function, but applies a different mathematical logic.


``````

---

### Exercise 2: Update the wrapper function

Stay in your `spatial_tools.py` file.

1. Update your existing `calculate_distance` function to support the new method.
2. Add an `elif method == "manhattan":` block that extracts the coordinates from the `pt1` and `pt2` lists and passes them to your new `manhattan_distance` function.
3. Save the file again.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution (spatial_tools.py)
:class: dropdown

```{code-cell} python
def calculate_distance(pt1, pt2, method="euclidean"):
    """Wrapper function to calculate distance between two points."""
    
    if method == "euclidean":
        dist = euclidean_distance(pt1[0], pt1[1], pt2[0], pt2[1])
        
    elif method == "manhattan":
        dist = manhattan_distance(pt1[0], pt1[1], pt2[0], pt2[1])
        
    else:
        print("Method not supported yet.")
        dist = None
        
    return dist
```

**Key idea:**
The wrapper function acts as a single, user-friendly interface. It routes the user's request to the correct underlying mathematical function based on the `method` argument.


``````

---

### Exercise 3: Test your updates

Return to your Jupyter notebook.

1. **Restart the kernel** to clear the memory.
2. Import your updated module.
3. Test both the Euclidean and Manhattan functionality to see how much longer the grid-based path is compared to the straight-line path.

```{code-cell} python
# Write your code here

```

``````{admonition} Sample solution (Jupyter Notebook)
:class: dropdown

```{code-cell} python
import spatial_tools as st

zurich = [2683000, 1248000]
bern = [2600000, 1200000]

euclid_dist = st.calculate_distance(zurich, bern, method="euclidean")
manhat_dist = st.calculate_distance(zurich, bern, method="manhattan")

print(f"Euclidean path: {euclid_dist / 1000:.1f} km")
print(f"Manhattan path: {manhat_dist / 1000:.1f} km")
```

**Key idea:**
Restarting the kernel is crucial. It ensures Python loads the newest saved version of your `.py` script into memory instead of reusing the old one.


``````

---

## 7. Summary

In this section, you learned how to move your code out of the notebook sandbox and into reusable script files. You discovered how to:

* Create and save a `.py` file containing custom functions.
* Verify your working directory using `%ls`.
* Import specific functions or entire scripts into your notebook.
* Safely reload updated scripts by restarting the IPython kernel.

By writing modular tools in separate scripts, you keep your main notebooks clean, readable, and focused entirely on data analysis.

### What comes next?

You have now built and imported your own custom module. But you do not have to write every tool from scratch! In the next section, we will explore the **{term}`Python Standard Library <Standard library>`** and discover how to use the exact same `import` syntax to unlock powerful tools that are already built into Python.
