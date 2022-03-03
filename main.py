n = int(input())
x = (n // 10) * 10
y = n - x
z = (n // 10) % 10
i = (n // 100)
print(y + z + i)
