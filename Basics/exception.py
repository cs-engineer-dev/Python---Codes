# def exceptionHandle():
#     try:
#         a=int(input("Enter first num: "))
#         b=int(input("Enter second num: "))
#         res=a/b
        
#     except ZeroDivisionError:
#         print("Error: cannt devide by zero")
        
#     except ValueError:
#         print("Value is not a valid integer")
        
#     else:
#         print("Result: ",res)
        
#     finally:
#         print("Execution Completed.")
# exceptionHandle()


a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
try:
    c=a/b
    print("Result: ",c)
    
except:
    print("Cant Divide by Zero.")
    
finally:
    print("Execution Completed...!")