from tkinter import DoubleVar

from .tool import Tool


class Zoom(Tool):
    def __init__(self, image_viewer):
        self.__image_viewer = image_viewer
        self.__canvas = self.__image_viewer.canvas
        self.__zoom_factor = DoubleVar(value=1.2)

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
        x = self.__canvas.canvasx(event.x)
        y = self.__canvas.canvasy(event.y)
        scale = 1.0
        zoom_factor = self.__zoom_factor.get()
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down
            i = min(self.__image_viewer.width, self.__image_viewer.height)
            if int(i * self.__image_viewer.imscale) < 300:
                return  # image is less than 30 pixels
            self.__image_viewer.imscale /= zoom_factor
            scale /= zoom_factor
        if event.num == 4 or event.delta == 120:  # scroll up
            i = min(self.__canvas.winfo_width(), self.__canvas.winfo_height()) / 8
            if i < self.__image_viewer.imscale:
                return  # 1 pixel is bigger than the visible area
            self.__image_viewer.imscale *= zoom_factor
            scale *= zoom_factor

        self.__canvas.scale('all', x, y, scale, scale)  # rescale all canvas objects

        self.__image_viewer.show_image()

    def ctrl_wheel(self, event):
        self.wheel(event)
        pass

    def click_release(self, event):
        pass

    def get_description(self):
        return "Zoom tool description (work in progress)"

    def get_parameters(self):
        param = [{"type": "spinbox", "name": "Zoom factor", "value": self.__zoom_factor, "max_value": 3,
                  "min_value": 1.1, "increment": 0.1}]
        return param

    def get_zoom_factor(self):
        return self.__zoom_factor.get()

    # def update_parameters(self, **kwargs):
    #     for clave, valor in kwargs.items():
    #         setattr(self, clave, valor)
