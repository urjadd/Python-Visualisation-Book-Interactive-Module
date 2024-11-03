#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:16:17 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Tuple:
    def __init__(self, shapes, top_width=5, bottom_width=7, height=4):
        self.shapes = shapes
        self.top_width = top_width
        self.bottom_width = bottom_width
        self.height = height
        self.facecolor = 'None'
        
        max_shapes = max(len(shapes), 8)
        fig_width = max_shapes * (bottom_width + 1)
        fig_height = 2 * height

        self.fig, self.ax = plt.subplots(figsize=(fig_width, fig_height))
        self.ax.axis([0, fig_width, -height, height])
        plt.axis("off")

        self.create_background()
        self.create()

    def trapezium_list(self, center_x, center_y, shape, top_label, bottom_label):
        half_top = self.top_width / 2
        half_bottom = self.bottom_width / 2

        x1 = center_x - half_bottom
        y1 = center_y - self.height / 2
        x2 = center_x + half_bottom
        y2 = center_y - self.height / 2
        x3 = center_x + half_top
        y3 = center_y + self.height / 2
        x4 = center_x - half_top
        y4 = center_y + self.height / 2

        trapezium = patches.Polygon(
            [(x1, y1), (x2, y2), (x3, y3), (x4, y4)],
            closed=True,
            facecolor=self.facecolor,
            edgecolor='black',
            linewidth=8
        )
        self.ax.add_patch(trapezium)

    def create_background(self):
        background_width = len(self.shapes) * (self.bottom_width + 0.1)
        background_height = 2 * self.height
        rectangle = patches.Rectangle(
            (0, -self.height),
            width=background_width,
            height=background_height,
            facecolor="None",
            edgecolor='None',
            linewidth=2
        )
        self.ax.add_patch(rectangle)

    def create(self):
        positions = [i * (self.bottom_width) for i in range(len(self.shapes))]
        centers = []

        for i, (shape, index) in enumerate(zip(self.shapes, range(len(self.shapes)))):
            center_x = positions[i] + self.bottom_width / 2
            center_y = 0
            top_label = index
            bottom_label = index - len(self.shapes)
            self.trapezium_list(center_x, center_y, shape, top_label, bottom_label)
            centers.append((center_x, center_y))

        for i in range(len(centers) - 1):
            x1, y1 = centers[i]
            x2, y2 = centers[i + 1]
            self.ax.plot([x1 + self.top_width / 2 + 0.6, x2 - self.top_width / 2 - 0.6], [y1, y2], color='black', linewidth=5)

        plt.show()


# Example usage:
shapes = ['trapezium', 'trapezium', 'trapezium']
tuple_obj = Tuple(shapes)


# Example usage:
shapes = ['trapezium', 'trapezium', 'trapezium']
tuple_obj = Tuple(shapes)


