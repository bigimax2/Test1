"""
 Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

 name – имя человека;
 surname – фамилия человека;
 patronymic – отчество человека;
 а затем выводит на печать ФИО человека.

 Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
"""


def print_fio(name, surname, patronymic):
    print(surname[0] + name[0] + patronymic[0])


name = input().capitalize()
surname = input().capitalize()
patronymic = input().capitalize()

print_fio(name, surname, patronymic)
