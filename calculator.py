a = float(input("Write the first number:"))
b = float(input("Write the second number:"))

print("Choose an option:")
print("1/Sum.")
print("2/Sumtract.")

option = int(input("Enter 1 or 2:"))

if option == 1: 
   result = a + b
   print(f"The result is {result}.")

elif option == 2: 
   result = a - b
   print(f"The result is {result}.")