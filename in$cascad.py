a = int(input())
b = int(input())
c = int(input())

if (a < b) and (b < c):
    print(b)
elif (b < a) and (a < c):
    print(a)
elif (c < a) and (c < b):
    print(c)
