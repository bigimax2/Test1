"""
 Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и
 возвращает значение True если число является простым и False в противном случае.

 Примечание. Следующий программный код:

 print(is_prime(1))
 print(is_prime(10))
 print(is_prime(17))
 должен выводить:

 False
 False
 True
"""


# объявление функции
def is_prime(num):
    k = 0
    if num != 0 and num != 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                k += 1
        if k <= 0:
            return True
        else:
            return False
    return False


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))