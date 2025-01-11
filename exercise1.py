#  Tahreem Khan
#  Marksheet
#  85 >= "A"
#  75 >= "B"
#  50 >= "C"
#  30 >= "D"
#  Fail

english: str = 79
urdu: str = 72
maths: str = 30
science: str = 29
islamiat: str = 49
if english >= 85:
   print (f"English Grade = 100/{english} A+")
elif urdu >= 75:
   print (f"urdu Grade = 100/ {urdu} A")
elif islamiat >= 50:
    print (f"islamiat Grade = 100/{islamiat} B")
elif science >= 30:
    print (f"science Grade = 100/{science} C" )
else: 
    print (f"maths Grade = 100/{maths} Fail")

#  maths Grade = 100/30 Fail