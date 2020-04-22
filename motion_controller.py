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

        """
            One of the most simple forms of controllers is the Pure pursuit controller. It work by simply looking at a
            target point in the future, and steering the wheels towards that. 
            Let's just pick one of the path_reference points, say 2, as our target point. 

            It's easiest to separate the two components of the controller out in to velocity control, and steering control.
                Velocity control:
                    The most basic controller I can think of is a P controller (P being 'proportional' from PID control).
                    For a PID type controller you need a setpoint and a current value to produce an error. (The output of the
                    controller is just a 'gain' (some scaling factor you manually tune) times by the error.) The current value 
                    we can get from the car's state, the setpoint we get from our chosen reference waypoint.

                Steering:
                    Intuitively, it should make sense that we want to steer the front wheels towards the chosen reference waypoint.
                    Imagine a vector going from the car's front wheels to the waypoint. We want the wheels to point along this vector,
                    so use some trigonometry to figure out what that angle is.
            
            You may find it useful to draw up a sketch of the above scenario and think about how the angles changes when the car moves or
            the waypoint moves.
        """

        # For dummy purposes just to show that the car moves (make the car move randomly)
        self.time += 0.02
        steering = -math.sin(self.time*0.1)
        throttle = math.sin(self.time)

        # Controls are of the form (steering (between [-1, 1]), throttle (between [-1, 1]))
        return Controls(steering, throttle)