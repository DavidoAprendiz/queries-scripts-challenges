from turtle import Turtle
import random

START_POSITIONS: list[tuple] = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 10
SPEED = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snake:

    def __init__(self):
        self.snake: list = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in START_POSITIONS:
            new = Turtle(shape="square")
            new.color("white")
            new.penup()
            new.setposition(i)
            new.speed(SPEED)
            self.snake.append(new)

    def move_body(self):
        for num in range(len(self.snake) - 1, 0, -1):
            x = self.snake[num - 1].xcor()
            y = self.snake[num - 1].ycor()
            self.snake[num].setposition(x, y)
        self.head.forward(STEPS)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_new(self):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.setposition(self.snake[-1].pos())
        new.speed(SPEED)
        self.snake.append(new)

    def reset_snake(self):
        for i in self.snake:
            i.setposition(1000, 1000)
        self.snake.clear()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed(0)
        x = random.randint(-int((SCREEN_WIDTH - 30) / 2), int((SCREEN_WIDTH - 30) / 2))
        y = random.randint(-int((SCREEN_HEIGHT - 30) / 2), int((SCREEN_HEIGHT - 30) / 2))
        self.setposition((x, y))

    def new_location(self):
        x = random.randint(-int((SCREEN_WIDTH - 30) / 2), int((SCREEN_WIDTH - 30) / 2))
        y = random.randint(-int((SCREEN_HEIGHT - 30) / 2), int((SCREEN_HEIGHT - 30) / 2))
        self.setposition((x, y))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = Turtle()
        with open("Day020_Scores.txt") as file:
            self.high_score = int(file.read())

        self.points = 0
        self.hideturtle()

    def plus_one(self):
        self.points += 1
        self.update_points()

    def update_points(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.write(f"Points: {self.points}     HighScore: {self.high_score}", True, align="center",
                   font=("Arial", 14, "normal"))
        self.hideturtle()

    def reset_points(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update_points()
        self.highscore()

    def highscore(self):
        with open("Day020_Scores.txt", "w") as file:
            file.write(str(self.high_score))
