from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from src.panels import ManagementPanel, ImageViewer, ToolPanel, MenuBar


class DICOMViewerApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("MOCID")
        self.geometry("1400x550")

        # Configurar la cuadricula de la ventana es un 5x5
        self.grid_rowconfigure(index=0, minsize=50)
        self.grid_rowconfigure(index=1, weight=1)
        self.grid_rowconfigure(index=2, weight=1)
        self.grid_rowconfigure(index=3, weight=1)
        self.grid_rowconfigure(index=4, weight=1)

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=1)
        self.grid_columnconfigure(index=3, weight=1)
        self.grid_columnconfigure(index=4, minsize=250)

        # la barra superior que dice "Archivo, Editar, Ayuda"
        self.menu_bar: Menu = MenuBar(self)

        # el panel de gestion de herramientas
        self.management_panel: Frame = ManagementPanel(self)
        self.management_panel.grid(column=4, row=1, rowspan=4, pady=3, padx=3, sticky="nsew")

        # Donde se muestran las imagenes
        # open a folder with dicom files (or a single file) tkinter
        # path = "Ejemplos/series"
        path = filedialog.askdirectory()
        print(path)
        self.image_viewer: Frame = ImageViewer(self, path=path)
        self.image_viewer.grid(column=0, row=1, columnspan=4, rowspan=4, pady=3, padx=3, sticky="nsew")

        # la barra de herramientas
        self.tool_panel: Frame = ToolPanel(self)
        self.tool_panel.grid(column=0, row=0, columnspan=5, sticky="nsew")


if __name__ == "__main__":
    app = DICOMViewerApp()
    app.mainloop()