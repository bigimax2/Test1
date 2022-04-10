# объявление функции
def print_digit_sum(num):
    global n
    num = 0
    while n != 0:
        num += n % 10
        n = n // 10
    print(num)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)