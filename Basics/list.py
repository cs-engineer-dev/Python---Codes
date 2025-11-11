#List Comprehension = A Concise way to create lists in python.
#                     Compact and Easier to read than traditional loops
#            Syntax = [Expression for value in iterable if condition]

# double = []
# for x in range(1, 11):
#     double.append(x * 2)
    
# print(double)


# double = [x * 2 for x in range(1, 11)]
# tripple = [y * 3 for y in range(1, 11)]
# square = [z * z for z in range(1, 11)]
# fruits = ["apple", "banana", "coconut", "guava"]
# fruits = [fruit.upper() for fruit in fruits]
# fruit_char = [fruit[0] for fruit in fruits]

# print(double)
# print(tripple)
# print(square)
# print(fruits)
# print(fruit_char)

nums = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]

print(positive_nums)
print(negative_nums)