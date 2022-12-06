from three_body_problem.parsing import Configuration, Body
import pandas as pd
import numpy as np


class Engine:
    def __init__(self, configuration: Configuration) -> None:
        self.video_length = configuration.video_length
        self.delta_t = configuration.delta_t
        self.bodies = configuration.bodies
        self.data = []

    def simulate(self):
        t_0 = 0
        t = t_0
        dt = self.delta_t
        t_end = self.video_length
        big_G = 6.67e-11
        while t < t_end:
            for m1_idx in range(len(self.bodies)):
                a_g = [0, 0]  # acceleration vector

                for m2_idx in range(len(self.bodies)):
                    if m1_idx != m2_idx:
                        r_vector = [0, 0]
                        r_vector[0] = self.bodies[m1_idx].x - \
                            self.bodies[m2_idx].x
                        r_vector[1] = self.bodies[m1_idx].y - \
                            self.bodies[m2_idx].y

                        r_mag = (r_vector[0]**2 + r_vector[1]**2)**0.5

                        acceleration = -1.0 * big_G * \
                            ((self.bodies[m2_idx].mass) / r_mag**2)
                        r_unit_vector = [r_vector[0]/r_mag, r_vector[1]/r_mag]

                        a_g[0] += acceleration * r_unit_vector[0]
                        a_g[1] += acceleration * r_unit_vector[1]

                self.bodies[m1_idx].v_x += a_g[0] * dt
                self.bodies[m1_idx].v_y += a_g[1] * dt

            for entity_idx in range(len(self.bodies)):
                self.bodies[entity_idx].x += self.bodies[entity_idx].v_x * dt
                self.bodies[entity_idx].y += self.bodies[entity_idx].v_y * dt
            row_data = [t]
            for entity_idx in range(len(self.bodies)):
                row_data.append(self.bodies[entity_idx].x)
                row_data.append(self.bodies[entity_idx].y)
            self.data.append(row_data)
            t += dt

    def get_dataframe(self):
        columns = ["time"]
        for entity_idx in range(len(self.bodies)):
            columns.append("x_pos" + str(entity_idx))
            columns.append("y_pos" + str(entity_idx))
        return pd.DataFrame(data=self.data, columns=columns)
