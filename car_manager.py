from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        """
        Moves the car from right to left by STARTING_MOVE_DISTANCE and return true if car is out of screen
        :return: True
        """
        for car in self.all_cars:
            car.backward(self.car_speed)
            # if car.xcor() < -320:
            #     return True

    def increase_speed(self):
        """
        Increases the speed of car everytime it is called
        :return:
        """
        self.car_speed += MOVE_INCREMENT
        self.car_move()










