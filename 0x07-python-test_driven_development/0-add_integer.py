def add_integer(a, b=98):
    int(a)
    int(b)
    if isinstance(a, int):
        if isinstance(b, int):
            return (a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
