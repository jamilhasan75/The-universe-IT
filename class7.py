# The __init__() Function
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# p2 = Person("John1", 30)

# print(p1.name)
# print(p1.age)

# print(p2.name)
# print(p2.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# # print(p1.name)
# # print(p1.age)
# print(p1)

#the __str__() function:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)


#Inheritance
class baba:
    car = "BMW"
    tk = "100 M"

class child1:
    bike = "R15"
    phone = "I phone 15"

class child2(baba, child1):
    laptop = "HP"
    phone = "I phone 15"

print(child1.bike)
print(child2.laptop)
