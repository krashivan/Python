"""
Задание 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, rows: list):
        self.rows = rows

    def __str__(self):
        return "\n".join(" ".join(str(el) for el in row) for row in self.rows)

    def add(self, matrix_to_add):
        result_matrix = []
        for row in range(len(self.rows)):
            result_matrix.append([0 for el in self.rows[row]])
            for el in range(len(self.rows[row])):
                result_matrix[row][el] = self.rows[row][el] + matrix_to_add.rows[row][el]
        return Matrix(result_matrix)


m1 = Matrix([[100, 200], [300, 400]])
m2 = Matrix([[500, 600], [700, 800]])

print(m1.add(m2))
