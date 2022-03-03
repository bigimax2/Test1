n = int(input())
a = n % 10
b = 0

while n != 0:
    var = n % 10
    if var != a:
        b += 1
    n = n // 10
if b == 0:
    flag = 'YES'
else:
    flag = 'NO'
print(flag)
