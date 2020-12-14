all_sec = int(input('Введите время в секундах: '))
hour = all_sec // 3600
minute = (all_sec - hour * 3600) // 60
sec = (all_sec - hour * 3600) % 60
print(f"Переведенное время {hour:02}:{minute:02}:{sec:02}")
