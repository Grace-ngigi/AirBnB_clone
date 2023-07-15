#!/usr/bin/python3
import json


class FileStorage():
    """Serializes and deserializes JSON instances"""
    __file_path = "file.json"
    __objects = {}

    def get_file_path(self):
        return self.__file_path

    def get_objects(self):
        return self.__objects

    def all(self):
        """return all objects"""
        return self.__objects

    def new(self, obj):
        """sets in objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file for storage"""
        obj_to_save = {}
        for key, obj in self.__objects.items():
            obj_to_save[key] = obj.to_dict()

        """open json file and save the object"""
        with open(self.__file_path, 'w') as f:
            json.dump(obj_to_save, f)

    def reload(self):
        """deserialize JSON file to objects if it exists"""
        from models.base_model import BaseModel
        try:
            """attempt to open file in __file_path path and deserialise it"""
            with open(self.__file_path, 'r') as f:
                objt = json.load(f)
            

            for key, value in objt.items():
                """splits the key into class_name and obj_id"""
                class_name, objt_id = key.split('.')
                name_class = BaseModel

                """if class name is available in globals retrieve class object"""
                if class_name in globals():
                    name_class = globals()[class_name]

                    """create the object of the class"""
                obj = name_class(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
 
