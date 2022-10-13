class Square:
    __a = None
    def __init__(self, a):
        if a > 0:
            self.__a = a
        else:
            print('Сторона не может быть отрицательной')

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value > 0:
            self.__a = value


s = Square(10)

print(s.__dir__())
print(s.a)

s.a = 100

print(s.a)