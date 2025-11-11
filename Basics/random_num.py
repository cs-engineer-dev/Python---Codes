import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# number = random.random()
# number = random.randint(low, high)
# number = random.choice(options)
# random.shuffle(cards)

# print(cards)

print("#------Number Guessing Games---------#")

low = 1
high = 100

answer = random.randint(low, high)
guesses = 0
is_running = True

print(f"Select a number between {low} and {high}: ")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low or guess > high:
            print("That number is out of range.")
            print(f"Please select a number between {low} and {high}: ")
        elif guess < answer:
            print("Too Low! try Again....")
        elif guess > answer:
            print("Too High! Try Again...")
        else:
            print(f"Correct! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
            
    else:
        print("Invalid guess.")
        print(f"please select a number between {low} and {high}: ")