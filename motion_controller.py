## Python
import math

## MMS
from utils import Controls

class MotionController():
    # To be implemented by the user. May make a keyboard controlled version as an example
    def __init__(self):
        self.time = 0

    def get_controls(self, car_state, path_reference):
        # For dummy purposes
        self.time += 0.02
        return Controls(-math.sin(self.time), math.sin(self.time))