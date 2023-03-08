from typing import List

from Shape import Shape
from Circle import Circle
from Square import Square
from Cube import Cube
from Rectangle import Rectangle
from AreaCalculator import AreaCalculator
from ShapePrinter import ShapePrinter


def main():
    print('Hello World')

    circle: Circle = Circle(10)
    square: Square = Square(10)
    cube: Cube = Cube(10)
    rectangle: Rectangle = Rectangle(10, 20)

    shapes: List[Shape] = [circle, square, cube, rectangle]

    area_calculator: AreaCalculator = AreaCalculator()
    sum: int = area_calculator.sum(shapes)
    """
    Notes:
        sum: int --> This is just indication value will be type of : int but actually it is not strictly automatic
        convert. We have to do manually typecast    
    """
    print(type(sum))
    print(int(sum))

    """
        single responsibility principle violation
    """
    # print(area_calculator.json(shapes))

    """
        single responsibility principle Achieved.
    """
    shape_printer: ShapePrinter = ShapePrinter(area_calculator)
    print(shape_printer.json(shapes))
    print(shape_printer.csv(shapes))


if __name__ == "__main__":
    main()
