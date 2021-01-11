class Road:
    __thickness = 5
    __mass_ce = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        return self._width * self._length * self.__thickness * self.__mass_ce


my_road = Road(20, 5000)
print(my_road.calc_mass())
