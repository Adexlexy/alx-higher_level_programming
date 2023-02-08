#!/usr/bin/python3
"""
functions that creates an onject from a JSON file 'filename"
"""


import json


def load_from_json_file(filename):
    """functions that load from a json file to "filename" """
    with open(filename, 'r', encoding='utf=8') as myFile:
        return json.load(myFile)
