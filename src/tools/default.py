from tkinter import IntVar

from src.tools import Navigation, Move, Zoom
from .tool import Tool


class Default(Tool):
    def __init__(self, image_viewer, zoom: Zoom, move: Move, navigation: Navigation):
        self.zoom = zoom
        self.move = move
        self.navigation = navigation
        self.__image_viewer = image_viewer
        self.__canvas = self.__image_viewer.canvas
        self.__steps = IntVar(value=1)

    def left_click(self, event):
        self.move.left_click(event)
        pass

    def right_click(self, event):
        pass

    def drag(self, event):
        self.move.drag(event)
        pass

    def wheel(self, event):
        self.navigation.wheel(event)
        pass

    def ctrl_wheel(self, event):
        self.zoom.ctrl_wheel(event)
        pass

    def click_release(self, event):
        pass

    @staticmethod
    def get_description():
        return "Zoom tool description (work in progress)"

    def get_parameters(self):
        param = [{"type": "spinbox", "name": "Steps", "value": self.navigation.get_steps_variable(), "max_value": 10,
                  "min_value": 1, "increment": 1},
                 {"type": "spinbox", "name": "Zoom factor", "value": self.zoom.get_zoom_factor(), "max_value": 3,
                  "min_value": 1.1, "increment": 0.1},
                 {"type": "spinbox", "name": "Move factor", "value": self.move.get_move_factor_variable(),
                  "max_value": 10, "min_value": 1, "increment": 1}
                 ]
        return param
