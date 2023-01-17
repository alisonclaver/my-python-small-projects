#MY CODED CALCULATOR IN PYTHON

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum = lambda x, y: print("SUM: " + str(x + y))
difference = lambda x, y : print("DIFFERENCE: " + str(x - y))
quotient = lambda x, y : print("QUOTIENT: " + str(x * y))
product = lambda x, y : print("PRODUCT: " + str(x / y))

chooseoperator = input("""
Choose your operator: 
  1 - ADDITION
  2 - SUBTRACTION
  3 - DIVISION
  4 - MULTIPLICATION
""")

if chooseoperator == '1':
  sum(x, y)
elif chooseoperator == '2':
  difference(x, y)
elif chooseoperator == '3':
  quotient(x, y)
else:
  product(x, y)

letscontinue = input("Do you still want to continue?")
                     


  
  


