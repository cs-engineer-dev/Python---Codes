# #keyword argument = an argument preceded by an identifier helps with readability.
# #                   Order of argument doesn't matter

# def hello(greetings, title, first, last):
#     print(f"{greetings} {title} {first} {last}")
    
# #hello("Hello.!", "Mr.", "Aniket", "Prakash")  #Positional arguemnt - position does matter

# hello("Hello.!", last = "Prakash", first = "Aniket", title = "Mr.") #Keyword argumnet - position doesn't matter
# hello("Hlw..", first = "Anand", last = "Sir", title = "Mr.")

def get_phone(country, area, first, last):
    return (f"{country}-{area}-{first}-{last}")
    
phone_num = get_phone(91, 123, 456, 7890)
print(phone_num)