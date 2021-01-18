from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 30:
            self.__size = 30
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 50:
            self.__size = 50
        elif size > 250:
            self.__size = 250
        else:
            self.__size = size

    @property
    def consumption(self):
        return self.size * 2 + 0.3


coat = Coat(45)
print(f"Для пальто размера {coat.size} потребуется {round(coat.consumption, 3)} ткани")

costume = Costume(150)
print(f"Для костюма с ростом {costume.size} потребуется {round(costume.consumption, 3)} ткани")
