class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'


newCircle = Circle(5, 10, 100)
print(newCircle)