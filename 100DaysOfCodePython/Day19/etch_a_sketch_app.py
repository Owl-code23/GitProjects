from turtle import Turtle, Screen

# W - Forwards
# S - Backwards
# A - Counter-Clockwise
# D - Clockwise
# C - Clear drawing (back at the center)

def move_forwards():
    bob.forward(10)

def move_backwards():
    bob.backward(10)

def turn_counter_clockwise():
    bob.left(10)

def turn_clockwise():
    bob.right(10)

def clear_drawing():
    # bob.reset()
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()

bob = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()
