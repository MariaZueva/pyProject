def int_func(str_f):
    """Возвращает строку из латинских букв (каждое слово с заглавной)"""
    my_list = str_f.split()
    my_list_res = []
    for el_l in my_list:
        flag = True
        for i in el_l:
            if ord(i) < 97 or ord(i) > 122:
                flag = False
                break
        if flag:
            my_list_res.append(el_l)
    res_str = ' '.join(my_list_res)
    return res_str.title()


my_str = "nice Gaff hkJ рПпн ЛЛЛ паоао RER cool"
print(int_func(my_str))
