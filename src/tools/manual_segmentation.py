from tkinter import Canvas, DoubleVar, StringVar

from shapely.geometry import LineString

from .tool import Tool


class ManualSegmentation(Tool):
    def __init__(self, image_viewer, zoom: Tool):
        self.zoom = zoom
        self.image_viewer = image_viewer
        self.canvas: Canvas = self.image_viewer.canvas
        self.tag_lines = []
        self.tag_polygons = []
        self.current_line = None
        self.is_invalid = False
        self.is_complete = False
        self.canvas.bind(sequence='<Motion>', func=self.drag)
        self.dash = (20, 20)
        self.width_line = DoubleVar(value=5)
        self.radius_stick = DoubleVar(value=15)
        self.color = StringVar(value="white")
        self.texture = StringVar(value="gray50")
        self.__values = ["gray50", "gray75", "gray25", 'gray12']

    def create_line(self, x0, y0, x1, y1):
        tag_line = f"line_{str(len(self.tag_lines))}_{str(len(self.tag_polygons))}"
        self.tag_lines.append(tag_line)
        return self.canvas.create_line(x0, y0, x1, y1, width=self.width_line.get(), fill=self.color.get(),
                                       tags=tag_line, smooth=True)

    def left_click(self, event):
        if self.is_invalid:
            return
        elif self.is_complete:
            self.draw_polygon()
            return
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if self.current_line is not None:
            x0, y0, _, _ = self.canvas.coords(self.tag_lines[-1])
            self.canvas.coords(self.current_line, x0, y0, x, y)

        self.current_line = self.create_line(x, y, x, y)

    def right_click(self, event):
        pass

    def drag(self, event):
        """ Drag (move) canvas to the new position """
        if self.tag_lines is None:
            return
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if self.current_line:  # relocate edge of the drawn polygon
            x1, y1, x2, y2 = self.canvas.coords(self.tag_lines[0])  # get coordinates of the 1st edge
            x3, y3, x4, y4 = self.canvas.coords(self.current_line)  # get coordinates of the current edge
            dx = x - x1
            dy = y - y1
            # Set new coordinates of the edge
            radius_stick = self.radius_stick.get()
            if radius_stick * radius_stick > dx * dx + dy * dy and len(self.tag_lines) >= 2:
                self.canvas.coords(self.current_line, x3, y3, x1, y1)  # stick to the beginning
                self.is_complete = True
            else:  # follow the mouse
                self.canvas.coords(self.current_line, x3, y3, x, y)  # follow the mouse movements
                self.set_dash(x3, y3, x, y)
                self.is_complete = False


    def draw_polygon(self):
        tag_poly = "poly" + str(len(self.tag_polygons))
        self.tag_polygons.append(tag_poly)
        cords_lines: list[tuple] = []
        # get all coords of the tag_lines
        for tag_line in self.tag_lines:
            cords_lines.append(tuple(self.canvas.coords(tag_line)))
            self.canvas.delete(tag_line)

        self.canvas.create_polygon(cords_lines, fill=self.color.get(), tags=tag_poly, width=self.width_line.get(),
                                   stipple=self.texture.get())

        self.current_line = None
        self.is_complete = False
        self.tag_lines.clear()

    def set_dash(self, x0, y0, x1, y1):
        if len(self.tag_lines) < 2:
            return
        coordes_current_line = LineString([(x0, y0), (x1, y1)])
        for line in self.tag_lines[:-2]:
            aux = self.canvas.coords(line)
            line = LineString((aux[:2], aux[2:]))
            if line.intersects(coordes_current_line):
                self.is_invalid = True
                self.canvas.itemconfigure(self.current_line, dash=self.dash)  # set dashed line
                return
        self.is_invalid = False
        self.canvas.itemconfigure(self.current_line, dash='')  # set solid line

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
        return [{"type": "spinbox", "name": "Width", "value": self.width_line, "max_value": 10},
                {"type": "spinbox", "name": "Radius stick", "value": self.radius_stick, "max_value": 100},
                {"type": "color", "name": "Color", "value": self.color},
                {"type": "option", "name": "Texture", "value": self.texture, "values": self.__values}]
        pass
