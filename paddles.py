from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 8)
        self.penup()
        self.setheading(90)
        self.goto(pos)

    def up(self):
        y_cor = self.ycor() + 25
        if y_cor < 440:
            self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 25
        if y_cor > -440:
            self.goto(self.xcor(), y_cor)

    def paddle_reset(self):
        self.goto(self.xcor(), 0)
