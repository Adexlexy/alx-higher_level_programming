#!/usr/bin/python3

def read_file(filename=""):
    """contains the read file functions"""


    with open("filename", "r", encoding="utf-8") as f:
        """reads a text file(UTF8) and prints it to stdout"""

    print(f.read(), end ="")
