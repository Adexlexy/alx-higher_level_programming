#!/usr/bin/python3

"""contains the function "append_write" """


def append_write(filename="", text=""):
    """returns the number of characters added to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as myFile:
        return myFile.write(text)
