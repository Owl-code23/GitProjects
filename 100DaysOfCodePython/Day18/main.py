from turtle import Turtle, Screen

bob_turtle = Turtle()
# bob_turtle.shape("turtle")
# bob_turtle.color("red")

for _ in range(4):
    bob_turtle.forward(100)
    bob_turtle.right(90)

screen = Screen()
screen.exitonclick()
