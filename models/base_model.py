#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class defining all common attributes and methods for the other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            """removes __class__ because it is present when creating an instance from a dictionary"""
            kwargs.pop('__class__', None)

            """Converts 'created_at' and 'updated_at' strings to datetime objects using strptime method"""
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

            """Assign kwargs key-value pairs as instance attributes"""
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            """If no keywords in kwargs these instant variables are set"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """prints what base class is and what it does"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """public instance method that updates updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values"""
        base_model_dict = self.__dict__.copy()
        """returns only the instance attributes"""
        base_model_dict['__class__'] = self.__class__.__name__
        base_model_dict['created_at'] = self.created_at.isoformat()
        base_model_dict['updated_at'] = self.updated_at.isoformat()
        return base_model_dict
