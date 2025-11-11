#Collections = single "variable" used to store multiple values
# List[] = ordered and changable, Duplicate values - OK
# Set{}  = unordered and unchangable, but add/remove - OK, No duplicates
# Tuple{} = ordered and unchangable, Duplicates OK, faster
#Dictionary = a collection of {key:value} pairs ordered and changable. No duplicates

#-----------------LIST[]-----------------#

#fruits = ["apple", "mango", "banana", "coconut", "orange"]

#print(len(fruits))
#print(dir(fruits))
# print(fruits[::-1])
#print(fruits[::2])
#print(fruits[:3])
#print(fruits[4])
#print("pineapple" in fruits)

# fruits[0] = "pineapple"
# for fruit in fruits:
#     print(fruit)

#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "lichi")
#fruits.reverse()
#fruits.sort()
#fruits.clear()
#print(fruits.index("banana"))
#print(fruits.count("banana"))


#-----------------SET{}-----------------#

# fruits = {"apple", "mango", "banana", "coconut", "orange","apple"}

#print(dir(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
# fruits.add("pineapple")
#fruits.remove("banana")
#fruits.pop()          random remove the items
#fruits.clear()
#print(fruits)

#-----------------TUPLE{}-----------------#

#fruits = ("apple", "mango", "banana", "coconut", "orange")

#print(dir(fruits))
#print(len(fruits))
#print("pineapple" in fruits)
#print(fruits.index("apple"))
#print(fruits.count("apple"))

# for fruit in fruits:
#     print(fruit)
#print(fruits)

#---------------DICTIONARY-------------#

# capitals = {"USA": "Washington D.C",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}

#print(dir(capitals))
#print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print(f"The capital is {capitals.get("Russia")}")
# else:
#     print("The capital doesn't exist.")

# capitals.update({"Germany": "Berlin"})
#capitals.pop("China")
#capitals.popitem()  remove the last one
#capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
#     print(key)

#values = capitals.values()
#for value in values:
#     print(value)

# items = capitals.items()   #.items() function - its reassamble a 2D list of tuples. it returns key and value during each iterations.
# for key, value in items:
#     print(f"{key} : {value}")

#---------MENU PROGRAM----------#

menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda":3.00,
        "lemonade":4.50}

cart = []
total = 0
print("#--------------MENU------------#")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    
print("-------------------------------")

while True:
    item = input("Select an item(q to quit): ")
    if item.lower() == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        
print("-----------YOUR ORDER----------")
        
for item in cart:
    total += menu.get(item)
    print(item, end=" ")
    
print()
print(f"Total is: {total:.2f}")

print("-------------------------------")