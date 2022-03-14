n = input()
r = 'Цифр нет'

for i in range(0, 10):
    if str(i) in n:
        r = 'Цифра'
        break
else:
    r = 'Цифр нет'
print(r)


