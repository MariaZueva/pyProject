import random


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def print_type(self):
        pass

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}")


class TownCar(Car):
    __limit_speed = 60

    def print_type(self):
        print(f"Городской автомобиль")

    def show_speed(self):
        if self.speed > self.__limit_speed:
            print(f"Превышение допустимой скорости {self.__limit_speed}. Скорость автомобиля {self.speed}")
        else:
            print(f"Скорость автомобиля {self.speed}")


class SportCar(Car):
    def print_type(self):
        print(f"Спортивный автомобиль")


class WorkCar(Car):
    __limit_speed = 40

    def print_type(self):
        print(f"Рабочий автомобиль")

    def show_speed(self):
        if self.speed > self.__limit_speed:
            print(f"Превышение допустимой скорости {self.__limit_speed}. Скорость автомобиля {self.speed}")
        else:
            print(f"Скорость автомобиля {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def print_type(self):
        print(f"Полицейский автомобиль")


direc = ('на лево', 'на право', 'назад')

rnd = random.randint(0, 2)
town = TownCar(70, 'red', 'Lada')
town.print_type()
town.go()
town.show_speed()
town.turn(direc[rnd])
town.stop()

print()

rnd = random.randint(0, 2)
work = WorkCar(39, 'blue', 'mazda')
work.print_type()
work.go()
work.show_speed()
work.turn(direc[rnd])
work.stop()

print()

rnd = random.randint(0, 2)
sport = SportCar(150, 'grey', 'volvo')
sport.print_type()
sport.go()
sport.show_speed()
sport.turn(direc[rnd])
sport.stop()

print()

rnd = random.randint(0, 2)
police = PoliceCar(150, 'grey', 'subaru')
police.print_type()
police.go()
police.show_speed()
police.turn(direc[rnd])
police.stop()
