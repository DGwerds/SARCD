import sys

from src.tools import AutoSegmentation, ManualSegmentation, Zoom, Tool, Move, Navigation, Figuras, Default


class ToolBox(Tool):
    """ This class is used to change the current tool in the canvas """

    def __init__(self, image_viewer, management_panel):
        self.current_tool = None
        self.management_panel = management_panel
        self.image_viewer = image_viewer
        self.canvas = self.image_viewer.canvas

        self.zoom = Zoom(self.image_viewer)
        self.mseg = ManualSegmentation(self.image_viewer, self.zoom)
        self.autoseg = AutoSegmentation(self.image_viewer, self.zoom)
        self.move = Move(self.image_viewer)
        self.navi = Navigation(self.image_viewer)
        self.default = Default(self.image_viewer, self.zoom, self.move, self.navi)
        self.figuras = Figuras(self.image_viewer, self.zoom)

        self.tools = {"MultiHerramienta": self.default,
                      "Zoom": self.zoom,
                      "Manual Segmentation": self.mseg,
                      "Automatic Segmentation": self.autoseg,
                      "Mover": self.move,
                      "Navegar": self.navi,
                      "Figuras": self.figuras}

        self.change_tool("default")

        self.init_controls()

    def init_controls(self):
        # Bind events to the Canvas
        self.canvas.bind(sequence='<ButtonPress-1>', func=self.left_click)
        self.canvas.bind(sequence='<ButtonRelease-1>', func=self.click_release)
        self.canvas.bind(sequence='<B1-Motion>', func=self.drag)
        # self.canvas.bind(sequence='<Motion>', func=self.drag)

        match sys.platform:
            case 'win32' | 'win64' | 'darwin':
                self.canvas.bind(sequence='<MouseWheel>', func=self.wheel)
                self.canvas.bind(sequence='<Control-MouseWheel>', func=self.ctrl_wheel)
            case 'linux':
                self.canvas.bind(sequence='<Button-5>', func=self.wheel)
                self.canvas.bind(sequence='<Button-4>', func=self.wheel)
                self.canvas.bind(sequence='<Control-4>', func=self.ctrl_wheel)
                self.canvas.bind(sequence='<Control-5>', func=self.ctrl_wheel)

    def get_herramienta_actual(self):
        pass

    def set_image_viewer(self, image_viewer):
        self.image_viewer = image_viewer
        self.canvas = self.image_viewer.canvas
        self.init_controls()

    def change_tool(self, tool_name):
        if tool_name in self.tools:
            self.current_tool = self.tools[tool_name]
            self.management_panel.get_tool_data(self.current_tool)
        else:
            self.current_tool = self.tools["Zoom"]
        self.init_controls()

    def get_tool_parameters(self):
        return self.current_tool.get_parameters()

    def left_click(self, event):
        self.current_tool.left_click(event)

    def click_release(self, event):
        self.current_tool.click_release(event)

    def drag(self, event):
        self.current_tool.drag(event)

    def wheel(self, event):
        self.current_tool.wheel(event)

    def ctrl_wheel(self, event):
        self.current_tool.ctrl_wheel(event)

    def right_click(self, event):
        self.current_tool.right_click(event)
