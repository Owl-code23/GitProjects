from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 0.03
        self.y_move = 0.03
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move += 0.01
        self.y_move += 0.01
        self.x_move *= -1

    def refresh(self):
        self.home()
        self.hit()
        self.x_move = 0.03
        self.y_move = 0.03