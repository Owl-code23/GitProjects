from turtle import Turtle, Screen
import turtle
import random
# import turtle
# fromt turtle * / (not good)
# import turtle as t / alias name

bob_turtle = Turtle()
screen = Screen()
turtle.colormode(255)
# bob_turtle.shape("turtle")
# bob_turtle.color("red")

# Challenge 1

# for _ in range(4):
#     bob_turtle.forward(100)
#     bob_turtle.right(90)


# Challenge 2

# for _ in range(20):
#     bob_turtle.forward(10)
#     bob_turtle.penup()
#     bob_turtle.forward(10)
#     bob_turtle.pendown()


# Challenge 3
# side length 100
# random color
# triangle - decagon

# colours = ["CornflowerBlue", 
#            "DarkOrchid", 
#            "IndianRed", 
#            "DeepSkyBlue", 
#            "LightSeaGreen", 
#            "wheat", 
#            "SlateGray", 
#            "SeaGreen"]

# full_circle = 360
# for side in range(3, 11):
#     bob_turtle.color(random.choice(colours))
#     for _ in range(side):
#         bob_turtle.forward(100)
#         bob_turtle.right(full_circle / side)


# Challenge 4
# increase thickness
# increase speed
# random walk

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# bob_turtle.pensize(10)
# bob_turtle.speed("fastest")

# while True:
#     bob_turtle.color(random_color())
#     direction = random.randint(0, 3)
#     bob_turtle.setheading(90 * direction)
#     bob_turtle.forward(30)


# Challenge 5
# draw circles with radius 100
# random colors

# bob_turtle.speed("fastest")

# size_of_gab = 1

# for _ in range(360 // size_of_gab):
#     bob_turtle.color(random_color())
#     bob_turtle.circle(100)
#     bob_turtle.right(size_of_gab)


# Documentation examples
# screen.clearscreen()
# bob_turtle.home()

# bob_turtle.color('red')
# bob_turtle.fillcolor('yellow')
# bob_turtle.begin_fill()

# while True:
#     bob_turtle.forward(200)
#     bob_turtle.left(170)
#     if abs(bob_turtle.pos()) < 1:
#         break
# bob_turtle.end_fill()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         bob_turtle.color(c)
#         bob_turtle.forward(steps)
#         bob_turtle.right(30)

screen.exitonclick()
