---
title: Strings & Basic Operations

site:
 outline_maxdepth: 1
---

<!-- markdownlint-disable MD033-->
<div class="page-subtitle">
Handling Text in Python
</div>
<!-- markdownlint-enable MD033 -->

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HendrikWulf/sds210-jb/blob/main/book/04_L02_variables/05_string-operations.ipynb)

```{admonition} Big idea
:class: tip

**{term}`Strings <String>`** represent text.  
They follow different rules than numbers and deserve special attention.

```

```{admonition} Chapter Relevance
:class: dropdown

**Lab Relevance:** ★☆☆ (Helpful context, but not strictly required for the numeric focus of the spatial distance tasks in the current lab.)  
**Project Relevance:** ★★☆ (Highly relevant for standardizing messy categorical text in project 1 or cleaning API metadata strings in project 2.)  
**Foundation:** ★★☆ (Core Python logic for file management, labels, and text wrangling.)  

**Time to Read:** 20 minutes  
**In a nutshell:** Strings represent text, requiring specific methods to cleanly slice, split, and standardize categories or file paths without breaking your mathematical engine.  
**Skip this if:** You already know how to safely concatenate strings, use escape characters (`\n`), and apply text-cleaning methods like `.split()`, `.strip()`, and `.replace()`.

```

So far, you have mainly worked with numeric values. In this chapter, we focus on text values, called strings.

Strings behave fundamentally differently from numbers. By isolating their special behaviour here, we avoid confusion later when data processing becomes more complex. After this chapter, you will be able to safely combine, clean, and prepare text for output.

---

## 1. What Is a String?

A string is a sequence of characters enclosed in quotation marks. Strings represent text values, not numbers. Even if they contain digits, Python treats them strictly as text.

```{code-cell} python
city = "Kampala"
elevation = "1190" # This is text, not a number!

```

Strings are commonly used in spatial data for:

* names (cities, countries)
* labels (chart titles)
* categories (land cover types)
* identifiers (station IDs)

### Creating Strings

Strings can be created using **single quotes** or **double quotes**. Both forms are valid and behave exactly the same way in Python.

```{code-cell} python
country1 = 'Uganda'
country2 = "Uganda"

```

The choice usually depends on readability or whether the text itself contains quotation marks (which we will cover below).

For longer text that spans multiple lines, Python also allows **triple quotes** using either three single quotes (`'''`) or three double quotes (`"""`). Triple-quoted strings preserve line breaks and are useful for multi-line text, longer labels, or documentation-style strings.

```{code-cell} python
description = """Kampala is the capital city of Uganda.
It is located near Lake Victoria.
The city is an important political and economic centre."""

print(description)

```

Single, double, and triple quotes all create strings. The main difference is that triple quotes make it easier to write strings across several lines.

---

## 2. String Concatenation (`+`)

Strings can be combined using the **plus operator** `+`. This operation is called **concatenation**. It creates a new string by joining the text parts together end-to-end.

```{code-cell} python
city = "Kampala"
country = "Uganda"

# Notice we have to manually add the comma and space!
location = city + ", " + country
print(location)


```

Concatenation is heavily used to build labels, file paths, or formatted output from smaller pieces of text.

### Strings vs Numbers

The `+` operator does **not** mean the same thing for all data types.

```{code-cell} python
# Math: Adds numbers
print(2 + 3)      # Output: 5

# Concatenation: Joins text
print("2" + "3")  # Output: 23


```

The symbol is the same, but the **behaviour depends entirely on the data type**.

---

## 3. String Repetition (`*`)

Strings can be repeated using the **multiplication operator** `*`.

```{code-cell} python
print("-" * 20)
print("Data Summary")
print("-" * 20)


```

This creates a new string where the original text is repeated exactly that many times. It is often used for creating visual separators in printed output or making headings more readable in your notebook.

```{admonition} String Repetition Requires an Integer
:class: note

Repetition only works when multiplying a **string by an integer**. Multiplying two strings together (`"A" * "B"`) or multiplying by a decimal (`"A" * 2.5`) is mathematically undefined and will raise an error.

```

