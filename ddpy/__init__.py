#!/usr/bin/env python
# This file is part of ddpy.

# Copyright (C) 2013 Brian Abelson, Thomas Levine and other contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

import itertools

import numpy
from midiutil.MidiFile import MIDIFile

__author__ = 'Brian Abelson (brianabelson.com) and Thomas Levine (thomaslevine.com)'
__version__ = '0.2.0'

def to_midi(table, filename, *args, **kwargs):
    '''
    Args:
        table: A pandas.DataFrame
        filename: A string (like 'output/data.midi')
        *args, **kwargs: passed along to df_to_midi
    Returns:
        None

    >>> import pandas; to_midi(pandas.DataFrame([{'year':2010 - 2000,'gdp':8},{'year':2011 - 2000,'gdp':9}]), 'gdp.midi')
    '''

    m = df_to_midi(table, *args, **kwargs)

    binfile = open(filename, 'wb')
    m.writeFile(binfile)
    binfile.close()

def from_midi(filename):
    '''
    Args:
        filename: A string (like 'input/data.midi')
    Returns:
        An iterable of dictionaries (table) and
        a dictionary of musical parameters (music)

    >>> map(type, from_midi('gdp.midi'))
    [<type 'generator'>, <type 'dict'>]
    '''
    raise NotImplementedError("We're not implementing this until we have a lossless to_midi function.")
    return (({} for row in range(3)), {})

def df_to_midi(df, bpm = 180):
    '''
    Args:
        table: A pandas.DataFrame
    Returns:
        A MIDI thingy
    '''
    m = MIDIFile(df.shape[1])
    for col_number, col_name in enumerate(df.columns):
        m.addTrackName(col_number,0,col_name)
        m.addTempo(col_number,0,bpm)
        for time,note in enumerate(df[col_name]):
            if numpy.isnan(note):
                pass
            elif note in range(128):
                m.addNote(col_number,0,note,time,1,100)
            else:
                raise NotImplementedError('Only notes 0 to 127 and NaN are supported.')
    return m

if __name__ == '__main__':
    import doctest
    doctest.testmod()
