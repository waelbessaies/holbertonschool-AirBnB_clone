#!/usr/bin/python3
"""Serializing and deserializng instances"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects of the dictionary"""
        return self.__objects

    def new(self, obj):
        """Adds a new object in objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """"serializes __objects to the JSON file"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        """deserializes the JSON file"""
        with open(self.__file_path, 'r') as f:
            self__objects = json.load(f)
