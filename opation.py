a = int(input())


num2 = 0


for i in range(1, a + 1):
    if i % 2 == 0:
        num2 -= i
    else:
        num2 += i
print(num2)
