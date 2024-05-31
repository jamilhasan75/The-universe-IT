"""
# list data
x = ["apple", "banana", "orange"]
print(x)
print(type(x))

# tuple data
x = ("apple", "banana", "orange")
print(x)
print(type(x))
"""
"""
# Dictionary data
x = {"name" : "jhon", "age" : 30}
print(x)
print(type(x))
"""
"""
# Frozen type data
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
"""

"""
# None type data
x = None
print(type(x)) 
"""
"""
# bhool type data
x = True
print(type(x)) 
"""
"""
#Operators
x = 5
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x ** y)
print(x // y)
"""
# +=
"""
i = 1
while i < 6:
    print(i)
    i += 1
"""
#==
"""
x = 5
y = 2

print(x==y)
print(x!=y)
print(x>y)
print(5>3 and 10<10)
print(5>3 or 10<10)

print(not(5>3 and 10<10))
"""
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(z)
print(x is z)
"""
"""
#in
x = ["apple", "banana"]
print("banana" in x)
"""

#if else
"""
a = 100
b = 50

if b > a:
    print("b is greter than a")
elif a==b:
    print("a  is equal b")
else:
    print("a is greter than b")
"""

x = 30
y = 100
z = 80

if x > y and z:
    print("X is largest number than y and z")
elif y > x and z:
    print("y is largest number than x and z")
else:
    print("z is largest number than x and y")