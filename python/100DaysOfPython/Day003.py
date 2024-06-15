# Day 3 - Conditional Statements, Logical Operators...
# Find the treasure
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
result = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\".\n").lower()
if result == "left":
    result = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if result == "wait":
        result = input("You arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?\n").lower()
        if result == "blue" or result == "red":
            print("Game Over. Don't open strange doors.")
        if result == "yellow":
            print("YOU WIN!!!")
    else:
        print("Game Over. You shouldn't swim here.")
else:
    print("Game Over. Bad path.")



# Exercise 1
number = int(input("Which number do you want to check? "))
if number % 2:
    print("This is an odd number.")
else:
    print("This is an even number.")



# Exercise 2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    #  (18 < bmi <= 22)
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")



# Exercise 3
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")



# Exercise 4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Prices (as immutable variables)
small_pizza: int = 15
medium_pizza: int = 20
large_pizza: int = 25
pepperoni_small: int = 2
pepperoni_big: int = 3
cheese: int = 1

if size == "s" or size == "S":
    if add_pepperoni == "y" or add_pepperoni == "Y":
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${small_pizza+pepperoni_small + cheese}.")
        else:
            print(f"Your final bill is: ${small_pizza + pepperoni_small}.")
    else:
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${small_pizza + cheese}.")
        else:
            print(f"Your final bill is: ${small_pizza}.")
elif size == "m" or size == "M":
    if add_pepperoni == "y" or add_pepperoni == "Y":
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${medium_pizza + pepperoni_big + cheese}.")
        else:
            print(f"Your final bill is: ${medium_pizza + pepperoni_big}.")
    else:
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${medium_pizza + cheese}.")
        else:
            print(f"Your final bill is: ${medium_pizza}.")
elif size == "l" or size == "L":
    if add_pepperoni == "y" or add_pepperoni == "Y":
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${large_pizza + pepperoni_big + cheese}.")
        else:
            print(f"Your final bill is: ${large_pizza + pepperoni_big}.")
    else:
        if extra_cheese == "y" or extra_cheese == "Y":
            print(f"Your final bill is: ${large_pizza + cheese}.")
        else:
            print(f"Your final bill is: ${large_pizza}.")



# Exercise 5
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowerName1 = name1.lower()
lowerName2 = name2.lower()
total_true = 0
total_love = 0

total_true += lowerName1.count("t") + lowerName2.count("t")
total_true += lowerName1.count("r") + lowerName2.count("r")
total_true += lowerName1.count("u") + lowerName2.count("u")
total_true += lowerName1.count("e") + lowerName2.count("e")

total_love += lowerName1.count("l") + lowerName2.count("l")
total_love += lowerName1.count("o") + lowerName2.count("o")
total_love += lowerName1.count("v") + lowerName2.count("v")
total_love += lowerName1.count("e") + lowerName2.count("e")

result = int(str(total_true)+str(total_love))

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif 40 < result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
