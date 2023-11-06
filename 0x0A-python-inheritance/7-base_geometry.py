#!/usr/bin/python3
""" 5. Geometry module """


class BaseGeometry:
    """ BaseGeometry (based on 6-base_geometry.py)"""

    def area(self):
        """ Area that raise exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value

        Raises:
            TypeError: if value not int
            ValueError: if value less than zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
