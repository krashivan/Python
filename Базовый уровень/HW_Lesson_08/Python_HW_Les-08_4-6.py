"""
Задание 4
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Задание 5
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Задание 6
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEquip:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name}"


class Printer(OfficeEquip):

    def __init__(self, name, location, paper_format):
        super().__init__(name, location)
        self.paper_format = paper_format

    def __str__(self):
        return self.name


class Scanner(OfficeEquip):

    def __init__(self, name, location, color):
        super().__init__(name, location)
        self.color = color

    def __str__(self):
        return self.name


class Xerox(OfficeEquip):

    def __init__(self, name, location, release_date):
        super().__init__(name, location)
        self.release_date = release_date

    def __str__(self):
        return self.name


class Storage:

    def __str__(self):
        return f'{self.items}'

    items = {}

    def put(self, equip: OfficeEquip, quantity):
        OfficeEquip.location = "Storage"
        try:
            int(quantity)
            self.items.update({equip.name: quantity})
        except ValueError:
            return print("Ошибка! Количесвто оборудования - текст")

    def move_to_office(self, equip: OfficeEquip, quantity):
        OfficeEquip.location = "Office"
        try:
            int(quantity)
            val = self.items.get(equip.name)
            self.items.update({equip.name: val - quantity})
        except ValueError:
            return print("Ошибка! Количесвто оборудования - текст")


Warehouse_1 = Storage()

printer_1 = Printer("Kyocera", "Office", "A4")
Warehouse_1.put(printer_1, 10)

scanner_1 = Scanner("HP", "Office", "b/w")
Warehouse_1.put(scanner_1, 110)

print(Warehouse_1)

Warehouse_1.move_to_office(scanner_1, 73)
print(Warehouse_1)

xerox_1 = Xerox("Canon", "Office", "b/w")
Warehouse_1.put(xerox_1, 'text')
Warehouse_1.put(xerox_1, '2')
print(Warehouse_1)
