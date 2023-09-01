from turtle import Turtle, Screen
import random

timmi = Turtle()
screen = Screen()
timmi.shape("turtle")
timmi.color("dark blue", "sky blue")
color = ["pale green", "royal blue", "medium spring green", "sandy brown", "rosy brown"]
def draw_shape(num_of_sides):
    angle = 360/num_of_sides    
    for _ in range (num_of_sides):
        print(num_of_sides)
        timmi.forward(50)
        timmi.right(angle)
        


for shape in range(3,11):
    draw_shape(shape)
    timmi.color(random.choice(color))
