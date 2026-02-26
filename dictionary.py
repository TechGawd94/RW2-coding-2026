# this is the dictionary exercise
teacher = {"name":"mike", 
           "age": "48"}

teacher["city"] = "boston"

print(f"{teacher['name']} is {teacher['age']} and lives in {teacher['city']}")
"""
print(teacher["name"] + " is " + str(teacher[age]) + " and lives in " + teacher["city"])
"""
print(teacher["name"] + " is " + (teacher["age"]) + " and lives in " + teacher["city"])

userInput = input("What is your name? ")

if userInput == "mike": 
    role = "teacher"
else:
    role = "student"

while role == "teacher":
    print("Life is great! ")

counter = 1
while counter <= 3:
    if role == "teacher":
        print("Life is great!")
else:
    print("Life is tough!")
counter +=1

#opening file with a python

myNameFile = open("names.txt")
for line in myNameFile:
    print(line)
    