#Indexing = accessing elements of a sequence using [] (indexing operator) [start : end: step]

#credit_num = "1234-5678-9012-3456"

# print(credit_num[2])
# print(credit_num[-1])

# String Slicing
# print(credit_num[:4])
# print(credit_num[0:4])
# print(credit_num[5:])
# print(credit_num[5:-1])
# print(credit_num[::3])
# print(credit_num[::-1])
# print(credit_num[0:18:2])

product = "LAptop pro Max 2025"
print(product[3:6])
print(product[-4:])
print(product[:6])
print(product[::2])
print("Reverse String:",product[::-1])

#last_digit = credit_num[-4:]
#print(f"XXXX-XXXX-XXXX-{credit_num[-4:]}")

#Python string function
# s = "Para Olympic Games"
# print("Split[]: ",s.split("m"))
# print("Partition(): ",s.partition("m"))
# print(s[5])

#All Possible Substrings
# str = "hello"
# substr = []
# for i in range(0, len(str)):
#     for j in range(i+1, len(str)+1):
#         substr.append(str[i:j])
        
# print(substr)