import matplotlib.pyplot as plt
import numpy as np

def plot_polygon(axes, polygon, mark_color='k', fill=False, color='k'):
    points = np.array(polygon.exterior.coords)
    axes.add_patch(plt.Polygon(points, fill=fill, color=color))
    axes.update_datalim(points)
    axes.autoscale()

    axes.plot(points[:, 0], points[:, 1], color=mark_color, marker='o', linestyle='')

def plot_line_string(axes, line_string):
    points = np.array(line_string.coords)
    axes.plot(points[:, 0], points[:, 1])