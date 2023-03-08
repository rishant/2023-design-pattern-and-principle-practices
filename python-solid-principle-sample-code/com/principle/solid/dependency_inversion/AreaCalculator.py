from Shape import Shape
from typing import List
from IAreaCalculator import IAreaCalculator


class AreaCalculator(IAreaCalculator):

    def sum(self, shapes: List[Shape]):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()

        return total_area
