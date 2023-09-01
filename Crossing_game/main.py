import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

cars = CarManager()
scoreboard = Scoreboard()
screen = Screen()
list_of_cars = []

screen.setup(width=600, height=600)
screen.title("Cross game")
screen.tracer(0)

turtle = Player()
index = 0
game_is_on = True
while game_is_on:
    random_number = random.randint(1, 6)
    scoreboard.display_level()
    time.sleep(0.1)
    screen.update()
    if random_number == 1:
        cars.create_car()
    cars.move_car()
    screen.listen()
    screen.onkey(turtle.move, "Up")

    # when successfully passed the screen
    next_level = turtle.finish_line()
    if next_level == True:
        scoreboard.clear()
        scoreboard.count_level()
        scoreboard.display_level()
        cars.increase_speed()

    # detect collision with car
    for some_car in cars.all_cars:
        if turtle.distance(some_car) < 15:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()