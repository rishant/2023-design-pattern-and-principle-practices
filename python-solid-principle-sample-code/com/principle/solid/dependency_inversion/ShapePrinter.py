from IAreaCalculator import IAreaCalculator


class ShapePrinter:

    """
        Dependency Inversion Violation - Taking Concreted Class Reference.
    """
    # def __init__(self, area_calculator: AreaCalculator):
    #     self.__area_calculator = area_calculator

    """
        Dependency Inversion Achieved - Instead of Concreted Class take a Interface Reference and Inject on-demand.
    """
    def __init__(self, area_calculator: IAreaCalculator):
        self.__area_calculator = area_calculator

    def json(self, shapes):
        return "{{shapes_sum: {}}}".format(int(self.__area_calculator.sum(shapes)))

    def csv(self, shapes):
        return "shapes_sum,{}".format(int(self.__area_calculator.sum(shapes)))
