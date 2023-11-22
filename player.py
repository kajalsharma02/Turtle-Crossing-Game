from turtle import *


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.left(90)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
        # print(self.ycor())


    def back(self):
        if(self.ycor()>FINISH_LINE_Y):
            self.setposition(STARTING_POSITION)

        
