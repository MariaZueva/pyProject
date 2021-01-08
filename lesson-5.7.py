import json

av_profit = 0
av_i = 0
res_dict = {}
with open("text_7.txt", "r", encoding="utf-8") as f:
    for line in f:
        tmp_l = line.split()
        profit = float(tmp_l[2]) - float(tmp_l[3])
        print(f"Прибыль фирмы {tmp_l[0]} = {profit}")
        if profit > 0:
            av_profit += profit
            av_i += 1
        res_dict[tmp_l[0]] = profit
av_profit /= av_i
res_dict["Средняя прибыль"] = av_profit
print(f"Средняя прибыль (для компаний с положительной прибылью) = {av_profit}")
print(res_dict)
with open("file_js.json", "w", encoding="utf-8") as write_f:
    json.dump(res_dict, write_f, indent=4, ensure_ascii=False)
