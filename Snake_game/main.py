from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard


snake = Snake()
food = Food()
score = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My body game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen = Screen()
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            





screen.exitonclick()