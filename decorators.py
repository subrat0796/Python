#Decorators

def log_time(func):
  def wrapper():
    print("Before")
    val = func()
    print("After")
  return wrapper

@log_time
def hello():
  """This is a hello function wrapped in decorator"""
  print("Hello")

hello()
print(help(hello))