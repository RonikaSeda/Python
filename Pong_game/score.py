from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        

    def display_score(self):
        self.goto(x=0, y=200)   
        self.write("SCORE", align= "center", font = ("Courier", 30, "normal"))
        

class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.l_score_position = (-100, 200)
        self.r_score = 0
        self.r_score_position = (100, 200)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(self.l_score_position)
        self.write(self.l_score, align="center", font=("Courier", 30, "bold"))
        self.goto(self.r_score_position)
        self.write(self.r_score, align="center", font=("Courier", 30, "bold"))

    def add_point_left(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def add_point_right(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()