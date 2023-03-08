from Shape import Shape
from AbstractShape import AbstractShape
from IllegalStateException import IllegalStateException

"""
    Liskov Substitution Principle Achieved - using `Abstract` Class for Substitution
"""


# class NoShapeV2(Shape):
class NoShapeV2(AbstractShape):

    def __init__(self):
        pass

    """
        Liskov Substitution Principle violation - It is Substitution able, Even if we don't override.
        We have to either provide Interface `Default` implementation /or/ `Abstract` Class for Substitution
    """
    # def area(self):
    # raise IllegalStateException("Cannot calculate area")
