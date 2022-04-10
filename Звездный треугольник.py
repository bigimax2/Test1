"""
 Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

 fill – символ заполнитель;
 base – величина основания равнобедренного треугольника;
 а затем выводит его.

 Примечание. Гарантируется, что основание треугольника – нечетное число.
"""

def draw_triangle(fill, base):
    for i in range(int(base) // 2 + 1):
        for j in range(i + 1):
            print(fill, end='')
        print()
    for i in range(int(base) // 2, 0, -1):
        for j in range(i):
            print(fill, end='')
        print()


fill = input()
base = int(input())

draw_triangle(fill, base)
