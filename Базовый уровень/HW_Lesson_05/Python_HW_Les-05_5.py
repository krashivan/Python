"""
Задание 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("out_text_5.txt", "w") as f_obj_1:
    number_list = input('\nВведите целые числа, разделённые только пробелами: ').strip().split()
    i = 0
    for el in number_list:
        f_obj_1.write(f"{el}\n")

with open("out_text_5.txt", "r") as f_obj_2:
    new_list = []
    for line in f_obj_2:
        new_list.append(int(line.strip('\n')))

    print(f"Сумма записанных в файл чисел = {sum(new_list)}")
