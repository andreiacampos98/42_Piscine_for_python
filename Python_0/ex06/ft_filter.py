print(filter.__doc__)

# filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função que retorna True para números pares


def is_even(n):
    return n % 2 == 0

def ft_filter():

    

result1 = filter(is_even, numbers)
result2 = ft_filter(is_even, numbers)
print(list(result1))
print(list(result2))
