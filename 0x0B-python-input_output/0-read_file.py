#!/usr/bin/python3

def read_file(filename=""):
    """contains the read file functions"""

    with open("filename", "r" encoding="utf-8") as myFile:
        """the code for opening and reading a file"""

    print(myFile.read())