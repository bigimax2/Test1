"""
 Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря
. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости
 довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
 Напишите программу для декодирования этого шифра.

 Формат входных данных
 В первой строке дается число n ,  (1≤ n ≤25) – сдвиг, во второй строке даётся
 закодированное сообщение в виде строки со строчными латинскими буквами.

 Формат выходных данных
 Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение,
 а не закодировать.
"""


a = int(input())
s = input()
b = ''

for c in s:
    if (ord(c) - a) < 97:
        b += chr((ord(c) - a) + 26)     # кольцуем алфавит
    else:
        b += chr(ord(c) - a)
print(b)
