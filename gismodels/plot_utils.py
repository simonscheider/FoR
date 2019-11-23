import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np
from shapely.geometry import Polygon, LineString, MultiLineString, MultiPolygon

def plot(axes, thing, **kwargs):
    if isinstance(thing, LineString):
        plot_line_string(axes, thing, **kwargs)
    elif isinstance(thing, Polygon):
        plot_polygon(axes, thing, **kwargs)
    elif isinstance(thing, MultiLineString):
        for line_string in thing.geoms:
            plot_line_string(axes, line_string, **kwargs)
    elif isinstance(thing, MultiPolygon):
        for polygon in thing.geoms:
            plot_polygon(axes, polygon, **kwargs)


def plot_polygon(axes, polygon, marker='', mark_color='k', fill=True, color='k'):
    points = np.array(polygon.exterior.coords)
    if not polygon.interiors:
        points = np.array(polygon.exterior.coords)
        axes.add_patch(plt.Polygon(points, fill=fill, color=color))
        axes.plot(points[:, 0], points[:, 1], color=mark_color, marker=marker, linestyle='')
    else:
        path = _pathify(polygon)
        patch = PathPatch(path, facecolor=color, linewidth=0)
        axes.add_patch(patch)
        axes.plot(points[:, 0], points[:, 1], color=mark_color, marker=marker, linestyle='')
        for hole in polygon.interiors:
            hole_points = np.array(hole.coords)
            axes.plot(hole_points[:, 0], hole_points[:, 1], color=mark_color, marker=marker, linestyle='')

def plot_line_string(axes, line_string, color='k'):
    points = np.array(line_string.coords)
    axes.plot(points[:, 0], points[:, 1], color=color)
    

# Adapted from https://sgillies.net/2010/04/06/painting-punctured-polygons-with-matplotlib.html
def _ring_coding(ob):
    # The codes will be all "LINETO" commands, except for "MOVETO"s at the
    # beginning of each subpath
    n = len(ob.coords)
    codes = np.ones(n, dtype=Path.code_type) * Path.LINETO
    codes[0] = Path.MOVETO
    return codes

# Adapted from https://sgillies.net/2010/04/06/painting-punctured-polygons-with-matplotlib.html
def _pathify(polygon):
    # Convert coordinates to path vertices. Objects produced by Shapely's
    # analytic methods have the proper coordinate order, no need to sort.
    vertices = np.concatenate(
                    [np.asarray(polygon.exterior)]
                    + [np.asarray(r) for r in polygon.interiors])
    codes = np.concatenate(
                [_ring_coding(polygon.exterior)]
                + [_ring_coding(r) for r in polygon.interiors])
    return Path(vertices, codes)