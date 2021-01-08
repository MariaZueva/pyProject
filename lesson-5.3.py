# предположим, что фамилии уникальны
lim = 20000.0
with open("text_3.txt", "r", encoding="utf-8") as f:
    my_tuple = {}
    for line in f:
        tmp_l = line.split()
        my_tuple[tmp_l[0]] = float(tmp_l[1])
# print(my_tuple)

print(f"Список сотрудников с ЗП менее {lim} рублей: ", end=" ")
sum_sal = 0.0
for t in my_tuple:
    sum_sal += my_tuple[t]
    if my_tuple[t] < lim:
        print(t, end=' ')
print(f"\nСредняя ЗП всех сотрудников = {sum_sal / len(my_tuple)}")
