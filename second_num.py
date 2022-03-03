a = int(input())
b = 0

while a != 0:
    var = a % 10
    if 10 < a < 100:
        b = a % 10
    a = a // 10
print(b)
