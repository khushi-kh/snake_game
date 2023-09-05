from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Times New Roman', 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.user_score()

    def user_score(self):
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.user_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E  O V E R", True, align=ALIGNMENT, font=FONT)
