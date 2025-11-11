#static methods = A method that belong to a class rather than any object from that class(instance)
#                 Usually used for general utility functions

#Instance method = Best for operations on instances of the class(Objects)
#Static methods = Best for utility functions that do not need access to class data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return(f"{self.name} = {self.position}")
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook", "Janitor"]
        return position in valid_positions
    
emp1 = Employee("Aniket", "Manager")
emp2 = Employee("Rahul", "Cashier")
emp3 = Employee("Rakesh","Cook")
emp4 = Employee("Sagun","Janitor")
    
print(Employee.is_valid_position("Rocket"))
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
print(emp4.get_info())