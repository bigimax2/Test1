"""
 Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
 и преобразует его в «змеиный регистр».

 Примечание 1. Почитать подробнее о стилях именования можно тут.

 Примечание 2. Следующий программный код:

 print(convert_to_python_case('ThisIsCamelCased'))
 print(convert_to_python_case('IsPrimeNumber'))
 должен выводить:

 this_is_camel_cased
 is_prime_number
"""

def convert_to_python_case(text):
    p = []
    s = text[::-1]
    for i in range(len(s)):
        p.append(s[i])
        if s[i].isupper():
            p.append('_')
    p.reverse()
    n = ''.join(p)
    n = n.lower()
    if '_' not in n[0]:
        return n
    else:
        return n[1:]


txt = input()


print(convert_to_python_case(txt))