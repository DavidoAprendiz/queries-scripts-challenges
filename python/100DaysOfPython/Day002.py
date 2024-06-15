# Day 2 - Data types
# Create Tip Calculator
print("Welcome to tip calculator")
total = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
num_people = input("How many people to split the bill? ")
result = (((float(total) * int(percentage)) / 100) / int(num_people)) + (float(total)/int(num_people))
print(f"Each person should pay: ${round(result, 2)}")


# Exercise 1
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# Exercise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# print(int(int(weight) / (float(height) * float(height))))
print(int(int(weight) / (float(height) ** 2)))


# Exercise 3
age = input("What is your current age?")
missing = 90 - int(age)
days = missing*365
weeks = missing*52
months = missing*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
