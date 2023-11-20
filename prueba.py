from abc import ABC, abstractmethod


class Tool(ABC):
	@abstractmethod
	def left_click(self):
		pass

	@abstractmethod
	def wheel(self):
		pass

	@abstractmethod
	def drag(self):
		pass


class Toolbox(Tool):
	def __init__(self):
		self.zoom_tool = Zoom()
		self.brush_tool = Brush()
		self.current_tool = self.zoom_tool

	def change_tool(self, tool_name):
		if tool_name == 'zoom':
			self.current_tool = self.zoom_tool
		elif tool_name == 'brush':
			self.current_tool = self.brush_tool
		else:
			print(f"Unknown tool: {tool_name}")

	def left_click(self):
		self.current_tool.left_click()

	def wheel(self):
		self.current_tool.wheel()

	def drag(self):
		self.current_tool.drag()


class Zoom(Tool):
	def drag(self):
		pass

	def left_click(self):
		print("Zoom: left_click")

	def wheel(self):
		print("Zoom: wheel")


class Brush(Tool):
	def wheel(self):
		pass

	def left_click(self):
		print("Brush: left_click")

	def drag(self):
		print("Brush: drag")


class Pincel(Tool):
	def left_click(self):
		print("Pincel: left_click")

	def wheel(self):
		print("Pincel: wheel")

	def drag(self):
		print("Pincel: drag")

# def wheel(self):
# 	try:
# 		super().wheel()
# 	except AttributeError:
# 		self.fallback_tool.wheel()


t = Toolbox()
t.left_click()
t.wheel()

print(t.current_tool)
t.change_tool('brush')
print(t.current_tool)

t.left_click()
t.wheel()
t.drag()
