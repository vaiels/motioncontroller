## Python
from pathlib import Path
import time
import sys

## MMS
from trackmap_gui import TrackMapGUI
from vehicle_model import VehicleModel
from path_planning import PathPlanner
from motion_controller import MotionController
from keyboard_controller import KeyboardController

rate = 50.0
keyboard_controller_enabled = False

track_csv = Path("./FSG2019.csv")
track_ref_csv = Path("./FSG2019_ref.csv")

gui = TrackMapGUI(track_csv)
vehicle = VehicleModel()
planner = PathPlanner(track_ref_csv)

if keyboard_controller_enabled or sys.argv[1]:
    controller = KeyboardController()
else:
    controller = MotionController()

while(True):
    car = vehicle.get_state(1.0/rate)
    next_reference = planner.get_next_reference(car)
    next_controls = controller.get_controls(car, next_reference)
    vehicle.set_control_inputs(next_controls)

    gui.update_vehicle(car)
    gui.update_reference(next_reference)
    gui.event_loop()
    
    time.sleep(1.0/rate)
