import colorgram
from turtle import Turtle, Screen, colormode
import random

timtom = Turtle()
screen = Screen()
colormode(255)
timtom.speed("fastest")
timtom.hideturtle()

rgb_colors = []
colors = colorgram.extract("48_001.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    if r == 245 and g == 243 and b == 238:
        continue
    else:
        rgb_colors.append(new_color)

print(rgb_colors)


def starting_point(angle, move):
    timtom.up()
    timtom.left(angle)
    timtom.forward(move)
    timtom.left(360-angle)

def new_row():
    timtom.left(90)
    timtom.forward(50)
    timtom.right(90)
    timtom.backward(500)

def draw_dot():
    timtom.dot(20, random.choice(rgb_colors))
    timtom.forward(50)

starting_point(225, 300)

number_of_dots = 100
for dot in range(1, number_of_dots+1):
    draw_dot()
    if dot % 10 == 0:
        new_row()




screen.exitonclick()
