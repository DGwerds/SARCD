from tkinter import *
from tkinter.ttk import *
from src.panels.Spinbox import Spinbox
from src.panels.ColorPicker import ColorPicker
from src.panels.OptionMenu import OptionMenu


class ManagementPanel(Frame):
    def __init__(self, root_window):
        super().__init__(root_window, style='ManagementPanel.TFrame')
        self.bg = "lightgreen"
        Style().configure(style='ManagementPanel.TFrame', background=self.bg, width=300, height=100)

        self.tool_name_label = Label(self, text="Nombre de la herramienta", background=self.bg)
        self.tool_name_label.grid(row=1, column=0, padx=2, pady=4, sticky="nsew")

        self.parameters_frame = Frame(self, style='ManagementPanel.TFrame')
        self.parameters_frame.grid(row=2, column=0, padx=2, pady=4, sticky="nsew")

    def get_tool_data(self, tool):
        for widget in self.parameters_frame.winfo_children():
            widget.grid_forget()
        self.tool_name_label.config(text=type(tool).__name__)
        val = None
        params: list = tool.get_parameters()
        for i, param in enumerate(params):
            aux = param.pop("type")
            match aux:
                case "spinbox":
                    val = Spinbox(self.parameters_frame, **param, bg=self.bg)
                case "color":
                    val = ColorPicker(self.parameters_frame, **param, bg=self.bg)
                case "option":
                    val = OptionMenu(self.parameters_frame, **param, bg=self.bg)

            val.grid(row=i, column=0, padx=2, pady=4, sticky="nsew")

        # self.tool_description_label.config(text=tool.get_description())
