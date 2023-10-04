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
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.points} High score: {self.high_score}", align=self.ALIGN, font=(self.FONT, self.FONT_SIZE, self.FONT_STYLE))

    def count_score(self):
        self.points += 1
        self.update_score()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode = "w") as data:
                data.write(str(self.high_score))
                data.close()
        self.points = 0
        self.update_score()
        


        
            