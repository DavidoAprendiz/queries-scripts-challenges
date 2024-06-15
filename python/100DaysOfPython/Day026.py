# Day026
# List Comprehension


def exercise1():
    alfabeto: dict = {"A": "alpha", "B": "bravo", "C": "charlie", "D": "delta", "E": "echo", "F": "foxtrot",
                      "G": "golf", "H": "hotel", "I": "india", "J": "juliett", "K": "kilo", "L": "lima", "M": "mike",
                      "N": "november", "O": "oscar", "P": "papa", "Q": "quebec", "R": "romeo", "S": "sierra",
                      "T": "tango", "U": "uniform", "V": "victor", "W": "whiskey", "X": "x-ray", "Y": "yankee",
                      "Z": "zulu"}

    nome_fonetico: list = []
    nome: str = input("Enter a word: ").upper()

    for letra in nome:
        if letra in alfabeto:
            nome_fonetico.append(alfabeto[letra])
    print(nome_fonetico)


def exercise1_with_comprehensions():
    alfabeto: dict = {"A": "alpha", "B": "bravo", "C": "charlie", "D": "delta", "E": "echo", "F": "foxtrot",
                      "G": "golf", "H": "hotel", "I": "india", "J": "juliett", "K": "kilo", "L": "lima", "M": "mike",
                      "N": "november", "O": "oscar", "P": "papa", "Q": "quebec", "R": "romeo", "S": "sierra",
                      "T": "tango", "U": "uniform", "V": "victor", "W": "whiskey", "X": "x-ray", "Y": "yankee",
                      "Z": "zulu"}

    nome: str = input("Enter a word: ").upper()

    nome_fonetico: list = [alfabeto[letra] for letra in nome if letra in alfabeto]
    print(nome_fonetico)


def exercise2():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers: list = [n * n for n in numbers]
    print(squared_numbers)


def exercise3():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result: list = [n for n in numbers if n % 2 == 0]
    print(result)


def exercise4():
    with open("Day026_File1.txt") as file1_full:
        file1 = file1_full.readlines()
    with open("Day026_File2.txt") as file2_full:
        file2 = file2_full.readlines()

    result: list = [int(n) for n in file1 if n in file2]
    print(f"{result}")


def exercise5():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    new_dict: dict = {line: len(line) for line in sentence.split()}
    print(new_dict)


def exercise6():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    new_dict: dict = {x: (y * 9 / 5) + 32 for x, y in weather_c.items()}
    print(new_dict)


exercise1()
exercise1_with_comprehensions()
exercise2()
exercise3()
exercise4()
exercise5()
exercise6()

