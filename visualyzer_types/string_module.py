# visualyzer_types/string_module.py

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle
from matplotlib.lines import Line2D

class String:
    def __init__(self, value):
        self.value = value
        self.fig, self.ax = plt.subplots()
        self.ax.axis([0, 10, 0, 10])
        plt.axis("scaled")
        plt.axis("off")
        plt.title('CHAR')
        self.create()

    def create(self):
        if type(self.value)==str and len(self.value) == 1:
                self.draw_circle(3, 5, 1.5)  # Draw a circle centered on the diamond
        elif type(self.value)==str:
            self.draw_circle(3, 5, 1.5)  # Draw the first circle
            self.draw_circle(7, 5, 1.5)  # Draw the second circle
            self.draw_line(4.5, 5, 5.5, 5)  # Draw a line connecting the two circles

            plt.show()


    def draw_line(self, x1, y1, x2, y2):
        line = Line2D([x1, x2], [y1, y2], color='black', linewidth=7)
        self.ax.add_line(line)

    def draw_circle(self, center_x, center_y, radius):
        circle = Circle((center_x, center_y), radius=radius, facecolor='black', linewidth=7, edgecolor="black")
        self.ax.add_patch(circle)