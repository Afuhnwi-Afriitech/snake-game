from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreCount = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.scoreCount}", align='center', font=('Arial', 22, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.scoreCount = self.scoreCount + 1
        self.clear()
        self.write(f"Score: {self.scoreCount}", align='center', font=('Arial', 22, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 25, 'normal'))
