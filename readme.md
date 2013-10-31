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

A MIDI track can contain 16 different channels, and each channel can represent
128 different notes, numbered 0 to 127. Thus, a single track can represent
$$128^16 = 2^112$$ different values, which is equivalent to 112 bits.


## Tweaking output
Most of these tweaks to output are set by a keyword argument. These keyword
arguments can take two structures, which we'll call the table form or the
column form.

The table form is just a value, and it applies to the full song. For example,
to set the volume for the full song, you can run `to_midi(table, volume = 0.7)`.
This is the table form.

The column form allows us to specify different values for each column. This
form is a dictionary whose keys are column names and values are parameters for
the different columns. You do not need to specify a key-value pair for each
column; a default value will be used for any that you don't specify.

### Volume
#### Specifying in `to_midi`
By default, all instruments play at full volume. There are two ways of
specifying volume: by instrument and by note.

To specify volume by instrument, pass a dictionary where the keys are
column names and the values are instrument volumes, represented as numbers
between 0 and 1. Columns for which you don't specify a volume use
full volume (1) by default.

    table = [{'debt':9001,'cats':8},{'debt':3,'cats':23}]
    to_midi(table, volume = {'debt': 0.8})

The example above shows how to specify volume by instrument when creating
the file with `to_midi`.

To specify a volume for each note, you should structure your table such
that cells contain `(data,volume)` tuples rather than simple `data`
values. For example, the following code would do the exact same thing as
the previous code.

    table = [{'debt':(9001,0.8),'cats':8},{'debt':(3,0.8),'cats':23}]
    to_midi(table)

If you use both methods to specify volume, the volume for a given note
will be the product of the two volumes.

#### Reading in `from_midi`
Tuple

By default, no volume tuples

When you reading a file with `from_midi`, the
instrument-level volumes are not returned;
they're just read as tuples.


### Key
By default, a key of C Major is used

You can change this...

`from_midi` won't give you the key back

### Rounding
Rounding your data to the key signature destroys information in order to
make the music sound better. Rounding is turned off by default, but you
can turn it on

### Tempo
















Each MIDI track has 16 channels, each of which can take 128 values.
We represent floats and integers in base 128.

$$ 128^8 = 2^\left(7\times8\right) = 2^15 $$

Integers: We use odd tracks for positive numbers and even tracks for
negative numbers. For positive numbers, he first track corresponds
to the first place, the third track to the second place, and so on.
For negative numbers, the second track corresponds to the first place,
the fourth to the second, and so on.

Floats: We use the first X tracks for the mantissa, the next Y tracks
for the exponent, and the final track for the sign. The sign is represented
as 0 or 1, with 0 being negative. Each of these components of the float
is an integer like above but with fewer than 16 tracks.

This scheme is chosen so that cells containing the exact values 0, 1, 2, ... 127
will be mapped to the identical number on the first channel in MIDI.



