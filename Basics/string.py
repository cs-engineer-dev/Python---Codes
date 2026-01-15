# name = input("Enter Your full name: ")
# num = input("Enter your phone number: ")

# result = name.isalpha()
# result = name.isdigit()
# result = name.lower()
# result = name.upper()
# result = name.capitalize()
#result = name.rfind("e")   if any word is not present, it returns -1
#result = name.find("n") 
#result = len(name)
#result = num.count(" ")
#result = num.replace(" ", "")

#print(help(str))

# username = input("Enter a username: ")

# if len(username) > 14:
#     print("username not contains more than 12 characters.")

# elif not username.find(" ") == -1:
#     print("username can't contain spaces.")
    
# elif not username.isalpha():
#     print("username can't contain number.") 
# else:
#     print(f"Welcome {username}")


#STRING METHODS

# text1 = "Hello Learners"
# print("Original string",text1)
# print("Remove Spaces:",text1.strip()) #strip - for all spaces, rtrip - for right side spaces, ltrip - for left side spaces
# print("Capital:",text1.capitalize())
# print("Upper:",text1.upper())
# print("Lower:",text1.lower())
# print("Proper:",text1.title().strip())
# print("Replace:",text1.replace(" "," python "))
# print("Count:",text1.count("e"))
# print("Start with:",text1.startswith("Hello"))
# print("Lower",text1.lower())

# msg = "Welcome to Python COding"
# words = msg.split()
# print("Word List: ",words)
# join_text = "-".join(words)
# print(join_text)

#Extract Domain
email = "aniketprakashkvs@gmail.com"
domain = email[email.find("@")+1:]
print("Domain:",domain)