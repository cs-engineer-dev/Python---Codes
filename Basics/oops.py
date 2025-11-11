# Object = A bundle of related attributes(variables) and methods(functions). Ex - Car, phone, book, cup
# You need a "class" to create many objects.
# class = (blueorint) used to design the structure and layout of an object.
# constructor method = def __init__(self, other attributes):  self means this object is creating right now.

from car import Car
        
car1 = Car("BMW", 2022, "Red", False)
car2 = Car("mustung", 2024, "Black", True)

car1.stop()
car2.drive()
car1.describe()