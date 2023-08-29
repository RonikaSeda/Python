from turtle import Turtle, Screen

screen = Screen()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ALIGN = "center"
        self.FONT = "Arial"
        self.FONT_SIZE = 20
        self.FONT_STYLE = "normal"
        self.points = 0
        self.hideturtle()
        self.up()
        self.goto([0, 270])
        self.color(("white"))
        self.update_score
        
    def update_score(self):
        self.write(f"Score: {self.points}", align=self.ALIGN, font=(self.FONT, self.FONT_SIZE, self.FONT_STYLE))

    def count_score(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.FONT_SIZE = 40
        self.FONT_STYLE = "bold"
        self.goto(0, 0)
        self.write("Game over!", align=self.ALIGN, font= (self.FONT, self.FONT_SIZE, self.FONT_STYLE))
        