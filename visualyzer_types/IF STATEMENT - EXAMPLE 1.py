#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:37:45 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# string 1
circle1 = patches.Circle((1, 1), radius=0.6, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle1)

circle2 = patches.Circle((2.9, 1), radius=0.6, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle2)

# Create connected lines between circles
y_l = 1
ax.plot([1.5, 2.3], [y_l, y_l], color='black', linewidth=5)

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

# Add text annotation for the "=="
ax.text(4, 1 - 0.15, "==", fontsize=20, va='center')

# string 2
circle3 = patches.Circle((5.8, 1), radius=0.6, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle3)

circle4 = patches.Circle((7.7, 1), radius=0.6, facecolor='black', edgecolor='black', linewidth=8)
ax.add_patch(circle4)

# Create connected lines between circles
y_l = 1
ax.plot([6.5, 7.5], [y_l, y_l], color='black', linewidth=5)

# Add text annotation for the "?"
ax.text(4.2, 1 + 0.7, "?", fontsize=20, va='center')

# Show the plot
plt.axis("off")
plt.show()


