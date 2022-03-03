a = int(input())

if ((1 <= a <= 10) or (19 <= a <= 28)):
    if (a % 2 == 0):
        print('черный')
        if ((1 <= a <= 10) or (19 <= a <= 28)) and (a % 2 != 0):
            print('красный')
    elif ((11 <= a <= 18) or (29 <= a <= 36)) and (a % 2 == 0):
        print('красный')
        if ((11 <= a <= 18) or (29 <= a <= 36)) and (a % 2 != 0):
            print('черный')
    elif a == 0:
        print('зеленый')
    else:
        print('ошибка ввода')
elif ((11 <= a <= 18) or (29 <= a <= 36)) and (a % 2 == 0):
    print('красный')
    if ((11 <= a <= 18) or (29 <= a <= 36)) and (a % 2 != 0):
        print('черный')
elif a == 0:
    print('зеленый')
else:
    print('ошибка ввода')