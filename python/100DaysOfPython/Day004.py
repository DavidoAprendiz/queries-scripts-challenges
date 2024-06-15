# Day 4 - Randomisation and Python Lists
#
import random
a: int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
b: int = random.randint(0, 2)

if a < 0 or a >= 3:
    print("Invalid Input")
elif a == 0:
    if b == 0:
        print("Tie")
    elif b == 1:
        print("Player 'A' Lose. PC Win.")
    elif b == 2:
        print("Player 'A' Win. PC Lose.")
elif a == 1:
    if b == 0:
        print("Player 'A' Win. PC Lose.")
    elif b == 1:
        print("Tie")
    elif b == 2:
        print("Player 'A' Lose. PC Win.")
elif a == 2:
    if b == 0:
        print("Player 'A' Lose. PC Win.")
    elif b == 1:
        print("Player 'A' Win. PC Lose.")
    elif b == 2:
        print("Tie")



# Exercise 1
import random
randomNumber: int = random.randint(0, 1)
if randomNumber == 1:
    print("Heads")
else:
    print("Tails")



# Exercise 2
# without random.choice()
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
randomPerson = random.randint(0, len(names)-1)
print(f"{names[randomPerson]} is going to buy the meal today!")



# Exercise 3
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if position[0] == "1" and position[1] == "1":
    row1 = ["'x'️", "⬜️", "⬜️"]
elif position[0] == "1" and position[1] == "2":
    row2 = ["'x'️", "⬜️", "⬜️"]
elif position[0] == "1" and position[1] == "3":
    row3 = ["'x'️", "⬜️", "⬜️"]

if position[0] == "2" and position[1] == "1":
    row1 = ["⬜️", "'x'️", "⬜️"]
elif position[0] == "2" and position[1] == "2":
    row2 = ["⬜️", "'x'️", "⬜️"]
elif position[0] == "2" and position[1] == "3":
    row3 = ["⬜️", "'x'️", "⬜️"]

if position[0] == "3" and position[1] == "1":
    row1 = ["⬜️", "⬜️", "'x'️"]
elif position[0] == "3" and position[1] == "2":
    row2 = ["⬜️", "⬜️", "'x'️"]
elif position[0] == "3" and position[1] == "3":
    row3 = ["⬜️", "⬜️", "'x'️"]

print(f"{row1}\n{row2}\n{row3}")
