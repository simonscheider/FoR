from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

import operations as ops
import plot_utils

def test_medial_line_of_polygon_1(debug=False):
    polygon = Polygon([(1, 1), (1, 1.5), (1, 2), (1, 3), (2, 3), (2, 2), (2, 1.5), (2, 1), (1.5, 1.5)])

    medial_line = ops.medial_line(polygon)

    assert medial_line.touches(Point(1.5, 2))
    assert medial_line.touches(Point(1.25, 1.75))
    assert medial_line.touches(Point(1.5, 2.5))
    assert medial_line.touches(Point(1.5, 2))
    assert medial_line.touches(Point(1.75, 1.75))

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, polygon, color='lightgrey', marker='x')
        plot_utils.plot(axes, medial_line, color='lightcoral')
        plt.show()


def test_medial_line_of_polygon_2(debug=False):
    polygon = Point(1, 1).buffer(2).union(Point(2, 2).buffer(2))

    medial_line = ops.medial_line(polygon)

    assert medial_line.within(polygon)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, polygon, color='lightgrey', marker='x')
        plot_utils.plot(axes, medial_line, color='lightcoral')
        plt.show()

def test_medial_line_of_polygon_3(debug=False):
    polygon = Polygon([(1, 1), (2, 1.5), (0, 3), (-1, 4), (-2, 3), (-0.5, 2)])

    medial_line = ops.medial_line(polygon)

    assert medial_line.within(polygon)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, polygon, color='lightgrey', marker='x')
        plot_utils.plot(axes, medial_line, color='lightcoral')
        plt.show()
