from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard, Points
import time
score_board = ScoreBoard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
points = Points()
ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    points.update_scoreboard()
    score_board.display_score()
    ball.move()
# detect colision with a wall on the Y-line
    if ball.ycor() < -285 or ball.ycor() > 285:
        ball.bounce_y()
# detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
# when the paddle missed the ball
    if ball.xcor() > 390:
       points.add_point_left()
       screen.update()
       ball.reset_position()
       continue
    if ball.xcor() < -390:
        points.add_point_right()
        screen.update()
        ball.reset_position()
        continue
    if points.l_score == 10:
        points.win_message()
        game_is_on = False
        continue

    if points.r_score == 10:
        points.win_message()
        game_is_on = False
        continue


screen.exitonclick()