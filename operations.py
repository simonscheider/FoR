import numpy as np
from scipy.spatial import Voronoi

from math import cos, sin, pi

from shapely.geometry import LineString, Point, MultiLineString, Polygon
from shapely.affinity import rotate, translate, scale
from shapely.ops import split, linemerge

def between(a, b):
    """
    :param a: The first `shapely.geometry.BaseGeometry`
    :param b: The second `shapely.geometry.BaseGeometry`
    :returns: `shapely.geometry.BaseGeometry` describing the region between `a` and `b`.
    """
    return a.union(b).convex_hull.difference(a).difference(b)


def outer_inner_buffer(a, r):
    """
    :param a: The `shapely.geometry.Polygon`
    :param r: The size of the buffer
    :returns: `shapely.geometry.Polygon` (in general with holes) that is the outer part of `a`.
    """
    return a.exterior.buffer(r).intersection(a)


def medial_line(a):
    points = np.array(a.exterior.coords)
    vor = Voronoi(points)
    line_points = []

    # Get the pairs of indices (into vor.vertices) of the points that form the
    # finite Voronoi ridges INSIDE the polygon.
    valid_ridges = [(ridge[0], ridge[1]) for ridge in vor.ridge_vertices if ridge[0] != -1 and ridge[1] != -1 and Point(vor.vertices[ridge[0]]).within(a) and Point(vor.vertices[ridge[1]]).within(a)]

    if not valid_ridges:
        raise Exception("There's not enough Voronoi ridges fully inside the polygon. TODO: Sample the LineStrings?")

    return linemerge([LineString([vor.vertices[ridge[0]], vor.vertices[ridge[1]]]) for ridge in valid_ridges])


def direction_cone(a, direction, fov, radius):
    direction = np.array(direction)
    direction_ortho = _rotate_2d(direction, pi / 2)

    # Find the two points most separated along the line orthogonal to the
    # direction of the cone. These will 'cast' the rays of the cone
    p_a, p_b = min_max_along(a, direction_ortho)

    # Buffer the shape with the size of the cone
    buffered = a.buffer(radius)

    # Remove the halfplanes from the result:
    # - one 'above' the upper ray,
    # - one 'below' the lower ray, and 
    # - one 'left from' the line between the ray origins.
    result = _remove_halfplane(buffered, p_a.coords[0], _rotate_2d(direction, -fov / 2 - pi / 2))
    result = _remove_halfplane(result, p_b.coords[0], _rotate_2d(direction, fov / 2 + pi / 2))
    result = _remove_halfplane(result, p_a.coords[0], _rotate_2d(np.array(p_b.coords[0]) - np.array(p_a.coords[0]), pi / 2))
    
    # Finally, remove the original shape.
    return result.difference(a)


def _remove_halfplane(polygon, origin, normal):
    """
    :param polygon: Polygon to cut
    :param origin: Point that defines the half-plane with `normal`
    :param normal: Vector that defines the half-plane with `origin`
    """
    unit_normal = _normalize(normal)
    cut_direction = _rotate_2d(unit_normal, pi / 2)

    # Assuming that `origin` is inside the polygon, we can use this length
    # (*2 even) and stretch the line from there to construct a line that cuts
    # the entire polygon.
    safe_length = 3 * _diagonal_length(polygon.bounds)
    cut_line = LineString([origin - safe_length * cut_direction, origin + safe_length * cut_direction])

    parts = split(polygon, cut_line)
    # Assumes `split` returns a collection of two geometries (I think it does):
    # one on the one side of the line, and one on the other side.
    for part in parts:
        if not _in_halfplane(part.representative_point().coords[0], origin, unit_normal):
            return part
    return Point() # The empty feature (nothing is left!)


def _in_halfplane(point, origin, normal):
    return (np.array(point) - np.array(origin)).dot(normal) > 0


def _diagonal_length(bounds):
    return ((bounds[2] - bounds[0])**2 + (bounds[3] - bounds[1])**2)**0.5


def _rotate_2d(v, theta):
    return np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]).dot(v)


def _normalize(v):
    norm = np.linalg.norm(v)
    return v / norm


def min_max_along(a, direction):
    if isinstance(a, Polygon):
        candidates = a.exterior.coords
    else:
        candidates = a.coords
    candidates = [Point(candidate) for candidate in candidates]
    return\
        min(candidates, key=lambda candidate: np.array(candidate).dot(direction)),\
        max(candidates, key=lambda candidate: np.array(candidate).dot(direction))