# Day 030
# Catch the exception and make sure the code runs without crashing.
import json


def exercise1():
    fruits = ["Apple", "Pear", "Orange"]

    # nº1 - without 'try:' but with 'if' to create the conditional
    def make_pie(index):
        max_index = len(fruits) - 1
        if index <= max_index:
            fruit = fruits[index]
            print(fruit + " pie")
        else:
            print(f"Please insert a range between '0' and '{max_index}'")

    make_pie(3)
    # nº2 - with try
    # try:
    #     def make_pie(index):
    #         fruit = fruits[index]
    #         print(fruit + " pie")
    #     make_pie(4)
    # except IndexError as index_message:
    #     print(f"Please insert a range between '0' and '{len(fruits)}'.\nError message: '{index_message}'.")


def exercise2():
    facebook_posts = [
        {'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Likes': 33, 'Comments': 8, 'Shares': 3},
        {'Comments': 4, 'Shares': 2},
        {'Comments': 1, 'Shares': 1},
        {'Likes': 19, 'Comments': 3}
    ]

    total_likes = 0

    for post in facebook_posts:
        if "Likes" in post.keys():
            total_likes += post['Likes']

    print(total_likes)


def exercise3():
    filename = "Day030.json"
    new = {
        "website": {
            "user": "abcd",
            "pass": "1234",
        }}
    with open(filename, "w") as file:
        json.dump(new, file, indent=4)


def exercise4():
    filename = "Day030.json"
    with open(filename) as file:
        data = json.load(file)
        print(data)


def exercise5():
    filename = "Day030.json"
    new = {
        "website3": {
            "user": "abc",
            "pass": "abc123"
        }}
    try:
        with open(filename) as file:
            dados = json.load(file)
            dados.update(new)
    except FileNotFoundError:
        with open(filename, "w") as file:
            json.dump(new, file, indent=4)
    else:
        with open(filename, "w") as file:
            json.dump(dados, file, indent=4)


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
