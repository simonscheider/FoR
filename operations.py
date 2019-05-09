import numpy as np
from scipy.spatial import Voronoi

from shapely.geometry import LineString, Point, MultiLineString


def between(a, b):
    """
    :param a: The first `shapely.geometry.BaseGeometry`
    :param b: The second `shapely.geometry.BaseGeometry`
    :returns: `shapely.geometry.BaseGeometry` describing the region between `a` and `b`.
    """
    return a.union(b).convex_hull.difference(a).difference(b)


def medial_line(a):
    points = np.array(a.exterior.coords)
    vor = Voronoi(points)
    line_points = []

    # Get the pairs of indices (into vor.vertices) of the points that form the finite Voronoi ridges INSIDE the polygon.
    valid_ridges = [(ridge[0], ridge[1]) for ridge in vor.ridge_vertices if ridge[0] != -1 and ridge[1] != -1 and Point(vor.vertices[ridge[0]]).within(a) and Point(vor.vertices[ridge[1]]).within(a)]

    if not valid_ridges:
        raise Exception("There's not enough Voronoi ridges fully inside the polygon. TODO: Sample the LineStrings?")

    # Order them so that they connect into (a) path(s). This might end up in multiple paths, as the Voronoi ridges (in general) branch.
    paths = []
    for (p1, p2) in valid_ridges:
        paths_with_p1 = [path for path in paths if path[-1] == p1 or path[0] == p1]
        paths_with_p2 = [path for path in paths if path[-1] == p2 or path[0] == p2]
        rest = [path for path in paths if path[-1] != p1 and path[0] != p1 and path[-1] != p2 and path[0] != p2]

        if len(paths_with_p1) > 1 or len(paths_with_p2) > 1:
            raise Exception('Found a single node in multiple paths.')
        
        path1, path2 = None, None
        if paths_with_p1:
            path1 = paths_with_p1[0]
        if paths_with_p2:
            path2 = paths_with_p2[0]

        new_paths = []
        if path1 and not path2:
            new_paths.append(_add_edge_to_path(path1, (p1, p2)))
        elif not path1 and path2:
            new_paths.append(_add_edge_to_path(path2, (p1, p2)))
        elif paths_with_p1 and paths_with_p2:
            new_paths.append(_connect_paths(path1, path2))
        else:
            new_paths += [[p1, p2]]
        
        paths = new_paths + rest

    if len(paths) > 1:
        return MultiLineString([LineString([vor.vertices[i] for i in line_string]) for line_string in paths])
    else:
        return LineString([vor.vertices[i] for i in paths[0]])


# 1 (a, b, c) and (c, d, e) => (a, b, c, d, e)
# 2 (a, b, c) and (a, d, e) => (e, d, a, b, c)
# 3 (a, b, c) and (d, e, c) => (a, b, c, e, d)
# 4 (a, b, c) and (d, e, a) => (d, e, a, b, c)
def _connect_paths(p1, p2):
    if p1[0] == p2[0]:
        return p2[::-1] + p1[1:]
    elif p1[0] == p2[-1]:
        return p2 + p1[1:]
    elif p1[-1] == p2[0]:
        return p1 + p2[1:]
    elif p1[-1] == p2[-1]:
        return p1 + p2[1::-1]


def _add_edge_to_path(p, e):
    if p[0] == e[0]:
        return [e[1]] + p
    elif p[0] == e[1]:
        return [e[0]] + p
    elif p[-1] == e[0]:
        return p + [e[1]]
    elif p[-1] == e[1]:
        return p + [e[0]]
    else:
        raise Exception("The origin nor the destination of the edge was found at the start or end of the path. Could not connect new edge.")
