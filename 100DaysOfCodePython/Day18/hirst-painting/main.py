import colorgram
import turtle as t
import random

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

color_list = [(225, 159, 67), (61, 121, 170), (50, 96, 57), (238, 203, 71), (182, 64, 49), (179, 173, 36), (221, 172, 198), (182, 51, 56), (211, 87, 57), (46, 46, 95), (209, 163, 187), (133, 160, 186), (38, 39, 80), (37, 84, 45), (244, 199, 4), (149, 169, 152), (76, 130, 186), (195, 75, 82), (227, 175, 165), (31, 65, 39), (180, 188, 211), (111, 139, 113), (181, 198, 185), (75, 142, 172), (139, 38, 52), (175, 198, 204)]

# painting 10x10
# dots size 20
# distance between dots is 50
t.colormode(255)
screen = t.Screen()
bob = t.Turtle()

distance = 50
dot_size = 20
x_axis = 10
y_axis = 10

bob.penup()
bob.hideturtle()
bob.speed("fastest")

for y in range(y_axis):
    bob.teleport(-200, - 200 + (y * distance))
    for x in range(x_axis):
        bob.dot(dot_size, random.choice(color_list))
        bob.forward(distance)

screen.exitonclick()
