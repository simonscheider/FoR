import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

import operations as ops

import plot_utils

def test_voronoi_of_lattice(debug=False):
    points = np.array([(1, 1), (1, 1.5), (1, 2), (1, 3), (2, 3), (2, 2), (2, 1.5), (2, 1), (1.5, 1.5)])
    polygon = Polygon(points)

    medial_line = ops.medial_line(polygon)

    if debug:
        plt.figure()
        axes = plt.subplot(111)
        plot_utils.plot(axes, polygon, color='grey')
        plot_utils.plot(axes, medial_line, color='r')
        plt.show()
