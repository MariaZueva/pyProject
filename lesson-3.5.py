var_oll = 0
while True:
    my_str = input('Введите числа разделенные пробелом, для выхода введите "q": ')
    my_list = my_str.split()
    ex = False
    var_temp = 0
    for el in my_list:
        if el == 'q':
            ex = True
            print('Выход о спецсимволу "q"')
            break
        else:
            try:
                var_temp += float(el)
            except ValueError:
                print('ERROR: Вы ввели не числа и не спецсимвол')
                ex = True
    var_oll += var_temp
    print(f"Сумма = {var_oll}; промежуточное значение суммы = {var_temp}")
    if ex:
        break
