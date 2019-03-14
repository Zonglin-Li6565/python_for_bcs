import math
import random
import turtle


class HeatSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, visible=False)
        self.shape('circle')
        self.penup()
        self.color(255, 190, 60)
        self.goto(0, 0)
        self.showturtle()


class Vehicle1(turtle.Turtle):

    def __init__(self, heatsource1, wn):
        turtle.Turtle.__init__(self, visible=False)
        self.heatsource = heatsource1
        self.onclick(self.move)
        self.create_turtle()
        self.wn = wn

    def create_turtle(self):
        self.shape('classic')
        self.turtlesize(2)
        self.penup()
        self.color(0, 0, 255)
        self.goto(random.randint(-390, 390), random.randint(-390, 390))
        self.right(random.randint(0, 360))
        self.showturtle()

    def move(self, x, y):
        while True:
            towards = self.towards(self.heatsource.xcor(),
                                   self.heatsource.ycor())
            distance = self.distance(self.heatsource.position())
            proportion = (0.3 / math.log(distance))
            current_heading = self.heading()
            current_heading += (towards - current_heading) * proportion
            print(proportion)
            self.setheading(current_heading)
            self.forward(0.1)
            self.wn.update()


def create_screen():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.setup(1200, 800)
    wn.title("Vehicle 1")
    return wn


def main():
    wn = create_screen()
    wn.tracer(0, 0)
    heatsource1 = HeatSource()
    vehicle_list = []
    for i in range(10):
        vehicle_list.append(Vehicle1(heatsource1, wn))
    wn.update()
    wn.mainloop()


main()
