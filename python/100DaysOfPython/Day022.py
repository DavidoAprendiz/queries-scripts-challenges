# Day 22
# Pong Game

from turtle import Screen
from Day022_Classes import Player, Ball, Points
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

player_a = Player((-350, 0))
player_b = Player((350, 0))
ball = Ball()
points = Points()

screen.onkey(player_a.move_up, "a")
screen.onkey(player_a.move_down, "z")
screen.onkey(player_b.move_up, "Up")
screen.onkey(player_b.move_down, "Down")
screen.onkey(screen.bye, "Escape")

is_game_on = True

while is_game_on:
    sleep(0.1)
    screen.update()

    points.board()

    ball.move_ball()
    ball.bounce(player_a, player_b)

    points.add_one(ball)

screen.exitonclick()
