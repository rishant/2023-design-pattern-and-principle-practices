from Shape import Shape


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def area(self):
        return self.length ** 2
