a = int(input())
b = int(input())
c = int(input())
if a <= c and b <= c:
    print(c)
elif c <= a and b <= a:
    print(a)
elif a <= b and c <= b:
    print(b)
