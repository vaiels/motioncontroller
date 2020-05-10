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
        self._throttle_Kp = 1.0
        self._steering_Kp = 1.0
        self._lookahead_index = 2

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
        vel_error = path_reference[self._lookahead_index].vel - car_state.velocity
        throttle = self._throttle_Kp * vel_error

        target_vec_x = path_reference[self._lookahead_index].x - car_state.x_pos
        target_vec_y = path_reference[self._lookahead_index].y - car_state.y_pos

        target_yaw = math.atan2(target_vec_y, target_vec_x)

        angle_error = wrap_angle(target_yaw - car_state.yaw)

        steering = self._steering_Kp * angle_error
        
        # print(f"target yaw: {math.degrees(target_yaw):4.0f}, current yaw: {math.degrees(car_state.yaw):4.0f}, angle error: {math.degrees(angle_error):4.0f}")
        # Controls are of the form (steering (between [-1, 1]), throttle (between [-1, 1]))
        return Controls(steering, throttle)