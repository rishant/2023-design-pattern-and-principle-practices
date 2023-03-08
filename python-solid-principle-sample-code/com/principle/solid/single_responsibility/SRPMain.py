from typing import List

from AreaCalculator import AreaCalculator
from Circle import Circle
from Shape import Shape
from ShapePrinter import ShapePrinter
from Square import Square


def main():
    print('Hello World')

    circle: Circle = Circle(10)
    square: Square = Square(10)

    shapes: List[Shape] = [circle, square]

    area_calculator: AreaCalculator = AreaCalculator()
    sum: int = area_calculator.sum(shapes)
    # Notes:
    # sum: int --> This is just indication value will be type of : int but actually it is not strictly automatic
    # convert. We have to do manually typecast
    print(type(sum))
    print(int(sum))

    # single responsibility principle violation
    # print(area_calculator.json(shapes))

    # single responsibility principle Achieved.
    shape_printer: ShapePrinter = ShapePrinter(area_calculator)
    print(shape_printer.json(shapes))
    print(shape_printer.csv(shapes))


if __name__ == "__main__":
    main()
