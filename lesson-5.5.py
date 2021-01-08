from random import randint

lst = [randint(-10, 10) for i in range(20)]
print(lst)
with open("lesson_5.5.txt", "w+", encoding="utf-8") as f:
    f.write(' '.join(list(map(str, lst))))
    f.seek(0)
    res_l = list(map(int, f.read().split()))
    res_sum = sum(res_l)
    print(res_l)
    print(res_sum)
