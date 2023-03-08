from Shape import Shape
from ThreeDimensionalShape import ThreeDimensionalShape

"""
    Interface Segregation Principle Achieved - Used Both separate Interface for Add-On Feature into Existing Application
"""


class Cube(Shape, ThreeDimensionalShape):

    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def area(self):
        # formula A = 6a2
        return 6 * self.__length ** 2

    def volume(self):
        # formula A = a3
        return self.__length ** 3
