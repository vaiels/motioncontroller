## Python
import math
import pygame

## MMS
from utils import Controls


ACCEL_SCALE = 0.1
ACCEL_MAX = 2.0
BRAKE_SCALE = 0.15
BRAKE_MAX = -3.0
STEER_SCALE = 0.03
STEER_MAX = 3.1415/4


class Car():
    def __init__(self):
        self.acceleration = 0
        self.steerAngle = 0


class KeyboardController():
    # Pops up an invisible pygame window to give keyboard input to the vehicle model
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1,1])

        self.car = Car()
        self.left, self.right, self.up, self.down = False, False, False, False

    def get_controls(self, car_state, path_reference):
        # Args ignored, just give the user input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
        
        if self.left or self.right:
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

        return Controls(self.car.steerAngle/STEER_MAX, self.car.acceleration/ACCEL_MAX)
