import sys


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        return
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return

    print(f'The text contains {len(args[0])}')
    upper = lower = punctuation = spaces = digits = 0
    for char in args[0]:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punctuation} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')


if __name__ == "__main__":
    main()
