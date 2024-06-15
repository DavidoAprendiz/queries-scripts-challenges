# Day005 - Loops
# Password Generator

import random

letters: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols: list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
numLetters: int = int(input("How many letters would you like in your password?\n"))
numSymbols: int = int(input(f"How many symbols would you like?\n"))
numNumbers: int = int(input(f"How many numbers would you like?\n"))

result: str = ""
resultRandom: str = ""
track: list = []

for i in range(0, numLetters):
    result += random.choice(letters)
for i in range(0, numSymbols):
    result += random.choice(symbols)
for i in range(0, numNumbers):
    result += random.choice(numbers)


while len(result) != len(resultRandom):
    a: int = random.randint(0, len(result)-1)
    if result[a] not in track:
        resultRandom += result[a]
        track += result[a]
        continue


print(result)
print(resultRandom)



# Exercise 1 - Calculate Averages
result: int = 0
student_heights: list = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    result += student_heights[n]

finalResult: float = result / int(len(student_heights))
finalResultRound: int = round(finalResult)
print(finalResultRound)



# Exercise 2 - The Highest score in a List
result: int = 0
student_scores: list = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > result:
        result = student_scores[n]
print(student_scores)
print(f"The highest score in the class is: {result}")



# Exercise 3
result: int = 0
for i in range(0, 101, 2):
    result += i
print(result)



# Exercise 4
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
