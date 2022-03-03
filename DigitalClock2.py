#a = int(input())
#b = (a // 3600) % 24
#d = (a // 60) % 60
#c = (a % 60)
#print(b, ':', d // 10, d % 10, ':', c // 10, c % 10, sep="")


a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)


