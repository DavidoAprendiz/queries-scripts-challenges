from time import sleep
from turtle import Screen
from Day023_Classes import Player, CarManager, Scoreboard, STARTING_POSITION

SCREEN_BG: str = "gray"
SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
SLEEP_SEC: float = 0.1
is_game_on: bool = True

screen: Screen = Screen()
screen.bgcolor(SCREEN_BG)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

player: Player = Player()
cars = CarManager()
points = Scoreboard()

screen.onkey(screen.bye, "Escape")
screen.onkeypress(player.move_up, "Up")

while is_game_on:
    sleep(SLEEP_SEC)
    screen.update()
    points.board()

    cars.create_new_cars()
    cars.move_car()

    if player.ycor() > 281:
        player.setposition(STARTING_POSITION)
        SLEEP_SEC -= 0.01
        points.add_one()

    for car in cars.cars:
        if car.distance(player) < 20:
            points.game_over()
            is_game_on = False
            break

screen.exitonclick()
