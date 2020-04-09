## Python
from pathlib import Path
import time

## MMS
from trackmap_gui import TrackMapGUI
from vehicle_model import VehicleModel
from path_planning import PathPlanner
from motion_controller import MotionController



rate = 50.0

track_csv = Path("./FSG2019.csv")
track_ref_csv = Path("./FSG2019_ref.csv")

gui = TrackMapGUI(track_csv)
vehicle = VehicleModel()
planner = PathPlanner(track_ref_csv)
controller = MotionController()

exit_counter=0

while(True):
    # car = vehicle.get_state_dummy(1.0/rate)
    car = vehicle.get_state(1.0/rate)
    # print(f"x: {car.x_pos}, y:{car.y_pos}, yaw: {car.yaw}")
    next_reference = planner.get_next_reference(car)
    next_controls = controller.get_controls(car, next_reference)
    vehicle.set_control_inputs(next_controls)
    gui.update_vehicle(car)
    gui.event_loop()
    time.sleep(1.0/rate)
    exit_counter += 1
