#input and typecasting
# name = input("Enter Your Name- ")
# print("Welcome",name)
# age = int(input("Enter Your Age- "))
# age+=5
# print("Your age is",age)

#Total Sales Calculator
# product = input("Product Name: ")
# quantity = int(input("Enter Quantity Sold: "))
# price_per_unit = float(input("Enter the price per unit: "))

# total_sales = quantity*price_per_unit
# print("Product: ",product)
# print("Total Price is: ",total_sales)

# Salary Slip Calculator
emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
bonus = float(input("Enter Bonus Amount: "))
tax_per = float(input("Enter Tax Percentage: "))

gross = basic_salary+bonus
tax = (gross*tax_per)/100
total_salary = gross-tax

print("#--------Employee Salary Slip---------#")
print("Employee Name:",emp_name)
print("Net Salary:",total_salary)


#take input from student
# print("Student ID")
# name=input("Enter student name: ")
# age=input("Enter age of student: ")
# grade=input("Enter grade of student: ")
# ph_no=input("Enter phone number: ")
# print("Name- ",name)
# print("Age- ",age)
# print("Class- ",grade)
# print("Phone number- ",ph_no)