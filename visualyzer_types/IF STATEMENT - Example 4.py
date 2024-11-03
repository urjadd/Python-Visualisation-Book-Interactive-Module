#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 00:18:59 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Create triangles
triangle1 = patches.Polygon(
    [(1.2, 1), (2.2, 2.4), (3.2, 1)],
    facecolor='none', edgecolor='black', linewidth=5)
ax.add_patch(triangle1)

# Add the letter 'x' inside the triangle
ax.text(2.2, 1.5, 'x', fontsize=20, ha='center', va='center')

# Add a question mark above the triangle
ax.text(2.2, 2.8, '?', fontsize=20, ha='center', va='center')

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")

# Show the plot
plt.show()


