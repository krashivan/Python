"""
Задание 5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def summation(row):
    sum = 0
    for i in row:
        try:
            sum += float(i)
        except ValueError:
            global stop_03_05
            stop_03_05 = 1
            break
    return sum


stop_03_05 = 0
final_05 = 0
while stop_03_05 == 0:
    x_05 = input("\nИспользуйте '*' чтобы завершить выполнение программы"
                 "\nВведите строку из чисел, разделённых только лишь пробелами: ")
    list_05 = [i for i in x_05.split(" ")]

    final_05 += summation(list_05)
    print(f"промежуточная сумма = {final_05}")
