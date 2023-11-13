#!/usr/bin/python3
"""1. Base class"""
import json
from os import path
import csv


class Base:
    """Base class with private attr nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base class initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [o.to_dictionary() for o in list_objs]

        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        else:
            return None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            with open('{}.csv'.format(cls.__name__), 'w', newline='') as f:
                writer = csv.writer(f)
                for o in list_objs:
                    if o is Rectangle:
                        writer.writerow([o.id, o.width, o.height, o.x, o.y])
                    elif o is Square:
                        writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        from models.rectangle import Rectangle
        from models.square import Square

        file = "{}.csv".format(cls.__name__)
        if not path.isfile(file):
            return []

        with open(file, "r", newline='') as f:
            reader = csv.reader(f)
            list_return = []
            header = next(reader, None)

            for row in reader:
                d = {header[i]: int(row[i]) for i in range(len(header))}
                list_return.append(cls.create(**d))

            return list_return
