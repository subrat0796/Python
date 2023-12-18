#Dictionaries : Key - Value pairs , Unordered , Mutable
mydict = {"name" : "Max" , "age" : 28 , "city" : "Bangalore"}
print(mydict)
mydict2 = dict(name="Max" , age=28 , city="Bangalore" , values=12)

for key , value in mydict2.items():
  print(f"{key} : {value}")