from tkinter import *
from tkinter.ttk import *


class ManagementPanel(Frame):
    def __init__(self, root_window):
        super().__init__(root_window, style='ManagementPanel.TFrame')
        Style().configure(style='ManagementPanel.TFrame', background='lightgreen', width=300, height=100)

        self.label = Label(self, text="ManagementPanel")
        self.label.grid(row=0, column=0, padx=2, pady=4, sticky="nsew")

        self.tool_name_label = Label(self, text="Nombre de la herramienta")
        self.tool_name_label.grid(row=1, column=0, padx=2, pady=4, sticky="nsew")

        self.tool_description_label = Label(self, text="Descripcion de la herramienta")
        self.tool_description_label.grid(row=2, column=0, padx=2, pady=4, sticky="nsew")

    def update_tool_data(self, tool):
        # Actualiza los datos de la herramienta en el panel
        # Este es un ejemplo, debes reemplazarlo con tu propia lógica
        self.tool_name_label.config(text=type(tool).__name__)
        self.tool_description_label.config(text=tool.get_description())
