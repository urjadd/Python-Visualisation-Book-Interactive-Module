#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:28:16 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Before
# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Create trapeziums
trap1 = patches.Polygon(
            [(1, 1), (2, 2.2), (4, 2.2), (5, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap1)

trap2 = patches.Polygon(
            [(6, 1), (7, 2.2), (9, 2.2), (10, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap2)

# Create connected lines between trapeziums
y_l = 1.6
ax.plot([4.5, 6.5], [y_l, y_l], color='black', linewidth=4)

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
# Show the plot
plt.show()

#After
# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Create trapeziums
trap1 = patches.Polygon(
            [(1, 1), (2, 2.2), (4, 2.2), (5, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap1)

trap2 = patches.Polygon(
            [(6, 1), (7, 2.2), (9, 2.2), (10, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap2)

trap3 = patches.Polygon(
            [(11, 1), (12, 2.2), (14, 2.2), (15, 1)],
            facecolor='None', edgecolor='black', linewidth=5)
ax.add_patch(trap3)

# Create connected lines between trapeziums
y_l = 1
ax.plot([4.5, 6.5], [y_l, y_l], color='black', linewidth=4)
ax.plot([9.5, 11.5], [y_l, y_l], color='black', linewidth=4)

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
# Show the plot
plt.show()
