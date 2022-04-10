

"""
 На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение,
 которая выведет квадраты четных чисел, которые не оканчиваются на цифру 44.

 Формат входных данных
 На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

 Формат выходных данных
 Программа должна вывести текст в соответствии с условием задачи.

 Примечание. Программу можно написать в одну строку кода.


 Там по условию нужно вывести квадраты ЧЕТНЫХ чисел не оканчивающихся на 4.
 Любое четное число заканчивающееся на 2 при возведении в квадрат даст четвёрку в конце (2×2=4, 12×12=144).
 То же самое с 8, любое число с 8 на конце, при возведение в квадрат даст 4 (8×8=64, 18×18 = 324).
 Получается из четных цифер подходят все остальное, кроме 2 и 8, а все остальные четные цифры это 0, 4 и 6.
 То есть мы отсеиваем ещё в самом начале, нам не нужно возводить число в квадрат чтобы проверять последнюю цифру,
 если мы заранее знаем какие последние цифры в возводимых числах дадут четвёрку в конце полученного квадрата
"""

print(*[int(i) ** 2 for i in input().split() if i[-1] in '046'])