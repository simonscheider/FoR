import numpy as np
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt
from math import pi

import operations as ops
import plot_utils

def test_min_max_of_point():
    p = Point(2, 2)
    minimum, maximum = ops.min_max_along(p, np.array([1, 0]))
    assert minimum.equals(p)
    assert maximum.equals(p)

def test_min_max_of_line():
    line = LineString([(0, 0), (1, 1)])
    minimum, maximum = ops.min_max_along(line, np.array([1, 0]))
    assert minimum.equals(Point(0, 0))
    assert maximum.equals(Point(1, 1))

    minimum, maximum = ops.min_max_along(line, np.array([-1, 0]))
    assert minimum.equals(Point(1, 1))
    assert maximum.equals(Point(0, 0))

def test_min_max_of_polygon():
    polygon = Polygon([(1, 1), (2, 3), (4, 2), (3, 1)])
    minimum, maximum = ops.min_max_along(polygon, np.array([1, 0]))
    assert minimum.equals(Point(1, 1))
    assert maximum.equals(Point(4, 2))

    minimum, maximum = ops.min_max_along(polygon, np.array([0, 1]))
    assert minimum.equals(Point(1, 1)) or minimum.equals(Point(3, 1))
    assert maximum.equals(Point(2, 3))

def test_direction_cone_of_triangle_east(debug=False):
    triangle = Polygon([(0, 0), (0.5, 1), (1, 0)])
    cone = ops.direction_cone(triangle, (1, 0), pi / 2, 2)

    assert Point(2, 0.5).within(cone)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, triangle, color='lightcoral')
        plot_utils.plot(axes, cone, color='lightblue', marker='x')
        plt.show()

def test_direction_cone_of_triangle_west(debug=False):
    triangle = Polygon([(0, 0), (0.5, 1), (1, 0)])
    cone = ops.direction_cone(triangle, (-1, 0), pi / 2, 2)

    assert Point(-1, 0.5).within(cone)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, triangle, color='lightcoral')
        plot_utils.plot(axes, cone, color='lightblue', marker='x')
        plt.show()

def test_direction_cone_of_triangle_south(debug=False):
    triangle = Polygon([(0, 0), (0.5, 1), (1, 0)])
    cone = ops.direction_cone(triangle, (0, -1), pi / 2, 2)

    assert Point(0.5, -1).within(cone)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, triangle, color='lightcoral')
        plot_utils.plot(axes, cone, color='lightblue', marker='x')
        plt.show()

def test_direction_cone_of_circle_west(debug=False):
    circle = Point(0, 0).buffer(1)
    cone = ops.direction_cone(circle, (0, -1), pi / 2, 5)

    assert Point(0.5, -1).within(cone)
    
    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, circle, color='lightcoral')
        plot_utils.plot(axes, cone, color='lightblue', marker='x')
        plt.show()
