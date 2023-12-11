from .tool import Tool
import random
from tkinter import Canvas


class AutoSegmentation(Tool):
    def __init__(self, image_viewer, zoom: Tool):
        self.zoom = zoom
        self.r = None
        self.image_viewer = image_viewer
        self.canvas: Canvas = self.image_viewer.canvas

    def left_click(self, event):
        x0 = self.canvas.canvasx(event.x)
        y0 = self.canvas.canvasy(event.y)
        color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
        self.r = self.canvas.create_rectangle(x0, y0, x0, y0, fill=color, stipple='gray50')
        self.image_viewer.show_image()

    def right_click(self, event):
        pass

    def drag(self, event):
        """ Drag (move) canvas to the new position """
        x2 = self.canvas.canvasx(event.x)
        y2 = self.canvas.canvasy(event.y)
        if self.r:
            x3, y3, x4, y4 = self.canvas.coords(self.r)
            self.canvas.coords(self.r, x3, y3, x2, y2)

        self.image_viewer.show_image()  # redraw the image

    def wheel(self, event):
        """ Zoom with mouse wheel """
        self.zoom.wheel(event)

    def ctrl_wheel(self, event):
        """ Zoom with mouse wheel """
        self.zoom.ctrl_wheel(event)

    def click_release(self, event):
        pass

    def get_description(self):
        return "Manual segmentation tool (in progress)"
