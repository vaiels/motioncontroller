## Python
from pathlib import Path

## 3rd Party
import PySimpleGUI as sg 
sg.change_look_and_feel('Dark Blue 3')

## MMS
from utils import load_track_cones, ConeTypes, Point, CarState, transform_vector

class TrackMapGUI():
    def __init__(self, csv_name):
        self.track_name = csv_name.stem

        self._track = load_track_cones(csv_name)
        print(f"Loading track : \"{self.track_name}\" with {len(self._track)} cones")

        self._buffer = 10
        self._canvas_width = 1280
        self._canvas_height = 1280
        bot_left, top_right = self._find_track_bounds()

        layout = [[sg.Graph(canvas_size=(self._canvas_width, self._canvas_height),
                        graph_bottom_left=bot_left,
                        graph_top_right=top_right,
                        background_color='grey', key='graph', float_values=True, enable_events=True, drag_submits=True)]]

        self._window = sg.Window('Simulation Track', layout)
        self._canvas = self._window['graph']
        self._window.Finalize()

        self._cones = []
        self._draw_cones()
        self._car_poly = ((-1.5, -0.7), (-1.5, 0.7), (1.5, 0.7), (2.2, 0), (1.5, -0.7))
        self._vehicle_fig = self._canvas.DrawPolygon(self._car_poly, fill_color='pink')
        self._vehicle_state = CarState()

    def update_vehicle(self, car_state):
        # self._canvas.relocate_figure(self._vehicle_fig, car_state.x_pos, car_state.y_pos)
       
        self._canvas.delete_figure(self._vehicle_fig)
        rotated_car_poly = []
        for pt in self._car_poly:
            rotated_car_poly.append(transform_vector(pt, car_state.x_pos, car_state.y_pos, car_state.yaw))
        self._vehicle_fig = self._canvas.DrawPolygon(rotated_car_poly, fill_color='pink')


    def event_loop(self):
        event, _ = self._window.read(0)
        if event is None or event == 'Exit':
            self._window.close()
            exit()        

    def _draw_cones(self):
        # TODO: Check cone size works properly on all platforms
        # (on some its metres, others its pixels)
        for cone in self._track:
            self._cones.append(self._canvas.DrawPoint((cone.x, cone.y), size=0.5, color=ConeTypes(cone.type).name))

    def _find_track_bounds(self):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        for cone in self._track:
            min_x = min(cone.x, min_x)
            max_x = max(cone.x, max_x)
            min_y = min(cone.y, min_y)
            max_y = max(cone.y, max_y)
        return Point(min_x-self._buffer, min_y-self._buffer), Point(max_x+self._buffer, max_y+self._buffer)