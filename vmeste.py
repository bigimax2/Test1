a = int(input())
suum = 0
kollichestvo = 0
prizvedenie = 1
arifmet = 0
pervaya = 0
poslednyaya = a % 10
c = a

while a != 0:
    b = a % 10
    if b % a == 0:
        pervaya += a
    kollichestvo += 1
    prizvedenie *= b
    suum += b
    a = a // 10
print(suum)
print(kollichestvo)
print(prizvedenie)
print(suum / kollichestvo)
print(pervaya)
print(pervaya + poslednyaya)
