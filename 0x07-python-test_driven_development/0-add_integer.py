def add_integer(a, b=98):
    if isinstance(a, float) or isinstance(a, int):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, float) or isinstance(b, int):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
