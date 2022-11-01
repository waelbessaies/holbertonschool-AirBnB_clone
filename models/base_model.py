#!/usr/bin/python3
"""CONSOLE"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """Base class"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = str(v)
                elif k == "created_at":
                    self.created_at = datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            models.storage.new(self)

    def __str__(self):
        """Print"""
        return "[{}] ({}) {}". format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionnary  with all keys and values"""

        Newdict = self.__dict__.copy()
        Newdict["created_at"] = self.created_at.isoformat()
        Newdict["updated_at"] = self.updated_at.isoformat()
        Newdict["__class__"] = self.__class__.__name__
        return Newdict
