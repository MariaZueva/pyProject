def my_func(var_1, var_2, var_3):
    """Возвращает сумму двух максимальных чисел"""
    tmp_list = [var_1, var_2, var_3]
    tmp_list.remove(min(tmp_list))
    return sum(tmp_list)


inp = input('Введите через пробел три числа: ')
inp = inp.split()
try:
    print(f'Сумма двух наибольших чисел {my_func(float(inp[0]), float(inp[1]), float(inp[2]))}')
except ValueError:
    print('Один или нескоклько параметров не являются числами')
except IndexError:
    print('Вы ввели слишком мало чисел')
