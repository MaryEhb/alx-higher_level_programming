#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ''
    for i in text:
        if (i in '.:?'):
            print(line.strip(" ") + i, end='\n\n')
            line = ''
        else:
            line += i

    if line:
        print(line.strip(), end='')
