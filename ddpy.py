import itertools

from midiutil.MidiFile import MIDIFile

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

# Add a note. addNote expects the following information:
track = 0
channel = 0
pitch = 60
time = 0
duration = 1
volume = 100

MyMIDI.addNote(track,channel,pitch,time,duration,volume)

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

def to_midi(table, filename, *args, **kwargs):
    '''
    Args:
        table: An iterable of dict-likes, a dict-like of iterables,
               or a pandas.DataFrame-like.
        filename: A string (like 'output/data.midi')
        *args, **kwargs: passed along to df_to_midi
    Returns:
        None

    >>> to_midi([{'year':2010,'gdp':8},{'year':2011,'gdp':9}], 'gdp.midi', {})

    >>> to_midi([[2010,8],[2011,9]], 'gdp.midi', {})
    Traceback (most recent call last):
        ...
    TypeError
    '''
    _check_types(table)

    if _is_like_dataframe(table):
        dict_table = iter(table.to_dict())
    elif _is_iterable(table):
        dict_table = iter(table)
    elif _is_like_dict(table):
        try:
            dict_table = (dict(table.keys(), row) for row in itertools.izip(table.values()))
        except:
            raise TypeError

    for row in dict_table:
        if not _is_like_dict(row):
            raise TypeError

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
    return (({} for row in range(3)), {})

def _check_types(table):
    '''
    Args:
        table: An iterable of dict-likes, a dict-like of iterables,
               or a pandas.DataFrame-like.
    Returns:
        None
    Raises:
        TypeError on invalid input

    >>> _check_types([{'year':2010,'gdp':8},{'year':2011,'gdp':9}])

    >>> _check_types({2010:8,2011:9})
    Traceback (most recent call last):
        ...
    TypeError
    '''
    if _is_like_dataframe(table):
        pass
    elif _is_like_dict(table):
        are_iterable = map(_is_iterable, table.values())
        if not set(are_iterable) == {True}:
            raise TypeError
    elif _is_iterable(table):
        pass
    else:
        raise TypeError

def _is_like_dataframe(thing):
    return hasattr(thing, 'to_dict')

def _is_like_dict(thing):
    return hasattr(thing, 'keys')

def _is_iterable(thing):
    return hasattr(thing, '__iter__')


def df_to_midi(df, bpm = 180):
    '''
    Args:
        table: A pandas.DataFrame
    Returns:
        A MIDI thingy
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
