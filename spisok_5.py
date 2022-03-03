"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит
 все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой
буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""
def find_elem_in_list(number_list,num):
    result_list = []
    for index, elem in enumerate(number_list):
        if elem == num:
            result_list.append(index+1)
    for i in result_list:
        print(i, end=' ')
    #print(result_list)

find_elem_in_list([1,6,3,5,6],6)