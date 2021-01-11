import time


class TrafficLight:
    __color = ''

    def __change_color(self, col, sl):
        self.__color = col
        print(self.__color)
        time.sleep(sl)

    def running(self, n_c):
        for i in range(n_c):
            self.__change_color('Красный', 7)
            self.__change_color('Желтый', 2)
            self.__change_color('Зеленый', 7)
            self.__change_color('Желтый', 2)


tr_l = TrafficLight()
tr_l.running(2)
