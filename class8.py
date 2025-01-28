#  String Method

name = "tahreem"
print (type(name))
# <class 'str'>
print(name.capitalize())
# Tahreem
print(name)
# tahreem
print(name.count("e"))
# 2
my_intro ="My name is Tahreem, and I am from Pakistan."
my_intro += "I have completed my intermediate education."
my_intro += "I always strive to experience new things and continue learning in life."
my_intro += "I am passionate about learning new things,"
my_intro += "and my goal is to ensure that whatever I learn benefits my loved ones."
print (len(my_intro))
# 273
print(my_intro.find("am"))
# 4
print(my_intro.replace("Pakistan","Dubai"))
# My name is Tahreem, and I am from Dubai.
print(my_intro.split())
# ['My', 'name', 'is', 'Tahreem,', 'and', 'I', 'am', 'from', 'Dubai.']
print(my_intro.upper())
# MY NAME IS TAHREEM, AND I AM FROM DUBAI.
print(my_intro.lower())
# my name is tahreem, and i am from dubai.
print(my_intro.title())
# My Name Is Tahreem, And I Am From Dubai.
print(my_intro.strip("."))
# My name is Tahreem, and I am from Dubai
print(my_intro.startswith("My"))
# True
print(my_intro.endswith("i"))
# false
print(my_intro.swapcase())
# mY NAME IS tAHREEM, aND I aM FROM dUBAI.

#  List Methods
#append
my_list = ["amna","qirat","sana","fatima"]
my_list.append("rimsha")
print(my_list)
# ['amna', 'qirat', 'sana', 'fatima', 'rimsha']

#insert
my_list.insert(1,"kinza")
print(my_list)
# ['amna', 'kinza', 'qirat', 'sana', 'fatima', 'rimsha']

#reverse
my_list.reverse()
print(my_list)
# ['rimsha', 'fatima', 'sana', 'qirat', 'kinza', 'amna']

#sort
my_list.sort()
print(my_list)
# ['amna', 'fatima', 'kinza', 'qirat', 'rimsha', 'sana']

#pop
my_list.pop(3)
print(my_list)
# ['amna', 'fatima', 'kinza', 'rimsha', 'sana']

#remove
my_list.remove("amna")
print(my_list)
# ['fatima', 'kinza', 'rimsha', 'sana']

#clear
# my_list.clear()
# print(my_list)

#extend:
new_list = ["samreen","ayesha","aimon","farah"]
my_list.extend(new_list)
print(my_list)
# ['fatima', 'kinza', 'rimsha', 'sana', 'samreen', 'ayesha', 'aimon', 'farah']
 
 #  Python Dictionary Methods
# keys
my_dict={"Ali": 109876,
         "Ahmed":9087,
         "fatima":8899}
print(my_dict.keys())   
# dict_keys(['Ali', 'Ahmed', 'fatima'])

#items
print(my_dict.items())
# dict_items([('Ali', 109876), ('Ahmed', 9087), ('fatima', 8899)])

#values
print(my_dict.values())
# dict_values([109876, 9087, 8899])

#get
print(my_dict.get("Ali"))
# 109876

#pop
my_dict.pop("Ali")
print(my_dict)
# {'Ahmed': 9087, 'fatima': 8899}

#update
new_dict = {"hamza":24759394}
my_dict.update(new_dict)
print(my_dict)
# {'Ahmed': 9087, 'fatima': 8899, 'hamza': 2374849}

#Tupple Methods

# Count
teachers = ("uroosa","dua","mariyam","rimsha","mahira","aimon")   
print(teachers.count("mariyam"))
# 1

# Index
print(teachers.index("mahira"))
# 4