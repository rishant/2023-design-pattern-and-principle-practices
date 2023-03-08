from typing import List

from Shape import Shape
from Square import Square
from AreaCalculator import AreaCalculator
from AreaCalculatorV2 import AreaCalculatorV2
from ShapePrinter import ShapePrinter
from IAreaCalculator import IAreaCalculator


def main():
    print('Hello World')

    square: Square = Square(10)

    shapes: List[Shape] = [square]

    area_calculator: IAreaCalculator = AreaCalculator()
    """ Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand. """
    shape_printer: ShapePrinter = ShapePrinter(area_calculator)
    print(shape_printer.json(shapes))
    print(shape_printer.csv(shapes))

    area_calculator: IAreaCalculator = AreaCalculatorV2()
    """ Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand. """
    shape_printer: ShapePrinter = ShapePrinter(area_calculator)
    print(shape_printer.json(shapes))
    print(shape_printer.csv(shapes))


if __name__ == "__main__":
    main()
