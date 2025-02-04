# String Method

name = "tahreem"
print (type(name))
# <class 'str'>
print(name.capitalize())
# Tahreem
print(name)
# tahreem
print(name.count("e"))
# 2
my_intro = "Hello, my name is tahreem khan, and"
my_intro += "I am an IT student with a passion for technology and innovation."
my_intro += "Currently, I am gaining valuable experience at Governor House,"
print(len(my_intro))
# 161

print(my_intro.find("for"))
# 69

print(my_intro.replace("tahreem","tehmi"))
# Hello, my name is tehmi khan,

print(my_intro.split())
# # ['My', 'name', 'is', 'Tahreem,']

print(my_intro.upper())
# HELLO, MY NAME IS TAHREEM KHAN,

print(my_intro.lower())
# hello, my name is tahreem khan,

print(my_intro.title())
# Hello, My Name Is Tahreem Khan,

print(my_intro.strip("."))
# Hello, my name is tahreem khan,

print(my_intro.startswith("Hello"))
# True

print(my_intro.endswith("i"))
# false

print(my_intro.swapcase())


# List Methods
# append
my_list = ["amna","qirat","sana","fatima"]

my_list.append("rimsha")
print(my_list)
# # ['amna', 'qirat', 'sana', 'fatima', 'rimsha']

# #insert
my_list.insert(1,"kinza")
print(my_list)
# # ['amna', 'kinza', 'qirat', 'sana', 'fatima', 'rimsha']

# #reverse
my_list.reverse()
print(my_list)
# # ['rimsha', 'fatima', 'sana', 'qirat', 'kinza', 'amna']

# #sort
my_list.sort()
print(my_list)
# # ['amna', 'fatima', 'kinza', 'qirat', 'rimsha', 'sana']

# #pop
my_list.pop(3)
print(my_list)
# # ['amna', 'fatima', 'kinza', 'rimsha', 'sana']

# #remove
my_list.remove("amna")
print(my_list)
# ['fatima', 'kinza', 'rimsha', 'sana']

#clear
# my_list.clear()
# print(my_list)

# #extend:
new_list = ["samreen","ayesha","aimon","farah"]
my_list.extend(new_list)
print(my_list)
# # ['fatima', 'kinza', 'rimsha', 'sana', 'samreen', 'ayesha', 'aimon', 'farah']

#  Python Dictionary Methods
# keys
my_dict={"Ali": 109876,
         "Ahmed":9087,
         "fatima":8899}
print(my_dict.keys())
# dict_keys(['Ali', 'Ahmed', 'fatima'])

# items
print(my_dict.items())
#  dict_items([('Ali', 109876), ('Ahmed', 9087), ('fatima', 8899)])

# values
print(my_dict.values())
#  dict_values([109876, 9087, 8899])

# get
print(my_dict.get("Ali"))
# 109876

# pop
my_dict.pop("Ali")
print(my_dict)
# {'Ahmed': 9087, 'fatima': 8899}

# update
new_dict = {"hamza":24759394}
my_dict.update(new_dict)
print(my_dict)
# {'Ahmed': 9087, 'fatima': 8899, 'hamza': 2374849}

# Tupple Methods

# Count
teachers = ("uroosa","dua","mariyam","rimsha","mahira","aimon")
print(teachers.count("mariyam"))
# 1

# Index
print(teachers.index("mahira"))
#  4

# Try and Except
try:
    result = 20/3  
except zerodivisionerror:
    print("Division by zero error")
else:
    print("Division successful result is", result)
  
# Division successful result is 6.666666666666667