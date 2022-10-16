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
