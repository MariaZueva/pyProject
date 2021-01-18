class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __del__(self):
        print("Object deleted")

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        res = []
        try:
            for i in range(0, len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise IndexError
                res.append([])
                for j in range(0, len(self.matrix[i])):
                    res[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(res)
        except IndexError:
            return "Матрицы должны быть одного размера"


my_matrix_1 = Matrix([[2, 3], [4, 5]])
my_matrix_2 = Matrix([[2, 3], [4, 5]])
print(my_matrix_1 + my_matrix_2)
