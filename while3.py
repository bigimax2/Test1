a = input()
b = 0

while a not in ('стоп','хватит', 'достаточно'):
    b += 1
    a = input()
print(b)
