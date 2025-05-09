from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turltes = []

is_race_on = False

for x in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 40 * x)
    all_turltes.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turltes:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! the {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()