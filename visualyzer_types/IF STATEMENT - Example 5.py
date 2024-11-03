#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 01:06:49 2024

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 3))

# Add text annotation for 'x >' with adjusted properties
ax.text(0.5, 1, 'x    >', fontsize=30, color='black', va='center', ha='right')

# Add '?' sign above '>'
ax.text(0.35, 2, '?', fontsize=30, color='black', va='center', ha='center')

# Create rectangles after the text
romb1 = patches.Polygon(
    [(1.5, 1), (2.5, 1.9), (3.5, 1), (2.5, 0.1)],  # Adjusted coordinates to position after the text
    facecolor='black', edgecolor='black', linewidth=5)
ax.add_patch(romb1)

# Set the x and y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 4)

plt.axis("off")
# Show the plot
plt.show()



