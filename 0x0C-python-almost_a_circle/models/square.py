#!/usr/bin/python3
"""10. And now, the Square!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inhiret from Rect"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of square obj"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get size att"""
        return self.width

    @size.setter
    def size(self, size):
        """set size att"""
        self.width = size
        self.height = size

    def __update(self, id=None, size=None, x=None, y=None):
        """private update func"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """public update func for att"""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """return dict of att"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
