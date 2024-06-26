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
        """ Method for value validation. """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif equal and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not equal and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Calculates the Area of the Rectangle. """
        return (self.width * self.height)

    def display(self):
        """ Prints the String representation of the Rectangle. """
        string = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(string, end='')

    def __str__(self):
        """ Returns the string information of the Rectangle. """
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def __rec_update(self, id=None, width=None, height=None, x=None, y=None):
        """ Method to update the instance attributes. """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def rec_update(self, *args, **kwargs):
        """ Updates the instance attributes through no-key and keyword args. """
        # print(args, kwargs)

        if args:
            self.__rec_update(*args)
        elif kwargs:
            self.__rec_update(**kwargs)
