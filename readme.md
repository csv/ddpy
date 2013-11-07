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

### Why music
Music gives lets us use a different sense (sound) that visuals do.
If we combine music with visuals, we can consume data through multiple
senses and thus experience higher-dimensional data. This ability to
represent multivariate data is the main promise I see in data-driven
music, but I see some side benefits too. Let's talk about three benefits
of data music.

* More dimensions
* Accessibility
* Reaching young people

#### More dimensions
Even the best of visuals can only represent so many dimensions.

![Minard's map of Napoleon's march](minard.png)
<!-- http://upload.wikimedia.org/wikipedia/commons/2/29/Minard.png -->

Typically, we deal with this by reducing dimensions before plotting or by making
multiple plots, but this approach loses information. Animations can help.

[![complicated plot](4l-FixedScale-NoMuProf2-preview.png)](4l-FixedScale-NoMuProf2.gif)

I think the future is in multisensory data experiences. Food is the prime
example of this, as we use all five senses in experiencing it.

![Artichoke pizza](artichoke.jpg)
<!-- http://www.flickr.com/photos/igorschwarzmann/4423705330/ -->

#### Accessibility
!["Opening Doors to IT" logo](open-doors.jpg)
<!-- http://www.section508.gov/images/open_doors_seal-b.jpg

