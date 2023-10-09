import os
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pydicom
# pydicom es la libreria que nos va a ayudar con muchas cosas
# todo: Solo me encargue de la parte visual, no hay ningun tipo de funcionalidad agregada


class DICOMViewerApp(Tk):
	# iniciar la ventana (En la mayoria de partes voy a hacer referencia a esta ventana con el nombre "raiz")
	def __init__(self):
		super().__init__()
		self.title("MOCID")
		self.geometry("900x550")

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=8)

		self.grid_rowconfigure(1, weight=8)
		self.grid_columnconfigure(1, weight=1)

		# Nose como conectar la opcion escogida en la BarraSuperior con el texto del PanelDerecho
		self.opcion_escogida = StringVar(self)

		# La barra que esta completamente arriba (La que dice Archivo, Editar, Ayuda...)
		self.BarraMenu = BarraMenu(self)

		# LA barra donde vamos a poner todas las herramientas (Frame azul)
		self.BarraSuperior = BarraSuperior(self)

		# Frame donde vamos a poner las opciones/parametros de las herramientas (Frame verde)
		self.PanelDerecho = PanelDerecho(self)

		# Donde se va a visualizar los dicom (Frame Rojo)
		self.Visualizador = Visualizador(self)

		self.mainloop()


class BarraMenu(Menu):
	def __init__(self, raiz):
		super().__init__(raiz)
		raiz.config(menu=self)
		self.contenido()

	def contenido(self):
		# Menu desplegable de "Archivo"
		menu_archivo = Menu(self, tearoff=0)
		menu_archivo.add_command(label="Nuevo")
		menu_archivo.add_command(label="Abrir", accelerator="Ctrl+N")

		def guardar():
			print("Jajajaj, archivo ''guardado''")

		menu_archivo.add_command(label="Guardar", accelerator="Ctrl+G", command=guardar)
		menu_archivo.add_separator()

		menu_archivo.add_command(label="Cerrar", accelerator="Alt+F4", command=self.master.destroy)
		self.add_cascade(label="Archivo", menu=menu_archivo)

		# Menu desplegable de "Editar"
		menu_editar = Menu(self, tearoff=0)
		menu_editar.add_command(label="Cortar", state=DISABLED)
		menu_editar.add_command(label="Copiar")
		menu_editar.add_command(label="Pegar")
		self.add_cascade(label="Editar", menu=menu_editar)

		# Menu desplegable de "Ayuda"
		menu_ayuda = Menu(self, tearoff=0)
		menu_ayuda.add_command(label="Ayudameeee", state=DISABLED)
		menu_ayuda.add_separator()

		def funcion_de_prueba():
			menu_ayuda.entryconfig(0, state=NORMAL)

		menu_ayuda.add_command(label="Activar boton ayudameeee", command=funcion_de_prueba)
		self.add_cascade(label="Ayuda", menu=menu_ayuda)


class BarraSuperior(Frame):
	def __init__(self, raiz):
		super().__init__(raiz, style="BarraSuperior.TFrame")
		Style().configure('BarraSuperior.TFrame', background='lightblue')
		self.grid(column=0, row=0, columnspan=2, sticky="nsew")
		# todo: nose como conectar la opcion_escogida para que el PanelDerecho muestre lo que se escogio
		self.opcion_escogida = self.master.opcion_escogida
		self.contenido()

	def contenido(self):
		# configurar boton segmentacion
		boton_segmentacion = Menubutton(self, text="Herramientas segmentacion")
		menu = Menu(boton_segmentacion, tearoff=0)

		opciones_segmentacion = ("Opcion 1", "Opcion 2", "etc...")
		for opcion in opciones_segmentacion:
			menu.add_radiobutton(label=opcion, value=opcion, variable=self.opcion_escogida)
		boton_segmentacion["menu"] = menu
		boton_segmentacion.pack(side=LEFT, padx=(4, 2), pady=3, fill="both", expand=True)

		# boton de medicion
		boton_medicion = Menubutton(self, text="Herramientas medicion")
		menu = Menu(boton_medicion, tearoff=0)

		opciones_medicion = ("Opcion a", "Opcion b", "etc...")
		for opcion in opciones_medicion:
			menu.add_radiobutton(label=opcion, value=opcion, variable=self.opcion_escogida)
		boton_medicion["menu"] = menu
		boton_medicion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

		# Boton visualizacion
		boton_visualizacion = Menubutton(self, text="Herramientas medicion")
		menu = Menu(boton_visualizacion, tearoff=0)
		opciones_visualizacion = ("Opcion c", "Opcion d", "etc...")
		for opcion in opciones_visualizacion:
			menu.add_radiobutton(label=opcion, value=opcion, variable=self.opcion_escogida)
		boton_visualizacion["menu"] = menu
		boton_visualizacion.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

		# Boton dibujo
		boton_dibujo = Menubutton(self, text="Herramientas medicion")
		menu = Menu(boton_dibujo, tearoff=0)
		opciones_dibujo = ("Opcion e", "Opcion f", "etc...")
		for opcion in opciones_dibujo:
			menu.add_radiobutton(label=opcion, value=opcion, variable=self.opcion_escogida)
		boton_dibujo["menu"] = menu
		boton_dibujo.pack(side=LEFT, padx=2, pady=3, fill="both", expand=True)

		# Boton basicas
		boton_basicas = Menubutton(self, text="Herramientas medicion")
		menu = Menu(boton_basicas, tearoff=0)
		opciones_basicas = ("Opcion g", "Opcion h", "etc...")
		for opcion in opciones_basicas:
			menu.add_radiobutton(label=opcion, value=opcion, variable=self.opcion_escogida)
		boton_basicas["menu"] = menu
		boton_basicas.pack(side=LEFT, padx=(2, 4), pady=3, fill="both", expand=True)


class PanelDerecho(Frame):
	# todo: Este panel esta completamente incompleto
	def __init__(self, raiz):
		super().__init__(raiz, style='PanelDerecho.TFrame')
		Style().configure('PanelDerecho.TFrame', background='lightgreen')
		self.opcion_escogida = self.master.opcion_escogida
		self.grid(column=1, row=1, pady=3, padx=3, sticky="nsew")

		self.label = Label(self, text="")
		self.label.pack()
		self.opcion_escogida.trace("w", self.actualizar_label)

	def actualizar_label(self, *args):
		# Obtener el valor de la variable y actualizar el Label
		valor = self.opcion_escogida.get()
		self.label.config(text=f"Herramientas de: {valor}")
		_args = args


class Visualizador(Frame):
	def __init__(self, raiz):
		super().__init__(raiz, style='Visualizador.TFrame')
		Style().configure('Visualizador.TFrame', background='lightpink')
		self.grid(column=0, row=1, pady=3, padx=3, sticky="nsew")
		self.contenido()

	def contenido(self):
		# boton_cargar = tk.Button(self, text="buscar")
		# boton_cargar.pack(expand=True)
		pass


if __name__ == "__main__":
	app = DICOMViewerApp()
	app.mainloop()
