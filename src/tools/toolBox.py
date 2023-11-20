import random
import sys
from src.tools import ManualSegmentation, Zoom, Tool


class ToolBox(Tool):
    """ This class is used to change the current tool in the canvas """

    def __init__(self, image_viewer, management_panel):
        self.management_panel = management_panel
        self.image_viewer = image_viewer
        self.canvas = self.image_viewer.canvas

        self.zoom = Zoom(self.image_viewer)
        self.mseg = ManualSegmentation(self.image_viewer, self.zoom)

        self.tools = {"zoom": self.zoom,
                      "mseg": self.mseg}
        self.current_tool = self.tools["zoom"]

        self.intit_controls()

    def intit_controls(self):
        # Bind events to the Canvas
        self.canvas.bind(sequence='<ButtonPress-1>', func=self.left_click)
        self.canvas.bind(sequence='<ButtonRelease-1>', func=self.click_release)
        self.canvas.bind(sequence='<B1-Motion>', func=self.drag)

        match sys.platform:
            case 'win32' | 'win64' | 'darwin':
                self.canvas.bind(sequence='<MouseWheel>', func=self.wheel)
            case 'linux':
                self.canvas.bind(sequence='<Button-5>', func=self.wheel)
                self.canvas.bind(sequence='<Button-4>', func=self.wheel)


    def get_herramienta_actual(self):
        pass

    def set_image_viewer(self, image_viewer):
        self.image_viewer = image_viewer
        self.canvas = self.image_viewer.canvas
        self.tools = {"zoom": self.Zoom(self.image_viewer),
                      "mseg": self.ManualSegmentation()}
        self.current_tool = self.tools["zoom"]

        self.intit_controls()

    def change_tool(self, tool_name):
        if tool_name in self.tools:
            self.current_tool = self.tools[tool_name]
            self.management_panel.update_tool_data(self.current_tool)
        else:
            self.current_tool = self.tools["zoom"]
            print(f"Unknown tool: {tool_name}")
        self.intit_controls()

    def left_click(self, event):
        self.current_tool.left_click(event)

    def click_release(self, event):
        self.current_tool.click_release(event)

    def drag(self, event):
        self.current_tool.drag(event)

    def wheel(self, event):
        self.current_tool.wheel(event)

    def right_click(self, event):
        self.current_tool.right_click(event)
