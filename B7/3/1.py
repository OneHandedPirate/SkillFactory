class Box:
    def __init__(self):
        self.__weight = 0

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight < 0:
            raise ValueError('negative weight')
        self.__weight = new_weight


b = Box()

print(b.weight)
b.weight = 1200
print(b.weight)

