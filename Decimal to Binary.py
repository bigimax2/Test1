n = int(input())
b = ''


while n > 0:
    b = str(n % 2) + b
    n = int(n / 2)
print(int(b))
