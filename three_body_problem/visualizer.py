from three_body_problem.parsing import Configuration
import pandas as pd
import turtle


class Visualizer():
    def __init__(self, configuration: Configuration, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        self.configuration = configuration
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")

        self.screen.setup(configuration.width, configuration.height)

        x_pos_data = []
        y_pos_data = []
        for column in dataframe.columns:
            if column.startswith("x_pos"):
                x_pos_data.append(column)
            elif column.startswith("y_pos"):
                y_pos_data.append(column)
        lower_x = dataframe[x_pos_data].min().min()
        lower_y = dataframe[y_pos_data].min().min()
        upper_x = dataframe[x_pos_data].max().max()
        upper_y = dataframe[y_pos_data].max().max()
        turtle.setworldcoordinates(lower_x, lower_y, upper_x, upper_y)

    def play_movie(self):
        turtles = []
        initial_conditions = self.dataframe.iloc[0]
        number_of_planets = len(self.configuration.bodies)
        for planet_id in range(number_of_planets):
            t = turtle.Turtle()
            turtles.append(t)
            t.up()
            t.shape("circle")
            t.speed("slow")
            t.turtlesize(1)
            t.setposition(initial_conditions["x_pos" + str(planet_id)],
                          initial_conditions["y_pos" + str(planet_id)])
            t.color(
                self.configuration.bodies[planet_id].color, self.configuration.bodies[planet_id].color)
            t.down()

        for i, cords in self.dataframe.iterrows():
            for planet_id in range(number_of_planets):
                turtles[planet_id].setpos(cords["x_pos" + str(planet_id)],
                                          cords["y_pos" + str(planet_id)])

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)
