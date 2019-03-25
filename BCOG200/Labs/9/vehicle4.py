import math
import random
import turtle

'''
    Modify this program in the following ways:
    
    Modify the vehicle so that, for things that it likes, it has a 'u-shaped' 
    preference curve, moving little when it is far away from something, 
    or when it is really close, but moving quickly when it is a moderate 
    distance away. If you get this working correctly, you should get your 
    Vehicles approaching and staying near the things they like
'''


class HeatSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, visible=False)
        self.shape('circle')
        self.penup()
        self.color(255, 190, 60)
        self.goto(random.randint(-200, 0), random.randint(-200, 0))
        self.showturtle()
        self.type = 'heat'


class ColdSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, visible=False)
        turtle.Turtle.__init__(self, visible=False)
        self.shape('circle')
        self.penup()
        self.color(60, 255, 190)
        self.goto(random.randint(0, 200), random.randint(0, 200))
        self.showturtle()
        self.type = 'cold'


class Vehicle4(turtle.Turtle):

    def __init__(self, input_list, vehicle_id, vehicle_type):
        turtle.Turtle.__init__(self, visible=False)
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.input_list = input_list
        self.create_vehicle()
        self.speed_parameters = [20, 0.2, 6]
        self.turn_parameters = [20]
        self.moves = 0
        self.distance_weights = {'heat': [0, 1], 'cold': [1, 0]}
        self.max_speed_distance = 250
        self.speed_range = 80
        self.gaussian_scale = 200

    def create_vehicle(self):
        self.shape('turtle')
        self.turtlesize(1)
        self.penup()
        if self.vehicle_type == 'crossed':
            self.color(random.randint(0, 150), random.randint(0, 150), 255)
        else:
            self.color(255, random.randint(0, 150), random.randint(0, 150))
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
        return left_distance, right_distance

    def compute_speed(self, left_distance, right_distance, source_type):
        left_weight, right_weight = self.distance_weights[source_type]
        if self.vehicle_type == 'crossed':
            left_speed = self.gaussian(right_distance * left_weight
                                       + left_distance * right_weight)
            right_speed = self.gaussian(right_distance * right_weight
                                        + left_distance * left_weight)
        else:
            right_speed = self.gaussian(right_distance * left_weight
                                        + left_distance * right_weight)
            left_speed = self.gaussian(right_distance * right_weight
                                       + left_distance * left_weight)
        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed

    def compute_turn_amount(self, left_speed, right_speed):
        turn_amount = self.turn_parameters[0] * (right_speed - left_speed)
        return turn_amount

    def gaussian(self, distance):
        """
        The speed is modulated by a gaussian function on the distance.
        :param distance:
        :return:
        """
        return self.gaussian_scale / (
                self.speed_range * math.sqrt(2 * math.pi)) * math.exp(
            -1 / 2 * math.pow(
                (distance - self.max_speed_distance) / self.speed_range, 2))

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
            print(self.gaussian(input_distance), input_distance)
            combined_speed += average_speed

        try:
            self.right(combined_turn_amount)
        except Exception:
            print(combined_turn_amount)
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
    num_vehicles = 2
    num_heat_sources = 1
    num_cold_sources = 1

    vehicle_list = []
    input_list = []

    for i in range(num_heat_sources):
        input_list.append(HeatSource())

    for i in range(num_cold_sources):
        input_list.append(ColdSource())

    for i in range(num_vehicles):
        vehicle_list.append(
            Vehicle4(input_list, i, random.choice(["crossed", "direct"])))

    wn.update()
    while True:
        for j in range(num_vehicles):
            vehicle_list[j].move()
        wn.update()


if __name__ == '__main__':
    main()
