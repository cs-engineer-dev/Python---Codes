#A Datatype tells Python what kind of information you are storing.
#1. String
customer_name = "Pankaj"
print("Customer Name is: ",customer_name)
print("Customer Datatype is: ",type(customer_name))

#2. Numeric - Integer
rating = 4
order_quantity = 3
print("Rating Datatype: ",type(rating))
print("Order_quantity: ",type(order_quantity))

#2. Numeric = Decimal
order_amount = 8999.99
print("Datatype of order_amount: ",type(order_amount))

#2. Numeric = Complex
a = 3+4j
print("Datatype of a: ",type(a))

#3. Boolean
paid = True
print("Paid Datatype: ",type(paid))

#4. Sequence - List
cities = ["JK","PB","HP","CH","HR","DL","UP","BR","WB"]
print("Datatype of Cities: ",type(cities))

#4. Sequence - Tuple(Unchangable)
dimension = (1920, 1080)
print("Dimension Datatype: ",type(dimension))

#4. Sequence - Range
number = range(5)
print(list(number))
print("Datatype of number: ",type(number))

#5. Sequence - Dictionary - JSON File
student = {
    "Name": "Aniket",
    "age": 24,
    "city": "Varanasi"
}
print(student)
print("Datatype of Student: ",type(student))

#4. Sequence - Set
num = {1,2,3,3,4,5,5}
print(num)
print("Datatype of num: ",type(num))

#4. Sequence - None
remarks = None
print(remarks, type(remarks))