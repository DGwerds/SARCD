from tkinter.colorchooser import askcolor
from customtkinter import CTkFrame, CTkLabel, CTkButton
from tkinter import StringVar


class ColorPicker(CTkFrame):
    def __init__(self, master, name: str, value: StringVar, bg: str = None):
        super().__init__(master=master, bg=bg)
        self.value = value
        label = CTkLabel(self, text=str(name), bg=bg)
        label.grid(row=0, column=0, sticky="nsew")

        button_color = CTkButton(self, text="Seleccionar Color", command=self.seleccionar_color)
        button_color.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

    def seleccionar_color(self):
        color = askcolor(title="Seleccionar color")[1]
        self.value.set(str(color))
