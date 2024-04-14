#!/usr/bin/python3
'''Text indentation module.'''


def text_indentation(text):
    '''Prints a text with 2 new lines after (., ? and :).

    Args:
        text: text to split and print.

    Raises:
        TypeError: if text is not a string.
    '''

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    for x in text:
        if (x == '.' or x == '?' or x == ':'):
            text = (x + "\n\n").join(
                [line.strip() for line in text.split(x)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
