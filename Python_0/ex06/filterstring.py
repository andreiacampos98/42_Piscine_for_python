import sys


# def filter_string(s: str, n: int):
#     list_ = s.split()
#     new_list = [x for x in list_ if len(x) > n]
#     return new_list


def filter_string(s: str, n: int):
    new_list = list(filter(lambda word: len(word) > n, s.split()))
    print(new_list)
    return new_list


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        raise AssertionError("the number of argument is different from 2")

    try:
        s = args[0]
        number = int(args[1])
    except ValueError:
        raise AssertionError("The second argument isn't a number")
    filter_string(s, number)


if __name__ == "__main__":
    main()
