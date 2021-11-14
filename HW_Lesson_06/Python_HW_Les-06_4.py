"""
Задание 4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("\nМашина находится в движении")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        d = direction
        print(f"Машина повернула на{d}")

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости! Ваша скрость на {self.speed - 60} км/ч выше допустимой")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости! Ваша скрость на {self.speed - 40} км/ч выше допустимой")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(70, "Blue", "Ford", False)
car_1.go()
car_1.turn("лево")
car_1.show_speed()
car_1.speed = 50
car_1.show_speed()

car_2 = SportCar(200, "Black", "Toyota", False)
car_2.go()
car_2.turn("право")
car_2.show_speed()
car_2.stop()
