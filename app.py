import calendar
year = 2025
month = 1
print (calendar.month(year,month))
#  January 2025
# Mo Tu We Th Fr Sa Su
#       1  2  3  4  5
# 6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31
table = 2
for table in range (1,11):
    print(f"2x{table}=",table*2)
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10= 20
square =lambda x: x**2
print(square (20))
print(square(15))
# 400
# 225