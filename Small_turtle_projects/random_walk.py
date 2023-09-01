from turtle import Turtle, Screen, colormode
import random
colormode(255)

screen = Screen()
tim = Turtle()

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
for _ in range (0, 100):
    tim.color(random_colour())
    tim.speed(20)
    tim.width(5)
    tim.forward(random.randint(20, 50))
    tim.setheading(random.choice(directions))

screen.exitonclick()