import math

a = int(input())

num = int(1)
for i in range(2, a + 1):
    num += 1 / i
print(num - math.log(a))
