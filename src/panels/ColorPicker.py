import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor


class ColorPicker(Frame):
    def __init__(self, master, name: str, value: StringVar, bg: str = None):
        super().__init__(master=master, bg=bg)
        self.value = value
        l = tk.Label(self, text=str(name), bg=bg)
        l.grid(row=0, column=0, sticky="nsew")

        boton_color = tk.Button(self, text="Seleccionar Color", command=self.seleccionar_color)
        boton_color.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

    def seleccionar_color(self):
        color = askcolor(title="Seleccionar color")[1]
        self.value.set(str(color))
