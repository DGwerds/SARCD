from customtkinter import CTkFrame, CTkLabel
from tkinter import StringVar


class OptionMenu(CTkFrame):
    def __init__(self, master, name: str, value: StringVar | str, values: tuple | dict):
        super().__init__(master=master)
        CTkLabel(self, text=str(name)).grid(row=0, column=0, sticky="nsew")
        option_menu = OptionMenu(self, value, values[0], *values)
        option_menu.grid(row=1, column=0, padx=5, sticky="nsew")
