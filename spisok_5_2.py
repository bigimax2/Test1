"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит
 все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой
буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""
number_list = [int(i) for i in input().split()]
num = int(input())
result_list = []
for index, elem in enumerate(number_list):
    if elem == num:
        result_list.append(index)
if len(result_list):
    pass
else:
    print("Отсутствует")
for i in result_list:
    print(i, end=' ')

# print(result_list
# find_elem_in_list([1,6,3,5,6],6)