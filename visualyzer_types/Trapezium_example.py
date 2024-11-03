#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:24:57 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Create trapeziums
trap1 = patches.Polygon(
            [(1, 1), (1.7, 2.2), (3.3, 2.2), (3.8, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap1)

trap2 = patches.Polygon(
            [(4, 1), (4.7, 2.2), (6.3, 2.2), (6.8, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap2)

trap3 = patches.Polygon(
            [(7, 1), (7.7, 2.2), (9.3, 2.2), (9.8, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap3)

trap4 = patches.Polygon(
            [(10, 1), (10.7, 2.2), (12.3, 2.2), (12.8, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap4)

trap5 = patches.Polygon(
            [(13, 1), (13.7, 2.2), (15.3, 2.2), (15.8, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap5)

# Create connected lines between trapeziums
y_l = 1.6
ax.plot([3.6, 4.25], [y_l, y_l], color='black', linewidth=4)
ax.plot([6.6, 7.25], [y_l, y_l], color='black', linewidth=4)
ax.plot([9.6, 10.25], [y_l, y_l], color='black', linewidth=4)
ax.plot([12.6, 13.25], [y_l, y_l], color='black', linewidth=4)

# Define a function to add shapes to the plot
line_length = 0.4
arrow = patches.FancyArrow(2.3, 1.2, 0, line_length, head_width=0.3, head_length=0.3, fc='black', ec='black', linewidth=5)
ax.add_patch(arrow)

circle1 = patches.Circle((5.4, 1.6), radius=0.3, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle1)

rhombus1 = patches.Polygon(
            [(8.5, 1.3), (8, 1.6), (8.5, 1.9), (9, 1.6)],
            facecolor='black', edgecolor='black', linewidth=5)
ax.add_patch(rhombus1)

circle2 = patches.Circle((11.5, 1.6), radius=0.3, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle2)

rhombus2 = patches.Polygon(
            [(14.5, 1.3), (14, 1.6), (14.5, 1.9), (15, 1.6)],
            facecolor='black', edgecolor='black', linewidth=5)
ax.add_patch(rhombus2)


# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
# Show the plot
plt.show()










