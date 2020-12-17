my_list = [7, 5, 3, 3, 2]
r = int(input('Введите целое число: '))
for i in range(len(my_list) - 1, -1, -1):
    if r <= my_list[i]:
        my_list.insert(i + 1, r)
        break
    if i == 0:
        my_list.insert(0, r)
print(my_list)
