#!/usr/bin/python3
"""2. First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inhitited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.validate(w, 'width')
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.validate(h, 'height')
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validate(x, 'x')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validate(y, 'y')
        self.__y = y

    def validate(self, value, name):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if name in ['width', 'height'] and value <= 0:
            raise ValueError(name + " must be > 0")
        if name in ['x', 'y'] and value < 0:
            raise ValueError(name + " must be >= 0")
