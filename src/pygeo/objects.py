import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    def __init__(self, point, vector):
        self._point = point
        self._vector = vector
    
    def __repr__(self):
        return f"Ray origin({self._point}), Ray vector({self._vector})"
    
    def __eq__(self, other):
        if np.array_equal(other._vector, self._vector) == True:
            if np.array_equal(other._point, self._point) == True:
                return True
            else:
                return False
        else:
            return False
    def get_vector(self):
        return(np.array(self._vector))


class Sphere:
    """A sphere."""

    def __init__(self, point, radius):
        self._point = np.array(point)
        self._radius = radius
    
    def __repr__(self):
        return f"Origin point({self._point}), Radius({self._radius})"
    
    def __eq__(self, other):
        if np.array_equal(other._point, self._point) == True:
            if np.array_equal(other._radius, self._radius) == True:
                return True
            else:
                return False
        else:
            return False


class Triangle:
    """A triangle."""
    def __init__(self, point1, point2, point3):
        self._point1 = np.array(point1)
        self._point2 = np.array(point2)
        self._point3 = np.array(point3)
