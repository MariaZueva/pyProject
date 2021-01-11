class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def return_income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self.return_income()["wage"] + self.return_income()["bonus"]


zm = Position('Zueva', 'Maria', 'Analyst', 80000, 10000)
print(zm.get_full_name())
print(f"Полная ЗП = {zm.get_total_income()} р.")