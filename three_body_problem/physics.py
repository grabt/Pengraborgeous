from three_body_problem.parsing import Configuration, Body
import pandas as pd
import numpy as np


class Engine:
    def __init__(self, configuration: Configuration) -> None:
        pass

    def simulate(self):
        pass

    def get_dataframe(self):
        data = []
        for t in range(0, 10000):
            data.append([t, np.cos(t/100), np.sin(t/100)])
        return pd.DataFrame(data=data, columns=["time", "x_pos0", "y_pos0"])
