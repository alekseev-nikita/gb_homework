class Cplx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}{"+" if self.y >= 0 else ""}{self.y}j'

    def __add__(self, other):
        return Cplx(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        x = (self.x * other.x) - (self.y * other.y)
        y = (self.x * other.y) + (self.y * other.x)
        return Cplx(x, y)


c1 = Cplx(4, 6)
c2 = Cplx(-2, -7)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)
