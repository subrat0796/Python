#Classes

class LivingBeing:
  def walk(self):
    print("I am walking...")

class Animal(LivingBeing):
  def __init__(self , name , age):
    self.name = name
    self.age = age

  def values(self):
    print(f"Woof ! My name is {self.name} and {self.age}")

Dog = Animal("Roger" , 8)
Dog.values()
Dog.walk()