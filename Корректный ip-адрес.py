"""
 На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу,
 которая определяет является ли введенная строка текста корректным ip-адресом.

 Формат входных данных
 На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
"""

for i in input().split('.'):
    if int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')

