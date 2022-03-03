# Заданы две клетки шахматной доски. Если они покрашены в один цвет,
# то выведите слово YES, а если в разные цвета – то NO.


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b + c + d) % 2 == 0:
    print("YES")
else:
    print("NO")
