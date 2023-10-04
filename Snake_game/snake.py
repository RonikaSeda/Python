from turtle import Turtle
STARTIN_POSSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.game_is_on = False

    def start_game(self):
        self.game_is_on = True

    def create_snake(self):
        for possition in STARTIN_POSSITIONS:
            self.add_segment(possition=possition)

    def move_forward(self):   
        for segment_number in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[segment_number-1].xcor()
            new_y = self.snake_body[segment_number-1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, possition):
        body = Turtle()
        body.up()
        body.shape("square")
        body.color("white")
        body.setposition(possition)
        self.snake_body.append(body)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]