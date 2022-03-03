a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > 8 or b > 8 or c > 8 or d > 8 or a < 0 or b < 0 or c < 0 or d < 0:
    print("NO")
else:
    if (a + c) % 2 == (b + d) % 2 and d > b:
        print("YES")
    else:
        print("NO")
