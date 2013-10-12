def to_midi(table, filename):
    '''
    Args:
        table: An iterable of dict-likes, a dict-like of iterables,
               or a pandas.DataFrame-like.
        filename: A string (like 'output/data.midi')
    Returns:
        None

    >>> to_midi([{'year':2010,'gdp':8},{'year':2011,'gdp':9}], 'gdp.midi')

    >>> to_midi([[2010,8],[2011,9]], 'gdp.midi')
    ValueError
    '''
    if _is_like_dataframe(table):
    elif _is_like_dict(table):
    elif _is_iterable(table):
    else:
        raise ValueError

if __name__ == '__main__':
    import doctest
    doctest.testmod()
