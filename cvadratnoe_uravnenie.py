import math


a = float(input())
b = float(input())
c = float(input())

D = (b**2) - (4 * a * c)

if D < 0:
    print('Нет корней')
elif D > 0:
    e = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (a * 2)
    f = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (a * 2)
    print(min(e, f))
    print(max(e, f))
elif D == 0:
    x1 = (b / (2 * a)) * -1
    print(x1)
