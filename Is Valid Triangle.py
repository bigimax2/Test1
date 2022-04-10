# объявление функции
def is_valid_triangle(side1, side2, side3):
    if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side1 + side2):
        return False
    else:
        return True


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))