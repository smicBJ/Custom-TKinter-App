
# List Comprehension
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


data = [
    User(name="Hudson", age=17),
    User(name="Adriaan", age=12),
    User(name="Samuel", age=14)
]

# students = []
#
# for item in data:
#     if item.name != "Adriaan":
#         students.append(item.name)
#
# print(students)

students = [student.name for student in data if "Adriaan" != student.name]
print(students)

student = "lol" if True else False
