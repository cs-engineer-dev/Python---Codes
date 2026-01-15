# age = int(input("Enter age: "))
# if age >=18:
#     print("You are eligible for Vote.")
    
# else:
#     print("Not Vote.")

#Discount
# amount = float(input("Enter total price: "))
# if amount>=2000:
#     print("30% Discount.")
# elif amount>= 1500:
#     print("20% Discount")
# elif amount>=1000:
#     print("10% Discount")
# else:
#     print("No Discount.")
    
# Email Validation
# email = input("Enter email: ")
# if "@" in email and "." in email:
#     print("Valid Email.")
# else:
#     print("Invalid Email.")

print("#----------Check Eligibility------#")
age = int(input("Enter your Age: "))
if age>=18:
    id_no = int(input("Enter id_NO: "))
    if id_no == 9852:
        print("Verified Succesfully...!")
    else:
        print("Retry...")
else:
    print("You are not Eligible.")