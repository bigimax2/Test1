n = int(input())

f1 = 1
f2 = 1

if n > 1:
    print(f1, f2, end='')
for _ in range(2, n):
    f1 = f2
    f2 = f1 + f2
    print(f2)
else:
    print(1)
