#    DATA TYPES 
client_leads={"Aamir": 923000212,
              "Amanullah":923152484,"Arif":9217965}
print (client_leads)
print (client_leads["Amanullah"])
# {'Aamir': 923000212, 'Amanullah': 923152484, 'Arif': 9217965}
# 923152484
print ("before", client_leads)
client_leads["Amanullah"]= 756947321134
print ("after", client_leads)
# before {'Aamir': 923000212, 'Amanullah': 923152484, 'Arif': 9217965}
# after {'Aamir': 923000212, 'Amanullah': 756947321134, 'Arif': 9217965}
def computer(ram):
  if ram > 512:
    return "slow"
  elif ram == 1:
    return "slow"
  else:
    return "fast"
  
print (computer(2))
# fast

def cal(num1,num2,op):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  elif op == "/":
    return num1 / num2
print (cal(6,8,"/"))
# 0.75

def calculator (num1,num2):
  return (num1 + num2,num1 - num2,num1 * num2,num1 / num2)
print (calculator(5,9))
# (14, -4, 45, 0.5555555555555556)

Info = {'Name': 'Taha', 'Age': 20,
        'Resident in': 'Pakistan',
        'Contact': 92347452}
print (Info)
# {'Name': 'Taha', 'Age': 20, 'Resident in': 'Pakistan', 'Contact': 92347452}

def print_x_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
print_x_pattern(7)
# *     *
#  *   * 
#   * *  
#    *   
#   * *  
#  *   * 
# *     *
