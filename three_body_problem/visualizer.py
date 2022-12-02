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
        lower_x = dataframe["x_pos0"].min()
        lower_y = dataframe["y_pos0"].min()
        upper_x = dataframe["x_pos0"].max()
        upper_y = dataframe["y_pos0"].max()
        turtle.setworldcoordinates(lower_x, lower_y, upper_x, upper_y)

    def play_movie(self):
        turtles = []
        initial_conditions = self.dataframe.iloc[0]
        #columns = self.dataframe.columns

        t = turtle.Turtle()
        turtles.append(t)
        t.up()
        t.shape("circle")
        t.speed("slow")
        t.turtlesize(1)
        t.setposition(initial_conditions["x_pos0"],
                      initial_conditions["y_pos0"])
        t.color("blue", "blue")
        t.down()

        for i, cords in self.dataframe.iterrows():
            t.setpos(cords["x_pos0"], cords["y_pos0"])

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)
