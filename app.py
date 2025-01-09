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
for table in range (10):
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
# 2 x 10 = 20
table = 3
for table in range (11):
    print(f"3x{table}=",table*3)
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
table = 4
for table in range (11):
    print(f"4x{table}=",table*4)
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40

square =lambda x: x**2
print(square (20))
print(square(15))
# 400
# 225
