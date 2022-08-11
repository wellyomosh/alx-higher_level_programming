#!/usr/bin/python3
""" This file imports the code found in /models/rectangle.py """
from models.rectangle import Rectangle
""" Square class """


class Square(Rectangle):
    """ Square class. Imports the Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def __str__(self):
        """ str() function, overloaded """
        return ("[{}] ({}) {}/{} - {}".format("Square", self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """ Size getter function """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """ Update function. Allows for changing values
        and supports *args and **kwargs """
        length = len(args)
        if length is not 0:
            for num in range(length):
                if num is 0:
                    self.id = args[num]
                elif num is 1:
                    self.width = args[num]
                elif num is 2:
                    self.x = args[num]
                elif num is 3:
                    self.y = args[num]
        else:
            for key, value in kwargs.items():
                if key in "id":
                    self.id = value
                elif key in "size":
                    self.width = value
                elif key in "x":
                    self.x = value
                elif key in "y":
                    self.y = value

    def to_dictionary(self):
        """ Dictionary function. Allows setting of parameters
        into a convenient dictionary """
        sq_dict = {'id': 0, 'size': 0, 'x': 0, 'y': 0}
        sq_dict['id'] = self.id
        sq_dict['size'] = self.width
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y
        return sq_dict
