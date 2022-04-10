# объявление функции
def get_factors(num):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    return divisors

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))