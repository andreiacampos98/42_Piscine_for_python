numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(n):
    return n % 2 == 0


def ft_filter(function=None, iterable=None):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if iterable is None:
        raise ValueError("You must provide an iterable")
    if function is None:
        return [x for x in iterable if x]
    else:
        return [x for x in iterable if function(x)]


print(ft_filter.__doc__)
print("############################")
print(filter.__doc__)


# result2 = filter(None, numbers)
# result4 = ft_filter(None, numbers)
# print(list(result2))
# print(list(result4))

# print(ft_filter(None, [0, 1, "", "hello", [], [1]]))
# print(list(ft_filter(None, [0, 1, "", "hello", [], [1]])))
# print(list(filter(None, [0, 1, "", "hello", [], [1]])))

# print(ft_filter(str.isupper, "aAbBcC"))
# print(list(ft_filter(str.isupper, "aAbBcC")))
# print(list(filter(str.isupper, "aAbBcC")))
