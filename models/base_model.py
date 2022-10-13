#!/usr/bin/python3
"""this is the base model"""

from datetime import datetime
from uuid import uuid4


class Basemodel:
    """a class"""

    def __init__(self):
        """Public instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


def __str__(self):
    """return [<class name>] (<self.id>) <self.__dict__>"""
    return "[{}] ({}) {}".format(
        self.__class__.__name__, self.id, self.__dict__)


def save(self):
    """updates the public instance attribute updated_at """
    self.updated_at = datetime.now()


def to_dict(self):
    """returns a dictionary containing all keys/values of __dict__ """
    my_dict = self.__dict__.copy()
    my_dict['__class__'] = self.__class__.__name__
    my_dict['created_at'] = self.created_at.isoformat()
    my_dict['updated_at'] = self.updated_at.isoformat()
    return my_dict
