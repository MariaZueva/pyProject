new_list = input('Ведите элементы списка через пробел: ')
new_list = new_list.split()
print(f"Исходный список: {new_list}")
for i in range(0, len(new_list) - 1, 2):
    tmp = new_list[i]
    new_list[i] = new_list[i + 1]
    new_list[i + 1] = tmp
print(f"Полученный список: {new_list}")

