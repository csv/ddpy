def to_midi(table, filename):
    '''
    Args:
        table: A list of dictionaries, a dictionary of lists,
               a list of lists, or a pandas.DataFrame.
        filename: A string (like 'output/data.midi')
    Returns:
        None

    >>> to_midi([{'year':2010,'gdp':8},{'year':2011,'gdp':9}], 'gdp.midi')
    None

    >>> to_midi([[2010,8},{'year':2011,'gdp':9}], 'gdp.midi')
    ValueError
    '''