### Checking String Length with `len()`

Because strings are sequences of characters, Python can count how many characters a string contains. For this, we use the built-in `len()` function.

```{code-cell} python
location_name = "Mont Blanc"

location_length = len(location_name)

print("The location name '" + location_name + "' has " + str(location_length) + " characters.")

```

The length includes all characters inside the string, including spaces.

```{code-cell} python
short_name = "Goa"
long_name = "Saint-Tropez"

print(short_name + ": " + str(len(short_name)) + " characters")
print(long_name + ": " + str(len(long_name)) + " characters")

```

String length is useful when checking names, labels, identifiers, or other text values from a dataset. It does not change the string; it only returns information about it.

---

## 4. Mixing Strings and Numbers

Strings and numbers are **not automatically compatible** in Python. If you try to concatenate them directly, Python raises a `TypeError`.

```{code-cell} python
# This will raise a TypeError!
"Distance: " + 10


```

Python refuses to guess whether you want to do math or join text.

### Explicit Conversion with `str()`

To combine strings and numbers safely, you must explicitly convert the number into a string first using the `str()` function.

```{code-cell} python
distance = 10
message = "Distance: " + str(distance) + " km"
print(message)


```

This forces you to be explicit about how values should be represented as text, preventing subtle errors in your data pipelines.

---

## 5. Escape Characters

Sometimes you need to include special characters inside your strings, like quotation marks or new lines.

For example, if you use single quotes to define a string that contains an apostrophe, Python gets confused about where the string actually ends:

```{code-cell} python
# ERROR: Python thinks the string ends after "It"
weather = 'It's cold today' 


```

### Escaping Characters (`\`)

You can "escape" the special meaning of a character by placing a **backslash** `\` in front of it.

```{code-cell} python
weather = 'It\'s cold today'


```

The backslash tells Python: *"Treat the very next character as ordinary text, not as code."*

### Common Escape Characters

Escape characters are often used to control layout when printing text:

* `\'` : Single quote
* `\"` : Double quote
* `\n` : New line (drops the text down one line)
* `\t` : Tab (indents the text)

```{code-cell} python
print("Coordinates:\n\tLat: 0.34\n\tLon: 32.58")


```

---

## 6. Basic String Cleaning

Raw text data is rarely perfectly formatted. Place names, file paths, coordinates, and labels often contain inconsistent capitalization, unwanted spaces, or pieces of information that need to be separated.

Before analyzing text, it helps to know a few common **{term}`string methods <Method>`**. String methods allow you to clean, standardize, split, and recombine text.

---

### Changing Letter Case

Geographic names may come from different sources and may not always use the same capitalization. Python provides several methods to standardize letter case:

* `.upper()` converts all letters to uppercase
* `.lower()` converts all letters to lowercase
* `.title()` capitalizes the first letter of each word
* `.capitalize()` capitalizes only the first letter of the whole string

```{code-cell} python
mountain_name = "mont blanc"

print("Original: " + mountain_name)
print("Uppercase: " + mountain_name.upper())
print("Lowercase: " + mountain_name.lower())
print("Title case: " + mountain_name.title())
print("Capitalize: " + mountain_name.capitalize())

```

This is useful when comparing place names. For example, `"maputo"`, `"Maputo"`, and `"MAPUTO"` look different to Python, even though they refer to the same city.

---

### Removing Extra Spaces with `.strip()`

Often, text imported from files or user input contains unwanted, invisible spaces at the beginning or end. These spaces can cause problems when comparing or combining strings.

The `.strip()` method removes spaces from both sides of a string.

```{code-cell} python
raw_name = "   Mont Blanc    "
clean_name = raw_name.strip()

print("Original: '" + raw_name + "'")
print("Cleaned: '" + clean_name + "'")

```

There are also two more specific methods:

* `.lstrip()` removes spaces from the left side
* `.rstrip()` removes spaces from the right side

