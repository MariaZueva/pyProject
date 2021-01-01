from sys import argv

try:
    hour, rate, award = map(float, argv[1:])
    print(f"Заработная плата сотрудника = {hour * rate + award}")
except ValueError:
    print("Введите три параметра")