* [Section 508](https://www.section508.gov/)
* [Web Content Accessibility Guidelines](http://www.w3.org/TR/WCAG10/
 -->


#### Reaching young people
Data is in.

[![Government representatives](dubstep-preview.png)](http://www.youtube.com/watch?v=JwuEnyV1Cb0)

### Thinking about sound and multivariate analysis
Given that you're reading this, I suspect that you already know something
about how to make meaningful plots. We've been studying data visualization
for quite a while, so we've come up with some pretty good theory about how
to make good graphics. Our ears work differently from our eyes, so much of
this theory won't apply very directly. You'll have to explore different ways
of creating sound such that our ears perceive the data properly.

#### Multivariate analysis
Here's a little tip to get you thinking. The world is multivariate, and we
should represent that in our visuals. (As Edward Tufte would say, escape
Flatland.) When we are representing dozens of variables at once, we can't
expect ourselves to be able to keep track of all of the individual variables;
once we get to more than a few variables, we tend to reduce the dimensionality
based on some sort of unsupervised learning, like clustering or principal
component analysis. We use these multivariate methods to get a bigger picture;
once we have the bigger picture, we can choose to delve deeper into specific
parts of the dataset and to look at the original variables.

#### Why vision might not be great for multivariate analysis
When you're producing music, food, or visuals from data, it's good to both
present the bigger picture and allow people to delve deeper into specifics.
I find that the sense of vision is particularly well suited for delving into
specifics. This is because visuals can be static and because we can easily
block out certain parts of visuals.

When I say that visuals can be static, I mean that a person can decide with
her eyes how long to spend looking at them. Contrast this to sound, where a
person has to spend time listening in order to perceive a full song. With a
visual, you can easily slow down to focus on just one part.

When I say that we can block out certain parts of visuals, mean that we can
cover up parts of the visuals and just focus on the interesting part.
For example, we could have a huge scatterplot matrix but choose to focus on
only one of the scatterplots. Contrast this to sound and smell; with those
two senses, we can focus our perception by walking around or by pointing our
heads in different directions, but it's harder for us to focus on a particular
range of receptors (a band of frequencies or a set of smells). We can focus
our taste by choosing what we eat and to some degree by choosing which part
of our tongue we put our food on, but it's still not as much focus as we get
with vision. Touch is, perhaps, the closest sense to vision in the ability
to focus on particular stimuli.

### Today
Today, you'll learn how to transform a dataset into music.
We'll use the `ddpy` package for this tutorial, but the
same concepts apply regardless of what tools you use to
turn your data into music.

## Install
You'll need a means of playing MIDI files.
[timidity++]() is one option.


You'll also need [ddpy](https://github.com/csv/ddpy).

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
df = pandas.DataFrame({'chromatic':range(50, 63)})
to_midi(df, 'chromatic.mid')
```

A major scale

```python
df = pandas.DataFrame({'major':[50, 52, 54, 55, 57, 59, 61, 62})
to_midi(df, 'major_scale.mid')
```

A XXX minor scale

```python
df = pandas.DataFrame({'minor':[]})
to_midi(df, 'minor_scale.mid')
```

Some minor chords (multiple instruments)

```python
df = pandas.DataFrame({'low':[50, 57, 64]})
df['middle'] = df['low'] + 3
df['high'] = df['low'] + 7
to_midi(df, 'chords.mid')
```

Random music of different distributions

```python
df = pandas.DataFrame({'normal':[round(random.normalvariate(55, 7)) for i in range(24)]})
to_midi(df, 'normal.mid')
```

```python
df = pandas.DataFrame({'gamma':[round(random.gammavariate(2, 3)) for i in range(24)]})
to_midi(df, 'gamma.mid')
```

You don't always need to play something; here's a Bernoulli rhythm.

```python
df = pandas.DataFrame({'bernoulli':[(52 if random.uniform(0,1) > 0.5 else numpy.nan) for i in range(24)]})
to_midi(df, 'bernoulli.mid')
```

### Exercise
Load a dataset into a pandas data frame, and convert it to MIDI.
You can use any dataset you want, but here's an option in case you
can't come up with any. XXX
Don't worry about doing anything that complicated; we'll do that
later.

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
Random music gets boring quickly.

```python
df = pandas.DataFrame({'normal':[round(random.gammavariate(2, 3)) for i in range(72)]})
to_midi(df, 'random.mid')
```

Similarly, empirical data that are effectively
random aren't that interesting either.

    Example

This gets more important as you add instruments
the second instrument normally needs to have
some relationship with the first instrument
in order for the piece to sound good.

```python
df = pandas.DataFrame({
    'a':[round(random.normalvariate(55, 7)) for i in range(24)],
    'b':[round(random.normalvariate(55, 7)) for i in range(24)],
})
to_midi(df, 'two_random_instruments.mid')
```

```python
# XXX add a real dataset
df = pandas.DataFrame()
to_midi(df, 'two_related_instruments.mid')
```

Periodic trends work particularly well.

```python
# XXX add a real dataset
df = pandas.DataFrame()
to_midi(df, 'periodic_trends.mid')
```

#### Exercise
Make a simple song from two variables that are somehow related.

### You're still making music
We started with the example of mapping numbers
to keys on a piano. You should treat this as a
primitive operation on which more interesting
things can be built.

Using Grammar of Graphics terminology, let's say
that pitch is one aesthetic that defines our music.
We could have other aesthetics, like the key/scale.
You could have one column defining the note within
a chord, another column defining the base note of
the chord, and a third defining whether the chord
is major or minor. Then you create one column to
convert to MIDI.

```python
# XXX add a real dataset
df = pandas.DataFrame({
    'year':[],
    'prop_something': [], # scale the value to a reasonable range of base notes
    'better_than_last_year': [], #this becomes major or minor
})
# Use different states from the ACS. Some interesting
# statistic means major/minor.
to_midi(df, 'periodic_trends.mid')
```

Also, rows in your dataset could correspond to things
other than beats, like a measure, a phrase, or a stanza.
This is especially helpful when you're dealing with data
of varied resolution (for example, monthly versus daily).

```python
df = pandas.DataFrame({
    'year':[],
    'new_york':[],
    'new_jersey':[],
    'total':[],
})
# Map total to aa lower something that varies less
# and the states to higher, melodic things. Each phrase
# includes all of the states, each state as a separate beat.
```

#### Exercise
Map some data onto musical aesthetics other than pitch. If you
know any music theory, do get creative with this.

For something simple, you could try chords. To make a major
chord from a base note, play the following notes.

* the base note
* the base note plus four
* the base note plus seven

To make a minor chord, play the following notes.

* the base note
* the base note plus three
* the base note plus seven

To make a seventh chord (XXX), play the ordinary major or minor
chord with a fourth note; the fourth note is the base note plus XXX

### Gaps in data along your time variable are annoying
Your music can get boring if it doesn't change for very long.
This can happen if you have a particular sort of missing data.
Let's say that you have a dataset about locations of XXX
and you map the locations to the time variable. That might sound
like this.

```python
```

If your instrument broke between locations 88 ft and 204 ft,
it'll sound like this.

```python
```

That gap is inconvenient. If you are dealing with datasets like
this, you'll have to come up with some way of dealing with it.

For inspiration, think about how we deal with this in graphs.
Sometimes, the gap occurs just once and we use a broken scale.

XXX

In some cases, it might make sense to interpolate the data and
indicate that we are doing so.

XXX

In other cases, the gap really just means that we should be
plotting our data on a different scale.

XXX

#### Exercise
No exercise for this, just something to think about

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

#### Exercise
No exercise for this, just something to think about

## Review

* Why music
  * Use other senses
  * High dimensions
  * Accessibility
  * Getting wider audiences interested
* Seeing music as a table
  * Instruments are columns.
  * Time units are rows.
  * You may have to transform your original dataset to be in this table format.
* MIDI
* Tips
  * Data need to have a pattern; random noise is boring.
  * You're still making music, so music theory applies.
  * Gaps along your musical time variable can be annoying.
  * Outliers are your solos.

## Other resources
* Copy our stuff from other places
* Grammar of Graphics
* Tufte
