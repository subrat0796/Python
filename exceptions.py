# Raising exceptions

try:
  raise Exception('An error has occured!')
except Exception as e:
  print(f"{e}")

class DogNotFoundException(Exception):
  print(f"Inside")
  pass

try:
  raise DogNotFoundException()
except DogNotFoundException as e:
  print(f"Dog not found !")