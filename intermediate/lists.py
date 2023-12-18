#Lists : ordered , mutable , allows duplicate elements
my_list = ['banana' , 'cherry' , 'apple']
print(f"Before sorting the list {my_list}")

my_list2 = list()
print(my_list2)

my_list.sort()
print(f"Sorted list {my_list}")

if "banana" in my_list:
  print("found")
else:
  print("not found")

mylist = [0 , 1 , 2 , 3 , 4 , 5 , 6, 7 , 8 , 9 , 10]
a = mylist[1:2]
b = mylist[:2]
c = mylist[1:]
d = mylist[::1]
e = mylist[::2]
f = mylist[::3]
print(a , b , c , d , e , f)

list_org = ['banana' , 'orange' , 'apple']
list_copy = list_org.copy()
list_copy.append('papaya')
print(list_org , list_copy)

org = [1 , 2 , 3 , 4 , 5 , 6]
org_sqr = [i*i for i in org]
print(org_sqr)