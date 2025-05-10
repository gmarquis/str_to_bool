def str_to_bool(value: str) -> bool:
    """Convert a string to a boolean.
    >>> str_to_bool("true")
    True
    >>> str_to_bool("false")
    False
    >>> str_to_bool('hello')
    Traceback (most recent call last):
        ...
    ValueError: invalid boolean: 'hello'
    """
    if (value := value.lower()) in ('false','f','0'):
        return False
    if (value := value.lower()) in ('true','t','1'):
        return True
    raise ValueError(f'invalid boolean: {value!r}')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

