#module = a file containing code you want to include in your program use 'import' to include a module(built-in or your own) useful to break up a large program reusable separate files.

#import math
#import math as mt
# from math import pi

import module1

# result = module1.pi
# result = module1.square(4)
# result = module1.cube(5)
# result = module1.circumference(4)
result = module1.area(4)

print(result)