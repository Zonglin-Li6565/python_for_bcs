import math
import random
import turtle

'''
    Modify this program in the following ways:
        - Add at least 1 more class representing another kind of input other 
        than heat.
        - Have the input_list contain multiple kinds of input sources.
        - Use custom images for each input sources
        - Modify vehicle 3 so that it has an 'innate preference' or 'innate 
        dislike' of each kind of input 
'''


class HeatSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, 'sun.gif', visible=False)
        self.penup()
        self.goto(random.randint(-200, -50), random.randint(-200, -50))
        self.showturtle()
        self.type = 'heat'


class ColdSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, 'moon.gif', visible=False)
        self.penup()
        self.goto(random.randint(50, 200), random.randint(50, 200))
        self.showturtle()
        self.type = 'cold'


class Vehicle4(turtle.Turtle):

    def __init__(self, input_list, vehicle_id, vehicle_type, prefer):
        turtle.Turtle.__init__(self, visible=False)
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.input_list = input_list
        self.create_vehicle()
        self.turn_parameters = [200]
        self.moves = 0
        self.prefer = prefer
        self.max_speed = 200
        # Max speed when 200 away from a source ('mean' of the gaussian
        # function)
        self.max_speed_distance = 200
        # The 'standard deviation' of the gaussian function
        self.range_of_speed_adjustment = 80

    def create_vehicle(self):
        self.shape('turtle')
        self.turtlesize(1)
        self.penup()
        if self.vehicle_type == 'crossed':
            self.color(0, 0, 255)
        else:
            self.color(255, 0, 0)
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
        self.right(random.randint(0, 360))
        self.pendown()
        self.showturtle()

    def get_input_information(self, position):
        input_distance = self.distance(position)
        input_angle = self.heading() - self.towards(position)
        return input_distance, input_angle

    def get_sensor_distances(self, distance, angle):
        sin_angle = math.sin(math.radians(angle))
        left_distance = distance - sin_angle
        right_distance = distance + sin_angle
        if left_distance == 0:
            left_distance = 0.00001
        if right_distance == 0:
            right_distance = 0.00001
        return left_distance, right_distance

    def _compute_speed_preference(self, distance):
        """
        The speed to distance is a gaussian function. When the distance is
        self.max_speed_distance, the speed will be largest. Then it will
        decrease if the vehicle gets close or farther.

        :param distance: How far the sensor is to the source
        :return: The speed corresponds to this sensor
        """
        gaussian = (self.max_speed /
                    (self.range_of_speed_adjustment
                     * math.sqrt(2 * math.pi))
                    * math.exp(-0.5 * ((distance - self.max_speed_distance)
                                       / self.range_of_speed_adjustment) ** 2))
        return gaussian

    def compute_speed(self, left_distance, right_distance, source_type):
        if self.vehicle_type == 'crossed':
            right_speed = self._compute_speed_preference(left_distance)
            left_speed = self._compute_speed_preference(right_distance)
        else:
            right_speed = self._compute_speed_preference(right_distance)
            left_speed = self._compute_speed_preference(left_distance)

        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed

    def compute_turn_amount(self, left_speed, right_speed):
        turn_amount = self.turn_parameters[0] * (right_speed - left_speed)
        return turn_amount

    def move(self):
        combined_speed = 0
        combined_turn_amount = 0

        for current_input in self.input_list:
            input_distance, input_angle = self.get_input_information(
                current_input.position())
            left_distance, right_distance = self.get_sensor_distances(
                input_distance, input_angle)
            left_speed, right_speed, average_speed = self.compute_speed(
                left_distance, right_distance, current_input.type)
            turn_amount = self.compute_turn_amount(left_speed, right_speed)
            combined_turn_amount += turn_amount
            combined_speed += average_speed

        self.right(combined_turn_amount)
        self.forward(combined_speed)
        self.moves += 1


def create_screen():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.setup(1200, 800)
    wn.title("Vehicle 3")
    wn.tracer(0, 0)
    return wn


def main():
    wn = create_screen()
    wn.addshape('sun.gif')
    wn.addshape('moon.gif')

    num_vehicles = 50
    num_heat_sources = 0
    num_cold_sources = 4

    vehicle_list = []
    input_list = []

    for i in range(num_heat_sources):
        input_list.append(HeatSource())

    for i in range(num_cold_sources):
        input_list.append(ColdSource())

    for i in range(num_vehicles):
        vehicle_list.append(
            Vehicle4(input_list, i, 'crossed', 'cold'))

    wn.update()
    while True:
        for j in range(num_vehicles):
            vehicle_list[j].move()
        wn.update()


if __name__ == '__main__':
    main()
