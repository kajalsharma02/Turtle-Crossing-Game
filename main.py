import time
import random
from turtle import Screen
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(p.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    p.back()
    car.create_car()
    car.move_car()
   
    for c in car.all_car:
        if c.distance(p)<20:
            # c.goto(280,random.randint(-200,200))
            game_is_on = False
            score.game_over()
            print("Game Over")

    if p.ycor()>260:
        # game_is_on = False
        car.increase_speed()
        p.setposition(0,-280)
        score.level_up()
        print("Congratulatios")

screen.exitonclick()