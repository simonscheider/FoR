import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

import operations as ops

import plot_utils

def test_voronoi_of_lattice(debug=True):
    points = np.array([(1, 1), (1, 2), (2, 2.5), (3, 2), (3, 1), (2, 1.5)])
    polygon = Polygon(points)

    medial_line = ops.medial_line(polygon)

    plt.figure()
    axes = plt.subplot(111)
    plot_utils.plot_polygon(axes, polygon, mark_color='r')
    
    plot_utils.plot_line_string(axes, medial_line)
    
    plt.show()
