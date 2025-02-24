from funtion import reduce # Import reduce from functon
number = [1,2,3,4,5,6,7,8,9]    # List of number
# Calculate the sum of the number using the reduce funtion
def num (x,y):
  return x + y
  sum = reduce(num,number) # Call reduce outside the num function
  print("sum>>>", sum)  # Print the sum outside the num function

# sum>>> 45