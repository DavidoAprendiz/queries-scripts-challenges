# Day 19
# Turtle Racing Game


from random import randint
from turtle import Turtle, Screen

nero_nyx: Turtle = Turtle()
screen: Screen = Screen()
screen.listen()
screen.colormode(255)


def exercise1():
    nero_nyx.reset()
    screen.reset()
    forward: int = 10
    rotate: int = 90

    def move_forward():
        nero_nyx.forward(forward)

    def move_backward():
        nero_nyx.left(rotate * 2)
        # nero_nyx.right(rotate*2)

    def move_lef():
        nero_nyx.left(rotate)

    def move_right():
        nero_nyx.right(rotate)

    screen.onkey(key="Up", fun=move_forward)
    screen.onkey(key="Down", fun=move_backward)
    screen.onkey(key="Left", fun=move_lef)
    screen.onkey(key="Right", fun=move_right)

    screen.onkey(key="c", fun=screen.reset)
    screen.onkey(key="q", fun=screen.bye)


def exercise2():
    nero_nyx.reset()
    screen.reset()
    screen.setup(900, 500)

    t2 = Turtle()
    t3 = Turtle()
    t4 = Turtle()
    t5 = Turtle()

    entidades = [nero_nyx, t2, t3, t4, t5]
    x: int = -350
    y: int = 200

    for i in entidades:
        i.penup()
        i.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        i.speed(0)

    nero_nyx.shape("turtle")
    t2.shape("classic")
    t3.shape("circle")
    t4.shape("square")
    t5.shape("triangle")

    nero_nyx.setposition((x, y))
    t2.setposition((x, y - 100))
    t3.setposition((x, y - 200))
    t4.setposition((x, y - 300))
    t5.setposition((x, y - 400))

    def mover_todos(entidades: [Turtle]):
        for i in entidades:
            steps = randint(1, 10)
            i.forward(steps)

    def parede(entidades: [Turtle]):
        for i in entidades:
            if i.pos()[0] > 400:
                return i.shape()

    user_choice = screen.textinput("Shapes Battle!", "Which one will win?")

    for i in entidades:
        i.pendown()

    for _ in range(150):
        mover_todos(entidades)
        a = parede(entidades)
        if a:
            if a == user_choice:
                print(f"YOU WIN!!! {user_choice}\nThe winner was: {parede(entidades)}!!!")
                # screen.bye()
            else:
                print(f"YOU LOSE!!! {user_choice}\nThe winner was: {parede(entidades)}!!!")
                # screen.bye()

            break


exercise1()
exercise2()

screen.exitonclick()
