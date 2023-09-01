import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2  

class CarManager:
    def __init__(self):
        self.all_cars = []  # Initialize an empty list to store car instances.

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        STARTING_POSITION_Y = random.randint(-200, 200)
        new_car.goto(340, STARTING_POSITION_Y)
        self.all_cars.append(new_car)

    def move_car(self):
        global STARTING_MOVE_DISTANCE
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def next_level(self):
        self.clear()
       
    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        return STARTING_MOVE_DISTANCE
