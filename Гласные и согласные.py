n = input().lower()

a = 0
s = 0

for i in n:
    if i in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
        a += 1
    if i in ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч']:
        s += 1
print('Количество гласных букв равно', a)
print('Количество согласных букв равно', s)
