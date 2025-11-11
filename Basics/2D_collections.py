groceries = ({"apple","banana","coconut","orange"},
             {"carrots", "potatoes","tomatoes","onion"},
             {"chicken","fish","mutton","turkey"})

for item in groceries:
    for foods in item:
        print(foods, end=" ")
    print()