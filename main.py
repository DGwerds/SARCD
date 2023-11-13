from tkinter import *
from tkinter.ttk import *
from src.canvas import ImageViewer


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

        self.opcion_escogida: StringVar = StringVar(self)

        # la barra superior que dice "Archivo, Editar, Ayuda"
        self.menu_bar: Menu = MenuBar(self)

        # la barra de herramientas
        self.main_bar: Frame = MainBar(self)
        self.main_bar.grid(column=0, row=0, columnspan=5, sticky="nsew")

        self.panel: Frame = Panel(self)

        # path = "Ejemplos/series"
        path = "Ejemplos/series2"
        self.image_viewer: Frame = ImageViewer(self, path)
        # self.image_viewer2: Frame = ImageViewer(self, path)
        self.image_viewer.grid(column=0, row=1, columnspan=4, rowspan=4, pady=3, padx=3, sticky="nsew")
        # self.image_viewer2.grid(column=2, row=1, columnspan=2, rowspan=4, pady=3, padx=3, sticky="nsew")


class MenuBar(Menu):
    def __init__(self, root_window):
        super().__init__(root_window)
        root_window.config(menu=self)
        self.create_menu()

    def create_menu(self):
        menu_archivo = Menu(self, tearoff=0)
        menu_archivo.add_command(label="Nuevo")
        menu_archivo.add_command(label="Abrir", accelerator="Ctrl+N")

        def guardar():
            print("Jajajaj, archivo ''guardado''")

        menu_archivo.add_command(label="Guardar", accelerator="Ctrl+G", command=guardar)
        menu_archivo.add_separator()

        menu_archivo.add_command(label="Cerrar", accelerator="Alt+F4", command=self.master.destroy)
        self.add_cascade(label="Archivo", menu=menu_archivo)

        menu_editar = Menu(self, tearoff=0)
        menu_editar.add_command(label="Cortar", state=DISABLED)
        menu_editar.add_command(label="Copiar")
        menu_editar.add_command(label="Pegar")
        self.add_cascade(label="Editar", menu=menu_editar)

        menu_ayuda = Menu(self, tearoff=0)
        menu_ayuda.add_command(label="Ayudameeee", state=DISABLED)
        menu_ayuda.add_separator()

        def funcion_de_prueba():
            menu_ayuda.entryconfig(index=0, state=NORMAL)

        menu_ayuda.add_command(label="Activar boton ayudameeee", command=funcion_de_prueba)
        self.add_cascade(label="Ayuda", menu=menu_ayuda)


class MainBar(Frame):
    def __init__(self, root_window):
        super().__init__(root_window, style="MainBar.TFrame")
        Style().configure(style='MainBar.TFrame', background='lightblue')
        self.create_widgets()

    def create_widgets(self):
        boton_basicas = Menubutton(self, text="Herramientas basicas")
        menu = Menu(boton_basicas, tearoff=0)
        opciones_basicas = ("Lopa", "Opcion h", "etc...")
        for i in opciones_basicas:
            menu.add_radiobutton(label=i, value=i, variable=self.master.opcion_escogida)
        boton_basicas["menu"] = menu
        boton_basicas.pack(side=LEFT, padx=(2, 4), pady=3, fill="both", expand=True)

        boton_segmentacion = Menubutton(self, text="Herramientas segmentacion")
        menu = Menu(boton_segmentacion, tearoff=0)
        menu.add_radiobutton(label="opcionx", value="opcionx", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="opciony", value="opciony", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="opcionz", value="opcionz", variable=self.master.opcion_escogida)
        boton_segmentacion["menu"] = menu
        boton_segmentacion.pack(side=LEFT, padx=(4, 2), pady=3, fill="both", expand=True)

        boton_medicion = Menubutton(self, text="Herramientas medicion")
        menu = Menu(boton_medicion, tearoff=0)
        menu.add_radiobutton(label="Opcion a", value="Opcion a", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="Opcion b", value="Opcion b", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="Opcion c", value="opcion c", variable=self.master.opcion_escogida)
        boton_medicion["menu"] = menu
        boton_medicion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_visualizacion = Menubutton(self, text="Herramientas visualizacion")
        menu = Menu(boton_visualizacion, tearoff=0)
        menu.add_radiobutton(label="Opcion c", value="Opcion c", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="Opcion d", value="Opcion d", variable=self.master.opcion_escogida)
        boton_visualizacion["menu"] = menu
        boton_visualizacion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

        boton_dibujo = Menubutton(self, text="Herramientas de dibujo")
        menu = Menu(boton_dibujo, tearoff=0)
        menu.add_radiobutton(label="Opcion e", value="Opcion e", variable=self.master.opcion_escogida)
        menu.add_radiobutton(label="Opcion f", value="Opcion f", variable=self.master.opcion_escogida)
        boton_dibujo["menu"] = menu
        boton_dibujo.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)




