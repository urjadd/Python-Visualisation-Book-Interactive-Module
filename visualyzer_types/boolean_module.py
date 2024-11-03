# visualyzer_types/boolean_module.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import RegularPolygon

class Boolean:
    def __init__(self, value):
        self.value = value
        self.create()

    def create(self):
        fig, ax = plt.subplots()
        ax.axis([0, 10, 0, 10])
        plt.axis("scaled")
        plt.axis("off")

        if self.value:
           
            self.draw_pointer(ax, 5, 3, 'up', 'black')
            plt.title('TRUE')
        else:
            self.draw_pointer(ax, 5, 7, 'down', 'black')
            plt.title('FALSE')

        plt.show()



    def draw_pointer(self, ax, center_x, center_y, direction, color):
        line_length = 3
        if direction == 'up':
            ax.arrow(center_x, center_y, 0, line_length, head_width=0.9, head_length=0.9, fc=color, ec=color,linewidth=7)
        else:
            ax.arrow(center_x, center_y, 0, -line_length, head_width=0.9, head_length=0.9, fc=color, ec=color,linewidth=7)

