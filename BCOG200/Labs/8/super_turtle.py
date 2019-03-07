import argparse
import sys
import threading
import time

""" Now let's put together what we know about inheritance with what we know
about the turtle class, and create a
    a special enhanced turtle class.

    If we want to use the Turtle class as a base, and enhance our turtles,
    we can do that by inheriting it. We just make
    the Turtle class an input parameter in our class definition. Before,
    when we inhereted Animal into Bird, we just
    had class Bird(Animal). This time, since the Turtle class is in the
    turtle module (and not defined in this file), we
    need to put turtle.Turtle as the input parameter in the class definition.
    And then we need to remember to call
    Turtle's init function as the first line of our init function.

    Then we can add other attributes and methods.


"""

from turtle import Turtle, Screen


class SuperTurtle(Turtle):
    def __init__(self, name) -> None:
        self.color = 0
        super().__init__()
        self.name = name
        self.shape('turtle')
        self.speed('fastest')
        self.onclick(self.glow)
        self.onrelease(self.unglow)

    def glow(self, x, y) -> None:
        self.fillcolor(255, 0, 0)

    def unglow(self, x, y) -> None:
        self.fillcolor("")

    def set_location(self, x, y) -> None:
        self.penup()
        self.setx(x)
        self.sety(y)

    def move_to(self, x: int, y: int) -> None:
        pass

    def _update(self) -> None:
        super()._update()
        self.fillcolor(0, 0, self.color)
        self.color += 1
        self.color %= 255


STAMP_SIZE = 20


