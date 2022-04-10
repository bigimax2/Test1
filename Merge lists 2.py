"""
 На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания.
 Из данных строк формируются списки чисел. Напишите программу,
 которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

 Формат входных данных
 На вход программе подается натуральное число nn, а затем nn строк, содержащих целые числа в порядке возрастания,
 разделенные символом пробела.

 Формат выходных данных
 Программа должна вывести текст в соответствии с условием задачи.
"""

def quick_merge(list1):
    list2 = []
    for i in range(list1):
        spisok1 = [int(c) for c in input().split()]
        list2.extend(spisok1)
        list2.sort()
    return list2


n = int(input())
print(*quick_merge(n))