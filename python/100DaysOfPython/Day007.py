# Day 07 -  Hangman game

import random

word_list: list = ["aardvark", "baboon", "camel"]
chosen_word: str = random.choice(word_list)
guess: str = str(input("Guess a letter: ")).lower()

HEARTS: int = 6
nums: int = len(chosen_word)
result: list = []
last: bool = False

for i in range(0, nums):
    result += ["_"]

print(f"\n###################################### \n{HEARTS} hearts and {nums} letters in Total.\n###################################### \n")

while HEARTS >= 0 and nums >= 0:
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            result[i] = guess
            nums -= 1
            last = True

    if not last:
        HEARTS -= 1

    if HEARTS == 0:
        print(f"\n###################################### \n\n {result} \n\n######################################")
        print(f"Finished with {HEARTS} hearts and {nums} letters missing.")
        print(f"The word was: {chosen_word}")
        print("YOU LOSE!!!")
        break
    elif nums == 0:
        print(f"\n###################################### \n\n {result} \n\n######################################")
        print(f"Finished with {HEARTS} hearts missing and {nums} letters.")
        print(f"The word was: {chosen_word}")
        print("YOU WON!!!")

        break

    last = False

    print(f"\n {result}\n")
    print(f"{HEARTS} hearts missing and {nums} letters")
    guess: str = str(input("Guess a letter: ")).lower()
