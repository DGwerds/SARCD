from tkinter import IntVar

from .tool import Tool


class Move(Tool):
    def __init__(self, image_viewer):
        self.__image_viewer = image_viewer
        self.__canvas = self.__image_viewer.canvas
        self.__move_factor = IntVar(value=1)

    def left_click(self, event):
        """ Remember previous coordinates for scrolling with the mouse """
        self.__canvas.scan_mark(event.x, event.y)

    def right_click(self, event):

        pass

    def drag(self, event):
        """ Drag (move) canvas to the new position """
        self.__canvas.scan_dragto(event.x, event.y, gain=1)
        self.__image_viewer.show_image()  # redraw the image

    def wheel(self, event):
        """ Zoom with mouse wheel """
        move_factor = self.__move_factor.get()
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down
            self.__canvas.yview_scroll(move_factor, "units")
            pass
        if event.num == 4 or event.delta == 120:  # scroll up
            self.__canvas.yview_scroll(-move_factor, "units")
        self.__image_viewer.show_image()

    def ctrl_wheel(self, event):
        """ Zoom with mouse wheel """
        move_factor = self.__move_factor.get()
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:
            self.__canvas.xview_scroll(move_factor, "units")
        if event.num == 4 or event.delta == 120:
            self.__canvas.xview_scroll(-move_factor, "units")

    def click_release(self, event):
        pass

    def get_description(self):
        return "Zoom tool description (work in progress)"

    def get_parameters(self):
        param = [{"type": "spinbox", "name": "Move factor", "value": self.__move_factor, "max_value": 10,
                  "min_value": 1, "increment": 1}]
        return param

    def get_move_factor_variable(self):
        return self.__move_factor

    # def update_parameters(self, **kwargs):
    #     for clave, valor in kwargs.items():
    #         setattr(self, clave, valor)
