res_t = {}
with open("text_6.txt", "r", encoding="utf-8") as f:
    f.seek(0)
    for line in f:
        num = line.find(':')
        name = line[0:num]
        # print(name)
        tmp_st = ''
        for i in line:
            if i.isdigit():
                tmp_st += i
            else:
                tmp_st += ' '
        sum_l = sum(map(int, tmp_st.split()))
        # print(sum_l)
        res_t[name] = sum_l
print(res_t)
