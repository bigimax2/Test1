"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран
 в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольн
"""
def sort_list(l):
    result_list = []
    for index, elem in enumerate(l):
        if elem in l[index+1:]:
            result_list.append(elem)
    print(result_list)
""" if result_list != 0:
        for i in result_list:
            print(i, end=' ')
"""

#sort_list([1, 2, 4,4,2,])
#sort_list([1, 2, 4,4,2, -1, -1])
#sort_list([1, 2, 4,4,2, -1, -1,0, 0])
sort_list([1,1,1,1,1,2,2,2])