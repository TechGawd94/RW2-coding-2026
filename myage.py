# birth_year =
birth_year = 1994
age = 2026 - birth_year
name = "Joshua"

print("My name is " + str(name) + " and my age is " + str(age))

#print to the screen:
#my name is x and my age is y
"""
#welcome to fstrings

print(f"My friend is {name}")
"""
"""
user_name = input("What is your name?")
num_1 = input("Give me a number ")
num_2 = input("Give me another number ")
total = int(num_1) + int(num_2)
str(total)

print(f"Your name is: {user_name} and the total is {total}")

#print(f"Your name is: {user_name}")
"""

#lets create functions and learn about global/local variables
"""
name = "Josh"
age =25
city = "KC"

def my_func_1(city):
    name = "Brea"
    age = 21
    city = "Independence"
    print(name,age, city)

print(name,age,city)
my_func_1(city)
"""
"""
#create variable x with value of 5
x = 5
y = "John"
print(type(x))
"""
my_cars = ["mercedes", "bmw", "subaru", "ford", "chrysler", "porsche"]
my_cars.append("corvette")

print(my_cars)
print(f"i drive a {my_cars[2]}")
print(len(my_cars))

# python "for" loop

counter = 0
for car in my_cars:
    print(f"car # {counter} is {car}")
    counter += 1

print("********")

my_range = range(4)
for val in my_range:
    print (f"car # {val} is {my_cars[val]}")

