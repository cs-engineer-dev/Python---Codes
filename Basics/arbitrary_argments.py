# *args    = allows you to pass multiple non-key arguments - we dont know user pass how many arguments. So use "args"
# **kwargs = allows you to pass multiple keyword - arguments
#            * unpacking operator

# def add(a, b):     Normal function
#     return a + b

#----------------- *args(tuple) --------------------#

# def add(*args):        # * - Unpacking operator
#     total = 0          # we can change the args parameter name with any other parameter name but use the * at the beggining.
#     for arg in args:
#         total += arg
#     return total
        
# print(add(1, 2, 3, 4, 5))

# def display_name(*names):
#     for name in names:
#         print(name, end = " ")
        
# display_name("Dr.", "Harpal", "Theti")

# #----------------- **kwargs(Dict) --------------------#

# def display_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key:6}: {value}")
        
# display_address(apt_no = "100",
#                 street = "Fake street",
#                 city = "Colambo",
#                 state = "MI",
#                 zip = "987650")

#----------------- **Exercise --------------------#
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for key, value in kwargs.items():
    #     print(f"{key:6}:{value}")
    print(f"{kwargs.get('apt')} {kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get("zip")}")
        
shipping_label("Dr.", "Aniket", "Prakash",
               apt = "100",
               street = "fake street",
               city = "Shikago",
               state = "Michigan",
               zip = "543210")    