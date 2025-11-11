import random

options = ("rock", "paper", "scissors")
running = True

while running:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        
    print(f"Player choose: {player}")
    print(f"Computer choose: :{computer}")

    if player == computer:
        print("it's Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")
        
    if not input("Play Again? (y/n): ").lower() == "y":
        running = False
        
print("Thanks for playing!")