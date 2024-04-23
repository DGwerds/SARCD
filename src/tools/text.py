from tkinter import Canvas
from .tool import Tool


class Text(Tool):
    def __init__(self, image_viewer):
        self.__image_viewer = image_viewer
        self.__canvas: Canvas = self.__image_viewer.canvas
        self.__text = None

    def left_click(self, event):
        pass

    def right_click(self, event):
        pass

    def drag(self, event):
        pass

    def wheel(self, event):
        pass

    def ctrl_wheel(self, event):
        pass

    def click_release(self, event):
        pass

    @staticmethod
    def get_description(_self):
        return "text tool description (work in progress)"

    def get_parameters(self):
        return
