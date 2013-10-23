ddpy
===================
Rather than mere [data-driven rhythms](https://github.com/csv/ddr),
this is data-driven music in python.

More precisely, ddpy serializes tables in python to midi files and
deserializes midi files to tables. It provides a `to_midi` function
and a `from_midi` function.

We plan on adding `to_midi` and `from_midi` as `pandas.DataFrame`
methods eventually.

## Table structure
In the present documentation, we use "table" in a rather generic way.
It refers to a collection of things (rows), with the same attributes
(columns) measured about each thing. `ddpy` recognizes two data
structures for representating a table.

1. A list of dicts
2. Pandas DataFrame

Each column in the table gets represented as an instrument, and each
row in the table gets represented as a beat.

## Columns and data types
The following data types can be stored in a column

* Strings (`unicode` or `str`)
* Factors (`pandas.Factor` )
* Booleans (`bool`)
* Integers (`int`, `numpy.int64`, &c.)
* Floats (`float`, `numpy.float64`, &c.)

The following sections explain how columns are structured by data type.

### Strings
Strings (`unicode` or `str`) are represented as lyrics.

### Factors
Factors (`pandas.Factor`) are represented as drum tracks, with a mapping
between drum notes and factor levels.

### Booleans


### Floats
Floats are represented as continuous notes merging into each other through
pitch bends.

### Integers
Integers are represented as discrete notes.
The pitches are determined by the same means as for floats.


## Tweaking output

### Volume
By default, all instruments play at full volume. There are two ways of
specifying volume: by instrument and by note.

#### Specifying in `to_midi`
To specify volume by instrument, pass a dictionary where the keys are
column names and the values are instrument volumes, represented as numbers
between 0 and 1. Columns for which you don't specify a volume use
full volume (1) by default.

    table = [{'debt':9001,'cats':8},{'debt':3,'cats':23}]
    to_midi(table, volume = {'debt': 0.8})

The example above shows how to specify volume by instrument when creating
the file with `to_midi`.


With any of the data types, you may specify a volume for each note.
 two-item tuple

#### Reading in `from_midi`
Tuple

By default, no volume tuples

When you reading a file with `from_midi`, the
instrument-level volumes are not returned;
they're just read as tuples.
