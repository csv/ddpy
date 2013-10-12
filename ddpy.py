import itertools

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
    Traceback (most recent call last):
        ...
    ValueError
    '''


def _check_types(table):
    '''
    Args:
        table: An iterable of dict-likes, a dict-like of iterables,
               or a pandas.DataFrame-like.
    Returns:
        None
    Raises:
        ValueError on invalid input

    >>> _check_types([{'year':2010,'gdp':8},{'year':2011,'gdp':9}])

    >>> _check_types({2010:8,2011:9})
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if _is_like_dataframe(table):
        pass
    elif _is_like_dict(table):
        are_iterable = map(_is_iterable, table.values())
        if not set(are_iterable) == {True}:
            raise ValueError
    elif _is_iterable(table):
        pass
    else:
        raise ValueError

def _is_like_dataframe(thing):
    return hasattr(thing, 'to_dict')

def _is_like_dict(thing):
    return hasattr(thing, 'keys')

def _is_iterable(thing):
    return hasattr(thing, '__iter__')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
