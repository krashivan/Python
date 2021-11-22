"""
Задание 7

Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __add__(self, other):
        new_re = self.re + other.re
        new_im = self.im + other.im
        return f"{new_re} + {new_im}i"

    def __mul__(self, other):
        new_re_1 = self.re * other.re
        new_re_2 = self.im * other.im
        new_im_1 = self.re * other.im
        new_im_2 = self.im * other.re
        return f"{new_re_1 - new_re_2} + {new_im_1 + new_im_2}i"


a = Complex(5, 10)
b = Complex(25, 17)
print(a + b)
print(a * b)
