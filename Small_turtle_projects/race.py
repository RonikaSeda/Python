from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["orange", "green", "yellow", "blue", "red"]
y = -130
index = 0
turtles = []
for symbol in range(5):
    symbol = Turtle(shape="turtle")
    symbol.up()
    symbol.color(colors[0+index])
    symbol.goto(x = -230, y = y)
    turtles.append(symbol)
    index += 1 
    y += 65

def move():
    symbol.forward(random.randint(0,10))
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for symbol in turtles:
        if symbol.xcor() > 230:
            winner_turtle = symbol.pencolor()
            if winner_turtle == user_bet:
                print(f"You won! The {winner_turtle} turtle won!")
            else:
                print(f"You loose! The {winner_turtle} turtle won!")
            is_race_on = False
        else:
            move()

        

screen.exitonclick()