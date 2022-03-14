n = int(input())
summ1 = 0

while n > 0:
    summ1 += n % 10
    n = n // 10
    if n == 0 and summ1 // 10 != 0:
        n = summ1
        summ1 = 0
print(summ1)

