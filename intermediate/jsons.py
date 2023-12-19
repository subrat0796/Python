import json 

person = {"name" : "Subrat" , "age" : 20 , "city" : "Bangalore" , "married" : False}

personJson = json.dumps(person , indent=4)
print(personJson)
