# visualyzer_types/none_module.py

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class MyNone:
    def __init__(self, value):
        self.value = value
        self.fig, self.ax = plt.subplots()
        self.ax.axis([0, 10, 0, 10])
        plt.axis("scaled")
        plt.axis("off")
        plt.title('NONE')
        self.create()

    def create(self):
        if self.value is None:
            self.draw_circle(5, 5, 2.5)
            self.ax.plot([2.5, 7.5], [2.5, 7.5], color='black', linewidth=7)

        plt.show()

    def draw_circle(self, center_x, center_y, radius):
        circle = Circle((center_x, center_y), radius=radius, facecolor='None', linewidth=7, edgecolor="black")
        self.ax.add_patch(circle)
