"""
 На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского
 алфавита ['a', 'b', 'c', ...] в нижнем регистре.

 Формат входных данных
 На вход программе подается натуральное число n ≤ 26.

 Формат выходных данных
 Программа должна вывести текст в соответствии с условием задачи.
"""


a = int(input())

b = list('abcdefghijklmnopqrstuvwxyz')
print(b[:a])


"""
 Альтернативное решение
 
 print([chr(i) for i in range(97, 97 + int(input()))])
"""