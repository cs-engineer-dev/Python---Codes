#variable scope = where a varibale is visible and accessible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#---------Variable Scope-----------#
# def fun1():
#     a=1
#     print(a)
    
# def fun2():
#     b=2
#     print(b)
    
# fun1()
# fun2()

#---------Local Scope-----------#
# def fun1():
#     x=1
#     print(x)
    
# def fun2():
#     x=2
#     print(x)
    
# fun1()
# fun2()

#---------Enclosed Scope-----------# One fn declare to another fn.
# def fun1():
#     x=1
        
#     def fun2():
#         x=2
#         print(x)
#     fun2()
    
# fun1()

#---------Global Scope-----------#
def fun1():
    print(x)
    
def fun2():
    print(x)
    
x=3
fun1()
fun2()