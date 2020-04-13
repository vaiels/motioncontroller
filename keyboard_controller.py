## Python
import math
from keyboard import is_pressed

## MMS
from utils import Controls


ACCEL_SCALE = 1.0
ACCEL_MAX = 2.25
BRAKE_SCALE = 4.0
BRAKE_MAX = -10.0
STEER_SCALE = 0.04
STEER_MAX = 1.0


class Car():
    def __init__(self):
        self.acceleration = 0
        self.steerAngle = 0


class KeyboardController():
    # Pops up an invisible pygame window to give keyboard input to the vehicle model
    def __init__(self):
        self.car = Car()
        self.left, self.right, self.up, self.down = False, False, False, False

    def get_controls(self, car_state, path_reference):
        # Args ignored, just give the user input
        self.left = is_pressed('left')
        self.right = is_pressed('right')
        self.up = is_pressed('up')
        self.down = is_pressed('down')

        if self.left or self.right:
            if not self.right and self.car.steerAngle < 0 or \
             not self.left and self.car.steerAngle > 0:
                self.car.steerAngle = 0
            
            if self.left and self.car.steerAngle <= STEER_MAX:
                self.car.steerAngle += 1.0 * STEER_SCALE
            
            if self.right and self.car.steerAngle >= -STEER_MAX:
                self.car.steerAngle += -1.0 * STEER_SCALE
        else:
            self.car.steerAngle = 0
        
        if self.down or self.up:
            if self.up:
                if self.car.acceleration < 0:
                    self.car.acceleration = 0
                if self.car.acceleration < ACCEL_MAX:
                    self.car.acceleration += 1.0 * ACCEL_SCALE
            if self.down:
                if self.car.acceleration > 0:
                    self.car.acceleration = 0
                if self.car.acceleration > BRAKE_MAX:
                    self.car.acceleration += -1.0 * BRAKE_SCALE
        else:
            self.car.acceleration = 0

        return Controls(self.car.steerAngle/STEER_MAX, self.car.acceleration)
