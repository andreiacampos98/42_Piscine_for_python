import sys
from ft_filter import ft_filter


def filter_string(s: str, n: int):
    """Function that accepts two arguments: a string(S),
    and an integer(N). The output is a list of words from S
    that have a length greater than N."""
    new_list = list(ft_filter(lambda word: len(word) > n, s.split()))
    return new_list


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        raise AssertionError("the arguments are bad")

    s = args[0]
    try:
        number = int(args[1])
    except ValueError:
        raise AssertionError("the arguments are bad")

    print(filter_string(s, number))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
