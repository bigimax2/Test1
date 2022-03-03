# a = int(input())
# b = (a-1) * (-1)
# print(b)


# s = int(input())
# c = (s / 3) / 2
# p = c
# k = s - (p + c)
# print(int(c), int(k), int(p))


#x, y, z = map(int, input().split())
#X1 = x * 3
#Y1 = y * 5
#Z1 = z * 12
#print(X1 + Y1 + Z1)


#N, A, B = map(int, input().split())
#print(N * (2 * (A * B)))


#h = int(input())
#m = int(input())
#s = int(input())
#h1 = int(input())
#m1 = int(input())
#s1 = int(input())
#summ1 = (s + (m * 60) + (h * 3600))
#summ2 = (s1 + (m1 * 60) + (h1 * 3600))
#print(summ2 - summ1)

g, L = map(int, input().split())
summ1 = ((g + L) - 1)
print(summ1 - g, summ1 - L)
