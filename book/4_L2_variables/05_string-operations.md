---
title: Strings & Basic Operations

site:
 outline_maxdepth: 1
---

<div class="page-subtitle">
Handling Text in Python
</div>

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/4_L2_variables/05_string-operations.ipynb)

```{admonition} Big idea
:class: tip

Strings represent text.  
They follow different rules than numbers and deserve special attention.
```

So far, you have mainly worked with numeric values.  
In this section, we focus on text values, called strings.

Strings behave differently from numbers.
By isolating their special behaviour here, we avoid confusion later when numeric reasoning becomes more complex.
After this section, you will be able to safely combine, clean, and prepare text for output.

---

## 1. What Is a String?

A **string** is a sequence of characters enclosed in quotation marks.

Strings represent **text values**, not numbers.  
Even if they contain digits, Python treats them as text.

```python
city = "Kampala"
```

Strings are commonly used for:

* names
* labels
* categories
* identifiers
* text output

Although strings may look simple, they follow **different rules than numbers**.
Understanding this difference early helps avoid confusion later.

---

### Creating Strings

Strings can be created using **single quotes** or **double quotes**.

```python
country = 'Uganda'
```

Both forms are valid and behave the same way in Python.
The choice usually depends on readability or whether the text itself contains quotation marks.

At this stage, the important point is simple:

> Text values are stored as strings, and Python treats them differently from numeric values.

---

## 2. String Concatenation

Strings can be combined using the **plus operator** `+`.

```python
city = "Kampala"
country = "Uganda"

city + ", " + country
```

This operation is called **concatenation**.
It creates a new string by joining the text parts together.

Concatenation is often used to build labels, messages, or formatted output from smaller pieces of text.

---

### Strings vs Numbers

The `+` operator does **not** mean the same thing for all data types.

```python
2 + 3
```

```python
"2" + "3"
```

In the first case, Python performs arithmetic.
In the second case, Python joins text.

The symbol is the same, but the **behaviour depends on the data type**.

```{admonition} Note
:class: note

Operators are defined by data type.  
When something behaves unexpectedly, first check whether you are working with strings or numbers.
```

---

## 3. String Repetition

Strings can be repeated using the **multiplication operator** `*`.

```python
"-" * 10
```

This creates a new string where the original text is repeated several times.

String repetition is often used for:

* visual separators in printed output
* simple formatting in the terminal or notebook
* making headings or dividers more readable

---

### What Works and What Does Not

However, repetition only works with **string multiplied by an integer**  
(or an integer multiplied with a string)

For example:

```python
"climate" * 3
3 * "biodiversity"
```

Other combinations are not defined and will raise an error.  
For instance, multiplying two strings or using a decimal number does not work.

The rule is simple: Python needs to know **how many times** the string should be repeated.

## 4. Mixing Strings and Numbers

Strings and numbers are **not automatically compatible** in Python.

For example, try the following expression:

```python
"Distance: " + 10
```

Python raises a `TypeError` because it does not know how to add text and a number directly.

---

### Explicit Conversion

To combine strings and numbers, you must convert the number into a string first.

```python
"Distance: " + str(10)
```

Here, `str(10)` turns the number into text so that both parts are compatible.

---

### Why This Is Intentional

This conversion step is deliberate.

It forces you to be explicit about:

* what kind of value you are working with
* how values should be represented as text
* whether a value is used for calculation or for display

Being explicit helps prevent subtle errors and keeps your code easier to read and debug.

---

## 5. Escape Characters

Some characters have a **special meaning** in strings.

For example, quotation marks define where a string starts and ends.  
This causes a problem:

```python
"It's cold today"
```

Python cannot tell where the string ends.

---

### Escaping Characters

You can escape special characters using a **backslash** `\`.

```python
"It\'s cold today"
```

The backslash tells Python to treat the next character as ordinary text.

Common escape characters include:

* `\n` new line
* `\t` tab
* `\'` single quote
* `\"` double quote

---

### New Lines in Strings

Escape characters are often used to control layout when printing text.

```python
print("Line one\nLine two")
```

This prints the text on two separate lines.

---

```{admonition} Note
:class: note

Escape characters are instructions inside a string.  
They change how the text is interpreted, not which characters it contains.
```

Escape characters are especially useful when formatting output or working with text files.

---

## 6. Basic String Cleaning

Before working with more complex text, it helps to know two simple and very common string methods.

---

### Splitting Strings with `split()`

The `split()` method breaks a string into parts based on a separator. It returns a **list of strings**.  
Lists store multiple values in order.
You can access individual items using their position, starting at zero. This is called **indexing**.

```python
text = "Kampala,Uganda"
parts = text.split(",")
parts[0]
parts[1]
```

Here:

* index 0 refers to the first item
* index 1 refers to the second item

You will learn more about *lists* later.
For now, it is enough to know that *indexing* lets you pick specific parts.

Splitting is useful when text follows a known structure, such as values separated by commas or spaces.

---

### Removing Extra Spaces with `strip()`

Sometimes text contains unwanted spaces at the beginning or end.

```python
raw_name = " African fish eagle    "
clean_name = raw_name.strip()
clean_name
```

The `strip()` method removes leading and trailing whitespace.

This is especially helpful when working with text from files, sensors, or user input.

---

```{admonition} Note
:class: note

`split()` separates text into parts.  
`strip()` cleans up extra spaces.

These two methods already cover a large share of everyday text cleaning tasks.
```

---

## 7. Short Exercise

1. Split the string so that you can work with the two parts separately.
2. Extract:

   * the species name
   * the country name
3. Clean both values so that there are no extra spaces
4. Combine the cleaned values into **one readable string**, for example:

```text
"Species:  African fish eagle , Country:  Uganda "
```

You do **not** need to print the result yet.
Focus on creating clear intermediate variables.

If your solution is correct, the final string should read exactly:  
Species: African fish eagle, Country: Uganda

---

````{admonition} Sample solution (click to compare with your results)
:class: dropdown

```{code-cell} python
# original record
record = "Species:  African fish eagle , Country:  Uganda "

# split the record into field-level parts using the comma
parts = record.split(",")

# extract the species value and remove extra spaces
species_part = parts[0]
species = species_part.split(":")[1].strip()

# extract and clean country
country_part = parts[1]
country = country_part.split(":")[1].strip()

# combine into a readable result
summary = "Species: " + species + ", Country: " + country

summary
```

**Explanation**

* `split(",")` separates the two fields
* `split(":")` separates labels from values
* `strip()` removes extra spaces
* `capitalize()` improves readability
* string concatenation combines everything into one result

````

---

## 8. Summary

After completing this section, you should understand that:

* strings represent text values
* strings are written using quotation marks
* the `+` operator concatenates strings
* the `*` operator repeats strings
* strings and numbers do not mix automatically
* escape characters control how text is interpreted and displayed
* `split()` and `strip()` help clean and structure text
* string operations are often used to prepare data for printing, files, or analysis

These ideas explain why strings behave differently from numbers and why they deserve special attention.

---

### Looking Ahead

Next, you will learn how to **display results clearly**.

In the section on *Printing and Formatting Output*, we focus on:

* printing values to the screen
* combining text and results cleanly
* formatting output for readability

This builds directly on string operations by focusing on how results are shown.
