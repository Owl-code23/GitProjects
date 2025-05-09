from turtle import Turtle, Screen

screen = Screen()
bob = Turtle('turtle')

def move_forwards():
    bob.forward(10)

screen.listen()
screen.onkey(fun=move_forwards, key="space")

screen.exitonclick()