from Shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return pi * self.__radius ** 2
