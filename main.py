from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
index_value = 0
y_coordinate = -160
all_turtles = []
for _ in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index_value])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    all_turtles.append(new_turtle)
    y_coordinate += 40
    index_value += 1


user_guess = screen.textinput(title="Turtle Race", prompt="Choose your turtle")
if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you're won. The winning color is {winning_color}")
            else:
                print(f"you've lost. The winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
