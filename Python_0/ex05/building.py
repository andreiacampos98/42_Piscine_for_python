import sys


def main():
    '''Take the argument and calculated the upper-case \
characters, lower-case characters, punctuation characters, \
digits and spaces.'''

    args = sys.argv[1:]

    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    # assert len(args) <= 1, "more than one argument is provided"

    if len(args) == 0:
        print("What is the text to count?")
        try:
            text = input()
        except EOFError:
            return
    else:
        text = args[0]

    print(f'The text contains {len(text)} characters:')
    upper = lower = punctuation = spaces = digits = 0
    for char in text:
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
    # print(main.__doc__)
