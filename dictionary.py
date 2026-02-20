# this is the dictionary exercise
teacher = {"name":"mike", 
           "age": "48"}

teacher["city"] = "boston"

print(f"{teacher['name']} is {teacher['age']} and lives in {teacher['city']}")
"""
print(teacher["name"] + " is " + str(teacher[age]) + " and lives in " + teacher["city"])
"""
print(teacher["name"] + " is " + (teacher["age"]) + " and lives in " + teacher["city"])