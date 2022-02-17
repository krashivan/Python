"""
Задание 4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open("text_4.txt", "r") as f_obj_1:
    new_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    i = 0
    for line in f_obj_1:
        new_list = line.strip().split()
        new_list[0] = new_dict.get(new_list[0])
        with open("out_text_4.txt", "a") as f_obj_2:
            f_obj_2.write(f"{' '.join(new_list)}\n")
