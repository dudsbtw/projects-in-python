first_value = input("Enter the first value: ")
second_value = input("Enter the second value: ")

if int(first_value) > int(second_value):
  print("The first value is higher.")
elif int(first_value) == int(second_value):
  print("The values are equal.")
else:
  print("The second value is higher.")
