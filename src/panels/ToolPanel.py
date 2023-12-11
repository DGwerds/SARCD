from tkinter import *
from tkinter.ttk import *

from src.tools import ToolBox


class ToolPanel(Frame):
    def __init__(self, master):
        super().__init__(master=master, style="ToolPanel.TFrame")
        Style().configure(style='ToolPanel.TFrame', background='lightblue')
        self.__tool_box: ToolBox = ToolBox(self.master.image_viewer, self.master.management_panel)
        self.__opcion_escogida: StringVar = StringVar()
        self.__create_widgets()

    def __create_widgets(self):
        boton_basicas = Menubutton(self, text="Herramientas basicas")
        menu = Menu(boton_basicas, tearoff=0)
        menu.add_radiobutton(label="Navigate", value="navi", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        menu.add_radiobutton(label="Zoom", value="zoom", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        menu.add_radiobutton(label="Move", value="move", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)

        boton_basicas["menu"] = menu
        boton_basicas.pack(side=LEFT, padx=(2, 4), pady=3, fill="both", expand=True)

        boton_dibujo = Menubutton(self, text="Herramientas de dibujo")
        menu = Menu(boton_dibujo, tearoff=0)
        menu.add_radiobutton(label="Pincel", value="rec", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        menu.add_radiobutton(label="figuras", value="cir", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        menu.add_radiobutton(label="Pintar", value="lin", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        boton_dibujo["menu"] = menu
        boton_dibujo.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_segmentacion = Menubutton(self, text="Herramientas segmentacion")
        menu = Menu(boton_segmentacion, tearoff=0)
        menu.add_radiobutton(label="Manual Segmentation", value="mseg", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        menu.add_radiobutton(label="Automatic Segmentation", value="autoseg", variable=self.__opcion_escogida,
                             command=self.__actualizar_panel)
        boton_segmentacion["menu"] = menu
        boton_segmentacion.pack(side=LEFT, padx=(4, 2), pady=3, fill="both", expand=True)

        boton_medicion = Menubutton(self, text="Herramientas medicion")
        menu = Menu(boton_medicion, tearoff=0)
        menu.add_radiobutton(label="Regla", value="Opcion a", variable=self.__opcion_escogida)
        menu.add_radiobutton(label="", value="Opcion b", variable=self.__opcion_escogida)
        menu.add_radiobutton(label="Opcion c", value="opcion c", variable=self.__opcion_escogida)
        boton_medicion["menu"] = menu
        boton_medicion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_visualizacion = Menubutton(self, text="Herramientas visualizacion")
        menu = Menu(boton_visualizacion, tearoff=0)
        menu.add_radiobutton(label="Opcion c", value="Opcion c", variable=self.__opcion_escogida)
        menu.add_radiobutton(label="Opcion d", value="Opcion d", variable=self.__opcion_escogida)
        boton_visualizacion["menu"] = menu
        boton_visualizacion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

    def __actualizar_panel(self):
        self.__tool_box.change_tool(self.__opcion_escogida.get())
