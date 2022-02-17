"""
Задание 2
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(first_name, last_name, date_of_birth, city_of_residence, email, phone_number):
    return print(f"Данные пользователя: {first_name} {last_name}, {date_of_birth}, {city_of_residence}, {email}, {phone_number}")


Name = input("Введите имя: ")
Surname = input("Введите фамилию: ")
Birthday = input("Введите дату рождения: ")
City = input("Введите город проживания: ")
Email = input("Введите email: ")
Phone = input("Введите телефон: ")

user_data(Name, Surname, Birthday, City, Email, Phone)
