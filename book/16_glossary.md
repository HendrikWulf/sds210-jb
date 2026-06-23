# Glossary

:::{glossary}

[Absolute path](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths)
: A file path that specifies the exact location of a file or directory starting from the root of the file system. In reproducible workflows, these should be avoided because they will break when code is run on a different computer.

[Abstraction](https://en.wikipedia.org/wiki/Abstraction_(computer_science))
: The process of hiding the complex, underlying implementation details of a process and exposing only the essential features. Functions provide abstraction by allowing users to execute complex logic using a simple name without needing to understand the internal code.

Accessor
: In Python libraries, an *accessor* is a way to attach specialized functionality to an existing data structure without changing its core implementation.  
  For example, libraries such as `xarray` add accessors to objects like a `Dataset` to provide domain-specific {term}`methods <Method>` and properties.

[Alias](https://en.wikipedia.org/wiki/Aliasing_(computing))
: A technique used during import statements to give a module or function a shorter or alternative name in the local namespace. In Python, this is typically done using the `as` keyword, such as `import pandas as pd`.

Anomaly
: A departure or deviation from a reference baseline of what is considered "normal" (a climatology). It is typically calculated by subtracting the baseline average from the observed data. Also known as `Climate anomaly`.

[API](https://en.wikipedia.org/wiki/API)
: See {term}`Application Programming Interface`.

[Application Programming Interface](https://en.wikipedia.org/wiki/API)
: An *application programming interface* (API) is a defined set of rules and tools that allow different pieces of {term}`software` to communicate and exchange information.  
  For example, the Nominatim service provides an API for accessing its geocoding functionality.

Argument
: A value passed to a {term}`function` when it is called.  
  Compare with a {term}`Parameter`, which refers to the variable name used in the function definition.

[Array](https://en.wikipedia.org/wiki/Array_data_structure)
: A data structure consisting of a grid of values, typically of the same data type. In Python, NumPy arrays are the standard for fast, large-scale numeric computations.

[Aspect](https://en.wikipedia.org/wiki/Aspect_(geography))
: Aspect describes the compass direction that a {term}`slope` faces and is derived from elevation data.  
  It is usually measured in degrees from 0° (north) to 360°.

[Assertion](https://en.wikipedia.org/wiki/Assertion_(software_development))
: A statement used in a Python program to check whether a condition evaluates to `True` when the code is executed.  
  If the condition is not `True`, an `AssertionError` is raised. Assertions are commonly used for debugging and testing code.

[Assignment operator](https://en.wikipedia.org/wiki/Assignment_(computer_science))
: A symbol used to store the result of an expression in a variable. In Python, the standard assignment operator is `=`.

[Attribute](https://en.wikipedia.org/wiki/Attribute_(computing))
: A value or variable that is associated with an instance of a specific data type or {term}`Class`.  
  Attributes represent static characteristics or properties of an object and are accessed using dot notation without parentheses.

Axes (Matplotlib)
: In the Matplotlib library, the Axes is the actual plotting area or chart that contains the data, axis lines, ticks, and labels. A single Figure can contain multiple Axes.

[Bar chart](https://en.wikipedia.org/wiki/Bar_chart)
: A type of chart that is best used for comparing discrete categories or groups.

[Basemap](https://en.wikipedia.org/wiki/Base_map)
: A background geographic map providing spatial context to analytical data layers overlaid on top of it.

[Boolean](https://en.wikipedia.org/wiki/Boolean_data_type)
: A primitive data type representing logical values. In Python, booleans can only be exactly one of two values: `True` or `False`.

Boolean indexing
: A technique used in Pandas to ask a dataset a True or False question simultaneously, creating a mask that filters rows based on logical conditions. Only rows that evaluate to `True` are kept.

[Box plot](https://en.wikipedia.org/wiki/Box_plot)
: A type of chart that is best used for showing statistical summaries, such as the median, quartiles, and outliers, of data distributions.

[Broadcasting](https://en.wikipedia.org/wiki/Array_broadcasting)
: A powerful feature in array programming (such as with NumPy) that automatically aligns arrays of different shapes during arithmetic operations, allowing mathematical operations to be applied to entire arrays without the need for manual loops.

[Built-in function](https://en.wikipedia.org/wiki/Subroutine#Built-in_functions)
: A function that is always available in standard Python without needing to import any modules. Examples include `print()`, `len()`, and `type()`.

[Camel case](https://en.wikipedia.org/wiki/Camel_case)
: A variable naming convention in which words are joined without spaces, with each new word starting with a capital letter (except the first).  
  Example: `gpsStationId`.  
  Compare with {term}`Snake case`.

Cartopy
: A Python library used to accurately project raw data matrices onto recognizable Earth cartography.

[Case sensitive](https://en.wikipedia.org/wiki/Case_sensitivity)
: A property of a programming language where uppercase and lowercase letters are treated as distinct.  
  For example, `x` and `X` refer to different {term}`Identifiers <Identifier>` in Python.  

[Choropleth map](https://en.wikipedia.org/wiki/Choropleth_map)
: A thematic map where geographic areas (polygons) are shaded, colored, or patterned in relation to a statistical data variable.

[Class](https://en.wikipedia.org/wiki/Class_(programming))
: A reusable template for creating {term}`objects <Object>` that share common properties and behavior.  
  For example, a class representing a geospatial point may store coordinates and provide methods such as distance calculations.

[Class attribute](https://en.wikipedia.org/wiki/Class_variable)
: A variable that is defined in the class blueprint and shared universally across all instances (objects) of that class.

[Climatology](https://en.wikipedia.org/wiki/Climatology)
: A reference baseline that establishes what environmental or climatic conditions are considered "normal" for a given period.

Code cell
: A cell in a Jupyter notebook that contains executable code.  
  When run, the code is sent to the {term}`Kernel` and the output is displayed directly below the cell.

[Collection](https://en.wikipedia.org/wiki/Collection_(abstract_data_type))
: A container that stores multiple values together.  
  Built-in Python collection types include {term}`List`, {term}`Dictionary`, {term}`Set`, and {term}`Tuple`.

[Colormap](https://en.wikipedia.org/wiki/Color_mapping)
: A palette used to map data values to distinct colors in a visualization. Types include Sequential (for continuous data progressing from low to high), Diverging (for highlighting deviations from a critical midpoint), and Qualitative (for distinct, unordered categories).

[Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values) 
: A text file format where values are separated by commas or semicolons. It is commonly used by government portals and scientific institutions to provide open data directly as text files. Abbreviation: `CSV`

[Comment](https://en.wikipedia.org/wiki/Comment_(computer_programming))
: A line or part of a line in code that is ignored by the interpreter and used to explain the code to humans.  
  In Python, comments start with `#`.

Commit message
: A clear, descriptive text explanation attached to a `Git` commit that documents exactly what changes were made (e.g., `"Filter wildfire dataset to remove NaN coordinates"`). These messages create a transparent history of a project, making it easy to track the development process and pinpoint when bugs were introduced.

[Computational thinking](https://en.wikipedia.org/wiki/Computational_thinking)
: A set of problem-solving methods that involve expressing spatial questions and their solutions in structured workflows that a computer can execute.

[Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
: The act of writing instructions in a programming language so that a computer can execute them.  
  Coding focuses on translating ideas into syntactically correct code, while programming also includes planning and problem-solving.

[Concatenation](https://en.wikipedia.org/wiki/Concatenation)
: The operation of joining text parts together end-to-end to create a new string. In Python, this is done using the plus operator (`+`).

[Conda](https://en.wikipedia.org/wiki/Conda_(package_manager))
: An open-source package and environment management system. It is heavily used in spatial data science because it reliably handles complex, non-Python dependencies (like C++ libraries) required by geospatial tools.

[Container](https://en.wikipedia.org/wiki/OS-level_virtualization)
: A lightweight, self-contained virtual environment that packages an operating system, Python, and all required libraries together. This ensures that the environment behaves exactly the same on any computer, preventing issues caused by system differences. Also reffered to as `Docker container`

Contextily
: A lightweight Python package designed to retrieve map tiles from the internet and seamlessly add them to Matplotlib figures as static background images.

[Continuous field](https://en.wikipedia.org/wiki/Continuous_field)
: A conceptual view of geographic space that assumes a specific variable can be measured at any given coordinate on Earth. Examples include elevation, air pressure, and soil moisture.

[Control flow](https://en.wikipedia.org/wiki/Control_flow)
: The order in which individual statements, instructions, or function calls are executed or evaluated in a software program. In Python, control flow is managed by conditional statements (like `if`) and loops (like `for` and `while`).

[Control variable](https://en.wikipedia.org/wiki/Control_variable_(programming))
: A variable used to govern the execution flow of a loop. In a `while` loop, this variable is updated inside the loop body to ensure the loop eventually terminates.

[Coordinate Reference System](https://en.wikipedia.org/wiki/Spatial_reference_system)
: A coordinate reference system (CRS) describes how coordinates or geometries relate to real locations on Earth.  
  It defines the coordinate system, projection, and mathematical model needed to locate positions accurately and exchange geographic data between systems.

Coordinate transformation
: See {term}`Map reprojection`.

[Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
: A metric that measures the angle between two vectors (or spectral signatures) rather than their magnitude. It evaluates the shape of the spectrum and is highly robust against overall brightness changes, such as shadows or illumination differences.

Cyclic colormap
: A type of color palette where the lightness of two different colors meets in the middle and wraps around at the beginning and end at an unsaturated color. It is best used for values that wrap around at the endpoints, such as phase angle, wind direction, or time of day.

[Data cube](https://en.wikipedia.org/wiki/Data_cube)
: A multidimensional matrix paired with explicit spatial and temporal labels that can be explored across space, time, bands, and variables. It conceptually transforms a static 2D raster into a dynamic, multidimensional structure.

[Data model](https://en.wikipedia.org/wiki/Data_model)
: A conceptual model that describes how data are structured, organized, and related to real-world entities.  
  Common examples include the vector data model (points, lines, polygons) and the raster data model (grids of cell values).

[Data type](https://en.wikipedia.org/wiki/Data_type)
: A classification that defines what kind of values a variable can store.  
  Common data types include Boolean, integer, float, string, and date/time types.

DataArray
: In `xarray`, a core data structure that holds a single variable and its accompanying dimension labels, functioning similarly to a `pandas.Series`.

[DataFrame](https://en.wikipedia.org/wiki/Data_frame)
: In the pandas library, a DataFrame is a two-dimensional, tabular data structure with labeled rows and columns.  
  It supports data manipulation tasks such as filtering, aggregation, and merging and is a core structure for data analysis in Python.

Dataset (xarray)
: In `xarray`, a container that stores multiple perfectly aligned `DataArray` variables sharing the same coordinates, acting similarly to a `geopandas.GeoDataFrame`.

DatetimeIndex
: An immutable array of datetime values used as the index of a pandas {term}`DataFrame`.  
  It enables indexing, grouping, and analysis based on time.

[Debugging](https://en.wikipedia.org/wiki/Debugging)
: The practical process of reading, interpreting, and resolving errors, bugs, or unexpected results within a computer program.

[Decimal degrees](https://en.wikipedia.org/wiki/Decimal_degrees)
: A method for expressing latitude and longitude as decimal values rather than degrees, minutes, and seconds.  
  Decimal degrees simplify calculations involving geographic coordinates.

Default parameter
: See {term}`Optional parameter`.

[Defensive programming](https://en.wikipedia.org/wiki/Defensive_programming)
: Also referred to as defensive coding. An approach to writing code that anticipates mistakes, explicitly checks assumptions, and fails clearly and early when something is wrong (e.g., verifying spatial compatibility before processing).

Dependency
: A software package that another package relies on in order to function correctly.  
  Dependencies typically need to be installed alongside the main package.

Detour factor
: A metric calculated by dividing the actual driving distance by the geodesic baseline distance. A detour factor of 1.0 indicates a perfectly straight road, while a factor of 1.5 indicates you must drive 50% further than the straight-line distance.

[Dictionary](https://en.wikipedia.org/wiki/Associative_array)
: A built-in Python data structure that stores key–value pairs.  
  Keys are used to access associated values, and dictionaries are enclosed in curly braces (`{}`).

[Digital elevation model](https://en.wikipedia.org/wiki/Digital_elevation_model) 
: A single-band raster representing a continuous surface of topographic elevation measurements. Abbreviation: `DEM`

[Diurnal cycle](https://en.wikipedia.org/wiki/Diurnal_cycle)
: The natural fluctuation of an environmental variable, such as temperature, between day and night.

[Docker](https://en.wikipedia.org/wiki/Docker_(software))
: A platform used to package entire working environments into standardized containers. It is especially powerful for reproducibility, teaching, and collaborative geospatial work.

[Docstring](https://en.wikipedia.org/wiki/Docstring)
: A text string used to document Python code, commonly {term}`functions <Function>` or classes.  
  Docstrings describe purpose, parameters, and outputs and can be accessed using Python’s `help()` function.

Dot notation
: The syntax used in Python to access an object's attributes and methods. It is written by placing a dot (`.`) between the object or module name and the specific attribute or function being called, such as `math.sqrt()`.

[Dot product](https://en.wikipedia.org/wiki/Dot_product)
: An algebraic operation that takes two equal-length sequences of numbers and returns a single number. When dealing with normalized unit vectors, the dot product is mathematically identical to Cosine Similarity.

Dunder method
: Short for "double underscore" method (also known as magic methods). These are special built-in methods in Python that start and end with double underscores, such as `__str__` or `__gt__`. They allow custom objects to deeply integrate with standard Python syntax, enabling the natural use of functions like `print()` or math operators.

[Dynamic typing](https://en.wikipedia.org/wiki/Dynamic_typing)
: A property of a programming language where variable types are determined at runtime rather than explicitly declared.  
  Python is dynamically typed, allowing flexible and rapid code development.

Element-wise operation
: A mathematical operation performed simultaneously across entire arrays or columns by matching rows based on their index, rather than looping through individual items.

[Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
: One of the core pillars of object-oriented programming. It refers to the practice of bundling internal state (attributes) and logic (methods) together into a single, secure entity (an object) to protect and isolate the data.

[Enhanced Vegetation Index](https://en.wikipedia.org/wiki/Enhanced_vegetation_index) 
: A derived environmental index used to monitor biomass and canopy structure. It mathematically combines Near Infrared, Red, and Blue light bands to correct for atmospheric conditions and canopy background noise. Abbreviation: `EVI`

[Equal Earth](https://en.wikipedia.org/wiki/Equal_Earth_projection)
: An equal-area map projection designed for global maps.  
  It preserves the relative size of areas, making it useful for comparing spatial patterns across continents and countries, while still providing a visually balanced representation of the world.

[EPSG code](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset)
: An EPSG code is a numeric identifier that uniquely defines a {term}`Coordinate Reference System` (CRS) or a spatial data transformation.  
  Examples include EPSG:4326 for WGS84 and EPSG:3857 for Web Mercator, which simplify referencing CRSs in geographic data processing.

[Escape character](https://en.wikipedia.org/wiki/Escape_character)
: A special character, such as a backslash (`\`), used inside a string to tell Python to treat the next character as ordinary text rather than code. They are also used to control layout, such as `\n` for a new line.

[Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
: The straight-line distance between two points. It is calculated using the Pythagorean theorem.

Execution order
: The sequence in which notebook cells are run.  
  In Jupyter notebooks, execution order determines the state of variables in memory and can affect results independently of the visual order of cells.

[Expression](https://en.wikipedia.org/wiki/Expression_(computer_science))
: A combination of values (operands) and operators that produces a result. Expressions are evaluated when code is executed to produce new values.

FacetGrid
: A plotting tool that generates grids of subplots, making it ideal for observing spatial changes over time on a shared color scale.

[False color](https://en.wikipedia.org/wiki/False_color) composite
: A multiband image representation where non-visible parts of the electromagnetic spectrum (such as Near Infrared or Shortwave Infrared) are mapped to the visible RGB color channels to highlight specific environmental features like healthy vegetation or bare earth.

[Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
: A series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

Figure (Matplotlib)
: The top-level container or "blank canvas" in Matplotlib that holds all plot elements, including one or more Axes.

[Floating-point number](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
: A primitive data type (`float`) that represents decimal values. They can store numbers with a fractional part.

Folium
: A Python library that acts as a bridge to Leaflet.js. It translates standard Python code into the HTML and JavaScript required to render fully interactive web maps directly in a browser or Jupyter Notebook.

[Fork](https://en.wikipedia.org/wiki/Fork_(software_development))
: A personal copy of a {term}`repository` hosted on GitHub and linked to a user’s account.  
  Forks allow users to modify files without affecting the original repository while still tracking upstream changes.

Forward geocoding
: The standard process of transforming text descriptions of a location (such as addresses or place names) into spatial latitude and longitude coordinates.

f-string
: A modern method for formatting output in Python that allows variable values and expressions to be embedded directly into a text string. They are defined by placing an `f` before the quotation mark and using curly braces `{}` as placeholders.

[Function](https://en.wikipedia.org/wiki/Subroutine)
: A reusable block of instructions that performs a specific task.  
  Functions may exist independently or as a {term}`method` associated with a {term}`Class`.

[GDAL](https://en.wikipedia.org/wiki/GDAL) 
: The industry-standard open-source C++ engine that handles reading, writing, and transforming complex geospatial data formats. Python libraries like `rasterio` act as practical wrappers around GDAL. Short for: `Geospatial Data Abstraction Library`

[Geocoding](https://en.wikipedia.org/wiki/Geocoding)
: The process of converting addresses into geographic coordinates, or coordinates back into addresses (reverse geocoding).  
  Compare with {term}`Georeferencing`, which assigns spatial reference to data rather than translating addresses.

[Geodesic distance](https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid)
: The absolute shortest path between two points on the surface of the Earth. Advanced calculations of geodesic distance use ellipsoidal models (such as WGS-84) to accurately account for the Earth's equatorial bulge and flattened poles.

GeoDataFrame
: A data structure provided by geopandas that extends a pandas {term}`DataFrame` to support geospatial data.  
  Each row represents a geometry (e.g. point, line, or polygon) with associated attributes and supports spatial operations such as spatial joins.

Geographic coordinate conversion
: See {term}`Map reprojection`.

[Georeferencing](https://en.wikipedia.org/wiki/Georeferencing)
: The process of assigning real-world coordinates to data that initially lack spatial reference, such as scanned maps or images.  
  Unlike {term}`Geocoding`, georeferencing does not involve address-based lookup.

GeoSeries
: A one-dimensional collection of geometric objects that extends a pandas {term}`Series` with spatial operations.  
  A GeoSeries is commonly used as the geometry column within a {term}`GeoDataFrame`.

[GeoTIFF](https://en.wikipedia.org/wiki/GeoTIFF)
: A standard public domain metadata format which allows georeferencing information to be embedded within a TIFF image file.

[Git](https://en.wikipedia.org/wiki/Git)
: A free and open-source distributed {term}`version control` system that tracks changes in {term}`source code`.  
  Git enables collaborative development while preserving a complete history of changes.

Git branch
: A parallel line of development in a Git {term}`repository` that starts from a specific snapshot.  
  Branches allow independent development without affecting the main codebase.

Git clone
: A command in {term}`Git` used to create a local copy of an existing {term}`repository`, including its files and version history.

Git commit
: Verb: the act of recording changes made to files in a {term}`repository`.  
  Noun: a snapshot of the repository at a specific point in time, identified by a unique ID and a descriptive message.

Git merge
: A Git command used to integrate changes from multiple {term}`commits <Git commit>` or branches into a single branch.  
  If conflicting changes exist, a {term}`Git merge conflict` may occur.

Git merge conflict
: A situation where Git cannot automatically combine changes because the same parts of a file were modified differently.  
  Conflicts must be resolved manually before creating a new commit.

Git pull
: A Git command that fetches updates from a remote {term}`repository` and merges them into the current branch.

Git push
: A Git command that uploads local {term}`commits <Git commit>` to a remote {term}`repository`, making changes available to others.

Git remote
: A reference to a repository stored on a server or hosting service such as GitHub.  
  Remotes are used to synchronize work between local and shared repositories.

[GitHub](https://en.wikipedia.org/wiki/GitHub)
: An online platform for collaborative development of {term}`software` built around the {term}`Git` {term}`version control` system.  
  GitHub provides tools for collaboration, issue tracking, and code review.

[Google Colab](https://en.wikipedia.org/wiki/Google_Colab)
: A cloud-based Jupyter notebook environment that runs entirely in the browser on remote machines. It provides a low-barrier entry point to programming, allowing users to start coding immediately without installing software locally.

Harmonic regression
: A statistical modeling technique used to fit raw data with a harmonic model to capture both the cyclical seasonal variations and the long-term trend. This prevents seasonal biases (like start- and end-dates) from skewing overall trend estimates.

[Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula)
: A mathematical formula used to calculate the spherical distance, or great-circle distance, between two coordinates across the surface of the Earth.

Hidden state
: A hidden state occurs when a notebook works only because something was executed earlier, even though that dependency is not obvious from the current cell. In other words, the notebook depends on memory that the reader cannot see.

Hillshade
: A grayscale, three-dimensional visualization of terrain derived from a digital elevation model (DEM).  
  Hillshading simulates illumination using a specified light source direction and angle to enhance topographic relief.

[Histogram](https://en.wikipedia.org/wiki/Histogram)
: A visual representation of the distribution of a single continuous numerical variable. It divides the entire range of values into a series of intervals (bins) and counts how many values fall into each bin.

IDE
: See {term}`Integrated Development Environment`.

[Identifier](https://en.wikipedia.org/wiki/Identifier_(computer_languages))
: Also known as a name.  
  An identifier is a reference to an {term}`Object` stored in memory. Objects are accessed using their identifiers.  
  In some cases, multiple identifiers may refer to the same object, meaning they point to the same memory location.

[Immutable](https://en.wikipedia.org/wiki/Immutable_object)
: A data type whose value cannot be changed after it is created.  
  This simplified definition is sufficient for our purposes. Opposite of {term}`Mutable`.

[Indentation](https://en.wikipedia.org/wiki/Indentation_(programming))
: The use of whitespace at the beginning of a line to define code structure.  
  In Python, indentation determines blocks of code such as loops, conditions, and functions.

Index
: A number indicating the position of a value within an ordered data structure such as a {term}`List` or {term}`Tuple`.  
  In Python, indexing starts at 0.

[Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
: A sequence of instructions in a computer program which loops endlessly, either due to the loop having no terminating condition, having one that can never be met, or one that causes the loop to start over.

[Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
: An architectural technique in object-oriented programming that allows a new, specialized class (the child) to build upon and reuse the structure and behavior of an existing class (the parent). This helps eliminate redundant code across similar objects.

__init__ method
: The specialized initialization function (often called a constructor) that is executed automatically upon object creation. It guarantees that every new object instance starts with a valid, structured baseline of attributes.

Inner join
: A join operation that returns only rows with matching keys (or spatial predicates) in both input (Geo)DataFrames.  
  Matching can be based on a shared attribute (table join) or a spatial relationship when performing a spatial join.

[Instance](https://en.wikipedia.org/wiki/Instance_(computer_science))
: A concrete, memory-backed entity built from the abstract blueprint of a class. In Python, an instance is synonymous with an object.

[Instance attribute](https://en.wikipedia.org/wiki/Instance_variable)
: A variable belonging to a specific object instance. Unlike class attributes, instance attributes are unique to each individual object, such as the specific latitude or longitude of a point.

[Integer](https://en.wikipedia.org/wiki/Integer_(computer_science))
: A primitive data type (`int`) that represents whole numbers without a decimal point.

[Integrated Development Environment](https://en.wikipedia.org/wiki/Integrated_development_environment)
: A software application that provides tools for writing, running, testing, and debugging {term}`software` in a single interface.  
  Common features include a code editor, debugger, and integrated terminal.

[Interpolation](https://en.wikipedia.org/wiki/Interpolation)
: The estimation of unknown values based on known values in a dataset.  
  For example, mean daily temperature may be estimated from minimum and maximum temperature measurements.

[Interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing))
: A program that executes instructions written in a programming language such as Python.  
  The interpreter reads and executes code statements sequentially, performing the specified actions.

[Iteration](https://en.wikipedia.org/wiki/Iteration)
: The repetition of a process or instruction sequence within a computer program. In Python, this is commonly achieved using loops to execute code for each item in a collection.

[Iterative design](https://en.wikipedia.org/wiki/Iterative_design) (Iterative development)
: A methodology where a project takes shape through repeated cycles of prototyping, testing, analyzing, and refining. In programming, this means making a simple baseline work first, and then improving and refining it step by step rather than trying to write perfect code immediately.

[JSON](https://en.wikipedia.org/wiki/JSON)
: Short for JavaScript Object Notation. A lightweight, universal text format used to store and transport data on the web. It is heavily used by Web APIs and behaves almost exactly like nested Python dictionaries and lists.

Jupyter server
: A backend process that executes code from a Jupyter notebook and communicates results to the browser interface.  
  The server can run locally or remotely.

[JupyterLab](https://en.wikipedia.org/wiki/Project_Jupyter)
: A browser-based interactive development environment for working with Jupyter notebooks, code, and data.  
  It provides a file browser, notebook interface, terminal, and editor in a single workspace.

Kernel
: The kernel is the computational engine that runs the code in a notebook. It executes Python commands, stores variables in memory, and returns results to the notebook interface. If the kernel is restarted, all variables and previously computed results stored in memory are lost.

Keyword argument
: An argument passed to a function that explicitly names the parameter it is intended for, such as `func(base=5)`. This allows arguments to be passed out of order and improves code readability.

[Large language model](https://en.wikipedia.org/wiki/Large_language_model)
: An artificial intelligence system trained on massive amounts of text data. In the context of programming, LLMs (like Copilot, ChatGPT, or Claude) can be used responsibly as learning aids to clarify syntax, explain error messages, or explore alternative implementations. Abbreviation: `LLM`

[Leaflet](https://en.wikipedia.org/wiki/Leaflet_(software))
: The gold standard JavaScript library for creating interactive web maps.

Left outer join
: A join operation that retains all rows from the left (Geo)DataFrame and includes matching rows from the right (Geo)DataFrame.  
  Rows in the left dataset without a match receive missing values (NaNs) for columns from the right dataset.

[Library](https://en.wikipedia.org/wiki/Library_(computing))
: Also known as a package or {term}`Module`.  
  An installable collection of code that provides reusable functionality through classes, {term}`methods <Method>`, or standalone {term}`functions <Function>`.

[Line chart](https://en.wikipedia.org/wiki/Line_chart)
: Also known as a Line plot. A type of chart that displays information as a series of data points connected by straight line segments, most commonly used to show the change of a variable over a continuous sequence like time.

[List](https://en.wikipedia.org/wiki/List_(abstract_data_type))
: A mutable Python data type used to store an ordered collection of values.  
  List elements can be added, removed, or modified, and values do not need to share the same {term}`Data type`.

[List comprehension](https://en.wikipedia.org/wiki/List_comprehension)
: A compact syntax in Python for creating a new list by applying an expression to each item in an existing iterable, optionally filtering items with a condition.

Local scope
: The narrowest namespace in Python, created when a function is called. Variables defined within a local scope are only accessible from inside that specific function and are destroyed when the function finishes running.

[Logical operator](https://en.wikipedia.org/wiki/Logical_connective)
: Operators such as `and`, `or`, and `not` that combine multiple comparison results into a single `True` or `False` answer.

Loop
: A programming construct that repeats a block of code a fixed number of times or until a condition is met.

[Lossless compression](https://en.wikipedia.org/wiki/Lossless_compression)
: A compression method that reduces file size without losing any data or precision.  
  Common lossless compression methods include `LZW` and `DEFLATE`.

[Magic number](https://en.wikipedia.org/wiki/Magic_number_(programming))
: Unexplained, hard-coded numbers inserted directly into code. Best practices dictate replacing these with named, uppercase constant variables at the top of a script to improve readability and make the workflow safer to rerun.

[Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)
: A measurement of distance that strictly follows a grid, similar to walking city blocks. It is calculated as the sum of the absolute differences of the Cartesian coordinates.

[Map algebra](https://en.wikipedia.org/wiki/Map_algebra)
: The process of performing mathematical operations pixel-by-pixel across one or multiple aligned raster grids to extract new environmental insights.

[Map projection](https://en.wikipedia.org/wiki/Map_projection)
: A mathematical method for representing the curved surface of the Earth on a flat map.

Map reprojection
: The process of converting spatial data from one {term}`Coordinate Reference System` to another.  
  Reprojection relies on mathematical transformations that account for the shape and orientation of the Earth.

[Markdown](https://en.wikipedia.org/wiki/Markdown)
: A lightweight markup language used to create formatted text from plain text input.  
  Markdown supports headings, lists, emphasis, and hyperlinks and is commonly used for documentation.

Markdown cell
: A cell in a Jupyter notebook that contains formatted text written in {term}`Markdown`.  
  Markdown cells are used for explanations, documentation, and structuring a notebook.

[Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
: The oldest, most powerful, and most widely used data visualization library in the Python ecosystem. It is a low-level, highly customizable library that allows users to build almost any static 2D plot from scratch.

Median
: A measure of central tendency representing the middle value of a sorted list of numbers. If the list has an even number of observations, the median is the average of the two middle values.

[Metadata](https://en.wikipedia.org/wiki/Metadata)
: Data that describe other data.  
  Metadata commonly include information such as content, resolution, format, coordinate reference system, and acquisition date.

[Method](https://en.wikipedia.org/wiki/Method_(computer_programming))
: A {term}`Function` that is associated with an instance of a specific data type or {term}`Class`.  
  Methods are accessed using dot notation on an object.

[Method overriding](https://en.wikipedia.org/wiki/Method_overriding)
: A feature of inheritance that allows a child class to redefine or replace a method inherited from its parent class, enabling the child to behave more specifically for its specialized role.

Module
: A Python file (`.py`) that contains definitions, statements, and executable code.  
  Modules are used to organize and reuse code.

[Moving average](https://en.wikipedia.org/wiki/Moving_average)
: Also known as a rolling average. A statistical calculation that creates a sliding window moving down a time series, averaging a set amount of past observations together to smooth out short-term fluctuations and highlight longer-term trends.

Mutable
: A data type whose value can be changed after it is created.  
  Examples include lists and dictionaries. Opposite of {term}`Immutable`.

[NaN](https://en.wikipedia.org/wiki/NaN) 
: A marker used by Pandas to represent missing data. Any mathematical operation involving a `NaN` usually results in a `NaN`. Short for `Not a Number`.

[Namespace](https://en.wikipedia.org/wiki/Namespace)
: A scope that defines where Python looks for identifiers.  
  Namespaces allow the same name to be reused in different contexts without conflict.  
  Python uses four main namespaces (from broadest to narrowest): built-in, global, enclosing, and local.

[Nested loop](https://en.wikipedia.org/wiki/Inner_loop)
: A loop placed inside the body of another loop. The inner loop executes completely for each iteration of the outer loop.

[NetCDF](https://en.wikipedia.org/wiki/NetCDF)
: A widely used hierarchical data format for persistently storing massive, native multidimensional datasets on disk. Short for `Network Common Data Form`

[Normalized Difference Snow Index](https://en.wikipedia.org/wiki/Normalized_Difference_Snow_Index)
: A spectral index used to map snow and ice coverage by comparing reflectance in the Green and Shortwave Infrared (SWIR) bands. Abbreviation: `NDSI`

[Notebook](https://en.wikipedia.org/wiki/Project_Jupyter#Jupyter_Notebook)
: A web-based interactive document that combines formatted text with executable code cells.  
  Jupyter Notebooks can include equations, images, visualizations, and code output and are widely used for data analysis and teaching.

[NumPy](https://en.wikipedia.org/wiki/NumPy)
: The core library for numerical computing in Python, which provides a fast and efficient structure (`ndarray`) for storing and manipulating large multidimensional grids of numbers.

[Object](https://en.wikipedia.org/wiki/Object_(computer_science))
: A container that stores data (and possibly behavior) at a specific location in computer memory.  
  Objects are accessed through an {term}`Identifier`.

[Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
: A programming paradigm where data structures are powerful objects that contain both the data and the built-in tools (methods) needed to manipulate it.

[Open data](https://en.wikipedia.org/wiki/Open_data)
: Freely available and accessible datasets that can be used, analyzed, and republished by anyone to answer real-world spatial questions.

[Operand](https://en.wikipedia.org/wiki/Operand)
: A literal value or a variable that an operator acts on within an expression.

[Operator](https://en.wikipedia.org/wiki/Operator_(computer_programming))
: A symbol used to combine values or variables into expressions. Examples include arithmetic operators (like `+` and `*`), comparison operators (like `==` and `>`), and logical operators.

Optional parameter
: A {term}`Parameter` that does not need to be explicitly provided when calling a {term}`Function`.  
  If omitted, the parameter takes a default value defined in the function signature.

[Package manager](https://en.wikipedia.org/wiki/Package_manager)
: A system that acts as an app store for code, used to find, download, and install external software packages and their required dependencies into local environments. Examples include `pip` and `conda`.

[Parameter](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
: Also known as an {term}`Argument`.  
  A variable listed in the parentheses of a function definition that receives a value when the function is called.  
  A parameter must either be assigned a value through an argument or have a default value.

PEP 8
: The official Python style guide.
  It defines widely used conventions for writing readable and consistent Python code, including naming, indentation, whitespace, line length, comments, and docstrings.
  The purpose of PEP 8 is to make Python code more readable, easier to debug and simpler to maintain.

Perceptually uniform colormap
: A colormap that weights the same data variation equally all across the dataspace. This ensures that the true data variation is accurately represented without unnecessary visual error or distortion.

[Pie chart](https://en.wikipedia.org/wiki/Pie_chart)
: A type of chart that is best used for showing parts of a whole, or proportions.

[pip](https://en.wikipedia.org/wiki/Pip_(package_manager))
: The standard package installer for Python, used to download and install software packages from the Python Package Index (PyPI).

[Pixel](https://en.wikipedia.org/wiki/Pixel)
: The smallest addressable element in a raster grid or array. In spatial data, the physical real-world size of each pixel determines the spatial resolution of the dataset.

[Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
: One of the core pillars of object-oriented programming that allows methods to adapt dynamically to different objects.

Positional argument
: An argument passed to a function without a keyword, where its assigned parameter is determined solely by its order in the function call. Positional arguments must be provided in the exact order defined by the function signature.

[Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming)
: A programming approach where data is stored in basic containers (like lists or dictionaries) and then passed into separate, external functions.

[Program](https://en.wikipedia.org/wiki/Computer_program)
: A sequence of step-by-step instructions that tells a computer what actions to perform.

[Programming language](https://en.wikipedia.org/wiki/Programming_language)
: A formal system of precise and unambiguous instructions that a computer can interpret and execute.

[Property](https://en.wikipedia.org/wiki/Property_(programming))
: Also known as an attribute or feature.  
  A single value associated with a {term}`Record`, such as `time_stamp` or `temperature`.  
  Properties are typically stored in columns.

Raster data model
: A geographic data model that represents the world as a continuous grid of cells (pixels), assigning a numerical value to every single location rather than using discrete boundary shapes.

[Rate limiting](https://en.wikipedia.org/wiki/Rate_limiting)
: A policy enforced by API providers to reject requests if a user sends too many queries too quickly, often returning an HTTP 429 error code. Developers must respect these limits by pausing code execution, typically using functions like `time.sleep()`.

[README](https://en.wikipedia.org/wiki/README)
: A document that acts as a standalone guide for a project. In reproducible research, it serves as the "front door" that explains the project objectives, data sources, outputs, and environment setup instructions before a user ever opens the code.

[Record](https://en.wikipedia.org/wiki/Record_(computer_science))
: Also known as an observation or event.  
  A single, usually independent, occurrence of a phenomenon, typically stored as a row in a table.

[Relative path](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths)
: A robust file path that specifies the location of a file or directory in relation to the current working directory. Using relative paths (often via the `pathlib` module) ensures that scripts can successfully locate data regardless of the operating system or machine they are run on.

[Repository](https://en.wikipedia.org/wiki/Software_repository)
: A collection of files and their complete change history managed by a version control system such as {term}`Git`.  
  Often referred to informally as a “repo”.

[Reproducibility](https://en.wikipedia.org/wiki/Reproducibility)
: The ability for another person (or yourself at a later time) to rerun an analysis using the exact same code, data, and software environment, and recover the exact same results. It depends fundamentally on organized workflows, robust defensive checks, and clear interpretability.

Required parameter
: A {term}`Parameter` that must be provided when calling a function.  
  Required parameters do not have default values and are sometimes called positional parameters.

Resampling
: The process of moving between different temporal resolutions by changing the frequency of time series data. For example, aggregating high-frequency hourly sensor data into daily summaries.

[Reserved word](https://en.wikipedia.org/wiki/Reserved_word)
: Also known as a keyword. A word that is reserved by Python's core logic (such as `for`, `if`, `True`) and cannot be used as a variable name.

[REST](https://en.wikipedia.org/wiki/REST)
: A standard used by most spatial APIs that allows programs to interact with servers over standard web protocols (HTTP), operating in the exact same way a web browser does when loading a page. Short for `Representational State Transfer`.

Return statement
: The instruction inside a function that specifies what value (or values) should be passed back to the caller. When a `return` statement is executed, the function immediately terminates.

Reverse geocoding
: The process of taking abstract GPS coordinates and retrieving the rich, human-readable physical street address or context associated with that precise location.

[Scatter plot](https://en.wikipedia.org/wiki/Scatter_plot)
: A type of plot that uses Cartesian coordinates to display values for two continuous numeric variables, used to observe relationships or correlations between them.

[Scope](https://en.wikipedia.org/wiki/Scope_(computer_science))
: The region of a program in which a name is valid and can be accessed.  
  Python searches for names through a hierarchy of {term}`Namespaces <Namespace>`: local, enclosing, global, and built-in.

[Script](https://en.wikipedia.org/wiki/Scripting_language)
: A file containing executable Python code that can be run like a {term}`Program`.

self parameter
: A dynamic placeholder convention used as the first parameter in class methods. It refers to the "current active object" and grants the method direct access to read or update that specific object's internal state.

Series
: In pandas, a one-dimensional labeled data structure that stores a sequence of values with an associated index.  
  A Series often represents a single column and serves as a building block for a {term}`DataFrame`.

[Set](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
: A data type that can store distinct values, without any particular order. Rather than retrieving a specific element from a set, one typically tests a value for membership in a set.

Shifting
: The process of moving values in a time series forward or backward in time.  
  Shifting is commonly used to compare values across different time steps.

Signature
: The first line of a function definition, which specifies the function's name and the parameters it accepts.

Signed integer
: An integer data type that can represent both positive and negative whole numbers.  
  In Python, integers are signed by default and can grow to arbitrary size.

Slicing
: A technique used to extract a range of values or segments from an ordered sequence, such as a list, using index positions.

Slope
: A measure of terrain steepness derived from elevation data.  
  Slope represents the rate of change in elevation over distance and is commonly expressed in degrees or percent.

Snake case
: A variable naming convention that uses lowercase letters and underscores (`_`) to separate words.  
  Example: `gps_station_id`.  
  Also known as pothole case. Compare with {term}`Camel case`.

[Software](https://en.wikipedia.org/wiki/Software)
: Another term for a {term}`Program`.

[Source code](https://en.wikipedia.org/wiki/Source_code)
: The human-readable instructions written in a {term}`Programming language` that define what a {term}`Program` does.

[Spatial data science](https://en.wikipedia.org/wiki/Spatial_data_science)
: An interdisciplinary field that extracts insights from geographic data by combining traditional GIS concepts with advanced programming, computational thinking, and reproducible data workflows. Abbreviation: SDS

Spatial extent
: In geographic data, spatial extent refers to the geographic area covered by a dataset or map.  
  It is typically defined by minimum and maximum coordinates that bound the data, often forming a rectangular boundary.

Spatial index
: A data structure that enables efficient querying of spatial objects such as points, lines, and polygons.  
  Spatial indexes speed up operations based on location or spatial relationships and are commonly used in GIS and spatial databases.  
  Examples include R-trees, quad-trees, and k-d trees.  

Spatial join
: A method for combining two geospatial datasets based on the spatial relationships between their features.  
  For example, attributes from polygons may be joined to points that fall within them.

[Spatial queries](https://en.wikipedia.org/wiki/Spatial_query)
: Operations that select or analyze features based on spatial relationships such as distance, intersection, or containment.  
  Spatial queries rely on geometric properties rather than attribute values alone.

Spatial resolution
: The level of spatial detail in raster data, typically expressed as the size of raster cells on the ground.  
  Smaller cell sizes correspond to higher spatial resolution.

Split-Apply-Combine
: A strategy for grouping data in Pandas. It involves splitting the dataset into groups based on a category, applying a mathematical function to each group independently, and combining the results back into a summary table.

[Standard library](https://en.wikipedia.org/wiki/Standard_library)
: A substantial collection of built-in, highly optimized, ready-to-use modules that come pre-installed with Python. It provides standardized tools for common programming tasks (such as advanced math, statistics, date/time manipulation, and file system navigation) without requiring external downloads.

[Standard score](https://en.wikipedia.org/wiki/Standard_score)
: A statistical measure that indicates exactly how many standard deviations an observation is above or below the mean. It is used to normalize anomalies relative to the baseline variability of a specific dataset or landscape. Also known as `Z-score`.

[Statement](https://en.wikipedia.org/wiki/Statement_(computer_science))
: A single instruction in a programming language that performs an action.  
  A {term}`Program` consists of one or more statements.

[Status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
: A code sent back by a web server in response to an API request. It informs the user if the request was successful (such as Code 200 for "OK") or if it failed.

[String](https://en.wikipedia.org/wiki/String_(computer_science))
: A sequence of characters used to represent text in a program.  
  In Python, strings are enclosed in single (`'`), double (`"`), or triple quotes (`"""`).

Subplots
: Individual plots arranged within a single figure in Matplotlib.

super() function
: A built-in Python function that allows child classes to cleanly call methods from their parent class. It is commonly used in a child's `__init__` method to reuse the parent's initialization logic and prevent redundant code.

[Syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
: The formal structure required to write valid code in a programming language.  
  For example, the correct syntax for printing text in Python is `print("hello")`.

[Syntax error](https://en.wikipedia.org/wiki/Syntax_error)
: An error that occurs when the code violates the grammatical rules of the programming language, preventing the interpreter from understanding or executing the instructions. Learning to constructively read and resolve these errors is a core part of programming.

[Terminal](https://en.wikipedia.org/wiki/Computer_terminal)
: A command-line interface used to interact with a computer by typing text commands.  
  Terminals are commonly used to run Python scripts, manage environments, and start tools such as {term}`JupyterLab`.

Third-party package
: A library or module created by the broader Python community that is not included in the standard Python installation. These collections of code are made available for public use and must be actively downloaded via a package manager (like `conda` or `pip`) before they can be utilized in your scripts. Also known as {term}`Module`.

[Time series](https://en.wikipedia.org/wiki/Time_series)
: A sequence of data points indexed in time order. In Pandas, data with a `DatetimeIndex` is fundamentally "time-aware," allowing for advanced operations like temporal slicing and resampling.

Topological spatial relations
: Relationships that describe how geometric objects relate to one another based on their boundaries and positions.  
  Examples include contains, touches, and intersects.

True color composite
: An image representation that mimics human vision by mapping the Red, Green, and Blue satellite bands into their corresponding red, green, and blue visual display channels.

[Truncation](https://en.wikipedia.org/wiki/Truncation)
: The process of dropping everything after a decimal point when converting floating-point numbers into integers, rather than mathematically rounding them.

[Tuple](https://en.wikipedia.org/wiki/Tuple)
: An immutable Python sequence used to store ordered collections of values.  
  Tuples are commonly used for fixed data such as coordinate pairs, for example `(60.192059, 24.945831)`.  
  Compare with {term}`List`, which is mutable.

[Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
: The process of changing the {term}`Data type` of an object.  
  For example, converting an integer to a float using `float(5)`.

Type hint
: A formal way to indicate the expected data types of variables, function parameters, and return values in Python. They serve as built-in documentation so collaborators can easily understand the inputs, outputs, and behavior of custom functions without having to read the underlying implementation.

TypeError
: An error raised by Python when an operation is attempted on incompatible data types. For example, attempting to add a string and a number will result in a `TypeError`.

Unsigned integer
: An integer data type that represents only non-negative values.  
  Unlike {term}`Signed integer`, unsigned integers do not include negative numbers.

[Unix time](https://en.wikipedia.org/wiki/Unix_time) 
: The mathematical starting point ($x=0$) for `xarray` datetime regressions, which corresponds to January 1, 1970. Consequently, the intercept in these models always represents the modeled baseline value on this specific date. Also known as `Unix epoch`.

uv
: A very fast tool used for managing Python packages.

ValueError
: An error raised by Python when an operation receives the correct data type, but the actual content does not make sense for the operation. For example, attempting to convert the word "Cold" into a float raises a `ValueError`.

[Variable](https://en.wikipedia.org/wiki/Variable_(computer_science))
: An {term}`Object` that has an {term}`Identifier` (its name) and stores one or more values in memory.  
  The value of a variable may change while a program is running.

[Vectorization](https://en.wikipedia.org/wiki/Array_programming)
: A concept used by Pandas to perform mathematical operations across entire datasets instantly using highly optimized C-language arrays, eliminating the need for slow Python `for` loops.

Version
: A specific recorded state of files in a {term}`Repository` managed by a {term}`Version control` system.  

[Version control](https://en.wikipedia.org/wiki/Version_control)
: The practice of tracking and managing changes to files over time, especially {term}`Source code`.  
  Version control enables collaboration and recovery of earlier versions.

Version drift
: A phenomenon where unpinned software dependencies evolve over time, silently changing mathematical behavior or spatial outputs. Locking down package versions in an `environment.yml` file prevents this issue.

View (Pandas)
: A subset of a DataFrame that acts as a window looking at the original dataset. Modifying a view can accidentally alter the original dataset, which triggers a `SettingWithCopyWarning`. This contrasts with a *copy*, which is a completely independent physical object.

[Violin plot](https://en.wikipedia.org/wiki/Violin_plot)
: A type of chart that is best used for visualizing the distribution of data and its probability density. It essentially combines a box plot with a smoothed kernel density estimate.

Virtual environment
: An isolated Python environment with its own interpreter and installed libraries.  
  Virtual environments prevent conflicts between dependencies used by different projects.

[Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)
: A lightweight, extensible code editor that serves as a central digital workspace. It integrates code editing, terminals, Jupyter notebooks, and version control into a single environment, making it highly suited for geospatial programming. Also known as `VS Code`.

[Web Map Tile Service](https://en.wikipedia.org/wiki/Web_Map_Tile_Service) 
: A standard protocol for serving pre-rendered, georeferenced map tiles over the internet. Instead of downloading massive geographic datasets, WMTS delivers small, seamless square image tiles based on the user's specific zoom level and map extent. Also known as `WMTS`

[Web Mercator](https://en.wikipedia.org/wiki/Web_Mercator_projection)
: A specific coordinate reference system (`EPSG:3857`) that perfectly preserves local angles and shapes, making it the de facto standard for almost all major online map providers.

Well-known binary
: A compact binary format for representing vector geometry objects in a machine-efficient form.  
  The human-readable equivalent is {term}`Well-known text`.

[Well-known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)
: A text-based format for representing vector geometry objects.  
  The binary equivalent of WKT is {term}`Well-known binary`.

[WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System)
: A global geographic coordinate reference system (`EPSG:4326`) that describes positions on Earth using latitude and longitude.  
  It is widely used by GPS devices, online datasets, and web mapping services as a common reference system for storing and exchanging location data.

[Working directory](https://en.wikipedia.org/wiki/Working_directory)
: The specific folder on your computer where Python is currently running and actively looking for imported script files or data.

xarray
: A Python library designed to handle massive, multidimensional environmental datasets by combining fast matrix operations with explicit spatial and temporal labels.

Zarr
: A cloud-optimized data format used to persistently store massive multidimensional datasets on disk or in cloud stores.

Zoom level
: A scale used in web map tile pyramids to determine resolution. At level 0, the entire world is rendered in a single image tile, and as the level increases, the map is divided into exponentially more tiles to reveal greater detail.

:::
