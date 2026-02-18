# the hash is a one line comment

"""
the triple quotes are a multi-line comment
see
believ me
anything inside will not execute
"""

#this will print to the screen
print("Hello World!")

#float
price = 5.99
#interger
age = 35
#boolean
is_here = True
#string
name = "Joshua"

print(type(name))
print(type(age))
print(type(is_here))
print(type(price))

print("Joshua's age is" + str(age))

#this is the basic python if statement

if age > 36:
    print("you are an unc")

#this a more complex if statement
"""
if age > 36:
    print("you are an unc")
else:
    print("you are not an unc")
    """
age = 99

    #this an even more complex if statement
if age > 36:
    print("you are an unc")
elif age < 34:
    print("you are not an unc")
else:
    print("you must be 35 years old")

# python operators arithmetic and comparison
"""
arithmetic: + add, - subtract, * multiplication, / Division

Comparison: ==equal, != not equal, > greater then, < less than, >= GT or Eq, <= LT or Eq
"""

print(5 * 5)

num_1 = 9
num_2 = 8
total = num_1 + num_2

print("The total of num_1 and num_2 is:" + str(total))