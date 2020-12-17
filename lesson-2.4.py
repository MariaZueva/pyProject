my_str = input('Введите строки разделенные пробелами: ')
my_list = my_str.split()
for ind, el in enumerate(my_list):
    print(f"{ind}: {el[0:10:1]}")
