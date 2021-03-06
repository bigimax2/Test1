"""
 Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c –
 коэффициенты квадратного уравнения ax^2+bx+c = 0

 +bx+c=0 и возвращает его корни в порядке возрастания.

 Примечание 1. С подобной задачей мы уже сталкивались.

 Примечание 2. Гарантируется, что квадратное уравнение имеет корни.

 Примечание 3. Следующий программный код:

 print(solve(1, -4, -5))
 print(solve(-2, 7, -5))
 print(solve(1, 2, 1))
 должен выводить:

 -1.0 5.0
 1.0 2.5
 -1.0 -1.0
"""


def solve(a, b, c):
    import math
    D = (b ** 2) - (4 * a * c)

    if D > 0:
        e = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (a * 2)
        f = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (a * 2)
        return min(e, f), max(e, f)

    if D == 0:
        x = (b / (2 * a)) * -1
        return x, x


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
