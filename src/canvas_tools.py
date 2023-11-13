from src.tools.zoom_tool import Zoom


class CanvasTools:
	def __init__(self, image_viewer):
		self.current_tool = None
		self.image_viewer = image_viewer
		self.zoom = Zoom(image_viewer)
		self.current_tool = self.zoom

	def click(self, event):
		self.current_tool.click(event)

	def drag(self, event):
		self.current_tool.drag(event)

	def wheel(self, event):
		self.current_tool.wheel(event)


