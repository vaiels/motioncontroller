## Python
import math

## MMS
from utils import CarState, Controls

class VehicleModel():
    def __init__(self):
        self._state = CarState()
        self._steer_req = 0.0
        self._throttle_req = 0.0

        self._steer_angle = 0
        self._slip_angle = 0

        self._COG_front = 0.8672
        self._COG_rear = 0.6183

    def set_control_inputs(self, controls):
        self._steer_req = controls.steering
        self._throttle_req = controls.throttle

    def get_state_dummy(self, delta_time):
        self._state.x_pos += delta_time * 5
        self._state.y_pos += delta_time *-1
        self._state.yaw += delta_time * -0.2
        return self._state #dummy for now
    
    def get_state(self, delta_time):
        if self._state.velocity < .0:
            self._state.accel = max(0, self._throttle_req * 4)
        else:
            self._state.accel = self._throttle_req * 4
        self._steer_angle = self._steer_req * 0.43 # map [-1, 1] to rads

        # Kinematic Bicycle Maths
        ratio = math.tan(self._steer_angle) * self._COG_rear / (self._COG_front + self._COG_rear)
        _slip_angle = math.atan(ratio)

        self._state.x_pos    += self._state.velocity * math.cos(_slip_angle + self._state.yaw) * delta_time
        self._state.y_pos    += self._state.velocity * math.sin(_slip_angle + self._state.yaw) * delta_time
        self._state.velocity += self._state.accel * delta_time
        self._state.yaw      += (self._state.velocity / self._COG_rear) * math.sin(_slip_angle) * delta_time
        return self._state 