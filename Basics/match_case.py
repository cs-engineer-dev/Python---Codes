#match_case statement(Switch) = An alternative to using many 'elif' statement.
#                               Execute some code if a value match a 'case'
#                    benifits = Cleaner and syntax is more redable

# def day_of_week(day):
#     if day == 1:
#         return "Sunday"
#     elif day == 2:
#         return "Monday"
#     elif day == 3:
#         return "Tuesday"
#     elif day == 4:
#         return "Wednesday"
#     elif day == 5:
#         return "Thursday"
#     elif day == 6:
#         return "Friday"
#     elif day == 7:
#         return "Saturday"
#     else:
#         return "Not a valid day..!"

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Tuesday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"
#         case _:    # wild card-(Same as the else statement)
#             return "Not a valid day..!"

def is_weekend(day):
    match day:
        case "Sunday" | "Monday":
            return True 
        case "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday":
            return False
        case _:    # wild card-(Same as the else statement)
            return "False"
     
print(is_weekend("Monday"))