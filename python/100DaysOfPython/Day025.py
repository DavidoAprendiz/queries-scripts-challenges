# Day 25
# US State Game

import csv
import pandas as pd
from turtle import Turtle, Screen


def exercise1():
    with open("Day025_Data.csv") as file:
        dados: csv = csv.reader(file)
        temperaturas: list = []
        for i in dados:
            temperaturas.append(i[1])

        for i in range(1, len(temperaturas)):
            temperaturas[i] = int(temperaturas[i])

        print(dados)
        print(temperaturas)


def exercise2():
    dados = pd.read_csv("Day025_Data.csv")

    dados_dict = dados.to_dict()
    print(dados_dict)

    dados_list = dados["temp"].to_list()
    print(dados_list)

    avg_temps = sum(dados_list) / len(dados["temp"])
    print(avg_temps)

    print(dados["temp"].mean())
    print(dados["temp"].max())

    print(dados[dados["day"] == "Monday"])

    print(dados[dados["temp"] == dados["temp"].max()])

    segunda = dados[dados["day"] == "Monday"]
    print(segunda)


def exercise3():
    dados = pd.read_csv("Day025-2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    is_black = dados["Primary Fur Color"] == "Black"
    is_gray = dados["Primary Fur Color"] == "Gray"
    is_cinnamon = dados["Primary Fur Color"] == "Cinnamon"

    soma_cores_total: int = dados["Primary Fur Color"].count()
    soma_cores_black: int = dados[is_black]
    soma_cores_gray: int = dados[is_gray]
    soma_cores_cinnamon: int = dados[is_cinnamon]

    dados_actualizados = {"Primary Fur Color": ["Black", "Gray", "Cinnamon"],
                          "Count": [soma_cores_black['Primary Fur Color'].count(),
                                    soma_cores_gray['Primary Fur Color'].count(),
                                    soma_cores_cinnamon['Primary Fur Color'].count()]}

    dados_actualizados_pd = pd.DataFrame(data=dados_actualizados)

    # print(dados_actualizados_pd)
    dados_actualizados_pd.to_csv("Day025-squirrel_colors_exported.csv")


def main_exercise():
    screen = Screen()
    screen.setup(width=725, height=491)
    screen.bgpic("Day025-blank_states_img.gif")
    screen.title("Discovery the 50 US States, if you can...  :)")
    screen.tracer(0)

    data_csv = pd.read_csv("Day025-50_states.csv")
    data = pd.DataFrame(data_csv)

    num_states: int = data.state.count()
    user_points: int = 0
    user_input = screen.textinput(title=f"{user_points} of 50 discovered", prompt="Choose wisely:").title()

    class States:
        def __init__(self):
            pass

        def create_state(self, _user_input, x, y):
            new_state = Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.setposition(x, y)
            new_state.write(_user_input, align="center")
            screen.update()

    state = States()

    while num_states > 0:
        print(f"NumStates: {num_states}, UserPoints:  {user_points}")
        print(user_input)
        print(data[data.state == user_input])
        if (data.state[data.state == user_input]).any():
            num_states -= 1
            user_points += 1
            state.create_state(user_input, int(data.x[data.state == user_input]), int(data.y[data.state == user_input]))
        user_input = screen.textinput(title=f"{user_points} of 50 discovered", prompt="Choose wisely:").title()

    screen.exitonclick()


# exercise1()
# exercise2()
# exercise3()
main_exercise()
