import nose.tools as n
import pandas
from midiutil.MidiFile import MIDIFile
from ddpy import df_to_midi

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

    n.assert_equal(observed, expected)

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
        {'vocals':38},
        {'vocals':40},
        {'vocals':42},
        {'vocals':43},
    ])
    observed = df_to_midi(df, bpm = 120)

    n.assert_equal(observed, expected)
