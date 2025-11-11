#if = if condition is true, then do some code
#else = do something else

# Python Calculator
num1 = float(input("Enter first number: "))
op = input("Enter the operator(+ - * / %): ")
num2 = float(input("Enter second number: "))

if op == "+":
    res = num1 + num2
    print(f"Result: {round(res,3)}")
    
elif op == "-":
    res = num1 - num2
    print(f"Result: {round(res,3)}")
    
elif op == "*":
    res = num1 * num2
    print(f"Result: {round(res,3)}")
    
elif op == "/":
    res = num1 / num2
    print(f"Result: {round(res,3)}")
    
elif op == "%":
    res = num1 % num2
    print(f"Result: {round(res,3)}")
    
else:
    print("Entered operator is invalid.")
    
    
    
    

'''name = input("Enter your name: ")
if name == "":
    print("You didn't type your name...")
    
else:
    print(f"Hello {name}...!") 
    
       

age = int(input('Enter your age: '))
if age >= 18:
    print("You are eligible for vote...!")
    
else:
    print("You are not eligible for vote...!")''' 