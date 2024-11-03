#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:42:44 2024

@author: syedaumaimaminhaj
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Create circles
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

# Add => sign above the circles
ax.annotate("=>", xy=(1.95, 1.8), xytext=(1.95, 2.2), fontsize=20, ha='center', va='center')

plt.axis("off")
# Show the plot
plt.show()

