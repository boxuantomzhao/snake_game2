from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial",14,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0,280)

    def add_score(self):
        self.score +=1

    def show_score(self):
        self.clear() #delete previous score
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(arg=f"Game Over :(", move=False, align=ALIGNMENT, font=FONT)