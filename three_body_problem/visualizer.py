from three_body_problem.parsing import Configuration,
import pandas as pd
import turtle


class Visualizer():
    def __init__(self, configuration: Configuration, dataframe: pd.DataFrame) -> None:
        pass

    def movie(self):
        pass


class SolarSystemBody(turtle.Turtle):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0), ):

        super().__init__()
        self.mass = mass
        self.setpoition(position)
        self.velocity = velocity

        self.penup()
        self.hideturtle()

        solar_system.add_body(self)


class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")

        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)
