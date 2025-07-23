from typing import Any, Callable


def callLimit(limit: int):

    def callLimiter(function: Callable):
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function()
    return callLimiter
