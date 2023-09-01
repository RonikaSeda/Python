from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()

    def count_level(self):
        global LEVEL
        LEVEL += 1
        return LEVEL
    
    def display_level(self):
        global LEVEL
        self.goto(x = -240, y = 240)
        self.write(f"Level: {LEVEL}", font=FONT)
        
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
