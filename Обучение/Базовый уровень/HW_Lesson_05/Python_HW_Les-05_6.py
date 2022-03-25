"""
Задание 6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

find_number = re.compile(r'(\d+)')


def extract_num(s):
    try:
        return int(find_number.search(s).group(1))
    except AttributeError:
        return 0


with open("text_6.txt", "r") as f_obj:
    list_of_lists = []
    for line in f_obj:
        list_of_lists.append(line.strip().split())

    new_dict = {}
    for el1 in list_of_lists:
        subj_sum = 0
        for el2 in el1:
            subj_sum += extract_num(el2)
        new_dict[el1[0].rstrip(':')] = subj_sum

    print(new_dict)
