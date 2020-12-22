def my_div(var_1, var_2):
    """Возвращает результат деления"""
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'ERROR Деление на 0'


try:
    a1 = input('Введите делимое ')
    a2 = input('Введите делитель ')
    print(f" {a1} / {a2} = {my_div(float(a1), float(a2))}")
except ValueError:
    print('Один или оба входных параметра не являются числами')

