class Square:
    def __init__(self, a):
        self.a = a
    def get_area(self):
        return self.a * self.a
    def get_side(self):
        return self.a


class SquareFactory:

    @staticmethod
    def c_square(side):
        return Square(side)


randomSquare = SquareFactory()

square1 = randomSquare.c_square(5)
square2 = randomSquare.c_square(10)
square3 = randomSquare.c_square(15)

print(isinstance(square1, SquareFactory))
print(isinstance(square1, Square))

square4 = SquareFactory.c_square(5)
print(square4.__dir__())