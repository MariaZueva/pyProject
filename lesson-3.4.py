def func_pow(x_f, y_f):
    """Возвращает значение числа в отрицательной степени"""
    i = 0
    while i < abs(y_f) - 1:
        x_f *= x_f
        i += 1
    try:
        return 1.0 / x_f
    except ZeroDivisionError:
        return 'ERROR Деление на 0'


try:
    x = float(input('Введите основание (действительное положительное число): '))
    y = int(input('Введите показатель (целое отрицательное число): '))
    if y < 0:
        print(f'{x}^{y} = {func_pow(x, y)}')
    else:
        print('Вы ввели не отрицательный показатель степени')
except ValueError:
    print('Одно из введенных значений не является числом')
