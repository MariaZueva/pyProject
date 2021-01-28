class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f"{self.r} + {self.i}*i" if self.i > 0 else f"{self.r} - {abs(self.i)}*i"

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)


complex_1 = Complex(-2, -3)
complex_2 = Complex(4, -3)
print(complex_1 + complex_2)
print(complex_1 * complex_2)