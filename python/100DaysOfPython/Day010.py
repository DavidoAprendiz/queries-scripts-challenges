# Day 10 - Functions
# Calculator

def calcular(first, op, second):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":
        return first / second
    else:
        return "Input invalid"


stop_game: bool = False
print("Welcome to Calculator")

while not stop_game:
    first_number = float(input("First Number: "))
    print("+", end="  ")
    print("-", end="  ")
    print("*", end="  ")
    print("/")
    operator = input("Choose the operator: ")
    second_number = float(input("Second Number: "))

    result = calcular(first_number, operator, second_number)
    print(f"{first_number} {operator} {second_number} = {result}")

    done = input("Quit game? Y or N\n").lower()
    if done == "y":
        stop_game = True



# Exercise 1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    elif month_days[month] in month_days:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)






