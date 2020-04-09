## Python
from enum import Enum
from collections import namedtuple
import math

class ConeTypes(Enum):
    blue = 0
    yellow = 1
    orange = 2

Cone = namedtuple('Cone', 'x y type')

Point = namedtuple('Point', 'x y')

def transform_vector(pt, x, y, angle):
    return (x + math.cos(angle)*pt[0] - math.sin(angle)*pt[1], y + math.sin(angle)*pt[0] + math.cos(angle)*pt[1])


Controls = namedtuple('Controls', 'steering throttle')

# TODO: Create a proper geometry class instead of just a tuple as above
# class Point():
#     def __init__(self, _x=.0, _y=.0):
#         self.x = _x
#         self.y = _y

class CarState():
    """ Struct to contain state params
    """
    def __init__(self):
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.velocity = 0.0
        self.accel = 0.0
        self.yaw = 0.0

def norm(x, y):
    return math.sqrt((x*x) + (y*y))

def load_track_cones(csv_path):
    track = []
    with open(csv_path, 'r') as track_file:
        for x in track_file.readlines():
            x, y, typ = x.strip().split(",")
            track.append(Cone(float(x), float(y), int(typ)))
    return track