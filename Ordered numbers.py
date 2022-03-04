n = int(input())
b = 0
c = 0
a = 0


while n != 0:
    b = n % 10
    if b < c:
        a += 1
    c = b
    n = n // 10
if a == 0 :
    flag = 'YES'
else:
    flag = 'NO'
print(flag)
