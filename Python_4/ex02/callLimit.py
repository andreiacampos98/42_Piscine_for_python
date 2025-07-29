from typing import Any, Callable


def callLimit(limit: int):
    """
    A decorator generator that limits the number of times
    a function can be called.
    """

    def callLimiter(function: Callable):
        """
        The actual decorator that wraps the given function.
        """
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that enforces the call limit.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
