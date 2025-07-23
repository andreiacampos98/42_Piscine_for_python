def square(x: int | float) -> int | float:
    """
    The function returns the square of argument.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    The function returns the Exponentiation of argument by himself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """The function that is called and return the result
    of the inner function."""
    count = 0

    def inner() -> float:
        """The function save the value of x and use the value as argument
        when call the function"""
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner
