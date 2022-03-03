"""
Напишите программу, которая вычисляет процентное содержание
символов G (гуанин) и C (цитозин) в введенной
строке (программа не должна зависеть от регистра вводимых символов).


Например, в строке "acggtgttat" процентное содержание символов
 G и C равно \dfrac4{10} \cdot 100 = 40.0
10
4
​
 ⋅100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.
"""


a = input()
b = len(a)
x = a.upper()
d = x.count('G')
c = x.count('C')
print(((d + c) / b) * 100)


"""
другой способ решения
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)
"""
