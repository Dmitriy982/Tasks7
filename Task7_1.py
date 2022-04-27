a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix)))

    def __str__(self):
        return '\n'.join(map(str, self.matrix))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(matrix_1 + matrix_2)
