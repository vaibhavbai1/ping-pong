from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

flag = True
while flag:
    time.sleep(ball.pase)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce2()

    # detect when paddle misses
    # right side
    if ball.xcor() > 370:
        ball.resat()
        scoreboard.l_point()
    # left side
    if ball.xcor() < -370:
        ball.resat()
        scoreboard.r_point()





screen.exitonclick()
