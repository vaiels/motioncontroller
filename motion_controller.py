## Python
import math

## MMS
from utils import Controls, Point, wrap_angle

from simple_pid import PID

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
                         car_state.velocity: velocity of car in m/s
                         car_state.yaw: The yaw(heading) of the car in radians, +/- pi.


            - path_reference: A list of RefPoint() objects
                              This is represented by the green line in the GUI
                              path_reference[0] is the first object in the list, a Refpoint
                              
                              path_reference[0].vel is a number that is the target velocity at that waypoint
                              path_reference[0].x is a number that is the x coordinate of the point
                              path_reference[0].y is a number that is the y coordinate of the point

        """
        def normalise_angle(angle):
            while angle > math.pi:
                angle -= 2.0 * math.pi
            while angle < -math.pi:
                angle += 2.0 * math.pi
            return angle
        pathyaw = math.atan2( (path_reference[2].y - path_reference[0].y) , (path_reference[2].x - path_reference[0].x) )
        headingError = normalise_angle(pathyaw - car_state.yaw)
        axleError = math.sqrt((path_reference[0].y - car_state.y_pos)**2 + (path_reference[0].x - car_state.x_pos)**2)
        k = 0.08
        crosstrackError = math.atan2(k * axleError , car_state.velocity)
        delta = headingError + crosstrackError
        # For dummy purposes just to show that the car moves (make the car move randomly)
        self.time += 0.02
        steering = delta
        
        pid = PID(0.02, 0.01, 0.005, setpoint = path_reference[0].vel)
        pid.sample_time = 0.02
        pid.tunings = (1.0, 1.0, 1.0)
        pid.output_limits = (-1,1)
        throttle = pid(car_state.velocity)
        # Controls are of the form (steering (between [-1, 1]), throttle (between [-1, 1]))
        return Controls(steering, throttle)