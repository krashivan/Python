"""
Задание 5
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("\nЗапуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Отрисовка карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print("Отрисовка маркером")


pen_1 = Pen("Синяя ручка")
pen_1.draw()

s_2 = Stationery("Неизвестный предмет")
s_2.draw()
