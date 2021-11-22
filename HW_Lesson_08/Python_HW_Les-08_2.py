"""
Задание 2

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionNew(Exception):

    def __str__(self) -> str:
        return "Произведено деление на НОЛЬ!!!"


try:
    numerator = int(input("Введите числитель: "))
    denominator = int(input("Введите знаменатель: "))
    if denominator == 0:
        raise ZeroDivisionNew
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionNew as err:
    print(err)
else:
    print(f"{numerator} / {denominator} = {numerator / denominator}")
