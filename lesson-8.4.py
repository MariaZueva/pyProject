from abc import ABC, abstractmethod


class Warehouse:
    unit_oll = {'Бугалтерия', 'Отдел кадров', 'Охрана труда'}

    def __init__(self):
        self.warehouse = {'Printer': [], 'Scanner': [], 'Copier': []}

    # Добавление единиц техники на склад
    def add_ware(self, *args):
        """Наименование, количество на складе, [(подразделение - количество), ...]"""
        for teh in args:
            type_teh = ''
            if type(teh) == Printer:
                type_teh = 'Printer'
            elif type(teh) == Scanner:
                type_teh = 'Scanner'
            elif type(teh) == Copier:
                type_teh = 'Copier'
            else:
                print("Неопределнный тип!")
                continue
            flag = False
            for n in self.warehouse[type_teh]:
                if teh == n[0]:
                    n[1] += 1
                    flag = True
                    break
            if not flag:
                self.warehouse[type_teh].append([teh, 1, []])

    # передача единицы техники в подразделение
    def transfer_to_unit(self, teh, unit):
        if not self.check_unit(unit):
            return f"подразделение в компании не числится"
        if type(teh) == Printer:
            type_teh = 'Printer'
        elif type(teh) == Scanner:
            type_teh = 'Scanner'
        elif type(teh) == Copier:
            type_teh = 'Copier'
        else:
            return f"неопределенный тип техники"
        for t in self.warehouse[type_teh]:
            if t[0] == teh:
                if t[1] > 0:
                    t[1] -= 1
                    fl = False
                    for un in t[2]:
                        if un[0] == unit:
                            fl = True
                            un[1] += 1
                            return f"успешно переведен в подразделение {unit}"
                    if not fl:
                        t[2].append([unit, 1])
                        return f"успешно переведен в подразделение {unit}"
                else:
                    return f"Нет доступных единиц техники для перевода"
        return f"Такой техники на складе не числится"

    # проверка на корректность подразделения
    @classmethod
    def check_unit(cls, u):
        return True if u in cls.unit_oll else False


class OfficeEquipment(ABC):

    def __init__(self, year_issue, company):
        self.year_issue = year_issue
        self.company = company

    @abstractmethod
    def print_oll_specifications(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, year_issue, company, type_print, quantity_color):
        """"Год выпуска, компания, тип печати (лазерный, струйный, светодиоидный), количество цветов"""
        super().__init__(year_issue, company)
        self.type_print = type_print
        self.quantity_color = quantity_color

    @property
    def print_oll_specifications(self):
        return f"Принтер марки {self.company},\n" \
               f"Год выпуска {self.year_issue},\n" \
               f"Тип печати {self.type_print},\n" \
               f"Количество цветов {self.quantity_color}."

    def __eq__(self, other):
        return True if (self.company == other.company and self.year_issue == other.year_issue and
                        self.type_print == other.type_print and self.quantity_color == other.quantity_color) else False


class Scanner(OfficeEquipment):

    def __init__(self, year_issue, company, type_scan, resolution):
        """"Год выпуска, компания, тип (планшетный, протяжный, слайд), разрешение"""
        super().__init__(year_issue, company)
        self.type_scan = type_scan
        self.resolution = resolution

    @property
    def print_oll_specifications(self):
        return f"Сканер марки {self.company},\n" \
               f"Год выпуска {self.year_issue},\n" \
               f"Тип {self.type_scan},\n" \
               f"Разрешение {self.resolution}."

    def __eq__(self, other):
        return True if (self.company == other.company and self.year_issue == other.year_issue and
                        self.type_scan == other.type_scan and self.resolution == other.resolution) else False


class Copier(OfficeEquipment):

    def __init__(self, year_issue, company, princ_copy, copy_speed, color_rendering):
        """"Год выпуска, компания,принцип копирования, скорость копирования, цветопередача"""
        super().__init__(year_issue, company)
        self.princ_copy = princ_copy
        self.copy_speed = copy_speed
        self.color_rendering = color_rendering

    @property
    def print_oll_specifications(self):
        return f"Ксерокс марки {self.company},\n" \
               f"Год выпуска {self.year_issue},\n" \
               f"Принцип копирования {self.princ_copy},\n" \
               f"Скорость копирования {self.copy_speed},\n" \
               f"Цветопередача {self.color_rendering}."

    def __eq__(self, other):
        return True if (self.company == other.company and self.year_issue == other.year_issue and
                        self.princ_copy == other.princ_copy and self.copy_speed == other.copy_speed and
                        self.color_rendering == other.color_rendering) else False


pr_1 = Printer(2008, "Canon", 'лазерный', 4)
pr_2 = Printer(2007, "Canon", 'лазерный', 4)
pr_3 = Printer(2006, "Canon", 'лазерный', 4)
cop = Copier(2010, "Canon", 'аналоговый', 33, 'монохромный')
sc = Scanner(2008, "Sony", "планшетный", 256)
# print(type(sc) == Scanner)
# print(cop.print_oll_specifications)
wh = Warehouse()
wh.add_ware(pr_1, pr_1, pr_2, cop, sc)
wh.transfer_to_unit(pr_1, 'Бугалтерия')
wh.transfer_to_unit(pr_1, 'Бугалтерия')
print(wh.transfer_to_unit(pr_3, 'еее'))
a = 1
