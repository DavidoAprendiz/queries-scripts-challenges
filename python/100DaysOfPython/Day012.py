# Day 12
# Guessing Number Game

import random


random_number: int
guess: int
attempts: int


def diff():
    choose_dif = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if "hard" in choose_dif:
        # attempt = 5
        return 5
    else:
        # attempt = 10
        return 10


print("welcome to the Guessing Number")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

attempts = diff()

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guess < random_number:
        print("Too low.\nGuess again.")
        attempts -= 1
    elif guess == random_number:
        print("YOU WON!!!")
        break

print(f"The random number was: {random_number}")





