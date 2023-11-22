from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-250,250)
        self.write(f"Level : {self.level}", align="Left", font=FONT)
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.level +=1
        self.write(f"Level : {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(-80,0)
        self.color("Red")
        self.write("Game Over", align="Centre", font=FONT)