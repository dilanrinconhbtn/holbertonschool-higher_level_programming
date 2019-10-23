#!/usr/bin/python3
""" This module create Class Base.
The “base” of all other classes in this project
See:
    ./17-main.py test file
"""

import json


class Base:
    """ Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialitation
        Args:
            id: Numeric númber
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or list_dictionaries == []:
            return str("[]")
        else:
            return json.dumps(list_dictionaries)
