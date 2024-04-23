from customtkinter import *

from src.customWidgets import CSpinbox, ColorPicker, OptionMenu


class ManagementPanel(CTkFrame):
    def __init__(self, root_window):
        super().__init__(root_window)

        self.tool_name_label = CTkLabel(self, text="Nombre de la herramienta")
        self.tool_name_label.grid(row=0, column=0, padx=2, pady=4, sticky="nsew")

        self.parameters_frame = CTkFrame(self)
        self.parameters_frame.grid(row=1, column=0, padx=2, pady=4, sticky="nsew")

    def get_tool_data(self, tool):
        for widget in self.parameters_frame.winfo_children():
            widget.grid_forget()
        self.tool_name_label.configure(text=type(tool).__name__)
        val = None
        params: list = tool.get_parameters()
        for i, param in enumerate(params):
            aux = param.pop("type")
            match aux:
                case "spinbox":
                    val = CSpinbox(self.parameters_frame, **param)
                case "color":
                    val = ColorPicker(self.parameters_frame, **param)
                case "option":
                    val = OptionMenu(self.parameters_frame, **param)

            val.grid(row=i, column=0, padx=2, pady=4, sticky="nsew")

        # self.tool_description_label.config(text=tool.get_description())
