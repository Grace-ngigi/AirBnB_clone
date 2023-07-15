#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class defining all common attributes and methods for the other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """prints what base class is and what it does"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """public instance method that updates updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values"""
        base_model_dict = self.__dict__.copy()
        """returns only the instance attributes"""
        base_model_dict['__class__'] = self.__class__.__name__
        base_model_dict['created_at'] = self.created_at.isoformat()
        base_model_dict['updated_at'] = self.updated_at.isoformat()
        return base_model_dict
