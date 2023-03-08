from AreaCalculator import AreaCalculator


class ShapePrinter:

    def __init__(self, area_calculator: AreaCalculator):
        self.__area_calculator = area_calculator

    def json(self, shapes):
        return "{{shapes_sum: {}}}".format(int(self.__area_calculator.sum(shapes)))

    def csv(self, shapes):
        return "shapes_sum,{}".format(int(self.__area_calculator.sum(shapes)))