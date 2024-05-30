import random

options = ('rock', 'paper', 'scissors')
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

print(f"Player's choice: {player}")
print(f"Computer chooses: {computer}")

if player == computer:
    print("I'ts a tie")
elif player == 'rock' and computer == 'scissors':
    print("Player wins!")
elif player == 'scissors' and computer == 'paper':
    print("Player wins!")
elif player == 'paper' and computer == 'rock':
    print("Player wins!")
else:
    print("You lose!")

