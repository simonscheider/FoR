from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt

from operations import between
import plot_utils

def test_between_triangles(debug=False):
    left = Polygon([(1, 1), (2, 2), (3, 1)])
    right = Polygon([(4, 2), (5, 1), (6, 2)])

    between_result = between(left, right)

    assert between_result.equals(Polygon([(2, 2), (3, 1), (5, 1), (4, 2)]))

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, left, color='lightcoral')
        plot_utils.plot(axes, right, color='lightblue')
        plot_utils.plot(axes, between_result, color='lightgrey')
        plt.show()

def test_between_polygon_and_line(debug=False):
    left = Polygon([(1, 1), (2, 2), (3, 1)])
    right = LineString([(4, 1), (4, 2)])

    between_result = between(left, right)

    assert between_result.equals(Polygon([(2, 2), (3, 1), (4, 1), (4, 2)]))

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, left, color='lightcoral')
        plot_utils.plot(axes, right, color='blue')
        plot_utils.plot(axes, between_result, color='lightgrey')
        plt.show()
