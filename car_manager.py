from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # super().__init__()
        self.all_car=[]
        self.level_up = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            x=random.randint(-200,200)
            new_car.setposition(280,x)
            self.all_car.append(new_car)

    def move_car(self):
        for i in self.all_car:
            i.backward(self.level_up)

    def increase_speed(self):
        self.level_up += 5

    
    