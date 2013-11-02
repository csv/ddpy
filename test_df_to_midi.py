import nose.tools as n
import pandas
from ddpy import df_to_midi

def test_one_int_column():
    df = pandas.DataFrame([
        {'guitar':38},
        {'guitar':40},
        {'guitar':42},
        {'guitar':43},
    ])
    observed = df_to_midi(df, bpm = 120)

    expected = MIDIFile(1)
    expected.addTrackName(0,0,"guitar")
    expected.addTempo(0,0,120)
    for time,note in enumerate([38, 40, 42, 43]):
        expected.addNote(0,0,note,time,1,100)

    n.assert_equal(observed, expected)
