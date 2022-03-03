from math import ceil

def find_days (n, m):
   if type(n) is str or type(m) is str:
       return "m or n is not digit"
   elif min(m, n) <= 0:
       return "m, n should be more as 0"
   else:
       return ceil(m/n)


print(find_days(50, 340))
print(find_days(0, 340))
print(find_days(50, 0))
print(find_days(-30, 340))
print(find_days(30, -400))
print(find_days(0.15, 20))
print(find_days("420", 70))