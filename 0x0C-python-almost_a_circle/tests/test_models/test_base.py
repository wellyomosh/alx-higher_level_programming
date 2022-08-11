#!/usr/bin/python3
""" Unittest for the Base class. To ensure Base works as intended """


import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases for the Base class"""

    def setUp(cls):
        """ Resets object. For id use """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Testing for valid id """
        a = Base()
        self.assertEqual(a.id, 1)
        a = Base()
        self.assertEqual(a.id, 2)
        a = Base(92)
        self.assertEqual(a.id, 92)
        a = Base()
        self.assertEqual(a.id, 3)
        a = Base(32767)
        self.assertEqual(a.id, 32767)
        a = Base(-1)
        self.assertEqual(a.id, -1)

    def test_json_string(self):
        """ Testing for valid json conversion """
        a = Base.to_json_string([])
        self.assertEqual(a, "[]")
        a = Base.to_json_string([{'plushie': 'kingdom'}])
        self.assertEqual(a, '[{"plushie": "kingdom"}]')
        a = {'x': 0, 'y': 0, 'width': 2, 'height': 4, 'id': 999}
        b = Base.to_json_string(a)
        self.assertEqual(Base.from_json_string(b), a)


if __name__ == '__main__':
    unittest.main()
