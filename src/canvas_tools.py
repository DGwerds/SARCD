from src.tools.zoom_tool import Zoom
from src.tools.manual_segmentation import ManualSegmentation


class CanvasTools:
	""" This class is used to change the current tool in the canvas """
	def __init__(self, image_viewer):
		self.current_tool = None
		self.image_viewer = image_viewer
		# self.zoom = Zoom(image_viewer)
		self.current_tool = Zoom(image_viewer)
		# self.current_tool = ManualSegmentation(image_viewer)

	def click(self, event):
		self.current_tool.click(event)

	def click_release(self, event):
		self.current_tool.click_release(event)

	def drag(self, event):
		self.current_tool.drag(event)

	def wheel(self, event):
		self.current_tool.wheel(event)


