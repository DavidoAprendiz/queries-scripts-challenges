# Day 11
# Blackjack game
############## Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# USER WINS = TRUE
# PC WINS = FALSE

import random
import os

cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on: bool = True
user: list = []
pc: list = []
result: bool
hit: str = ""


def deal_cards(user_cards, pc_cards, game_cards, choice):
    if not bool(user_cards):
        user_cards += [random.choice(game_cards)]
        user_cards += [random.choice(game_cards)]
        pc_cards += [random.choice(game_cards)]
        pc_cards += [random.choice(game_cards)]
    else:
        if choice == "y":
            user_cards += [random.choice(game_cards)]
        elif choice == "n":
            pc_cards += [random.choice(game_cards)]


def is_blackjack(user_cards, pc_cards):
    if sum(user_cards) == 21 and sum(pc_cards) < 21:
        return True
    elif sum(pc_cards) == 21 and sum(user_cards) < 21:
        return False
    elif sum(user_cards) == 21 and sum(pc_cards) == 21:
        return False


def check_21_or_more(user_cards, pc_cards):
    for i in range(len(user_cards)):
        if user_cards[i] == 11 and sum(user_cards) > 21:
            user_cards[i] = 1
    for i in range(len(pc_cards)):
        if pc_cards[i] == 11 and sum(pc_cards) > 21:
            pc_cards[i] = 1


def check_draw(user_cards, pc_cards):
    if sum(user_cards) == sum(pc_cards):
        return True
    return False


print("\n\nWelcome to Blackjack\n")

while game_on:

    deal_cards(user, pc, cards, hit)

    print(f"User:  {user}")
    if not bool(pc):
        print(f"PC:    {pc}\n")
    else:
        print(f"PC:    {[pc[0]]}\n")

    check_21_or_more(user, pc)
    if sum(user) > 21:
        print(f"#User:  {user}")
        print(f"#PC:    {pc}\n")
        print("PC WINS!!!")
        exit_game: str = input("\nExit game?? Y or N:    ").lower()
        if exit_game == "y":
            game_on = False
            break
        else:
            os.system("cls")
            print("\n\nWelcome to Blackjack\n")
            user = []
            pc = []
            hit = ""
            game_on = True
            break
    elif sum(pc) > 21:
        print(f"#User:  {user}")
        print(f"#PC:    {pc}\n")
        print("USER WINS!!!")
        exit_game: str = input("\nExit game?? Y or N:    ").lower()
        if exit_game == "y":
            game_on = False
            break

    hit = input("One more card? Y or N:    ").lower()

    if hit == "n":
        game_on_2: bool = True
        while game_on_2:
            if sum(pc) < 16:
                deal_cards(user, pc, cards, hit)
                print(f"User:  {user}")
                print(f"PC:    {pc}\n")
            else:
                check_21_or_more(user, pc)
                if sum(user) > 21:
                    print("PC WINS!!!")
                    print(f"#User:  {user}")
                    print(f"#PC:    {pc}\n")
                    game_on = False
                    break
                elif sum(pc) > 21:
                    print("USER WINS!!!")
                    print(f"#User:  {user}")
                    print(f"#PC:    {pc}\n")
                    game_on_2 = False
                    break

                if check_draw(user, pc):
                    print("nobody wins. It's a DRAW!!!")
                    print(f"#User:  {user}")
                    print(f"#PC:    {pc}\n")
                    game_on_2 = False
                    break

                if is_blackjack(user, pc):
                    print("USER WINS!!!")
                    print(f"#User:  {user}")
                    print(f"#PC:    {pc}\n")
                    game_on_2 = False
                    break
                else:
                    print("PC WINS!!!")
                    print(f"#User:  {user}")
                    print(f"#PC:    {pc}\n")
                    game_on_2 = False
                    break

        exit_game: str = input("\nExit game? Y or N:    ").lower()
        if exit_game == "y":
            game_on = False
            break
        else:
            os.system("cls")
            print("\n\nWelcome to Blackjack\n")
            user = []
            pc = []
            hit = ""
            game_on = True
