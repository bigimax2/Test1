a, b = int(input()), int(input())
summ, max = 0, 0
for i in range(a, b + 1):
  count = 0
  for j in range(1, i + 1):
    if i % j == 0:
      count += j
    if count >= summ:
      summ = count
      max = i
print(max, summ)
