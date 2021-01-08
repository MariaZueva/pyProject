# 1 task
print('Введите строку для записи в файл')
my_str = ""
while True:
    tmp_str = input()
    if tmp_str == "":
        break
    my_str += tmp_str + '\n'
# print(my_str)
my_file = open("file_5.1.txt", "w", encoding="utf-8")
my_file.write(my_str)
my_file.close()

# 2 task
with open("file_5.1.txt", "r", encoding="utf-8") as f:
    i = 1
    for line in f:
        print(f"В {i} - ой строке {len(line.split())} слов")
        i += 1
print(f"Всего {i - 1} строк")
