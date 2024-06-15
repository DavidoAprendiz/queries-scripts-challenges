# Day 14
# Higher Lower Game

# 'name': 'Instagram',
# 'follower_count': 346,
# 'description': 'Social media platform',
# 'country': 'United States'

from Day014_GameData import data
import random
import os

result_a: dict
result_b: dict
guess: str
game: bool = True
user_points: int = 0

os.system("cls")
print("\nWelcome to Higher Lower\n")

result_a = random.choice(data)
result_b = random.choice(data)
while result_a == result_b:
    result_a = random.choice(data)
    result_b = random.choice(data)

while game:
    if user_points > 0:
        result_a = result_b
        result_b = random.choice(data)
        while result_a == result_b:
            result_b = random.choice(data)

    print(f"Compare A: {result_a['name']}, a {result_a['description']}, from {result_a['country']}.")
    print(f"Against B: {result_b['name']}, a {result_b['description']}, from {result_b['country']}.")
    guess = input("\nWho has more followers. Type 'A' or 'B': ").lower()

    if guess == "a":
        if result_a["follower_count"] > result_b["follower_count"]:
            print("You are right!!")
            user_points += 1
        else:
            print("WRONG")
            game = False
    elif guess == "b":
        if result_b["follower_count"] > result_a["follower_count"]:
            print("You are right!!")
            user_points += 1
        else:
            print("WRONG")
            game = False


print(f"User Final Points: {user_points}")
print(f"A: {result_a['name']}, a {result_a['description']}, from {result_a['country']} with {result_a['follower_count']}.")
print(f"B: {result_b['name']}, a {result_b['description']}, from {result_b['country']} with {result_b['follower_count']}.")
