import nose.tools as n
import pandas
import numpy
from midiutil.MidiFile import MIDIFile

from ddpy import df_to_midi

def assert_midi_equal(a, b):
    n.assert_equal(len(a.tracks), len(b.tracks))
    for i in range(len(a.tracks)):
        n.assert_equal(a.tracks[i].eventList,
                       b.tracks[i].eventList)

def test_one_int_column():
    '''
    A data frame with a single integer column
    should be converted correctly.
    '''
    expected = MIDIFile(1)
    expected.addTrackName(0,0,"guitar")
    expected.addTempo(0,0,120)
    for time,note in enumerate([38, 40, 42, 43]):
        expected.addNote(0,0,note,time,1,100)

    df = pandas.DataFrame([
        {'guitar':38},
        {'guitar':40},
        {'guitar':42},
        {'guitar':43},
    ])
    observed = df_to_midi(df, bpm = 120)
    assert_midi_equal(observed, expected)

def test_missing_value():
    '''
    A data frame with a single integer column
    should be converted correctly.
    '''
    expected = MIDIFile(1)
    expected.addTrackName(0,0,"guitar")
    expected.addTempo(0,0,120)
    for time,note in enumerate([38, None, 42, 43]):
        if note != None:
            expected.addNote(0,0,note,time,1,100)

    df = pandas.DataFrame([
        {'guitar':38},
        {'guitar':numpy.nan},
        {'guitar':42},
        {'guitar':43},
    ])
    observed = df_to_midi(df, bpm = 120)
    assert_midi_equal(observed, expected)

def test_two_int_columns():
    '''
    A data frame with a single integer column
    should be converted correctly.
    '''
    expected = MIDIFile(2)
    expected.addTrackName(0,0,"guitar")
    expected.addTempo(0,0,120)
    for time,note in enumerate([38, 40, 42, 43]):
        expected.addNote(0,0,note,time,1,100)

    expected.addTrackName(1,0,"piano")
    expected.addTempo(1,0,120)
    for time,note in enumerate([46, 48, 50, 51]):
        expected.addNote(1,0,note,time,1,100)

    df = pandas.DataFrame([
        {'guitar':38,'piano':46},
        {'guitar':40,'piano':48},
        {'guitar':42,'piano':50},
        {'guitar':43,'piano':51},
    ])
    observed = df_to_midi(df, bpm = 120)
    assert_midi_equal(observed, expected)

@n.nottest
def test_one_text_column():
    '''
    A data frame with a single integer column
    should be converted correctly.
    '''
    expected = MIDIFile(1)
    expected.addTrackName(0,0,"vocals")
    expected.addTempo(0,0,120)
    for time,note in enumerate([38, 40, 42, 43]):
        expected.addNote(0,0,note,time,1,100)

    df = pandas.DataFrame([
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'badger'},
        {'vocals':'mushroom'},
        {'vocals':'mushroom'},
    ])
    observed = df_to_midi(df, bpm = 120)

    n.assert_equal(observed, expected)
