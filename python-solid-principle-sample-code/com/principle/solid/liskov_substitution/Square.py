from Shape import Shape


class Square(Shape):

    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def area(self):
        return self.__length ** 2
