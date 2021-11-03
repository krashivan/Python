"""
Задание 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def div(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("Произведено деление на ноль")
        return


dividend_1 = int(input('Введите делимое: '))
divisor_1 = int(input('Введите делитель: '))

print(f"{dividend_1} / {divisor_1} = {div(dividend_1, divisor_1)}")
