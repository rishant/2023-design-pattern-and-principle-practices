from Shape import Shape


class Cube(Shape):

    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def area(self):
        # formula A = 6a2
        return 6 * self.__length ** 2