class Panel(Frame):
    def __init__(self, root_window):
        super().__init__(root_window, style='Panel.TFrame')
        Style().configure(style='Panel.TFrame', background='lightgreen',  width=300, height=100)
        self.grid(column=4, row=1, rowspan=4, pady=3, padx=3, sticky="nsew")

        self.label = Label(self, text="Panel")
        self.label.grid(row=0, column=0, padx=2, pady=4, sticky="nsew")


# class ImageViewer(Frame):
#     def __init__(self, root_window):
#         super().__init__(root_window, style='ImageViewer.TFrame')
#         Style().configure(style='ImageViewer.TFrame', background='white')
#         self.grid(column=0, row=1, columnspan=4, rowspan=4, pady=3, padx=3, sticky="nsew")
#
#         # Grid 3x3, en el 2x2 se muestran imagenes, y la otra fila y columna la dejo por si al caso
#         self.grid_rowconfigure(index=0, weight=1)
#         self.grid_columnconfigure(index=0, weight=1)
#
#         self.grid_rowconfigure(index=1, weight=1)
#         self.grid_columnconfigure(index=1, weight=1)
#
#         self.grid_rowconfigure(index=2, weight=0)
#         self.grid_columnconfigure(index=2, weight=0)
#
#         self.load_dicom_files("series")
#
#     def load_dicom_files(self, folder_path):
#         print(type(self))
#         slice_number: int = 0
#         self.canvas1 = Canvas(self)
#
#
#         img_paths: list[str] = [os.path.join(folder_path, file)
#                                 for file in os.listdir(folder_path) if file.endswith(".dcm")]
#
#         dicoms_data = [dcm.dcmread(img) for img in img_paths]
#
#         pixel_array = dicoms_data[slice_number].pixel_array
#
#         photo = Image.fromarray(pixel_array)
#
#         # resize photo to canvas1 sizes
#         photo = ImageTk.PhotoImage(image=photo)
#
#         # show image in canvas1
#         canvas1.create_image(0, 0, image=photo, anchor=NW)
#         canvas1.image = photo  # Evita que la imagen se recolecte por el recolector de basura
#
#         canvas1.grid(row=0, column=0, columnspan=2, rowspan=2, padx=(4, 2), pady=(4, 2), sticky="nsew")
#         # canvas2.grid(row=0, column=1, padx=(2, 4), pady=(4, 2), sticky="nsew")
#         # canvas3.grid(row=1, column=0, padx=(4, 2), pady=(2, 4), sticky="nsew")
#         # canvas4.grid(row=1, column=1, padx=(2, 4), pady=(2, 4), sticky="nsew")
#         # imagen = imagen.resize((400, 300), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen según sea necesario
#         # imagen_tk = ImageTk.PhotoImage(imagen)
#
#         # Crea un widget Label para mostrar la imagen
#         # label_imagen = Label(self, image=imagen_tk)


if __name__ == "__main__":
    app = DICOMViewerApp()
    app.mainloop()
