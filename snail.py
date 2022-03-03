h = int(input())  # Высота шеста
d = int(input())  # Пройденый путь за день
n = int(input())  # Откат дневного пути
y = d - n
x = (h - d) // y
print(x + 1)
