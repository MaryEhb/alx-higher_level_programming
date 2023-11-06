#!/usr/bin/python3
""" 10. Square #1 """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return super().area()

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
