#!/usr/bin/python3
""" Module for a Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ Represents a Rectangle class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width of the Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        self.int_valid_method("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ Height of the Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        self.int_valid_method("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ x coordinate of the Rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        self.int_valid_method("x", value)
        self.__x = value

    @property
    def y(self):
        """ y coordinate of the Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        self.int_valid_method("y", value)
        self.__y = value

    def int_valid_method(self, name, value, equal=True):
        """ Method for value validation """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if equal and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not equal and value <= 0:
            raise ValueError("{} must be > 0".format(name))
