import turtle
import pandas

# Adding the image to the screen and setting up the screen
image = "game.gif"
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Missing body part game")
screen.addshape(image)
turtle.shape(image)

# Importing the data from bodu part of the csv file with the panda module

data = pandas.read_csv("body Part.csv")
body_list = data.body.to_list()
guessed_body_part = []

while len(guessed_body_part) < len(body_list):
    user_answer = turtle.textinput(
        title=f"{len(guessed_body_part)}/12 guessed ", prompt="What is your guess").title()

    if user_answer == "Exit":
        break

    if user_answer in body_list:
        guessed_body_part.append(user_answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        part_data = data[data.body == user_answer]
        t.goto(int(part_data.x), int(part_data.y))
        t.write(user_answer)


screen.exitonclick()
