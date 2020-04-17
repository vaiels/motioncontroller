## Python
import math

## MMS
from utils import Controls

class MotionController():
    # To be implemented by the user
    def __init__(self):
        """
            The constructor function called when you make an object of type MotionController()
        """
        self.time = 0

    def get_controls(self, car_state, path_reference):
        """
        Input parameters:
            - car_state: An object of type CarState(), you can find the definition in utils.py
                         This is represented by the pink shape in the GUI
                         It has the attributes:
                         car_state.x_pos: x position of car in world frame
                         car_state.y_pos: x position of car in world frame
                         car_state.velocity: velocity of car
                         car_state.yaw: The yaw(heading) of the car


            - path_reference: A list of RefPoint() objects
                              This is represented by the green line in the GUI
                              path_reference[0] is the first object in the list, a Refpoint
                              path_reference[0].vel is a number that is the target velocity at that waypoint
                              path_reference[0].coord is a Point() object
                              path_reference[0].coord.x is a number that is the x position
                              path_reference[0].coord.y is a number that is the y position

        """

        # For dummy purposes just to show that the car moves (make the car move randomly)
        self.time += 0.02
        steering = -math.sin(self.time*0.1)
        throttle = math.sin(self.time)

        # Controls are of the form (steering (between [-1, 1]), throttle (between [-1, 1]))
        return Controls(steering, throttle)