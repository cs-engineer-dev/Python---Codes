# class variables = shared among all instances of a class
#                   define outside the constuctor
#                   allow you to share data among all objects created from that class

class Student:
    class_year = 2025  #class_variable - outside the constructor
    num_students = 0

    def __init__(you, name, age):
        you.name = name
        you.age = age
        Student.num_students += 1
        
student = Student("Neha", 25)
student1 = Student("Aniket", 24)
student2 = Student("Smita", 22)

print(f"Graduating class of {Student.class_year} has {Student.num_students} students.")

print(f"Name: {student.name:.6},  Age: {student.age}")
print(f"Name: {student1.name:.6}, Age: {student1.age}")
print(f"Name: {student2.name:.6}, Age: {student2.age}")


# print(student1.class_year)
# print(f"My graduating year is: {Student.class_year}")
# print(f"Num of Students: {Student.num_students}")
