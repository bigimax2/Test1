# заплатите ведьмаку чеканной монетой

a = int(input())
b = 0
var = a
while var >= 25:
    b += 1
    var -= 25
    while 25 > var >= 10:
        b += 1
        var -= 10
    while 10 > var >= 5:
        b += 1
        var -= 5
    while 5 > var >= 1:
        b += 1
        var -= 1

print(b)
