from random import randint

my_list = [randint(0, 20) for i in range(20)]
res_list = [i for i in my_list if my_list.count(i) == 1]
# print(my_list)
print(res_list)
