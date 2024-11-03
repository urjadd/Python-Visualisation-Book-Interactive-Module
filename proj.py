#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 01:47:06 2023

@author: syedaumaimaminhaj
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


# Function to plot a circle
def plot_circle():
    circle = plt.Circle((0, 0), 0.5, color='black')
    ax = plt.gca()
    ax.add_patch(circle)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Function to plot a rectangle
def plot_rectangle():
    rectangle = plt.Rectangle((-0.5, -0.5), 1, 1, color='black')
    ax = plt.gca()
    ax.add_patch(rectangle)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Function to plot a fancy arrow representing loops
def plot_loop_arrow():
    loop_arrow = FancyArrowPatch((0, 0.4), (0, -0.4), connectionstyle="arc3,rad=0.3", arrowstyle='->', color='black', linewidth=2)
    ax = plt.gca()
    ax.add_patch(loop_arrow)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Plotting individual shapes
plot_circle()  # Plot a circle
plot_rectangle()  # Plot a rectangle
plot_loop_arrow()  # Plot a loop arrow

