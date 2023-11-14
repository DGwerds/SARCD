from src.canvas import Canvas
import random


class ManualSegmentation:
	def __init__(self, image_viewer):
		self.r = None
		self.y0 = None
		self.x0 = None
		self.image_viewer = image_viewer
		self.canvas: Canvas = image_viewer.canvas
		self.delta = 1.2
		# self.delta = 1.2

	def click(self, event):
		self.canvas.scan_mark(event.x, event.y)
		# self.x0, self.y0 = (event.x, event.y)
		self.x0 = self.canvas.canvasx(event.x)
		self.y0 = self.canvas.canvasy(event.y)

		color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
		self.r = self.canvas.create_rectangle(self.x0, self.y0, self.x0, self.y0, fill=color)
		# self.r = self.canvas.create_line(self.x0, self.y0, self.x0, self.y0)
		self.image_viewer.show_image()  # redraw the image
		# self.canvas.show_image()
		# self.canvas.scan_mark(event.x, event.y)

	def drag(self, event):
		""" Drag (move) canvas to the new position """
		# self.canvas.scan_dragto(event.x, event.y, gain=1)
		curX, curY = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
		self.canvas.coords(self.r, self.x0, self.y0, curX, curY)
		# self.image_viewer.show_image()  # redraw the image

	def wheel(self, event):
		""" Zoom with mouse wheel """
		x = self.canvas.canvasx(event.x)
		y = self.canvas.canvasy(event.y)
		scale = 1.0
		# Respond to Linux (event.num) or Windows (event.delta) wheel event
		if event.num == 5 or event.delta == -120:  # scroll down
			i = min(self.image_viewer.width, self.image_viewer.height)
			if int(i * self.image_viewer.imscale) < 30:
				return  # image is less than 30 pixels
			self.image_viewer.imscale /= self.delta
			scale /= self.delta
		if event.num == 4 or event.delta == 120:  # scroll up
			i = min(self.canvas.winfo_width(), self.canvas.winfo_height())
			if i < self.image_viewer.imscale:
				return  # 1 pixel is bigger than the visible area
			self.image_viewer.imscale *= self.delta
			scale *= self.delta
		self.canvas.scale('all', x, y, scale, scale)  # rescale all canvas objects
		self.image_viewer.show_image()


	def click_release(self, event):
		curX, curY = (event.x, event.y)
		self.r = self.canvas.create_line(self.x0, self.y0, self.x0, self.y0)
		# print("sefe")
		# self.canvas.delete(self.r)
