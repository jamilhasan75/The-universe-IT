#while loop
"""
i = 2
while i < 10:
    print(i, 'i love bangladesh')
    i += 2
"""
#break while
"""
i = 1
while i < 10:
    i += 1
    print(i)
    if i == 3:
        break
  """  

#continue while
"""
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
"""

#For loop
# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print()
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
     break
    print(x)
"""
#for loop range
"""
for x in range(0,10,2):
    print(x)
"""

#nested loop
"""
adj = ["red", "blue", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for x in fruits:
        print(i,x)
"""

# Function
"""
def my_function():
    print("Hello")

my_function()
"""
"""
def home():
    print("My home")

home()
"""
"""
def add(x, y): #parameter(x,y)
    z = x + y
    print(z)
add(1, 2)
add(15, 5)
add(5, 3)
"""

#Type casting
"""
x = (1)
y = (2.5)
z = int("5")

print(type(x))
print(type(y))
print(type(z))
"""

#String formating
"""
p = 50
txt = f"The price is {p} dollars"
print(txt)
"""

