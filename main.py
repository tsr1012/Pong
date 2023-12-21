import time as t
import _tkinter
from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from score_board import ScoreBoard


def screen_divider():
    """Divides screen in two parts i.e. P1 and P2"""
    y_cor = 480
    for _ in range(20):
        divider = Turtle("square")
        divider.color("gray60")
        divider.penup()
        divider.shapesize(stretch_len=.5)
        divider.goto(0, y_cor)
        y_cor -= 50

        p1_p2 = Turtle()
        p1_p2.penup()
        p1_p2.hideturtle()
        p1_p2.goto(0, -345)
        p1_p2.color("gray10")
        p1_p2.write("P1 P2", align="center", font=("unispace", 400, "normal"))


def animation_delay(seconds):
    """Duration of animation in seconds."""
    scr.update()
    t.sleep(seconds)


def paddle_animation(paddle, bounce_amount, original_pos):
    """Paddle bounce upon contact with the ball."""
    paddle.goto(bounce_amount, paddle.ycor())
    paddle.color("darkgreen")
    animation_delay(.05)
    paddle.goto(original_pos, paddle.ycor())
    paddle.color("white")


def screen_reset():
    """Resetting the screen after scoring points."""
    ball.reset_position()
    r_paddle.paddle_reset()
    l_paddle.paddle_reset()
    for _ in range(3):
        scr.bgcolor("grey")
        animation_delay(.08)
        scr.bgcolor("black")
        animation_delay(.08)


def winner_declare(player):
    animation_delay(.5)
    global game_over
    game_over = True
    scr.clear()
    scr.bgcolor("black")
    end_scr = Turtle()
    end_scr.penup()
    end_scr.hideturtle()
    end_scr.color("white")
    end_scr.goto(0, 0)
    end_scr.write(player, align="center", font=("unispace", 250, "normal"))
    end_scr.goto(0, -350)
    end_scr.write("WON", align="center", font=("unispace", 250, "normal"))


def close_game():
    """Setup to close the program."""
    global game_over
    game_over = True
    t.sleep(.5)
    exit()


scr = Screen()
root = Screen()._root
scr.setup(1900, 990, 0, 0)
scr.bgcolor("black")
scr.title("Pong")
root.iconbitmap("icon.ico")

# Take input for number of rounds to play
try:
    rounds = int(scr.textinput(title="Pong", prompt="How many rounds you want to play?"))
# If none given then default to 1 round
except (TypeError, ValueError):
    rounds = 1

scr.tracer(0)
screen_divider()
score = ScoreBoard()

r_paddle = Paddle((920, 0))
l_paddle = Paddle((-930, 0))

ball = Ball()

# Key input
scr.listen()
scr.onkeypress(l_paddle.up, "w")
scr.onkeypress(l_paddle.down, "s")
scr.onkeypress(r_paddle.up, "Up")
scr.onkeypress(r_paddle.down, "Down")
scr.onkeypress(close_game, "Escape")


flag = 0
game_over = False
while not game_over and rounds:
    t.sleep(ball.ball_speed)
    scr.update()
    # If game terminates unexpectedly then close the program
    try:
        ball.move()
    except _tkinter.TclError:
        close_game()

    # Bugfix
    if flag > 0:
        flag -= 1

    # Detect collision with wall
    if ball.ycor() >= 475 or ball.ycor() <= -475:
        ball.bounce_y()

    # Detect collision with R paddle
    if ball.distance(r_paddle) < 85 and ball.xcor() > 895 and flag == 0:
        paddle_animation(r_paddle, 930, 920)
        ball.bounce_x()
        flag = 10

    # Detect collision with L paddle
    elif ball.distance(l_paddle) < 85 and ball.xcor() < -900 and flag == 0:
        paddle_animation(l_paddle, -940, -930)
        ball.bounce_x()
        flag = 10

    # Detect R paddle miss
    elif ball.xcor() > 940:
        score.l_point()
        screen_reset()
        if score.winner_check(rounds):
            winner_declare("P1")

    # Detect L paddle miss
    elif ball.xcor() < -950:
        score.r_point()
        screen_reset()
        if score.winner_check(rounds):
            winner_declare("P2")

scr.exitonclick()
