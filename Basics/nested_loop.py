#nested loop = A loop within another loop(outer, inner)

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()

rows = int(input("Enter the no of rows: "))
columns = int(input("Enter the no of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
        
    print("\n")