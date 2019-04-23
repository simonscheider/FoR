from operations import between

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
        plt.ylim(0, 3)
        plt.xlim(0, 7)
        plt.gca().add_patch(plt.Polygon(array(left.exterior.coords), color='red'))
        plt.gca().add_patch(plt.Polygon(array(right.exterior.coords), color='green'))
        plt.gca().add_patch(plt.Polygon(array(between_result.exterior.coords), color='blue'))
        plt.show()

def test_between_polygon_and_line(debug=False):
    left = Polygon([(1, 1), (2, 2), (3, 1)])
    right = LineString([(4, 1), (4, 2)])

    between_result = between(left, right)

    assert(between_result.equals(Polygon([(2, 2), (3, 1), (4, 1), (4, 2)])))

    if debug:
        plt.figure()
        plt.ylim(0, 3)
        plt.xlim(0, 7)
        plt.gca().add_patch(plt.Polygon(array(left.exterior.coords), color='red'))
        plt.gca().add_line(mlines.Line2D(array(right.coords).T[0, :], array(right.coords).T[1, :], color='green', linewidth=4))
        plt.gca().add_patch(plt.Polygon(array(between_result.exterior.coords), color='blue'))
        plt.show()
