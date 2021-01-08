from googletrans import Translator

my_f = open("text_4.txt", "r", encoding="utf-8")
res_f = open("text_4_res.txt", "w", encoding="utf-8")
for line in my_f:
    tmp_l = line.split()
    s = Translator().translate(text=tmp_l[0], dest='ru').text
    print(s + ' ' + ' '.join(tmp_l[1:]), file=res_f)

my_f.close()
res_f.close()
