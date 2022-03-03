a, b, c = int(input()), int(input()), int(input())
if ((a == b) and (a != c)) or ((a == c) and (a != b)):
    print("2")
elif ((b == a) and (b != c)) or ((b == c) and (b != a)):
    print("2")
elif c == b == a:
    print("3")
else:
    print("0")
