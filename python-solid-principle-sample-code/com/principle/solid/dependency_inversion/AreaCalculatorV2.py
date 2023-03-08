from Shape import Shape
from typing import List
from IAreaCalculator import IAreaCalculator


class AreaCalculatorV2(IAreaCalculator):

    def sum(self, shapes: List[Shape]):
        total_area = 0
        for shape in shapes:
            total_area += shape.area() * 5

        return total_area
