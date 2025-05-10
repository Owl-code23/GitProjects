from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # Collision with top and bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() - 340):
        ball.hit()

    # Collision with right and left wall
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()