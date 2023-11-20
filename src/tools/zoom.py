from .tool import Tool


class Zoom(Tool):
    def __init__(self, image_viewer):
        self.image_viewer = image_viewer
        self.canvas = self.image_viewer.canvas
        self.__zoom_factor = 1.2

    def left_click(self, event):
        """ Remember previous coordinates for scrolling with the mouse """
        self.canvas.scan_mark(event.x, event.y)

    def right_click(self, event):
        pass

    def drag(self, event):
        """ Drag (move) canvas to the new position """
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.image_viewer.show_image()  # redraw the image

    def wheel(self, event):
        """ Zoom with mouse wheel """
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        scale = 1.0

        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down
            i = min(self.image_viewer.width, self.image_viewer.height)
            if int(i * self.image_viewer.imscale) < 300:
                return  # image is less than 30 pixels
            self.image_viewer.imscale /= self.__zoom_factor
            scale /= self.__zoom_factor
        if event.num == 4 or event.delta == 120:  # scroll up
            i = min(self.canvas.winfo_width(), self.canvas.winfo_height())/8
            if i < self.image_viewer.imscale:
                return  # 1 pixel is bigger than the visible area
            self.image_viewer.imscale *= self.__zoom_factor
            scale *= self.__zoom_factor

        self.canvas.scale('all', x, y, scale, scale)  # rescale all canvas objects

        self.image_viewer.show_image()

    def click_release(self, event):
        pass

    def get_description(self):
        return "Zoom tool description (work in progress)"
