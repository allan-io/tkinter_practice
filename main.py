import turtle
from turtle import Screen
import pandas

CORRECT_GUESSES = 0
GUESSED_STATES = []
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess State", prompt="What's another States name:").title()
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

game_is_on = True
while game_is_on:
    if answer_state in state_list and answer_state not in GUESSED_STATES:
        print(data.row(answer_state))
        CORRECT_GUESSES += 1
        GUESSED_STATES.append(answer_state)
        answer_state = screen.textinput(title=f"{CORRECT_GUESSES}/50 States Correct", prompt="What's another States name:").title()
    else:
        answer_state = screen.textinput(title=f"{CORRECT_GUESSES}/50 States Correct", prompt="What's another States name:").title()
screen.exitonclick()