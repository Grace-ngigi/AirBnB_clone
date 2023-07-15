#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test instance variables"""

    def test_init(self):
        kwargs = {
            'id': 'e3a73f8c-2ef1-4f4d-8a93-ae67e87d23be',
            'created_at': '2023-07-11T3:30:00.000000',
            'updated_at': '2023-07-11T3:30:00.000000',
            'name': 'Test Model'
        }

        model = BaseModel(**kwargs)

        self.assertEqual(model.id, 'e3a73f8c-2ef1-4f4d-8a93-ae67e87d23be')
        self.assertEqual(model.name, 'Test Model')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, datetime(2023, 7, 11, 3, 30, 0))
        self.assertEqual(model.updated_at, datetime(2023, 7, 11, 3, 30, 0))

    def test_init_without_kwargs(self):
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_invalid_kwargs(self):
        kwargs = {
            '__class__': 'InvalidClass',
            'created_at': '2023-07-11T3:30:00.000000',
            'updated_at': '2023-07-11T3:30:00.000000',
            'name': 'Test Model'
        }

        model = BaseModel(**kwargs)

        self.assertEqual(model.__class__.__name__, 'BaseModel')
        self.assertEqual(model.name, 'Test Model')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, datetime(2023, 7, 11, 3, 30, 0))
        self.assertEqual(model.updated_at, datetime(2023, 7, 11, 3, 30, 0))


    def test_save(self):
        """test save function to assert that chnages are being made"""
        model = BaseModel()
        original_updated_at = model.updated_at

        """Simulate a delay of 2 seconds"""
        import time
        time.sleep(2)

        model.save()

        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_to_dict(self):
        """test__dict__ to assert the dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

        created_at = datetime.fromisoformat(model_dict['created_at'])
        updated_at = datetime.fromisoformat(model_dict['updated_at'])

        self.assertEqual(model.id, model_dict['id'])
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_str(self):
        """test __str__ to assert the output is the expected output"""
        model = BaseModel()
        model_str = str(model)

        self.assertEqual(model_str, (
            "[BaseModel] ({}) {}".format(model.id, model.__dict__)))


if __name__ == '__main__':
    unittest.main()
