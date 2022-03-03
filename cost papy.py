a = int(input())
b = int(input())
n = int(input())
cost1 = a * 100 + b
totalCost = cost1 * n
print(totalCost // 100, totalCost % 100)
