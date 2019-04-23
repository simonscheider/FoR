def between(a, b):
    """
    :param a: The first `shapely.geometry.BaseGeometry`
    :param b: The second `shapely.geometry.BaseGeometry`
    :returns: `shapely.geometry.BaseGeometry` describing the region between `a` and `b`.
    """
    return a.union(b).convex_hull.difference(a).difference(b)
