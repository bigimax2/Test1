"""
 На вход программе подается строка текста. Напишите программу, которая выводит на экран символ,
 который появляется наиболее часто.

 Формат входных данных
 На вход программе подается строка текста. Текст может содержать строчные и заглавные буквы английского и русского
 алфавита, а также цифры.

 Формат выходных данных
 Программа должна вывести символ, который появляется наиболее часто.

 Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.

 Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
"""

s = input()

max = 0
b = 0

for i in s:
    if s.count(i) >= max:
        max = s.count(i)
        b = i
print(b)
