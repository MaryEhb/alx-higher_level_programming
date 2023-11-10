#!/usr/bin/python3
"""2. First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inhitited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .\
            format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """get width att"""
        return self.__width

    @width.setter
    def width(self, w):
        """set width att"""
        self.validate(w, 'width')
        self.__width = w

    @property
    def height(self):
        """get height att"""
        return self.__height

    @height.setter
    def height(self, h):
        """set height att"""
        self.validate(h, 'height')
        self.__height = h

    @property
    def x(self):
        """get x att"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x att"""
        self.validate(x, 'x')
        self.__x = x

    @property
    def y(self):
        """get y att"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y att"""
        self.validate(y, 'y')
        self.__y = y

    def validate(self, value, name):
        """validate inputs before setting"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if name in ['width', 'height'] and value <= 0:
            raise ValueError(name + " must be > 0")
        if name in ['x', 'y'] and value < 0:
            raise ValueError(name + " must be >= 0")

    def area(self):
        """calc area or rect"""
        return self.height * self.width

    def display(self):
        """prints the rect"""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """private update fun"""
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

    def update(self, *args, **kwargs):
        """public update fun"""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """return dic of att"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
