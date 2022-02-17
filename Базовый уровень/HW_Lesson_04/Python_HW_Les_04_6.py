"""
Задание 6
а) итератор, генерирующий целые числа, начиная с указанного,
"""
from itertools import count, cycle

initial = int(input("\nПункт a"
                    "\nВведите стартовое число: "))
eventual = int(input("Введите конечное число: "))

for i in count(initial):
    print(i)
    if i >= eventual:
        break

"""
Задание 6
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
print("\nПункт b")
my_list = [1, 2, 3, 4, 5]
i = 0
for el in cycle(my_list):
    if i > 20:
        break
    print(el)
    i += 1
