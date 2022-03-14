import math
n = int(input())
summ = 0

for i in range(1, n + 1):
    summ += math.factorial(i)
print(summ)
