from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

import operations as ops
import plot_utils


def test_outer_inner_buffer_square(debug=False):
    square = Polygon([(-1, -1), (-1, 1), (1, 1), (1, -1)])
    oi_buffer = ops.outer_inner_buffer(square, 0.2)

    assert Point(0.9, 0.9).within(oi_buffer)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, square, color='lightgrey', marker='x')
        plot_utils.plot(axes, oi_buffer, color='lightcoral', marker='+')
        plt.show()


def test_outer_inner_buffer_circle(debug=False):
    circle = Point(0, 0).buffer(1)
    oi_buffer = ops.outer_inner_buffer(circle, 0.2)

    assert Point(0.49 * 2**0.5, 0.49 * 2**0.5).within(oi_buffer)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, circle, color='lightgrey', marker='x')
        plot_utils.plot(axes, oi_buffer, color='lightcoral', marker='+')
        plt.show()
