from typing import List

from Shape import Shape
from Circle import Circle
from Square import Square
from AreaCalculator import AreaCalculator
from ShapePrinter import ShapePrinter
from Cube import Cube
from Rectangle import Rectangle
from NoShape import NoShape
from NoShapeV2 import NoShapeV2

def main():
    print('Hello World')
    circle: Circle = Circle(10)
    square: Square = Square(10)
    cube: Cube = Cube(10)
    rectangle: Rectangle = Rectangle(10, 20)
    """
        Liskov Substitution Principle violation - It is Substitution able, Even if we don't override.
    """
    # no_shape: NoShape = NoShape()
    # shapes: List[Shape] = [circle, square, cube, rectangle, no_shape]

    """
        Liskov Substitution Principle Achieved - using `Abstract` Class for Substitution
    """
    no_shape_v2: NoShapeV2 = NoShapeV2()
    shapes: List[Shape] = [circle, square, cube, rectangle, no_shape_v2]

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
