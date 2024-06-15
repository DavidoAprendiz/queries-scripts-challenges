from turtle import Turtle
from random import randint

SCREEN_HEIGHT: int = 600
STARTING_POSITION = (0, -((SCREEN_HEIGHT / 2) - 20))
MOVE_DISTANCE = 10
FINISH_LINE_Y = (SCREEN_HEIGHT / 2) - 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)


####################
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_new_cars(self):
        if randint(1, 7) == 1:
            new = Turtle()
            new.penup()
            new.shape("square")
            new.color(COLORS[randint(0, len(COLORS) - 1)])
            new.shapesize(stretch_wid=1, stretch_len=1)
            new.setposition(380, randint(-360, 360))
            new.setheading(180)
            self.cars.append(new)

    def move_car(self):
        for i in self.cars:
            i.forward(MOVE_INCREMENT)


####################
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.points = 0

    def board(self):
        self.clear()
        self.setposition(0, 260)
        self.write(f"Points: {self.points}", True, align="center", font=FONT)

    def add_one(self):
        self.points += 1

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"{self.points} points...\nGAME OVER!!!", True, align="center", font=FONT)
