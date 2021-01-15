import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

CARS = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car.pos()) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing of player
    if player.ycor() > 260:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()