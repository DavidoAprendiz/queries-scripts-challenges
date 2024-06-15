# Day 20
# Snake Game


from turtle import Screen
from time import sleep
from Day020_Classes import Snake, Food, Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("SNAKE!!!")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
points = Scoreboard()


def keyboard():
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)
    screen.onkey(key="q", fun=screen.bye)
    screen.onkey(key="r", fun=snake.reset_snake)


def game_walls(_snake):
    for i in _snake:
        if i.pos()[0] >= (SCREEN_WIDTH / 2) or i.pos()[0] <= -(SCREEN_WIDTH / 2) \
                or i.pos()[1] >= (SCREEN_HEIGHT / 2) or i.pos()[1] <= -(SCREEN_HEIGHT / 2):
            return i.pos()
        return False


keyboard()
points.update_points()
is_game_on = True
while is_game_on:

    if game_walls(snake.snake):
        # is_game_on = False
        # print(f"GAME OVER!!! Total points: {points.points}. You hit the wall.")
        # break
        snake.reset_snake()
        points.reset_points()
    for n in snake.snake[1:]:
        if snake.head.distance(n) < 1:
            # is_game_on = False
            # print(f"GAME OVER!!! Total points: {points.points}. You hit yourself.")
            # break
            snake.reset_snake()
            points.reset_points()

    if snake.head.distance(food) < 14:
        food.new_location()
        snake.add_new()
        points.plus_one()
        points.update_points()

    screen.update()
    sleep(0.05)
    snake.move_body()

screen.exitonclick()
