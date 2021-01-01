def factorial(x):
    tmp = 1
    if x == 0:
        yield f'{x}! = 1'
    for i in range(1, x + 1):
        tmp *= i
        yield f'{i}! = {tmp}'


for el in factorial(int(input("Введите целое число для расчета факториала: "))):
    print(el)
