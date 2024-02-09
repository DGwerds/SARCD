from tkinter import Canvas, DoubleVar, StringVar

from .tool import Tool


class Figuras(Tool):
    def __init__(self, image_viewer, zoom: Tool):
        self.zoom = zoom
        self.image_viewer = image_viewer
        self.canvas: Canvas = self.image_viewer.canvas
        self.current_figure = None
        self.tags = []
        self.width_line = DoubleVar(value=5)
        self.color = StringVar(value="")
        self.outline = StringVar(value="black")
        self.texture = StringVar(value="")
        self.figure = StringVar(value="rect")
        self.__figures = {"rect": self.canvas.create_rectangle,
                          "oval": self.canvas.create_oval,
                          "line": self.canvas.create_line,
                          "arc": self.canvas.create_arc}
        self.__values = ("", "gray50", "gray75", "gray25", 'gray12')

    def left_click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        tag = f"fig_{str(len(self.tags))}"
        self.tags.append(tag)
        current_form = self.__figures[self.figure.get()]
        if current_form == self.canvas.create_line:
            self.color.set("black" if self.color.get() == "" else self.color.get())
            self.current_figure = current_form(x, y, x, y, width=self.width_line.get(), fill=self.color.get(),
                                               tags=tag, smooth=True)
        elif current_form == self.canvas.create_arc:
            self.current_figure = current_form(x, y, x, y, width=self.width_line.get(), fill=self.color.get(),
                                               tags=tag, outline=self.outline.get(), style="arc")
        else:
            self.current_figure = current_form(x, y, x, y, width=self.width_line.get(), fill=self.color.get(),
                                               tags=tag, outline=self.outline.get())
        # self.current_figure = fig
        self.image_viewer.show_image()

    def right_click(self, event):
        pass

    def drag(self, event):
        """ Drag (move) canvas to the new position """
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if self.current_figure is None:
            return
        x1, y1, _, _ = self.canvas.coords(self.current_figure)
        self.canvas.coords(self.current_figure, x1, y1, x, y)

    def wheel(self, event):
        """ Zoom with mouse wheel """
        self.zoom.wheel(event)

    def ctrl_wheel(self, event):
        pass

    def click_release(self, event):
        pass

    def get_description(self):
        return "Manual segmentation tool (in progress)"

    def get_parameters(self):
        return [{"type": "option", "name": "Figures", "value": self.figure, "values": tuple(self.__figures.keys())},
                {"type": "color", "name": "Color", "value": self.color},
                {"type": "color", "name": "Outline color", "value": self.outline},
                {"type": "option", "name": "Texture", "value": self.texture, "values": self.__values},
                {"type": "spinbox", "name": "Width", "value": self.width_line, "max_value": 50}]
