"""
Задание 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    print("Сумма двух наибольших аргументов = ", arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3))


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

my_func(a, b, c)