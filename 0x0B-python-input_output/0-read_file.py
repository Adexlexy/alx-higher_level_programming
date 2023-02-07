#!/usr/bin/python3

def read_file(filename=""):
    """contains the read file functions"""

    with open("filename", encoding="utf-8") as filename:
        """reads a text file(UTF8) and prints it to stdout"""

        print(filename.read(), end ="")
