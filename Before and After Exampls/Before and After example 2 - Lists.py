#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:02:47 2024

@author: syedaumaimaminhaj
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Define the coordinates and dimensions of the rectangle
x = 1  # x-coordinate of the lower-left corner
y = 1  # y-coordinate of the lower-left corner

phi = 1.61803398875  # Golden ratio
# Calculate the width and height based on the golden ratio
width = 2
height = width / phi  # Height is calculated to maintain the golden ratio

# Create rectangles
rectangle1 = patches.Rectangle((x, y), width, height, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(rectangle1)

rectangle2 = patches.Rectangle((x + 3, y), width, height, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(rectangle2)


# Create connected lines between rectangles
y_l = 1.6
ax.plot([3, 4], [y_l, y_l], color='black', linewidth=4)

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
plt.show()


# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Define the coordinates and dimensions of the rectangle
x = 1  # x-coordinate of the lower-left corner
y = 1  # y-coordinate of the lower-left corner

phi = 1.61803398875  # Golden ratio
# Calculate the width and height based on the golden ratio
width = 2
height = width / phi  # Height is calculated to maintain the golden ratio

# Create rectangles
rectangle1 = patches.Rectangle((x, y), width, height, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(rectangle1)

rectangle2 = patches.Rectangle((x + 3, y), width, height, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(rectangle2)

rectangle3 = patches.Rectangle((x + 6, y), width, height, linewidth=4, edgecolor='black', facecolor='none')
ax.add_patch(rectangle3)


# Create connected lines between rectangles
y_l = 1
ax.plot([3, 4], [y_l, y_l], color='black', linewidth=4)
ax.plot([6, 7], [y_l, y_l], color='black', linewidth=4)


# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
plt.show()
