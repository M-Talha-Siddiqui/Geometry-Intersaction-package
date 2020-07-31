from .objects import Ray, Sphere, Triangle, Point, Vector
import numpy as np
import math


def intersect(first_object, second_object):
    ...

def _intersect_ray_with_sphere(ray, sphere):
    # u is the unit vector ,direction of ray
    u = ray._vector/np.linalg.norm(ray._vector)
    delta = ((np.dot(u,(ray._point-sphere._point)))**2) - (np.dot((ray._point-sphere._point),(ray._point-sphere._point))-sphere._radius**2)
    #If DELTA >0, two solutions exist, and thus the line touches the sphere in two points (case 1).
    if delta > 0:
        d = np.array([-(np.dot(u,(ray._point-sphere._point)))+abs(math.sqrt(delta)),-(np.dot(u,(ray._point-sphere._point)))-abs(math.sqrt(delta))])
        value = []
        for d in d[d>=0]:
            value.append(Point(ray._point+(d*u)))
        return np.array(value)

    #If DELTA = 0, then exactly one solution exists, i.e. the line just touches the sphere in one point (case 2).
    elif delta == 0:
        d = -1*(np.dot(u,(ray._point-sphere._point)))
        return np.array(Point(ray._point+(d*u)))
    #If DELTA < 0, then it is clear that no solutions exist, i.e. the line does not intersect the sphere (case 3).
    else:
        print("Ray does not intersect sphere")


def _intersect_ray_with_triangle(ray, triangle):
    ...
