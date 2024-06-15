# Day 18
#


from random import randint
from turtle import Turtle, Screen

nero_nyx: Turtle = Turtle()
screen: Screen = Screen()
screen.colormode(255)


def exercise1():
    nero_nyx.reset()
    nero_nyx.shape("turtle")
    nero_nyx.shapesize(.25, .25, .25)
    nero_nyx.speed(0)

    # Moving
    for i in range(4):
        nero_nyx.forward(100)
        nero_nyx.right(90)


def exercise2():
    nero_nyx.reset()
    forward: int = 10
    nero_nyx.shape("circle")
    nero_nyx.shapesize(.25, .25, .25)
    nero_nyx.speed(0)

    for _ in range(10):
        nero_nyx.pendown()
        nero_nyx.forward(forward)
        nero_nyx.penup()
        nero_nyx.forward(forward)


def exercise3():
    nero_nyx.reset()
    forward: int = 50
    area: int = 360
    sides: int = 3
    turn: float
    nero_nyx.speed(0)
    nero_nyx.shape("turtle")
    nero_nyx.shapesize(1, 1, 1)

    while sides < 20:
        turn = area / sides
        nero_nyx.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        for _ in range(sides):
            nero_nyx.forward(forward)
            nero_nyx.right(turn)
        sides += 1


def exercise4():
    nero_nyx.reset()
    forward: int = 25
    rotate: int = 90
    n_turns: int = randint(1, 100)
    nero_nyx.speed(0)
    nero_nyx.shape("turtle")
    nero_nyx.shapesize(1.5, 1.5, 1.5)
    nero_nyx.pensize(7)

    # Moving
    while n_turns > 0:
        turn: int = randint(0, 1)
        if turn:
            nero_nyx.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            nero_nyx.forward(forward)
            nero_nyx.left(rotate)
        else:
            nero_nyx.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            nero_nyx.forward(forward)
            nero_nyx.right(rotate)

        n_turns -= 1


def exercise5():
    nero_nyx.reset()
    raio: int = 100
    nero_nyx.speed(0)

    for _ in range(0, 100):
        nero_nyx.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        nero_nyx.circle(raio)
        nero_nyx.right(5)


def main_challenge():
    nero_nyx.reset()
    columns: int = 10
    rows: int = 10
    nero_nyx.speed(0)
    nero_nyx.shape("turtle")
    nero_nyx.shapesize(0.5)
    nero_nyx.pensize(10)
    nero_nyx.setheading(0)
    screen.screensize(bg="gray")

    for _ in range(columns):
        for _ in range(rows):
            nero_nyx.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            nero_nyx.pendown()
            nero_nyx.circle(1)
            nero_nyx.penup()
            nero_nyx.forward(20)

        x: float = nero_nyx.pos()[0]
        y: float = nero_nyx.pos()[1]

        nero_nyx.setposition((x, y + 20))
        if nero_nyx.heading() == 0:
            nero_nyx.setheading(180)
        else:
            nero_nyx.setheading(0)


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
main_challenge()

screen.exitonclick()
