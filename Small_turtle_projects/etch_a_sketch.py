from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_counterclockwise():
    tim.right(10)
def turn_clockwise():
    tim.left(10)
def clear():
    tim.reset()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
