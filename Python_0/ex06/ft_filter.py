print(filter.__doc__)

# filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função que retorna True para números pares


def is_even(n):
    return n % 2 == 0


# def ft_filter(function=None, iterable=None):
#     if iterable is None:
#         raise ValueError("You must provide an iterable")
#     if function is None:
#         return [x for x in iterable if x]
#     else:
#         return [x for x in iterable if function(x)]
    

def ft_filter(function, iterable):
    for item in iterable:
        if function is None and item:
            yield item
        elif function is not None and function(item):
            yield item


result1 = filter(is_even, numbers)
result2 = filter(None, numbers)
result3 = ft_filter(is_even, numbers)
result4 = ft_filter(None, numbers)
print(list(result1))
print(list(result2))
print(list(result3))
print(list(result4))
print(ft_filter(None, [0, 1, "", "hello", [], [1]]))
print(ft_filter(str.isupper, "aAbBcC"))
print(list(ft_filter(None, [0, 1, "", "hello", [], [1]])))
print(list(ft_filter(str.isupper, "aAbBcC")))
print(list(filter(None, [0, 1, "", "hello", [], [1]])))
print(list(filter(str.isupper, "aAbBcC")))
