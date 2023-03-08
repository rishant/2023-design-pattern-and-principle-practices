from Shape import Shape
from IllegalStateException import IllegalStateException


class NoShape(Shape):

    def __init__(self):
        pass

    """
        Liskov Substitution Principle violation - It is Substitution able, Even if we don't override.
        We have to either provide Interface `Default` implementation /or/ `Abstract` Class for Substitution
    """
    def area(self):
        raise IllegalStateException("Cannot calculate area")
