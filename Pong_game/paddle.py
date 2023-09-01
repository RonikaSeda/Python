from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.up()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.speed("fastest")
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() -30
        self.goto(self.xcor(),new_y)

    #roman si hraje
    def make_it_harder(self):
        size = self.turtlesize()
        self.turtlesize(size[0]*0.95,size[1],size[2])