```{code-cell} python
messy_left = "   Saint-Tropez"
messy_right = "Zurich   "

print("Left cleaned: '" + messy_left.lstrip() + "'")
print("Right cleaned: '" + messy_right.rstrip() + "'")

```

---

### Replacing Text with `.replace()`

The `.replace()` method substitutes one part of a string with another. This is useful for correcting values, updating labels, or simplifying file paths.

```{code-cell} python
location = "Mont Blanc, France"
updated_location = location.replace("France", "France/Italy")

print("Original: " + location)
print("Updated: " + updated_location)

```

You can also replace repeated text in longer strings.

```{code-cell} python
path_string = "data/raw_data/geographic_data/raw_data/points.csv"
clean_path = path_string.replace("raw_data/", "")

print("Original path: " + path_string)
print("Clean path: " + clean_path)

```

Most string methods do not change the original string. Instead, they return a new string that you can store in another **{term}`variable <Variable>`**.

---

### Splitting Strings with `.split()`

The `.split()` method breaks a single string into parts based on a separator character, such as a comma, colon, space, or slash. It returns a **{term}`list <List>`** of strings.

:::{figure} images/08_string-operation-split.png
:alt: *The `split()` method breaks a single string into a list of multiple strings based on a specific separator character.*
:width: 700px
:align: center

*The `split()` method breaks a single string into a list of multiple strings based on a specific separator character.*
:::

Lists store multiple values in a specific order. You can access individual items in that list using their position, **starting at zero**. This is called **{term}`indexing <Index>`**.

```{code-cell} python
text = "Kampala,Uganda"

# Split the text at the comma
parts = text.split(",")

print(parts[0]) # The first item (Index 0)
print(parts[1]) # The second item (Index 1)

```

You will learn much more about lists later. For now, it is enough to know that `.split()` chops up text, and indexing (`[0]`, `[1]`) lets you grab the specific pieces you need.

Splitting is also useful for structured geographic information.

```{code-cell} python
location_full = "Mont Blanc,France,Europe"

location_parts = location_full.split(",")

print("Mountain: " + location_parts[0])
print("Country: " + location_parts[1])
print("Continent: " + location_parts[2])

```

You can also split coordinate strings before converting the values to numbers.

```{code-cell} python
coordinate_string = "46.8523,6.8652"

lat_str, lon_str = coordinate_string.split(",")

latitude = float(lat_str)
longitude = float(lon_str)

print("Latitude: " + str(latitude))
print("Longitude: " + str(longitude))

```

A similar idea works for file paths.

```{code-cell} python
file_path = "data/geographic/cities/european_cities.csv"

path_components = file_path.split("/")

print("Path components:")
print(path_components)

print("Filename: " + path_components[-1])

```

---

### Joining Strings with `.join()`

The `.join()` method does the reverse of `.split()`: it combines several strings into one string.

The separator is written first, followed by `.join()`.

```{code-cell} python
city_names = ["Saint-Tropez", "Bettyhill", "Kharkiv"]

city_list = ", ".join(city_names)

print(city_list)

```

This is useful when you want to create readable output from a list of text values.

You can also use `.join()` to build simple file paths from separate parts.

```{code-cell} python
path_parts = ["data", "geographic", "elevation", "dem.tif"]

full_path = "/".join(path_parts)

print(full_path)

```

Or to turn coordinate values stored as strings into one coordinate string.

```{code-cell} python
coordinates = ["46.8523", "6.8652"]

coordinate_string = ",".join(coordinates)

print(coordinate_string)

```

<!-- markdownlint-disable MD033-->
<iframe
    src="https://hendrikwulf.github.io/sds210_assets_L02_ch05_01_string_methods_visualizer/"
    width="100%"
    height="600px"
    frameborder="0"
    style="border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); background-color: #f8fafc; margin-bottom: 15px;">
</iframe>

