from itertools import count, cycle

# a
iterat_1 = count(int(input('Введите число, с которого будут начинаться генерироваться числа: ')))
res_list_1 = [i for i in range(7)]
for i in range(7):
    print((next(iterat_1)))

# b
inp_list = input('Введите элементы списка через пробел').split()
iterat_2 = cycle(inp_list)
for i in range(5):
    print(next(iterat_2))
