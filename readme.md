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

## Column translations
