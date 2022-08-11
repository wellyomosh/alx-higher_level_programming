#!/usr/bin/python3
""" This file imports the code found in /models/base.py """
from models.base import Base
""" Rectangle class """


class Rectangle(Base):
    """ Rectangle class. Imports the Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter function """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ X getter function """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter function """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y getter function """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter function """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area function. Returns the area """
        return self.__width * self.__height

    def display(self):
        """ Display function. Prints and shifts the shape with '#' """
        for i in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ str() function, overloaded """
        return ("[{}] ({}) {}/{} - {}/{}".format("Rectangle",
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Update function. Allows for changing values and
        supports *args and **kwargs """
        length = len(args)
        if length is not 0:
            for num in range(length):
                if num is 0:
                    self.id = args[0]
                elif num is 1:
                    self.__width = args[1]
                elif num is 2:
                    self.__height = args[2]
                elif num is 3:
                    self.__x = args[3]
                elif num is 4:
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key in "id":
                    self.id = value
                elif key in "width":
                    self.__width = value
                elif key in "height":
                    self.__height = value
                elif key in "x":
                    self.__x = value
                elif key in "y":
                    self.__y = value

    def to_dictionary(self):
        """ Dictionary function. Allows setting of parameters
        into a convenient dictionary """
        rec_dict = {'x': 0, 'y': 0, 'id': 0, 'height': 0, 'width': 0}
        rec_dict['x'] = self.__x
        rec_dict['y'] = self.__y
        rec_dict['id'] = self.id
        rec_dict['height'] = self.__height
        rec_dict['width'] = self.__width
        return rec_dict