class MoveTurtle(Turtle):
    def __init__(self, stamp_size_x: int, stamp_size_y: int,
                 shape: str) -> None:
        super().__init__()
        self.penup()
        self.shape(shape)
        self.setheading(0)
        self.turtlesize(stamp_size_y, stamp_size_x)
        self.pixel_size_x = stamp_size_x * STAMP_SIZE
        self.pixel_size_y = stamp_size_y * STAMP_SIZE
        self._speed_x = 0
        self._speed_y = 0

    @property
    def move_speed_x(self) -> int:
        return self._speed_x

    @move_speed_x.setter
    def move_speed_x(self, speed: int) -> None:
        self._speed_x = speed

    @property
    def move_speed_y(self) -> int:
        return self._speed_y

    @move_speed_y.setter
    def move_speed_y(self, speed: int) -> None:
        self._speed_y = speed

    def set_location(self, x: int, y: int) -> None:
        self.penup()
        self.setx(x)
        self.sety(y)

    def maybe_collide(self, other: 'MoveTurtle') -> bool:
        x_diff = other.xcor() - self.xcor()
        y_diff = other.ycor() - self.ycor()
        if (abs(x_diff) < (self.pixel_size_x + other.pixel_size_x) / 2
                and other.ycor() - other.pixel_size_y / 2 < self.ycor()
                and other.ycor() + other.pixel_size_y / 2 > self.ycor()):
            if x_diff * self._speed_x >= 0:
                self._speed_x = -self._speed_x
            return True
        if (abs(y_diff) < (self.pixel_size_y + other.pixel_size_y) / 2
                and other.xcor() - other.pixel_size_x / 2 < self.xcor()
                and other.xcor() + other.pixel_size_x / 2 > self.xcor()):
            if y_diff * self._speed_y >= 0:
                self._speed_y = -self._speed_y
            return True
        return False

    def move(self) -> None:
        self.set_location(self.xcor() + self.move_speed_x,
                          self.ycor() + self.move_speed_y)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('SuperTurtle')
    parser.add_argument('-g', choices=['triangle', 'tree', 'pingpong'],
                        help='Draw which one?')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    wn = Screen()
    wn.delay(1)
    wn.colormode(255)


    def update_color():
        while True:
            wn.update()
            time.sleep(0.05)


    def timed(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            f(*args, **kwargs)
            end = time.time()
            print('Time: %ds' % (end - start))

        return wrapper


    def draw_tree(my_turtle: SuperTurtle, x: int, y: int, angle: int,
                  distance: int, color: int, angle_inc: int) -> None:
        if distance < 15 or angle_inc <= 0:
            return
        my_turtle.set_location(x, y)
        my_turtle.setheading(angle)
        my_turtle.pencolor((0, color, 0))
        my_turtle.pendown()
        my_turtle.forward(distance)
        decay_distance = int(distance * 0.85)
        draw_tree(my_turtle, my_turtle.xcor(), my_turtle.ycor(),
                  angle + angle_inc, decay_distance, color + 25, angle_inc - 1)
        draw_tree(my_turtle, my_turtle.xcor(), my_turtle.ycor(),
                  angle - angle_inc, decay_distance, color + 25, angle_inc - 1)
        my_turtle.set_location(x, y)
        my_turtle.setheading(angle)
        my_turtle.pencolor((0, color, 0))


    def draw_triangle(my_turtle: SuperTurtle, x: int, y: int,
                      length: int) -> None:
        if length < 16:
            return
        my_turtle.set_location(x, y)
        headings = [-60, 180, 60]
        for heading in headings:
            my_turtle.setheading(heading)
            my_turtle.pendown()
            my_turtle.forward(length)
        draw_triangle(my_turtle, x, y, length // 2)
        my_turtle.setheading(-60)
        my_turtle.penup()
        my_turtle.forward(length // 2)
        draw_triangle(my_turtle, my_turtle.xcor(), my_turtle.ycor(),
                      length // 2)
        my_turtle.set_location(x, y)
        my_turtle.setheading(-120)
        my_turtle.penup()
        my_turtle.forward(length // 2)
        draw_triangle(my_turtle, my_turtle.xcor(), my_turtle.ycor(),
                      length // 2)
        my_turtle.set_location(x, y)


    boundaries = []
    pads = []

    ball = None


    def move_ball() -> None:
        ball = MoveTurtle(1, 1, 'circle')
        box_size = 740
        wall1 = MoveTurtle(1, box_size // STAMP_SIZE, 'square')
        wall1.set_location(-box_size // 2, 0)
        wall2 = MoveTurtle(1, box_size // STAMP_SIZE, 'square')
        wall2.set_location(box_size // 2, 0)
        wall3 = MoveTurtle(box_size // STAMP_SIZE, 1, 'square')
        wall3.set_location(0, -box_size // 2)
        wall4 = MoveTurtle(box_size // STAMP_SIZE, 1, 'square')
        wall4.set_location(0, box_size // 2)
        boundaries.append(wall1)
        boundaries.append(wall2)
        boundaries.append(wall3)
        boundaries.append(wall4)
        print(wall1.xcor(), wall1.ycor())

        pad1 = MoveTurtle(1, 15, 'square')
        pad1.set_location(-200, 0)
        pad1.move_speed_x = 0
        pad1.move_speed_y = 10
        pads.append(pad1)

        pad2 = MoveTurtle(1, 15, 'square')
        pad2.set_location(200, 0)
        pad2.move_speed_x = 0
        pad2.move_speed_y = -10
        pads.append(pad2)

        ball.move_speed_y = -2
        ball.move_speed_x = -4
        while True:
            ball.move()
            for pad in pads:
                pad.move()
            time.sleep(0.005)
            for wall in boundaries:
                ball.maybe_collide(wall)
            for pad in pads:
                ball.maybe_collide(pad)
                for wall in boundaries:
                    pad.maybe_collide(wall)


    @timed
    def draw_tree_wrapper():
        try:
            my_turtle = SuperTurtle('Jon')
            my_turtle.set_location(0, -200)
            draw_tree(my_turtle, 0, -250, 90, 100, 0, 25)
        except KeyboardInterrupt:
            return


    @timed
    def draw_triangle_wrapper():
        try:
            my_turtle = SuperTurtle('Jon')
            my_turtle.set_location(0, -200)
            draw_triangle(my_turtle, 0, 250, 512)
        except KeyboardInterrupt:
            return


    threading.Thread(target=update_color).start()

    if args.g == 'tree':
        threading.Thread(target=draw_tree_wrapper).start()
    elif args.g == 'triangle':
        threading.Thread(target=draw_triangle_wrapper).start()
    elif args.g == 'pingpong':
        threading.Thread(target=move_ball).start()

    wn.mainloop()

""" the advantage to creating these custom classes is that we can put all the 
complex program code in our class 
defitions, and maek the actual code that we use to do stuff simple and easy 
to read. WHen you add stuff to a list,
dozens of lines of code are executed. But they are all in the list class 
definition, and so you can just type 
list.append() without needing to copy and paste that code every time. And 
then if you want to change how it works,
you only need to change it in the class definition, not everywhere you used 
it."""

# Comment this code and then add your own turtle functions.
