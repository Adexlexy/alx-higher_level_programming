#!/usr/bin/python3
"""contains the functions that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """functions that save a text file to Json 'filename' """
    with open(filename, 'w', encoding='utf=8') as myFile:
        json.dumps(my_obj, myFile)
