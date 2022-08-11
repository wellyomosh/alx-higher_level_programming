#!/usr/bin/python3
""" Unittest for the Square base.
To ensure the Square works as intended """

import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTesting(unittest.TestCase):
    """ Test cases for the Square class """

    def setUp(self):
        """ Resets object to 0. For id use """
        Base._base__nbobjects = 0

    def test_square(self):
        """ Test for valid square """
        sq = Square(5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        sq2 = Square(9, 2, 5, 99)
        self.assertEqual(sq2.width, 9)
        self.assertEqual(sq2.height, 9)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 5)
        self.assertEqual(sq2.id, 99)

    def test_area(self):
        """ Test for valid area calculation """
        sq = Square(7)
        self.assertEqual(sq.area(), 49)
        sq2 = Square(20, 2, 4, 8)
        self.assertEqual(sq2.area(), 400)

    def test_text(self):
        """Tests representation"""
        sq = Square(9, 7, 8, 2)
        sq_line = "[Square] ({}) {}/{} - {}".format(
                sq.id, sq.x, sq.y, sq.size)
        self.assertEqual(str(sq), sq_line)
        sq.update(77)
        sq_line = "[Square] ({}) {}/{} - {}".format(
                sq.id, sq.x, sq.y, sq.size)
        self.assertEqual(str(sq), sq_line)
        sq.update(77, 5, 1)
        sq_line = "[Square] ({}) {}/{} - {}".format(
                sq.id, sq.x, sq.y, sq.size)
        self.assertEqual(str(sq), sq_line)
        sq.update(id=325, x=7)
        sq_line = "[Square] ({}) {}/{} - {}".format(
                sq.id, sq.x, sq.y, sq.size)
        self.assertEqual(str(sq), sq_line)

if __name__ == '__main__':
    unittest.main()
