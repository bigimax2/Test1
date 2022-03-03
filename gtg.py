a = input()
if a == "треугольник":
    b = float(input())
    c = float(input())
    d = float(input())
    p = (b + c + d) / 2
    s = (p * (p - b) * (p - c) * (p - d)) ** 0.5
    print(s)
elif a == "прямоугольник":
    b = float(input())
    c = float(input())
    s = b * c
    print(s)
elif a == "круг":
    r = float(input())
    s = 3.14 * (r ** 2)
    print(s)
