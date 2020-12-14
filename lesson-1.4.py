num = int(input('Введите целое положительное число '))
# т.к число целое положительное можем так сделать
num_max = 0
while num:
    tmp = num % 10
    num = num // 10
    if tmp > num_max:
        num_max = tmp
print(f"Максимальное число {num_max}")
