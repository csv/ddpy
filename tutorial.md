Data music for big data analysis
=====

## Introduction
Visualization can only support so many variables.
In order to study high-dimensional datasets,
we need to leverage more senses, like the sense of sound.

### History of ddpy
[csv soundsystem](http://csvsoundsystem.com) makes
music from data, and we have developed a few tools
to help us do that. We started out by with disgusting
hacks in R, which we eventually abstracted into a
package called
[data-driven rhythms (ddr)](https://github.com/csv/ddr).
dd**py** is confusingly named after the package dd**r**,
even though there's no pun anymore.
The API for ddpy is inspired largely by a prototype
we build for making music
[from Google Spreadsheets](https://github.com/csv/sheetmusic).

### Today
Today, you'll learn how to transform a dataset into music.
We'll use the `ddpy` package for this tutorial, but the
same concepts apply regardless of what tools you use to
turn your data into music.

## Install
You'll need a means of playing MIDI files.
[timidity++]() is one option.


You'll also need [ddpy]().

    pip install ddpy

## Tables
I see the whole world as collections of things,
which I like to represent as data tables. Rows
are records, and columns are variables.

I see music the same way. A given sound is a
function of the notes that are being played by
various instruments, and a song consists of a
collection of sounds. Thus, columns are
instruments, rows are beats (or some other
time-related thing), and cells contain notes.

![Ordinary sheet music]()

![Music as a spreadsheet/table, with cells containing notes like "A4" and "C#3"]()

## Pandas to MIDI
ddpy provides a `to_midi` function that converts
a pandas data frame to a MIDI file.

    to_midi(df, 'output.mid')

It currently supports the following subset of data
frame possibilities.

* ...

Text is represented as lyric events, integers are
represented as discrete beats, and floats are
represented as notes that gradually merge into each other.

The main thing that probably isn't obvious to you is
how pitches get created. MIDI files can represent 128
different notes per instrument. If the instrument is a
piano with exactly 128 keys (white and black), then
zero correspends to the lowest (left-most) key, and 127
corresponds to the right-most key. ddpy just passes
these numbers from our data frame into the MIDI file.

![Piano with 128 keys, numbered from 0 to 127]()

Thus, we can compose some simple music by making columns
with numbers from 0 to 127. Here's a chromatic scale.

```python
pandas.DataFrame({'piano':range(50, 63)})
```

A major scale

```python
pandas.DataFrame({'piano':[50, 52, 54, 55, 57, 59, 61, 62})
```

A XXX minor scale

```python
pandas.DataFrame({'piano':[]})
```

Some minor chords (multiple instruments)

```python
df = pandas.DataFrame({'low':[50, 57, 64]})
df['middle'] = df['low'] + 3
df['high'] = df['low'] + 5
```


Random music of different distributions

## More about MIDI
Let's talk a bit more about MIDI so you get a better
feel for what is going on. I think of everything as
tables, so I also think of MIDI files as a format for
serializating tables, and that's how I'm going to
explain it.

A MIDI file contains up to 128 different instruments (columns).
Each of these contains up to 16 different tracks.
Within each track, we have a bunch of events, including

* note
* ...

There are also "meta-events", which include

* a
* b

Why do we need this concept of events? We are using a
MIDI file, but you can also emit MIDI events directly to
other software, live. These live events use the same
protocol as the events in our file.

## Preparing our data so the music sounds nice
I've come up with a few elements in the production of
interesting data music.

scaling

### Data must have a noticeable pattern.
Random music doesn't sound that interesting

    Example

Similarly, empirical data that are effectively
random aren't that interesting either.

    Example

This is obvious with one instrument, but it
can be easy to forget when you add a second;
the second instrument normally needs to have
some relationship with the first instrument
in order for the piece to sound good.

    Example with unrelated variables

    Example with related variables

Periodic trends work particularly well.




### You're still making music
We started with the example of mapping numbers
to keys on a piano. You should treat this as a
primitive operation on which more interesting
things can be built.

Using Grammar of Graphics terminology, let's say
that pitch is one aesthetic that defines our music.
We could have other aesthetics, like the key/scale.
You could have one column defining the note within
a scale, another column defining the base note of
the scale, and a third defining whether the scale
is major or minor. Then you create one column to
convert to MIDI.

    Example

Also, rows in your dataset could correspond to things
other than beats, like a measure, a phrase, or a stanza.
This is especially helpful when you're dealing with data
of varied resolution (for example, monthly versus daily).

    Example



### Gaps in data along your time variable are annoying

### Outliers are your solos
If you follow the advice above, you'll have a very
coherent piece, where everything within in relates to
everything else. This in itself gets boring, but it
allows you to create interesting sequences that
sharply contrast the rest of the piece. And these
interesting sequences naturally arise if you have
outliers.

    Example

This is actually the same for data visuals;
people often focus quite strongly on outliers
in graphs.

    Equivalent graph example

    ![Equivalent graph]()

Data music, just like data visuals, can be set up
to emphasize specific parts of a dataset. That is,
you could use the same dataset to produce one
song or graph that emphasizes an trend and one that
completely ignores it.

Anyway, keep in mind that outliers make your music
interesting.
