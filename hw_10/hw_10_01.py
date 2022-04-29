class Matrix:
    def __init__(self, matrix, start=0):
        self.matrix = matrix
        self.i = start

    def __str__(self):
        r = ''
        for row in self.matrix:
            line = ' '.join([str(x) for x in row])
            r += f'| {line} |\n'
        return r

    def __add__(self, other):
        r = []
        for row1, row2 in zip(self.matrix, other.matrix):
            r.append([(x1 + x2) for (x1, x2) in zip(row1, row2)])
        return Matrix(r)


m1 = Matrix([[1, 1, 1], [2, 2, 2]])
m2 = Matrix([[2, 2, 2], [3, 3, 3]])
m3 = m1 + m2
print(m3)
