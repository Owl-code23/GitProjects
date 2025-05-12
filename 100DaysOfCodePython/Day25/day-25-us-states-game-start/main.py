import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()

correct_guesses = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

game_is_on = True

while True:

    if answer_state in states_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data["state"] == answer_state]
        x = state_data["x"].item()
        y = state_data["y"].item()
        state.goto((x, y))
        state.write(answer_state)

    if answer_state == "Exit":
        break

    if len(correct_guesses) == len(states_list):
        game_is_on = False
    else:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

# states to learn.csv
for state in correct_guesses:
    if state in states_list:
        states_list.remove(state)

new_data = pd.DataFrame(states_list)
new_data.to_csv("states_to_learn.csv")