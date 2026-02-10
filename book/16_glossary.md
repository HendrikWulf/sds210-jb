# Glossary

:::{glossary}

Accessor
: In Python libraries, an *accessor* is a way to attach specialized functionality to an existing data structure without changing its core implementation.  
  For example, libraries such as `xarray` add accessors to objects like a `Dataset` to provide domain-specific {term}`methods <Method>` and properties.

[Application Programming Interface](https://en.wikipedia.org/wiki/API)
: An *application programming interface* (API) is a defined set of rules and tools that allow different pieces of {term}`software` to communicate and exchange information.  
  For example, the Nominatim service provides an API for accessing its geocoding functionality.

[API](https://en.wikipedia.org/wiki/API)
: See {term}`Application Programming Interface`.

Argument
: A value passed to a {term}`function` when it is called.  
  Compare with a {term}`Parameter`, which refers to the variable name used in the function definition.

[Aspect](https://en.wikipedia.org/wiki/Aspect_(geography))
: Aspect describes the compass direction that a {term}`slope` faces and is derived from elevation data.  
  It is usually measured in degrees from 0° (north) to 360°.

[Assertion](https://en.wikipedia.org/wiki/Assertion_(software_development))
: A statement used in a Python program to check whether a condition evaluates to `True` when the code is executed.  
  If the condition is not `True`, an `AssertionError` is raised. Assertions are commonly used for debugging and testing code.

[Camel case](https://en.wikipedia.org/wiki/Camel_case)
: A variable naming convention in which words are joined without spaces, with each new word starting with a capital letter (except the first).  
  Example: `gpsStationId`.  
  Compare with {term}`Snake case`.

[Class](https://en.wikipedia.org/wiki/Class_(programming))
: A reusable template for creating {term}`objects <Object>` that share common properties and behavior.  
  For example, a class representing a geospatial point may store coordinates and provide methods such as distance calculations.

Collection
: A container that stores multiple values together.  
  Built-in Python collection types include {term}`List`, {term}`Dictionary`, {term}`Set`, and {term}`Tuple`.

Computer
: We use the definition of a computer given by {cite}`Zelle2017`:  
  “A machine that stores and manipulates information under the control of a changeable program.”

Coordinate Reference System
: A coordinate reference system (CRS) describes how coordinates or geometries relate to real locations on Earth.  
  It defines the coordinate system, projection, and mathematical model needed to locate positions accurately and exchange geographic data between systems.

Coordinate transformation
: See {term}`Map reprojection`.

Cost surface
: A raster representation in which each cell value indicates the cost (e.g. time, energy, money, or difficulty) required to traverse that cell.  
  Cost surfaces are commonly used to compute least-cost paths or accumulated cost in spatial analysis.

Curvature
: Curvature describes how quickly the {term}`slope` changes across a surface.  
  Positive curvature indicates an upwardly convex surface, while negative curvature indicates a downwardly convex surface.

DataFrame
: In the pandas library, a DataFrame is a two-dimensional, tabular data structure with labeled rows and columns.  
  It supports data manipulation tasks such as filtering, aggregation, and merging and is a core structure for data analysis in Python.

Data model
: A conceptual model that describes how data are structured, organized, and related to real-world entities.  
  Common examples include the vector data model (points, lines, polygons) and the raster data model (grids of cell values).

Data type
: A classification that defines what kind of values a variable can store.  
  Common data types include Boolean, integer, float, string, and date/time types.

DateOffset
: A pandas object that represents a calendar-based time duration, such as days or weeks (e.g. `"W"` for one week).

DatetimeIndex
: An immutable array of datetime values used as the index of a pandas {term}`DataFrame`.  
  It enables indexing, grouping, and analysis based on time.

Decimal degrees
: A method for expressing latitude and longitude as decimal values rather than degrees, minutes, and seconds.  
  Decimal degrees simplify calculations involving geographic coordinates.

Dependency
: A software package that another package relies on in order to function correctly.  
  Dependencies typically need to be installed alongside the main package.

Dictionary
: A built-in Python data structure that stores key–value pairs.  
  Keys are used to access associated values, and dictionaries are enclosed in curly braces (`{}`).

Docstring
: A text string used to document Python code, commonly {term}`functions <Function>` or classes.  
  Docstrings describe purpose, parameters, and outputs and can be accessed using Python’s `help()` function.

Edge effect
: Edge effect refers to spatial distortion (bias) that occurs near the boundaries of a geographic dataset, both raster and vector.  
  It often arises from incomplete neighboring data and can affect operations such as filtering, classification, and spatial modeling near dataset edges.

EPSG code
: An EPSG code is a numeric identifier that uniquely defines a {term}`Coordinate Reference System` (CRS) or a spatial data transformation.  
  Examples include EPSG:4326 for WGS84 and EPSG:3857 for Web Mercator, which simplify referencing CRSs in geographic data processing.

Fork
: A personal copy of a {term}`repository` hosted on GitHub and linked to a user’s account.  
  Forks allow users to modify files without affecting the original repository while still tracking upstream changes.

Function
: A reusable block of instructions that performs a specific task.  
  Functions may exist independently or as a {term}`method` associated with a {term}`Class`.

Geocoding
: The process of converting addresses into geographic coordinates, or coordinates back into addresses (reverse geocoding).  
  Compare with {term}`Georeferencing`, which assigns spatial reference to data rather than translating addresses.

GeoDataFrame
: A data structure provided by geopandas that extends a pandas {term}`DataFrame` to support geospatial data.  
  Each row represents a geometry (e.g. point, line, or polygon) with associated attributes and supports spatial operations such as spatial joins.

Geographic coordinate conversion
: See {term}`Map reprojection`.

Georeferencing
: The process of assigning real-world coordinates to data that initially lack spatial reference, such as scanned maps or images.  
  Unlike {term}`Geocoding`, georeferencing does not involve address-based lookup.

GeoSeries
: A one-dimensional collection of geometric objects that extends a pandas {term}`Series` with spatial operations.  
  A GeoSeries is commonly used as the geometry column within a {term}`GeoDataFrame`.

Git
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

GitHub
: An online platform for collaborative development of {term}`software` built around the {term}`Git` {term}`version control` system.  
  GitHub provides tools for collaboration, issue tracking, and code review.

Hillshade
: A grayscale, three-dimensional visualization of terrain derived from a digital elevation model (DEM).  
  Hillshading simulates illumination using a specified light source direction and angle to enhance topographic relief.

IDE
: See {term}`Integrated Development Environment`.

Identifier
: Also known as a name.  
  An identifier is a reference to an {term}`Object` stored in memory. Objects are accessed using their identifiers.  
  In some cases, multiple identifiers may refer to the same object, meaning they point to the same memory location.

Immutable
: A data type whose value cannot be changed after it is created.  
  This simplified definition is sufficient for our purposes. Opposite of {term}`Mutable`.

Index
: A number indicating the position of a value within an ordered data structure such as a {term}`List` or {term}`Tuple`.  
  In Python, indexing starts at 0.

Inner join
: A join operation that returns only rows with matching keys (or spatial predicates) in both input (Geo)DataFrames.  
  Matching can be based on a shared attribute (table join) or a spatial relationship when performing a spatial join.

Integrated Development Environment
: A software application that provides tools for writing, running, testing, and debugging {term}`software` in a single interface.  
  Common features include a code editor, debugger, and integrated terminal.

Interpolation
: The estimation of unknown values based on known values in a dataset.  
  For example, mean daily temperature may be estimated from minimum and maximum temperature measurements.

Interpreter
: A program that executes instructions written in a programming language such as Python.  
  The interpreter reads and executes code statements sequentially, performing the specified actions.

Jupyter Notebook
: A web-based interactive document that combines formatted text with executable code cells.  
  Jupyter Notebooks can include equations, images, visualizations, and code output and are widely used for data analysis and teaching.

Left outer join
: A join operation that retains all rows from the left (Geo)DataFrame and includes matching rows from the right (Geo)DataFrame.  
  Rows in the left dataset without a match receive missing values (NaNs) for columns from the right dataset.

Library
: Also known as a package or {term}`Module`.  
  An installable collection of code that provides reusable functionality through classes, {term}`methods <Method>`, or standalone {term}`functions <Function>`.

List
: A mutable Python data type used to store an ordered collection of values.  
  List elements can be added, removed, or modified, and values do not need to share the same {term}`Data type`.

Loop
: A programming construct that repeats a block of code a fixed number of times or until a condition is met.

Lossless compression
: A compression method that reduces file size without losing any data or precision.  
  Common lossless compression methods include `LZW` and `DEFLATE`.

Lossy compression
: A compression method that reduces file size by discarding some data, resulting in reduced quality or precision.  
  Common lossy compression methods include `JPEG` and `JPEG2000`.

Map projection
: A mathematical method for representing the curved surface of the Earth on a flat map.

Map reprojection
: The process of converting spatial data from one {term}`Coordinate Reference System` to another.  
  Reprojection relies on mathematical transformations that account for the shape and orientation of the Earth.

Markdown
: A lightweight markup language used to create formatted text from plain text input.  
  Markdown supports headings, lists, emphasis, and hyperlinks and is commonly used for documentation.

Metadata
: Data that describe other data.  
  Metadata commonly include information such as content, resolution, format, coordinate reference system, and acquisition date.

Method
: A {term}`Function` that is associated with an instance of a specific data type or {term}`Class`.  
  Methods are accessed using dot notation on an object.

Module
: A Python file (`.py`) that contains definitions, statements, and executable code.  
  Modules are used to organize and reuse code.

Mutable
: A data type whose value can be changed after it is created.  
  Examples include lists and dictionaries. Opposite of {term}`Immutable`.

Namespace
: A scope that defines where Python looks for identifiers.  
  Namespaces allow the same name to be reused in different contexts without conflict.  
  Python uses four main namespaces (from broadest to narrowest): built-in, global, enclosing, and local.

Object
: A container that stores data (and possibly behavior) at a specific location in computer memory.  
  Objects are accessed through an {term}`Identifier`.

Optional parameter
: A {term}`Parameter` that does not need to be explicitly provided when calling a {term}`Function`.  
  If omitted, the parameter takes a default value defined in the function signature.

[Parameter](https://en.wikipedia.org/wiki/Parameter_(computer_programming))
: Also known as an {term}`Argument`.  
  A variable listed in the parentheses of a function definition that receives a value when the function is called.  
  A parameter must either be assigned a value through an argument or have a default value.

Program
: A sequence of step-by-step instructions that tells a computer what actions to perform.

Programming language
: A formal system of precise and unambiguous instructions that a computer can interpret and execute.

Property
: Also known as an attribute or feature.  
  A single value associated with a {term}`Record`, such as `time_stamp` or `temperature`.  
  Properties are typically stored in columns.

Radiometric resolution
: In satellite imagery, radiometric resolution describes how precisely a sensor can distinguish differences in signal intensity.  
  It is determined by the number of bits per pixel (e.g. 8-bit or 16-bit), which defines the range of possible values.

Radius query
: A type of {term}`Spatial queries` that retrieves all points within a specified distance from a query point.  
  Radius queries are often implemented using spatial index structures such as a KD-tree.  

Record
: Also known as an observation or event.  
  A single, usually independent, occurrence of a phenomenon, typically stored as a row in a table.

Repository
: A collection of files and their complete change history managed by a version control system such as {term}`Git`.  
  Often referred to informally as a “repo”.

Required parameter
: A {term}`Parameter` that must be provided when calling a function.  
  Required parameters do not have default values and are sometimes called positional parameters.

Revision
: Another term for a {term}`Version`.

Right outer join
: A join operation that retains all rows from the right (Geo)DataFrame and includes matching rows from the left (Geo)DataFrame.  
  Rows in the right dataset without a match receive missing values (NaNs) for columns from the left dataset.

Scope
: The region of a program in which a name is valid and can be accessed.  
  Python searches for names through a hierarchy of {term}`Namespaces <Namespace>`: local, enclosing, global, and built-in.

Script
: A file containing executable Python code that can be run like a {term}`Program`.

Semantics
: The meaning of a construct in a programming language, such as a statement or function.  
  For example, the semantics of `len()` define that it returns the number of elements in a data structure.

Series
: In pandas, a one-dimensional labeled data structure that stores a sequence of values with an associated index.  
  A Series often represents a single column and serves as a building block for a {term}`DataFrame`.

[Set](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
: A data type that can store distinct values, without any particular order. Rather than retrieving a specific element from a set, one typically tests a value for membership in a set.

Shifting
: The process of moving values in a time series forward or backward in time.  
  Shifting is commonly used to compare values across different time steps.

Signed integer
: An integer data type that can represent both positive and negative whole numbers.  
  In Python, integers are signed by default and can grow to arbitrary size.

Slope
: A measure of terrain steepness derived from elevation data.  
  Slope represents the rate of change in elevation over distance and is commonly expressed in degrees or percent.

Snake case
: A variable naming convention that uses lowercase letters and underscores (`_`) to separate words.  
  Example: `gps_station_id`.  
  Also known as pothole case. Compare with {term}`Camel case`.

Software
: Another term for a {term}`Program`.

Source code
: The human-readable instructions written in a {term}`Programming language` that define what a {term}`Program` does.

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

Spatial queries
: Operations that select or analyze features based on spatial relationships such as distance, intersection, or containment.  
  Spatial queries rely on geometric properties rather than attribute values alone.

Spatial resolution
: The level of spatial detail in raster data, typically expressed as the size of raster cells on the ground.  
  Smaller cell sizes correspond to higher spatial resolution.

Spatio-temporal data model
: A data model that represents both spatial dimensions (x, y) and a temporal dimension (t).  

Spectral resolution
: In multispectral satellite data, spectral resolution describes how finely a sensor distinguishes wavelengths of electromagnetic radiation.  
  It is determined by the number and width of spectral bands.

Statement
: A single instruction in a programming language that performs an action.  
  A {term}`Program` consists of one or more statements.

Subplots
: Individual plots arranged within a single figure in Matplotlib.

Syntax
: The formal structure required to write valid code in a programming language.  
  For example, the correct syntax for printing text in Python is `print("hello")`.

Temporal resolution
: In satellite imagery, temporal resolution refers to how frequently the same area on Earth is observed.  
  It is typically expressed as the time interval between observations (e.g. daily or weekly).

Topological spatial relations
: Relationships that describe how geometric objects relate to one another based on their boundaries and positions.  
  Examples include contains, touches, and intersects.

Tuple
: An immutable Python sequence used to store ordered collections of values.  
  Tuples are commonly used for fixed data such as coordinate pairs, for example `(60.192059, 24.945831)`.  
  Compare with {term}`List`, which is mutable.

Type conversion
: The process of changing the {term}`Data type` of an object.  
  For example, converting an integer to a float using `float(5)`.

Unary union
: A geometric operation that merges multiple geometries into a single geometry.  
  Unary union is often used to treat collections of shapes as one object.  

Unsigned integer
: An integer data type that represents only non-negative values.  
  Unlike {term}`Signed integer`, unsigned integers do not include negative numbers.

Variable
: An {term}`Object` that has an {term}`Identifier` (its name) and stores one or more values in memory.  
  The value of a variable may change while a program is running.

Version
: A specific recorded state of files in a {term}`Repository` managed by a {term}`Version control` system.  
  Also referred to as a {term}`Revision`.

Version control
: The practice of tracking and managing changes to files over time, especially {term}`Source code`.  
  Version control enables collaboration and recovery of earlier versions.

Virtual environment
: An isolated Python environment with its own interpreter and installed libraries.  
  Virtual environments prevent conflicts between dependencies used by different projects.

Watershed
: An area of land in which all surface water drains toward a common outlet such as a river, lake, or ocean.

Well-known binary
: A compact binary format for representing vector geometry objects in a machine-efficient form.  
  The human-readable equivalent is {term}`Well-known text`.

Well-known text
: A text-based format for representing vector geometry objects.  
  The binary equivalent of WKT is {term}`Well-known binary`.

:::