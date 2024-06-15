# Day 09 - Dictionaries and nesting
# Auction game

import os

print("Welcome to Auction!")

bids_on: bool = True
name: str
bid: int
total_bids: dict = {}
ask_player_exit: str
winner_user: str = ""
winner_bid: int = 0


while bids_on:
    name = input("Input your name: ")
    bid = int(input("Input your bid: €"))

    total_bids[name] = bid

    ask_player_exit = input("Next player? yes or no\n").lower()
    if ask_player_exit == "no":
        bids_on = False
    elif ask_player_exit == "yes":
        os.system("cls")

for user in total_bids:
    if total_bids[user] > winner_bid:
        winner_user = user
        winner_bid = total_bids[user]


print(f"The winner is {winner_user} with a bid of €{winner_bid}")
# print(total_bids)



# Exercise 1
student_scores: dict = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades: dict = {}
for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 91:
        student_grades[student] = "Outstanding"

print(student_grades)




# Exercise 2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country: str, visits: int, cities: list):
    travel_log.append({"country": country, "visits": visits, "cities": [cities]})


add_new_country("Portugal", 9000, ["Lisboa", "Porto"])
print(travel_log)
