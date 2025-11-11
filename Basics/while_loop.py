#while loop = execute some code WHILE some condition remains true

# age = int(input("Enter Your age: "))

# while age < 0:
#     print("age can't be negative.")
#     age = int(input("Enter Your age: "))
    
# print(f"Your age is {age} years old.")


food = input("Enter a food that like you(q to quit): ")
while not food == "q":
    print(f"you like {food}!!")
    food = input("Enter another food that you like (q to quit): ")
    
print("Bye...!!!")