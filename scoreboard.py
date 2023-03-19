from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 12, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.setposition(x=0, y=280)
        self.count = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.count}", False, align=ALIGN, font=FONT)

    def add_score(self):
        self.clear()
        self.count += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)
