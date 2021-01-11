class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}", end=' ')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"Ручка")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"Карандаш")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"Маркер")


obj_pen = Pen('Pilot')
obj_pen.draw()

obj_pencil = Pencil('Crayola')
obj_pencil.draw()

obj_handle = Handle('Doodle&Sketch')
obj_handle.draw()
