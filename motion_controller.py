## Python
import math

## MMS
from utils import Controls, Point, wrap_angle


class MotionController():
    # To be implemented by the user
    def __init__(self):
        """
            The constructor function called when you make an object of type MotionController()
        """

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
        # Stanley controller
        pathyaw = math.atan2( (path_reference[2].y - path_reference[0].y) , (path_reference[2].x - path_reference[0].x) )
        headingError = wrap_angle(pathyaw - car_state.yaw)
        axleError = math.sqrt((path_reference[0].y - car_state.y_pos)**2 + (path_reference[0].x - car_state.x_pos)**2)
        k = 0.1
        crosstrackError = math.atan2(k * axleError , car_state.velocity)
        delta = headingError + crosstrackError

        steering = delta
        # P controller
        velError = path_reference[0].vel - car_state.velocity
        Kp = 1
        throttle = Kp * velError
        #pid = PID(Kp= 1, Ki= 0.5, Kd=0.2, setpoint = path_reference[0].vel, sample_time = 0.02, output_limits= (-1,1))
        #throttle = pid(car_state.velocity)
        # Controls are of the form (steering (between [-1, 1]), throttle (between [-1, 1]))
        return Controls(steering, throttle)