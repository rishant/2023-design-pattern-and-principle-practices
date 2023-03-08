from math import pi

from Shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return pi * self.radius ** 2
