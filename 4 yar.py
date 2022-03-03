a = int(input())
b = a % 400
c = a % 4
d = a % 100
if ((b == 0) and (c == 0)) or ((d != 0) and (c == 0)):
    print("Високосный")
elif (b == 0) and (d == 0):
    print("Високосный")
else:
    print("Обычный")
