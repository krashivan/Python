"""
Задание 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("text_3.txt", "r") as f_obj:
    surn_sal_list = []
    for line in f_obj:
        new_list = line.strip().split()
        surn_sal_list.append(list([new_list[0], new_list[1]]))

    salary_list = [float(i[1]) for i in surn_sal_list]

    print("Сотрудники с зарплатой менее 20000: ", *[i[0] for i in surn_sal_list if float(i[1]) < 20000])
    print(f"Средняя зарплата сотруников: {sum(salary_list) / len(salary_list):.2f}")
