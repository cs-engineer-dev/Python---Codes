#Magic methods = Dunder methods(double underscore)__init__, __str__, __eq__
#                They are automatically called by many of python's built-in operations.
#                They allow developers to define or customize the behaviour of the objects.

class Student:
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
    def __str__(self):
        return (f"name: {self.name} gpa:{self.gpa}")
    
    def __eq__(self, other):
        return (self.name == other.name)
    
    def __gt__(self, other):
        return (self.gpa > other.gpa)
    
    student1 = Student("Aniket", 7.7)
    