from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_positions = [-100, -60, -20, 20, 60, 100]
finish_line = 225

# Create turtles and place them at starting positions
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Now run the race: move all turtles repeatedly until one wins
race_on = True
while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > finish_line:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations, the {user_bet} turtle won")
            else:
                print("Sorry, you loose")
            break

screen.exitonclick()