#!/usr/bin/python3
""" Unittest for the Rectangle class.
To ensure Rectangle is working as intended """

import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle


class RectangleTesting(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def setUp(cls):
        """ Resets object to 0. For id """
        Base._Base__nb_objects = 0

    def test_rec(self):
        """ Test for valid rectangle """
        rec = Rectangle(1, 5)
        self.assertEqual(type(rec.width), int)
        self.assertEqual(type(rec.height), int)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y, rec.id),
                         (1, 5, 0, 0, 1))
        rec = Rectangle(3, 3, 1)
        self.assertEqual((rec.width, rec.height, rec.x, rec.y, rec.id),
                        (3, 3, 1, 0, 2))
        with self.assertRaises(TypeError):
            rec = Rectangle("Potato", 1)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -99)

    def test_area(self):
        """ Test for correct area calculation """
        rec = Rectangle(5, 5)
        self.assertEqual(rec.area(), 25)
        rec = Rectangle(6, 11, 2, 7, 32767)
        self.assertEqual(rec.area(), 66)

    def test_text(self):
        """Tests for correct syntax """
        rec = Rectangle(9, 7, 8, 2, 5)
        rec_line = "[Rectangle] ({}) {}/{} - {}/{}".format(
                rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), rec_line)
        rec.update(77)
        rec_line = "[Rectangle] ({}) {}/{} - {}/{}".format(
                rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), rec_line)
        rec.update(55, 6, 1)
        rec_line = "[Rectangle] ({}) {}/{} - {}/{}".format(
                rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), rec_line)
        rec.update(id=9853, width=10, y=0)
        rec_line = "[Rectangle] ({}) {}/{} - {}/{}".format(
                rec.id, rec.x, rec.y, rec.width, rec.height)
        self.assertEqual(str(rec), rec_line)


if __name__ == '__main__':
    unittest.main()
