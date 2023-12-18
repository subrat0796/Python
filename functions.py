# Map , reduce , filter

from functools import reduce

expenses = [
  ('Dinner' , 20),
  ('Car repair' , 80)
]

def summation(a , b):
  return a[1] + b[1]

sum = reduce(summation , expenses)
print(sum)

numbers = [1 , 2 , 3]

def double(a):
  return a * 2

result = map(double , numbers)
print(list(result))

def isEven(a):
  return a % 2 == 0

result = filter(isEven , numbers)
print(list(result))