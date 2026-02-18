running = True
while running:
  a = float(input("Write the first number:"))
  b = float(input("Write the second number:"))
  print("Choose an option:")
  print("1/Sum.")
  print("2/Sumtract.")
  print("3/Multiplication")
  print("4/Division")
  option = int(input("Enter your number choice:"))

  if option == 1: 
   result = round(a + b, 2)
   print(f"The result is {result:g}.")

  elif option == 2: 
   result = round(a - b, 2)
   print(f"The result is {result:g}.")

  elif option == 3:
   result = round(a * b, 2)
   print(f"The result is {result:g}.")

  elif option == 4:
   if b == 0:
    print("You cannot divide by zero.")
   elif b != 0:
    result = round(a / b, 2)
    print(f"The result is {result:g}.")

  elif option == 5:
   print("Goodbay")
   running = False 