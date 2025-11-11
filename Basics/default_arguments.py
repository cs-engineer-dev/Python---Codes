# default arguments = A default value for certain parameters. 
# default is used when that argument is omitted make your functions more flexible, reduces of arguments.   
# 1. positional, 2. Default, 3. keyword, 4. Arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):   # default value of discount and tax
#     return list_price * (1 - discount) * (1 + tax)

#print(net_price(500, 0, 0.05))
#print(net_price(500))
#print(net_price(500, 0.1,0))  # it will override the default discount and tax value


import time
#def count(start, end):
def count(end, start = 1):   #starting from 1 is set default argument, so we need to declare after non-default argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE...!")

count(30, 15) # dafult argument will be override
#count(10)