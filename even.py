# Даны три целых числа A, B, C.
# Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
a = int(input())
b = int(input())
c = int(input())
if (a + b) % 2 != 0:
    print("YES")
elif (a + c) % 2 != 0:
    print("YES")
elif (c + b) % 2 != 0:
    print("YES")
else:
    print("NO")
