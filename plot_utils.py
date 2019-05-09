import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, LineString, MultiLineString

def plot(axes, thing, **kwargs):
    if isinstance(thing, LineString):
        plot_line_string(axes, thing, **kwargs)
    elif isinstance(thing, Polygon):
        plot_polygon(axes, thing, **kwargs)
    elif isinstance(thing, MultiLineString):
        for line_string in thing.geoms:
            plot_line_string(axes, line_string, **kwargs)


def plot_polygon(axes, polygon, marker='', mark_color='k', fill=True, color='k'):
    points = np.array(polygon.exterior.coords)
    axes.add_patch(plt.Polygon(points, fill=fill, color=color))

    axes.plot(points[:, 0], points[:, 1], color=mark_color, marker=marker, linestyle='')


def plot_line_string(axes, line_string, color='k'):
    points = np.array(line_string.coords)
    axes.plot(points[:, 0], points[:, 1], color=color)
    