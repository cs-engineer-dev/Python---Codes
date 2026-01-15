#for loops = execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

#for x in range(1 , 11):
#for x in reversed(range(1 , 11)):
#for x in range(1 , 11, 2):

# credit_num = "1234-5678-9012-3456"
# for x in credit_num:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

#print characters
# word = "python"
# for i in word:
#     print(i)
    
# word = "python"
# for i in range(1,11):
#     print(word)

# items = ["pen","pencil","eraser","sharpner","scale"]
# for item in items:
#     print(item)

# for i in range(1,11):
#     print(i*2)

# for i in range(1,21,2):
#     print(i)

# marks = [42,58,63,47,90]
# total = 0
# for mark in marks:
#     total += mark
# print("Total are: ",total)

# nums = [4,2,14,17,8,1]
# for n in nums:
#     if n<10:
#         print(n, "is smaller than 10.")
#     else:
#         print(n, "is greater than 10.")

nums = [4,2,14,17,8,1]
for n in nums:
    if n%2==0:
        print(n, "is even.")
    else:
        print(n, "is odd.")