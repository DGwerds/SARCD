from tkinter import *


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
