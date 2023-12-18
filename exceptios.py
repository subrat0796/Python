#Exceptions

def divide(a , b):
  try:
    res = a/b
  except ZeroDivisionError:
    print("Cannot divide by zero")
  except ArithmeticError:
    print("There was some arithmetic division error")
  finally:
    print(f"Result {res}")

divide(2 , 1)