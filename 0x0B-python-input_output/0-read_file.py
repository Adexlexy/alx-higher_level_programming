#!/usr/bin/python3

def read_file(filename=""):
    """contains the read file functions"""

    with open("filename", encoding="utf-8") as filename:
        """the code for opening and reading a file"""

        print(filename.read(), end ="")
