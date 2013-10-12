def to_midi(table, filename):
    '''
    Args:
        table: A list of dictionaries, a dictionary of lists,
               or a pandas.DataFrame.
        filename: A string (like 'output/data.midi')
    Returns:
        None

    >>> to_midi([{'year':2010,'gdp':8},{'year':2011,'gdp':9}], 'gdp.midi')

    >>> to_midi([[2010,8],[2011,9]], 'gdp.midi')
    ValueError
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
