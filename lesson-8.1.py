class Date:
    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    @staticmethod
    def validation(dd, mm, yy):
        return [dd, mm, yy] if (1 <= dd <= 31 and 1 <= mm <= 12 and 1000 <= yy <= 9999) else [1, 1, 1000]

    @classmethod
    def transformation(cls, data):
        try:
            dd_t, mm_t, yy_t = map(int, data.split('-'))
            dd, mm, yy = cls.validation(dd_t, mm_t, yy_t)
            return cls(dd, mm, yy)
        except ValueError:
            print("Не верный формат даты")
            return cls(1, 1, 1000)

    def __str__(self):
        return f"{self.dd:02d}.{self.mm:02d}.{self.yy}"


date = Date.transformation('01-12-1990')
print(date)
