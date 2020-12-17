t_list = []
while True:
    num = input('Введите 1 для ввода данных \n'
                'Введите 2 для просмотра товаров \n'
                'Введите 3 для просмотра аналитики \n'
                'Введите любую другую строку для выхода \n')
    if num == '1':
        tmp_l = input('Через пробел введите наименование товара, цену, количество и ед. измерения. \n').split()
        t_dic = {'наименование': tmp_l[0], 'цена': float(tmp_l[1]), 'количество': int(tmp_l[2]), 'ед. изм.': tmp_l[3]}
        t_list.append((len(t_list) + 1, t_dic))
    elif num == '2':
        for i in t_list:
            list_el = i
            print(list_el)
    elif num == '3':
        res_dic = []
        temp_name = []
        temp_price = []
        temp_qu = []
        temp_units = []
        for el in t_list:
            temp_name.append(el[1]['наименование'])
            temp_price.append(el[1]['цена'])
            temp_qu.append(el[1]['количество'])
            temp_units.append(el[1]['ед. изм.'])
        res_dic = {'наименование': temp_name,
                   'цена': temp_price,
                   'количество': temp_qu,
                   'ед. изм.': temp_units}
        print(res_dic)
    else:
        break
