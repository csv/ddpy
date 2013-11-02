import pandas
from ddpy import df_to_midi

def test_one_int_column():
    df = pandas.DataFrame([
        {'guitar':38},
        {'guitar':40},
        {'guitar':42},
        {'guitar':43},
    ])
    observed = df_to_midi(df)
    expected =
