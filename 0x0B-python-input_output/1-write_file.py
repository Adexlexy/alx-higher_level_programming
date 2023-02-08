#!/usr/bin/python3
"""
contains the functions "write file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as myFile:
        return myFile.write(text)
