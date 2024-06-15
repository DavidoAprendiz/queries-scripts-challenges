from turtle import Turtle


class Player(Turtle):
    def __init__(self, position: ()):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor() + 30
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 30
        self.goto(self.xcor(), y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(1)
        self.penup()
        self.goto(0, 0)
        self.speed(1)
        self.x = 10
        self.y = 10

    def move_ball(self):
        self.setposition(self.pos()[0] + self.x, self.pos()[1] + self.y)

    def bounce(self, player_a, player_b):
        if self.distance(player_a) < 50 and self.xcor() > 320 or self.distance(player_a) < 50 and self.xcor() < -325 \
                or self.distance(player_b) < 50 and self.xcor() > 320 or self.distance(player_b) < 50 and \
                self.xcor() < -325:
            self.x *= -1
        if self.ycor() > 280 or self.ycor() < -280:
            self.y *= -1


class Points(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.points_a = 0
        self.points_b = 0

    def board(self):
        self.clear()
        self.setposition(0, 280)
        self.write(f"Player A: {self.points_a} , Player B: {self.points_b}", True, align="center", font=("Arial", 14,
                                                                                                         "normal"))

    def add_one(self, ball):
        if ball.xcor() > 400:
            self.points_a += 1
            ball.setposition(0, 0)
        elif ball.xcor() < -400:
            self.points_b += 1
            ball.setposition(0, 0)
