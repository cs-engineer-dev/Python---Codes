
# name = input("Enter Your full name: ")
# num = input("Enter your phone number: ")

#result = name.isalpha()
#result = name.isdigit()
#result = name.lower()
#result = name.upper()
#result = name.capitalize()
#result = name.rfind("e")   if any word is not present, it returns -1
#result = name.find("n") 
#result = len(name)
#result = num.count(" ")
#result = num.replace(" ", "")

#print(help(str))

username = input("Enter a username: ")

if len(username) > 14:
    print("username not contains more than 12 characters.")

elif not username.find(" ") == -1:
    print("username can't contain spaces.")
    
elif not username.isalpha():
    print("username can't contain number.") 
else:
    print(f"Welcome {username}")