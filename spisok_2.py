some_numbers = input()
sum = 0
list_of_numbers = some_numbers.split()

for num in list_of_numbers:
    sum += int(num)

print(sum)

