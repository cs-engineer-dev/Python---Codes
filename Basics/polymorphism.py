'''Polymorphism = Greek word that means to have many form or faces
           Poly = Many
         Morphe = forms
         TWO WAYS TO ACHIEVE POLYMORPHISM
         1. Inheritence = An object could be trated of the same type as parent class
         2. Duck Typing = Object must have necessary attributes/methods'''
         
 
'''from abc import ABC, abstractmethod       
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * pow(self.radius,2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return pow(self.side, 4)

class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return (self.height * self.width)/2
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(5), Square(5), Triangle(5, 4), Pizza("pepperoni", 15)]

for shape in shapes:
    print(shape.area())'''
    
    
# Duck Typing = Another way to acheive polymorphism besides inheritence
#               Object must have minimum necessary attributes/methods
#               "if it looks like a duck and quacks like duck, it must be a duck."

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Car:
    alive = False
    def speak(self):
        print("HONK!")
        
        
animals = [Dog(), Cat(), Car()]
for animal in animals:
    print(animal.speak())
    print(animal.alive)