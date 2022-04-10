"""
 BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

 Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
 Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

 число a – должно быть палиндромом;
 число b – должно быть простым;
 число c – должно быть четным.
 Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
 и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

 print(is_valid_password('1221:101:22'))
 print(is_valid_password('565:30:50'))
 print(is_valid_password('112:7:9'))
 print(is_valid_password('1221:101:22:22'))

 должен выводить:

 True
 False
 False
 False
"""


def is_valid_password(password):
    password_list = password.split(':')
    n = 0
    a = password_list[0]
    b = int(password_list[1])
    c = int(password_list[2])

    if len(password_list) > 3:
        return False
    if a == a[::-1]:
        n += 1
    else:
        return False
    if b == 0 or b == 1:
        return False
    else:
        k = 0
        for i in range(2, b // 2 + 1):
            if int(b) % i == 0:
                k += 1
        if k <= 0:
            n += 1
        else:
            return False
    if c % 2 == 0:
        n += 1
    else:
        return False
    if n == 3:
        return True
    else:
        return False


psw = input()

print(is_valid_password(psw))
