# Guess computer 

import random

def guess(x):

    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))

        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")
    
    print("Congratulation! you won")
        
guess(10)