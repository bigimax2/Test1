"""
 На вход программе подается одна строка. Напишите программу, которая определяет сколько в
 ней одинаковых соседних символов.

 Формат входных данных
 На вход программе подается одна строка.

 Формат выходных данных
 Программа должна вывести количество одинаковых соседних символов.
"""

n = input()
a = 0

for i in range(0, len(n) - 1):
    if str[i] == str(i + 1):
        a += 1
print(a)
