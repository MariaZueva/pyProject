revenue = float(input('Введите значение выручки фирмы '))
cost = float(input('Введите значение издержек фирмы '))
if revenue > cost:
    print('Финансовый результат фирмы - прибыль')
    print(f"Рентабельность фирмы {((revenue - cost) / revenue):.3f}")
    quantity = int(input('Введите количество сотрудников фирмы '))
    print(f"Прибыль фирмы в расчете на одного сотрудника {((revenue - cost) / quantity):.3f}")
elif revenue < cost:
    print('Финансовый результат фирмы - убыток')
else:
    print('Фирма отработала в 0')
