import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # spawn random cars
    random_num = random.randint(0,4)
    if random_num == 1:
        carManager.spawn_car()
    carManager.move()

    # collision with top edge of screen
    if player.hit_finish_line():
        carManager.increase_speed()
        scoreboard.increase_level()

    # collision with car
    for car in carManager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
