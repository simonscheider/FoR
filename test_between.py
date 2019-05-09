from operations import between

import plot_utils

from shapely.geometry import Polygon, LineString
from numpy import array

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def test_between_triangles(debug=False):
    left = Polygon([(1, 1), (2, 2), (3, 1)])
    right = Polygon([(4, 2), (5, 1), (6, 2)])

    between_result = between(left, right)

    assert(between_result.equals(Polygon([(2, 2), (3, 1), (5, 1), (4, 2)])))

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, left, color='red')
        plot_utils.plot(axes, right, color='green')
        plot_utils.plot(axes, between_result, color='blue')
        plt.show()

def test_between_polygon_and_line(debug=False):
    left = Polygon([(1, 1), (2, 2), (3, 1)])
    right = LineString([(4, 1), (4, 2)])

    between_result = between(left, right)

    assert(between_result.equals(Polygon([(2, 2), (3, 1), (4, 1), (4, 2)])))

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, left, color='red')
        plot_utils.plot(axes, right, color='green')
        plot_utils.plot(axes, between_result, color='blue')
        plt.show()
