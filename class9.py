i = 1
while i <= 5:
    if (i == 3):
        i += 1
        break
    print (i)
    i += 1
# 1
# 2
i = 1
while i <= 10:
    if (i%2 != 0):
         i += 1
        continue
    print (i)
    i += 1
print(i)

friends_name =("sahar", "rubab", "guriya", "afshan", "ayesha",) 
bestie = "guriya"
idx = 0
while idx < len(friends_name):
  if (friends_name[idx] == bestie):
     print("i miss you alot", bestie,idx)
     break
  idx += 1
# i miss you alot guriya 2

table = int(input("enter number: "))
for num1 in range(1,11):
    print("5 x", num1, "=", num1*5)
# enter number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

def calc_avg (a,b,c):
    sum = a + b + c
    avg = sum / 4
    return avg
print(calc_avg(74, 34, 56))
# 41.0
# WHILE LOOP METHOD
# Qst.1
n = int(input("enter number: "))
i = 1
while i <= 10:
  print (2*i)
  i += 1
  print (2*i)
# enter number: 2
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# Qst.2
i = 1
while i <= 10:
  print(i)
  i += 1
print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

# Qst.3
nums = [1, 4, 7, 12, 17, 20, 35, 63, 89, 100]
idx = 0
while idx < len(nums):
  print (nums[idx])
  idx += 1

# 1
# 4
# 7
# 12
# 17
# 20
# 35
# 63
# 89
# 100

# Qst.4
nums = (1, 4, 7, 12, 17, 20, 35, 63, 89, 100)
x = 35
idx = 0
while idx < len(nums):
  if(nums[idx] == x):
     print("Found at idx", idx)
  idx += 1
# Found at idx 6

# Qst.5
nums = (1, 4, 7, 12, 17, 20, 35, 63, 89, 100)
x = 35
idx = 0
while idx < len(nums):
  if(nums[idx] == x):
     print("Found at idx", idx)
  idx += 1
# Finding..
# Finding..
# Finding..
# Finding..
# Finding..
# Finding..
# Found at idx 6
# Finding..
# Finding..
# Finding..
# Found at idx 10

# Qst.6
def calculator(a,b,c):
  if(c == "+"):
    print (a+b)
  elif(c == "-"):
      print (a-b)
  elif(c == "*"):
      print (a*b)
  elif(c == "/"):
      print (a/b)
  elif(c == "%"):
      print (a%b)
  elif(c == "**"):
      print (a**b)
  else:
      print("Invalid operator")

calculator(2,7, "+")
# 9
calculator(2,7, "-")
# -5
calculator(2,7, "*")
# 14
calculator(2,7, "/")
# 0.2857142857142857
calculator(2,7, "%")
# 2
calculator(2,7, "**")
# 128
calculator(2,7,"a")
# Invalid operator

# Qst.7
def calc_sum(x,y):
  return x * y
  sum = (calc_sum)
print(calc_sum(2,4))
# 8

# Qst.8
client_data = ("Ayesha", 22, "Property cosultant")
name, age, profession = client_data
print(f"Name:{name}" ,end= " ")
print(f"Age:{age}", end= " " )
print(f"Profession:{profession}")
# Name:Ayesha Age:22 Profession:Property cosultant

# Qst.9
def calc_avg (a,b,c):
  sum = a + b + c
  avg = sum / 3
  return avg
print(calc_avg(50,78,89))
# 72.33333333333333

# Qst.10
squares = []
for x in range(1,10):
  squares.append(x**2)
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Qst.11
nums = (1, 4, 9, 16, 25, 36, 49, 64, 82, 49, 100)
x = 49
idx = 0
for el in nums:
  if (el == x):
    print("Number found at idx", idx)
  idx += 1
# Number found at idx 6
# Number found at idx 9

# Qst.12
num= int(input("enter number: "))
print ("table of 2")
try:
  for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")
except error:
    print ("try to resolve the error")
#     enter number: 2
# table of 2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20

# Qst.13
n = 5 
sum = 0
try:
   for i in range(1, n+1):
    sum += i
   
   print("total sum =", sum)    

except error:
   print ("try to resolve the value")
# total sum = 15

# Qst.14
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#   Hello
# Nothing went wrong
