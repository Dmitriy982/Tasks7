class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num / other.num)

    def __str__(self):
        return str(self.num)

    def make_order(self, row):
        return '\n' .join(['*' * row for i in range(self.num // row)]) + '\n' + '*' * (self.num % row)


cell1 = Cell(10)
cell2 = Cell(20)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(3))
