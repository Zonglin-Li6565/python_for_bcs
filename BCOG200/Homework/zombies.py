import time
from math import sqrt
from random import randint
from turtle import Screen, Turtle
from typing import List

TOTAL = 10
SCREEN_SIZE = 900
NUM_TURNS = 50

screen = Screen()

screen.addshape('human-50-50.gif')
screen.addshape('zombie-50-50.gif')
screen.setup(SCREEN_SIZE, SCREEN_SIZE)


class Human(Turtle):
    def __init__(self) -> None:
        super().__init__('human-50-50.gif')
        self.penup()
        self.speed('fastest')
        self._speed = 50

    def run_away(self):
        half_range = SCREEN_SIZE // 2 - 25
        x = randint(-half_range, half_range)
        y = randint(-half_range, half_range)

        self.setheading(self.towards(x, y))
        self.forward(self._speed)


class Zombie(Turtle):
    def __init__(self):
        super().__init__('zombie-50-50.gif')
        self.penup()
        self.speed('fastest')
        self._speed = 75

    def _distance_to(self, other):
        diff_x = self.xcor() - other.xcor()
        diff_y = self.ycor() - other.ycor()
        return sqrt(diff_x ** 2 + diff_y ** 2)

    def attack(self, human):
        zombie = Zombie()
        zombie.setx(human.xcor())
        zombie.sety(human.ycor())
        return zombie

    def chase(self, humans: List[Human]):
        shortest_distance = 1e20
        killed_human = []
        new_zombies = []
        next_human = None
        for human in humans:
            distance = self._distance_to(human)
            print(distance)
            if distance < 25:
                killed_human.append(human)
                new_zombies.append(self.attack(human))
            elif distance < shortest_distance:
                next_human = human
                shortest_distance = distance

        if next_human:
            self.setheading(self.towards(next_human.xcor(), next_human.ycor()))
            self.forward(self._speed)

            if self._distance_to(next_human) < 25:
                killed_human.append(next_human)
                new_zombies.append(self.attack(next_human))

        for killed in killed_human:
            killed.ht()
            humans.remove(killed)

        return new_zombies


if __name__ == '__main__':
    human_list = []
    zombie_list = []
    half_size = SCREEN_SIZE // 2
    random_range = (-half_size + 25, half_size - 25)
    for _ in range(TOTAL):
        human = Human()
        human.setx(randint(*random_range))
        human.sety(randint(*random_range))
        human_list.append(human)

        zombie = Zombie()
        zombie.setx(randint(*random_range))
        zombie.sety(randint(*random_range))
        zombie_list.append(zombie)

    for _ in range(NUM_TURNS):
        new_zombies = []
        for zombie in zombie_list:
            new_zombies += zombie.chase(human_list)

        zombie_list += new_zombies

        if not human_list:
            break

        for human in human_list:
            human.run_away()

        time.sleep(0.05)

    screen.mainloop()
