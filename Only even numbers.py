num = 0

for _ in range(1, 10 + 1):
    a = int(input())
    if a % 2 == 0:
        num += 1
if num == 10:
    print('YES')
else:
    print('NO')
