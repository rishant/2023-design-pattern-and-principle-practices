from math import pi
from typing import List

from Circle import Circle
from Shape import Shape
from Square import Square


class AreaCalculator:

    def sum(self, shapes: List[Shape]):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Square):
                total_area += shape.getLength() ** 2
            if isinstance(shape, Circle):
                total_area += shape.getRadius() ** 2 * pi
        return total_area

    # single responsibility principle violation
    # def json(self, shapes):
    #     return "{{sum: {}}}".format(int(self.sum(shapes)))

