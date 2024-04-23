from tkinter import *
from customtkinter import CTkFrame, CTkOptionMenu
from src.tools import ToolBox


class ToolPanel(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.__tool_box: ToolBox = ToolBox(self.master.image_viewer, self.master.management_panel)
        self.__opcion_escogida: StringVar = StringVar()
        self.__create_widgets()

    def __create_widgets(self):
        boton_basicas = CTkOptionMenu(self, values=["MultiHerramienta", "Navegar", "Zoom", "Mover"],
                                      command=self.__actualizar_panel)
        boton_basicas.pack(side=LEFT, padx=(2, 4), pady=3, fill="both", expand=True)

        boton_dibujo = CTkOptionMenu(self, values=["Figuras", "Texto", "Pincel"], command=self.__actualizar_panel)
        boton_dibujo.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_segmentacion = CTkOptionMenu(self, values=["Manual Segmentation", "Automatic Segmentation"],
                                           command=self.__actualizar_panel)
        boton_segmentacion.pack(side=LEFT, padx=(4, 2), pady=3, fill="both", expand=True)

        boton_medicion = CTkOptionMenu(self, values=["Regla", "Ángulo", "Distancia"], command=self.__actualizar_panel)
        boton_medicion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_visualizacion = CTkOptionMenu(self, values=["Opción c", "Opción d"], command=self.__actualizar_panel)
        boton_visualizacion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

    def __actualizar_panel(self, tool_name: str):
        self.__tool_box.change_tool(tool_name)
