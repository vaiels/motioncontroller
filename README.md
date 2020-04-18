# Simple Project
A self contained python codebase to act as a platform to experiment with motion control implementations. This aims to have as few dependencies as possible and be compatible with both Linux and Windows. To run, type `python main.py` into the command line.

### Requirements

 - Python 3.6+
 - PySimpleGUI
 - pynput


### Classes

#### Kinematic Vehicle Model
Implements a kinematic bicycle model that takes in a thottle and steering input between [-1, 1].
There is nothing implementing drag, so this will go infinitely fast if you hold down the throttle.

#### Path Planner
Takes in the cars current state and gives a list of waypoints in the form [x, y, target_velocity]. The waypoints have been precomputed for simplicity.


#### Motion Controller
A class that the user should extend and implement their own functions into in order to make everything work.
Ideas of types of controllers to look at for inspiration:

 - Pure Pursuit
 - Stanley
 - PID

You should take in the car's position and reference waypoints, and then output steering & throttle controls to follow the waypoints.

The framework for this has already been implemented for you, but feel free to extend it as you wish. This should be the only thing that you have to touch. 

#### Trackmap GUI
Visualizes the cones on the track, the car's current position, and the reference waypoints.


#### Keyboard Controller
Overrides the Motion Controller, and allows the user to control the vehicle model with the keyboard. Use WASD or Arrows.
To use this, type `python main.py keyboard` into the command line.
