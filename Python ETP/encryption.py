import random
import string

chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
char = list(chars)
key = char.copy()

random.shuffle(key)

print(f"chars: {char}")
print(f"keys: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
ciphar_text = " "

for letter in plain_text:
    index = chars.index(letter)
    ciphar_text += key[index]
    
print(f"Original Text: {plain_text}")
print(f"Encrypted Text: {ciphar_text}")


#DECRYPT
ciphar_text = input("Enter a message to encrypt: ")
plain_text = ""

for leter in ciphar_text:
    index  = key.index(letter)
    plain_text += chars[index]
    
print(f"Encrypted Text: {ciphar_text}")
print(f"Original Text: {plain_text}")