<figcaption>
    <em><b>Interactive Explorer: String Methods Visualizer.</b><br>
    Click the different method buttons to see exactly how Python manipulates the messy string <code>"   Kampala, Uganda   "</code>. Pay close attention to how <code>.strip()</code> removes exterior spaces without affecting the inside, and how <code>.split(",")</code> breaks the text into a list while keeping the surrounding spaces intact! For improved visibility of the explorer, follow this <a href="https://hendrikwulf.github.io/sds210_assets_L02_ch05_01_string_methods_visualizer/" target="_blank">link</a>.</em>
</figcaption>
<!-- markdownlint-enable MD033 -->

#### Concept Check: Chaining String Methods

You are cleaning a messy dataset of European capitals and find a heavily formatted string representing the city of Paris:

`raw_entry = "   ---Paris---   "`

You want to extract just the clean word `"Paris"`. Which sequence of string methods will successfully produce this result?

A) `raw_entry.strip().replace("-", "")`

B) `raw_entry.split("-")`

C) `raw_entry.lower().strip()`

```{admonition} Check your understanding
:class: dropdown

**Answer: A**
First, `.strip()` removes the outside spaces, leaving the intermediate string `"---Paris---"`. Then, `.replace("-", "")` finds all the remaining dashes and replaces them with empty text, leaving the perfectly clean string `"Paris"`. Option B would create a list of empty strings and `"Paris"`, while Option C would only change the case and remove spaces but leave the dashes intact.

```

---

## 7. Short Exercise

Look at the following raw data record:

```{code-cell} python
record = "Species:  African fish eagle , Country:  Uganda "

```

The record contains useful information, but it is not yet clean:

* the species and country are stored in one long string
* the values contain extra spaces
* the species name is not consistently capitalized

**Task:**

1. Split the `record` string at the comma so that you can work with the two halves separately.
2. Extract the actual species name (`"African fish eagle"`) and the country name (`"Uganda"`).
*Hint: You will need to use `.split()` again on the halves!*
3. Clean both extracted values using `.strip()` so there are no extra spaces.
4. Standardize the species and country names using `.title()`.
5. Combine the cleaned values into **one readable string** using concatenation.
6. Print the length of the final cleaned string using `len()`.

If your solution is correct, your final string should look exactly like this:

`"Species: African Fish Eagle, Country: Uganda"`

````{admonition} Sample solution (click to expand)
:class: dropdown

```{code-cell} python
# 1. Split the record into two halves using the comma
parts = record.split(",")

# 2 & 3. Extract and clean the species
species_half = parts[0]                         # "Species:  African fish eagle "
species_name = species_half.split(":")[1]       # "  African fish eagle "
clean_species = species_name.strip()            # "African fish eagle"

# 2 & 3. Extract and clean the country
country_half = parts[1]                         # " Country:  Uganda "
country_name = country_half.split(":")[1]       # "  Uganda "
clean_country = country_name.strip()            # "Uganda"

# 4. Standardize the species and country names
clean_species = clean_species.title()           # "African Fish Eagle"
clean_country = clean_country.title()           # "Uganda"

# 5. Combine into a readable result
summary = "Species: " + clean_species + ", Country: " + clean_country

print(summary)

# 6. Print the length of the final cleaned string
summary_length = len(summary)

print("The final cleaned string has " + str(summary_length) + " characters.")
```


````

---

## 8. Summary

After completing this chapter, you should understand that:

* **Strings represent text values** and are written using single, double, or triple quotation marks.
* The `+` operator **concatenates** strings, while the `*` operator **repeats** strings.
* `len()` returns the number of characters in a string.
* Strings and numbers do not mix automatically; use `str()` to convert numbers to text.
* **Escape characters** such as `\n` and `\t` control how text is interpreted and displayed.
* Common string methods such as `.strip()`, `.replace()`, `.split()`, and `.join()` help clean, structure, and recombine text data.

---

### Looking Ahead

Next, you will learn how to **display results clearly**.

In the upcoming chapter on *Printing and Formatting Output*, we focus on:

* advanced ways to print values to the screen
* using modern f-strings to inject variables directly into text
* formatting numbers (like rounding decimals) directly inside your print statements
