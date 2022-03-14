n = int(input())
count = 0

for j in range(1, n + 1):
    for i in range(1, j + 1):
        count += 1
        print(count, end=' ')
    print()
