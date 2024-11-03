#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 00:37:09 2024

@author: syedaumaimaminhaj
"""


import matplotlib.pyplot as plt
import numpy as np

# Create circle points
theta = np.linspace(0, 2*np.pi, 100)
r = 1  # radius of the circle

x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the circle in black
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='black')  # Change circle color to black

# Add arrows on the top and bottom with increased thickness and in black color
arrow_length = 0.1
arrow_prop_top = dict(arrowstyle='->', shrinkA=0, shrinkB=0, linewidth=2, color='black')  # Black arrow
arrow_prop_bottom = dict(arrowstyle='<-', shrinkA=0, shrinkB=0, linewidth=2, color='black')  # Black arrow

# Arrow on the top
plt.annotate('', xy=(x[int(len(theta) * 0.25)], y[int(len(theta) * 0.25)]), 
             xytext=(x[int(len(theta) * 0.2)], y[int(len(theta) * 0.2)]), 
             arrowprops=arrow_prop_top)

# Arrow on the bottom
plt.annotate('', xy=(x[int(len(theta) * 0.75)], y[int(len(theta) * 0.75)]), 
             xytext=(x[int(len(theta) * 0.8)], y[int(len(theta) * 0.8)]), 
             arrowprops=arrow_prop_bottom)

plt.axis('off')  # Turn off the axes
plt.grid(False)  # Turn off the grid
plt.show()


















