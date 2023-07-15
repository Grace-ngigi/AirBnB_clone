#!/usr/bin/python3
import unittest
import json
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage = None

    def test_all(self):
        """Adding objects to storage"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        """Retrieving all objects"""
        all_objects = self.storage.all()

        """Checking if objects are present in the returned dictionary"""
        self.assertIn("BaseModel.{}".format(obj1.id), all_objects)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objects)

    def test_new(self):
        # Creating a new object
        obj = BaseModel()
        self.storage.new(obj)

        """Checking if the object is present in the storage dictionary"""
        self.assertIn(
                "BaseModel.{}".format(obj.id),
                self.storage.get_objects())

        self.assertEqual(
                self.storage.get_objects()
                ["BaseModel.{}".format(obj.id)], obj)

    def test_save(self):
        """Creating a mock file object"""
        with patch("builtins.open") as mock:
            mock_file = mock.return_value.__enter__.return_value
            # Adding objects to storage
            obj1 = BaseModel()
            obj2 = BaseModel()
            self.storage.new(obj1)
            self.storage.new(obj2)

            # Calling the save method
            self.storage.save()

    def test_reload(self):
        """Testing reload function"""
        with patch("builtins.open") as mock_open:
            # Creating a mock JSON content
            mock_json = {
                "BaseModel.1234": {
                    "id": "1234",
                    "created_at": "2023-07-11T00:00:00.000000",
                    "updated_at": "2023-07-11T00:00:00.000000"
                }
            }

            # Setting the return value of mock_open
            mock_open.return_value.__enter__.return_value.read.return_value = (
                json.dumps(mock_json)
            )

            # Calling the reload method
            self.storage.reload()

            """Checking if the object is present in the storage dictionary"""
            self.assertIn("BaseModel.1234", self.storage.get_objects())
            self.assertEqual(
                    self.storage.get_objects()["BaseModel.1234"].id, "1234")
            self.assertEqual(
                self.storage.get_objects()["BaseModel.1234"].created_at,
                datetime.fromisoformat("2023-07-11T00:00:00.000000")
            )
            self.assertEqual(
                self.storage.get_objects()["BaseModel.1234"].updated_at,
                datetime.fromisoformat("2023-07-11T00:00:00.000000")
            )


if __name__ == '__main__':
    unittest.main()
