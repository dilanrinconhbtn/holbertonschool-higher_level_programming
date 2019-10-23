#!/usr/bin/python3
"""Class Base."""

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json String to a file"""
        filename = cls.__name__ + ".json"

        lista = []
        if list_objs:
            for x in list_objs:
                r = x.to_dictionary()
                lista.append(r)
        diccionario = cls.to_json_string(lista)
        with open(filename, mode='w') as f:
            f.write(diccionario)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""

        lista = []
        if json_string:
            return json.loads(json_string)
        else:
            return lista

    @classmethod
    def create(cls, **dictionary):
        """create function"""

        if cls.__name__ == "Rectangle":
            dummie = cls(1, 10)
        elif cls.__name__ == "Square":
            dummie = cls(2)
        dummie.update(**dictionary)
        return dummie

    @classmethod
    def load_from_file(cls):
        """load_from_file function"""
        lista = []
        string = ""
        try:
            with open(cls.__name__ + ".json") as f:
                string = f.read()
                otra = Base.from_json_string(string)
            for elements in otra:
                lista.append(cls.create(**elements))
        except Exception:
            return lista

        return lista
