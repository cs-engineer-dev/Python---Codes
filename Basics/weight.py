weight = float(input("Enter your weight: "))
unit = input("Kilograms OR Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    
elif unit == "L":
    weight = weight/2.205
    unit = "Kg."
    
else:
    print(f"{unit} is not valid.")
    
print(f"Your weight is: {round(weight,1)} {unit}")