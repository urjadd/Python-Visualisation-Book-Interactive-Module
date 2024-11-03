# visualyzer_types/numeric_module.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon


class Numeric:
    def __init__(self, value):
        self.value = value
        self.fig, self.ax = plt.subplots()
        self.ax.axis([0, 10, 0, 10])
        plt.axis("scaled")
        plt.axis("off")
        self.create()

    def create(self):
        if type(self.value)==int or type(self.value)==float or type(self.value)==complex:
            self.draw_rhombus(5, 5, 4)  
            plt.title('NUMERIC')
            plt.show()

    def draw_rhombus(self, center_x, center_y, side_length):
        # Define the vertices of the rhombus
        vertices = [
            (center_x, center_y + side_length / 2),
            (center_x + side_length / 2, center_y),
            (center_x, center_y - side_length / 2),
            (center_x - side_length / 2, center_y),
        ]

        rhombus = Polygon(vertices, closed=True, facecolor='black', edgecolor='black', linewidth=7)
        self.ax.add_patch(rhombus)

