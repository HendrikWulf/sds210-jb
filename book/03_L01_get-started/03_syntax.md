---
title: Python syntax
site:
  outline_maxdepth: 1
---

<div class="page-subtitle">
How Python code is structured
</div>

---

```{admonition} Big idea
:class: tip
Python follows clear structural rules. Understanding syntax helps you write readable code and avoid errors.
```

---

Programming works only if the computer understands the structure of your code.  
This structure is called **syntax**.

Syntax defines:

- how code must be written  
- where spaces matter  
- how blocks of code are organised  

Even small syntax mistakes can prevent code from running. Clear syntax is not only about avoiding errors.
It also makes your code easier for others to read and reuse.

---

## 1. Identifiers and case

An **identifier** is a name used for:

- variables  
- functions  
- classes  

Example:

```python
x = 5
X = "Harry"

print(x)
print(X)
```

Python is **case sensitive**.

`x` and `X` are two different identifiers.

````{admonition} Concept check
:class: dropdown

What will this print?

```{code-cell} python
value = 10
Value = 20
print(value)
```

A) 10  
B) 20  
C) Error  

Think first, then try it.
````

---

## 2. Comments

Comments explain your code to humans.  
They are ignored by Python.

Comments start with `#`.

```{code-cell} python
# This is a comment
number = 5  # This comment is after code

print(number)
```

Good comments:

- explain *why* something is done  
- do not repeat obvious code  

---

## 3. Strings and quotes

Strings represent text.

Python allows:

- single quotes `'text'`  
- double quotes `"text"`  
- triple quotes `"""multi-line text"""`

The same quote type must start and end the string.

```{code-cell} python
a = 'Eier'
b = "Kuchen"
c = """This is
a multi-line
string"""

print(a, b)
print(c)
```

Triple quotes are useful for multi line text.

---

## 4. Statements and lines

Each line in Python normally represents one **statement**.

```{code-cell} python
x = 5
y = 12
```

You *can* write multiple statements on one line using `;`, but this reduces readability.

```{code-cell} python
x = 5; y = 12
print(x + y)
```

In this course, prefer one statement per line.

---

### Continuing long lines

Sometimes a statement is too long to fit comfortably on one line.

Inside brackets `()`, `[]`, or `{}`, Python automatically allows the statement to continue across multiple lines.

```{code-cell} python
week_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

print(week_days)
```

---

## 5. Indentation and blocks

Indentation is not just formatting in Python.  
It defines structure.

Blocks such as loops, conditions, and functions:

- end with a colon `:`  
- require indentation  

Example:

```{code-cell} python
for i in range(0, 10, 2):
    print(i)
```

If indentation is missing or inconsistent, Python raises an error.

```{admonition} Important
:class: important

Indentation defines logical structure in Python.

Consistent indentation is required.
```

---

### Nested indentation

Blocks can contain other blocks.

```{code-cell} python
def calculate_fee(x):
    if x < 100:
        fee = x * 0.05
    else:
        fee = x * 0.10
    return fee

print(calculate_fee(80))
```

```{admonition} Notice
:class: note

Each colon introduces a block.
Each block must be consistently indented.
```
 
---

## 6. Common beginner errors

If your code does not run, first check:

- missing colons  
- inconsistent indentation  
- mismatched quotes  
- misspelled variable names  

```{admonition} Handling syntax errors
:class: tip

If Python shows a syntax error, read the message carefully.  
It usually tells you where the problem starts.
```

---

## 7. Summary

In this section, you learned:

- identifiers are case sensitive  
- comments start with `#`  
- strings require matching quotes  
- each line is a statement  
- indentation defines structure  

Syntax may feel strict, but it enables clarity.  
Structure is what makes code readable, maintainable, and reproducible.  
Clear structure is essential for reproducible workflows.

---

### Looking ahead

In the next section, you will apply your syntax knowledge in a real notebook environment. You will:

- run cells interactively  
- observe how execution order matters  
- experience how notebooks store variables in memory  

Syntax tells Python what your code means.
Running notebooks shows you what it does.
