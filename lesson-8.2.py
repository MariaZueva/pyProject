class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введте делитель: '))
    if b == 0:
        raise ZeroError("Деление на 0")
except ValueError:
    print("Делимое или делитель не являются числом")
except ZeroError as err:
    print(err)
else:
    c = a / b
    print(c)
