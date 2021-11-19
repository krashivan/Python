"""
Задание 3
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
"""


class Cell:

    def __init__(self, cell_parameter: int):
        self.cell_parameter = cell_parameter

    def __str__(self):
        return f"{self.cell_parameter}"

    def __add__(self, other):
        return Cell(round(self.cell_parameter + other.cell_parameter))

    def __sub__(self, other):
        if self.cell_parameter - other.cell_parameter > 0:
            return Cell(round(self.cell_parameter - other.cell_parameter))
        else:
            return "Итоговое количество ячеек меньше или равно 0"

    def __mul__(self, other):
        return Cell(self.cell_parameter * other.cell_parameter)

    def __truediv__(self, other):
        return Cell(self.cell_parameter // other.cell_parameter)

    def make_order(self, quantity):
        rows = self.cell_parameter // quantity
        return "{0}\n{1}".format('\n'.join(''.join('*' for i in range(quantity)) for i in range(rows)),
                                 "".join("*" for i in range(self.cell_parameter % quantity)))


cell1 = Cell(18)
cell2 = Cell(4)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)

print(cell1.make_order(5))
