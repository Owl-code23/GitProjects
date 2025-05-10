from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.setheading(180)
        rand_y = random.randint(-250, 250)
        new_car.goto(300, rand_y)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            if car.xcor() < - 350:
                # delete car object if finish crossing
                pass
            else:
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

