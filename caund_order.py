a = int(input())
c = 0
d = 9

while a != 0:
    b = a % 10
    if b > c:
        c = b
    if b < d:
        d = b
    a = a // 10
print('Максимальная цифра равна', c)
print('Минимальная цифра равна', d)
