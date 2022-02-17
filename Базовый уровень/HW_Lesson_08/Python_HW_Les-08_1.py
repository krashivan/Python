"""
Задание 1

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date_init: str):
        numbers = Date.get_numbers(date_init)
        Date.validation(numbers)
        self.day = Date.get_numbers(date_init)[0]
        self.month = Date.get_numbers(date_init)[1]
        self.year = Date.get_numbers(date_init)[2]

    def __str__(self):
        return (f"{self.day:02}.{self.month:02}.{self.year}")

    @classmethod
    def get_numbers(cls, date_init):
        return *(int(i) for i in date_init.strip().split("-")),

    @staticmethod
    def validation(numbers):
        day, month, year = numbers
        assert 1 <= day < 32, "Неправильно введен день"
        assert 1 <= month < 13, "Неправильно введен месяц"
        assert 0 <= year < 2022, "Неправильно введен год (требуется текущая эра до текущего года)"


print(Date("01-08-2021"))
