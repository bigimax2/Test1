"""
 Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и
 возвращает первое простое число большее числа num.

 Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

 print(get_next_prime(6))
 print(get_next_prime(7))
 print(get_next_prime(14))
 должен выводить:

 7
 11
 17
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

# объявление функции
def get_next_prime(num):
    i = 0
    while i == 0:
        if is_prime(num + 1):
            return num + 1
        else:
            num += 1



# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

"""
альтернативное решение

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    m = num+1
    while is_prime(m) == False:
        m +=1
    return m  
"""