"""
Задание 7
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
"""

import json

with open("text_7.txt", "r") as f_obj:
    list_of_lists = []
    for line in f_obj:
        list_of_lists.append(line.strip().split())

    profit_dict = {}
    av_profit = 0
    for el in list_of_lists:
        profit = int(el[2]) - int(el[3])
        profit_dict[el[0]] = profit
        if profit > 0:
            av_profit += (profit / len([i for i in list_of_lists if int(i[2]) - int(i[3]) > 0]))

    av_profit_dict = dict(average_profit=round(av_profit, 2))

    final_list = [profit_dict, av_profit_dict]

    print(final_list)

    with open("out_json_7.json", "w") as write_f:
        json.dump(final_list, write_f)
