# # Inheritence = Allows a class to inherit attributes and methods from another class
# #               helps with code reusability and extansibility
# #               class - child(parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
        
#     def eat(self):
#         print(f"{self.name} is eating.")
        
#     def sleep(self):
#         print(f"{self.name} is sleeping.")

        
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass

# dog = Dog("Scooby")
# cat = Cat("Hirena")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(dog.is_alive)
# dog.speak()
# dog.eat()
# dog.sleep()


#--------------- Multiple Inheritence--------------#

#multiple inheritence = inherit from more than one parent class C(A, B)

'''class Animal:
    def __init__(self,name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
rabbit.flee()
hawk.eat()
hawk.sleep()
hawk.hunt()'''






#multilevel inheritence = inherit from a parent which inherit from another parent  C(B) <- B(A) <- A
#super keyword = Function used in a child class to call the method from a parent class(superclass). allows you to extend the functionality of the inherited method.

'''class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        self.area = (1 * width * height)/2
        
circle = Circle("red", True, 5)
triangle = Triangle("Blue", False, 7, 8)

print(circle.color)
print(circle.is_filled)
print(triangle.color)
print(f"{triangle.area} cm")'''


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"it is {self.color} and {"filled " if self.is_filled else "not filled."}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"The area of the circle is {3.14 * self.radius * self.radius} cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side
        self.area = pow(self.side,4)

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        self.area = (1 * self.width * self.height)/2
        
circle = Circle("red", True, 5)
square = Square("yellow", True, 7)
triangle = Triangle("Blue", False, 7, 8)

print(circle.color)
print(circle.is_filled)
print(f"{square.area} cm")
print(triangle.color)

circle.describe()
square.describe()
triangle.describe()