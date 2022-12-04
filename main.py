from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard

from paddle import Paddle
from ball import Ball


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Turtle()
net.color("white")
net.hideturtle()
net.setposition(0,-300)
net.goto(0,300)

screen.listen()

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 310 or ball.distance(left_paddle) < 50 and ball.xcor() < -310:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()










screen.exitonclick()
