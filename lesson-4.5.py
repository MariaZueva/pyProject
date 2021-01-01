from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2


my_list = [i for i in range(100, 1001, 2)]
res = reduce(mul_list, my_list)
print(f"Исходный список: {my_list}\nПроизведение чисел {res}")
