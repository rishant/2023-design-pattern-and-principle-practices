from math import pi
from typing import List

from Shape import Shape
from Circle import Circle
from Square import Square
from Cube import Cube
from Rectangle import Rectangle


class AreaCalculator:

    def sum(self, shapes: List[Shape]):
        total_area = 0
        for shape in shapes:
            # if isinstance(shape, Square):
            #     total_area += shape.get_length() ** 2
            # if isinstance(shape, Circle):
            #     total_area += pi * shape.get_radius() ** 2

            """
                Open Closed Principle violation - It is Open for Modification but it should be Open for Extension
            """
            # if isinstance(shape, Cube):
            #     total_area += 6 * shape.get_length() ** 2

            """
                Open Closed Principle Achieved - Using Interface
            """
            total_area += shape.area()

        return total_area

    """
        single responsibility principle violation
    """
    # def json(self, shapes):
    #     return "{{sum: {}}}".format(int(self.sum(shapes)))
