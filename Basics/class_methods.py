#class methods = Allow operations related to the class itself
#                Take (self) as first parameter, which represents class itself.

class Student:
    
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa  = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    def get_info(self):
        return(f"{self.name} {self.gpa}")
    
    @classmethod
    def get_count(cls):
        return(f"Total # of Students: {cls.count}")
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return (f"{cls.total_gpa/cls.count}")

Student1 = Student("Aniket", 8.7)
Student2 = Student("Anshul", 8.1)   
Student3 = Student("Gaurav", 8.2)   

print(Student.get_count())
print(Student.get_average_gpa())