## Python
import math

## MMS
from utils import Controls

class MotionController():
    # To be implemented by the user
    def __init__(self):
        self.time = 0

    def get_controls(self, car_state, path_reference):
        # For dummy purposes just to show that the car moves
        self.time += 0.02
        return Controls(-math.sin(self.time*0.1), math.sin(self.time))