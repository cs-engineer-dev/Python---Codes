#Membership Operators = used to test whether a value or variable is present in sequence or not.
#                       (string, list, tuple, set or dictionary)
#                       1. in      2. not in

# word = "ANIKET"
# letter = input("Guess a letter in the word: ")
# if letter in word:
#     print("Right Guess...!")
    
# else:
#     print("Not Found - X")
    
    
# students = {"Aniket", "Deepak", "Daya", "Nitesh"}
# student = input("Enter the student name: ")

# if student not in students:
#     print(f"{student} not found.")
    
# else:
#     print(f"{student} is present.")

grades = {"Aniket":"A", 
            "Deepak":"B",
            "Daya":"C",
            "Nitesh":"D"}
student = input("Enter the student name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
    
else:
    print(f"{student} is not present.")