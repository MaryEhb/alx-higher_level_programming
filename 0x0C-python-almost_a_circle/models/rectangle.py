#!/usr/bin/python3
"""2. First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inhitited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
