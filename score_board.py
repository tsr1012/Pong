from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(80, 310)
        self.write(self.r_score, align="center", font=("unispace", 120, "normal"))
        self.goto(-80, 310)
        self.write(self.l_score, align="center", font=("unispace", 120, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def winner_check(self, r):
        if self.l_score == r or self.r_score == r:
            return True
        return False
