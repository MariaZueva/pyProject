class Cell:
    def __init__(self, num=0.0):
        self.num = round(num)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if (self.num - other.num) >= 0:
            return Cell(self.num - other.num)
        else:
            print("Вычитание невозможно")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, k):
        return '\n'.join(['*' * k for i in range(0, self.num // k)]) + '\n' + '*' * (self.num % k)

    def __str__(self):
        return f"{self.num}"


cell_one = Cell(13)
cell_two = Cell(7)

cell_three = cell_one + cell_two
print(cell_three)

cell_three = cell_one - cell_two
print(cell_three)

cell_three = cell_one * cell_two
print(cell_three)

cell_three = cell_one // cell_two
print(cell_three)

print(cell_one.make_order(4))
