a = int(input())
if (10 <= a <= 20) or (a % 10 in [0, 5, 6, 7, 8, 9]) or (a % 100 in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]):
    print(a, "программистов")
elif (a == 1) or (a % 10 == 1):
    print(a, "программист")
else:
    print(a, "программиста")
