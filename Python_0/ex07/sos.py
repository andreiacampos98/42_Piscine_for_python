import sys


def sos(s: str):
    NESTED_MORSE = {
                        " ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. "
                    }
    new_word = ''
    for x in s:
        if x not in NESTED_MORSE:
            raise AssertionError("There is characters that are not space and \
alphanumeric")
        new_word += NESTED_MORSE[x]
    print(new_word)
    return new_word


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise AssertionError("the number of argument is different from 1")
    sos(args[0].upper())


if __name__ == "__main__":
    main()
