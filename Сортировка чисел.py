"""
 На вход программе подается строка текста, содержащая целые числа.
 Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по
 возрастанию, а затем по убыванию.

 Формат входных данных
 На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

 Формат выходных данных
 Программа должна вывести две строки текста в соответствии с условием задачи.
"""

n = input()
s = []
for i in n:
    if int(i):
        s.append(i)
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)
