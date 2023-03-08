from typing import List

from Shape import Shape
from Cube import Cube
from Rectangle import Rectangle
from ThreeDimensionalShape import ThreeDimensionalShape


def main():
    print('Hello World')

    cube: Cube = Cube(10)
    rectangle: Rectangle = Rectangle(10, 20)

    shapes: List[Shape] = [cube, rectangle]

    for shape in shapes:
        print("{{shapes_sum: {}}}".format(int(shape.area())))

    for shape in shapes:
        if isinstance(shape, ThreeDimensionalShape):
            print("{{shapes_volume: {}}}".format(int(shape.volume())))


if __name__ == "__main__":
    main()
