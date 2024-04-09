from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
